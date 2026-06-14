import streamlit as st
import os
import requests
import numpy as np

class SimpleRAG:
    def __init__(self):
        self.host = "http://127.0.0.1:11434"
        self.model = "qwen2:0.5b"
        self.embedding_model = "nomic-embed-text"
        self.embeddings = []
        self.documents = []
    
    def embed_text(self, text):
        response = requests.post(
            f"{self.host}/api/embeddings",
            json={"model": self.embedding_model, "prompt": text}
        )
        return np.array(response.json()["embedding"], dtype=np.float32)
    
    def load_documents(self, folder_path):
        documents = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1].lower()
                if ext == '.docx':
                    from docx import Document
                    doc = Document(file_path)
                    text = "\n".join([p.text for p in doc.paragraphs])
                    if text.strip():
                        documents.append({"text": text, "source": filename})
        return documents
    
    def split_text(self, text, chunk_size=1000, chunk_overlap=200):
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            if end < len(text):
                gap = text.rfind(' ', start, end)
                if gap != -1 and gap > start + chunk_size // 2:
                    end = gap
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            start = end - chunk_overlap
            if start >= len(text):
                break
        return chunks
    
    def build_knowledge_base(self, folder_path):
        docs = self.load_documents(folder_path)
        all_chunks = []
        for doc in docs:
            chunks = self.split_text(doc["text"])
            for chunk in chunks:
                all_chunks.append({"text": chunk, "source": doc["source"]})
        
        self.embeddings = []
        self.documents = all_chunks
        for chunk in all_chunks:
            embedding = self.embed_text(chunk["text"])
            self.embeddings.append(embedding)
        
        return len(all_chunks)
    
    def search(self, query, k=3):
        if not self.embeddings:
            return [], []
        
        query_embedding = self.embed_text(query)
        similarities = []
        for i, emb in enumerate(self.embeddings):
            similarity = np.dot(query_embedding, emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(emb))
            similarities.append((i, similarity))
        
        similarities.sort(key=lambda x: x[1], reverse=True)
        results = []
        scores = []
        for i, sim in similarities[:k]:
            results.append(self.documents[i])
            scores.append(sim)
        return results, scores
    
    def ask(self, query):
        if not self.embeddings:
            return "知识库未初始化"
        
        results, scores = self.search(query, k=3)
        
        # 如果最高相似度低于0.3，直接返回未找到
        if not scores or max(scores) < 0.3:
            return "文档中未找到相关答案"
        
        context = "\n\n".join([f"来源: {r['source']}\n内容: {r['text']}" for r in results])
        
        prompt = f"""请根据参考文档回答问题。

参考文档：
{context}

问题：{query}

要求：
1. 必须完全按照文档原文回答
2. 文档中没有的内容回答：文档中未找到相关答案
3. 不要添加任何额外内容

回答："""
        
        response = requests.post(
            f"{self.host}/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False}
        )
        return response.json()["response"].strip()
    
    def get_document_count(self):
        return len(self.documents)

st.set_page_config(
    page_title="RAG问答系统",
    page_icon="📚",
    layout="wide"
)

if "rag" not in st.session_state:
    st.session_state.rag = SimpleRAG()
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("📚 RAG问答系统")

with st.sidebar:
    st.header("知识库管理")
    
    if st.button("📁 从documents文件夹加载文档"):
        with st.spinner("正在加载文档..."):
            try:
                count = st.session_state.rag.build_knowledge_base("./documents")
                st.success(f"✅ 知识库构建成功！共 {count} 个文档块")
            except Exception as e:
                st.error(f"❌ 加载失败: {str(e)}")
    
    doc_count = st.session_state.rag.get_document_count()
    st.metric("文档块数量", doc_count)
    
    if st.button("🗑️ 清空知识库"):
        st.session_state.rag = SimpleRAG()
        st.session_state.messages = []
        st.success("知识库已清空")
    
    st.markdown("---")
    st.markdown("### 测试问题")
    st.markdown("""
    **相关问题：**
    - 什么是自然语言处理？
    - 词向量有什么优势？
    - Transformer模型的核心创新是什么？
    
    **无关问题：**
    - 今天天气怎么样？
    - 如何做红烧肉？
    """)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_question = st.chat_input("请输入问题...")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.write(user_question)
    
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            try:
                answer = st.session_state.rag.ask(user_question)
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"错误: {str(e)}")
