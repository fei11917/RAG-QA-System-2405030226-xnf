import os
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from knowledge_base import KnowledgeBase

class RAGQASystem:
    def __init__(self, model_name="deepseek-r1:7b"):
        self.model_name = model_name
        self.kb = KnowledgeBase()
        self.llm = ChatOllama(model=model_name)
        self.qa_chain = None
        self.chat_history = []
    
    def build_knowledge_base(self, folder_path):
        print(f"从 {folder_path} 加载文档...")
        documents = self.kb.load_documents_from_folder(folder_path)
        if documents:
            self.kb.build_vectorstore(documents)
            self._setup_qa_chain()
            return True
        return False
    
    def _setup_qa_chain(self):
        retriever = self.kb.get_retriever(k=3)
        if retriever:
            prompt = ChatPromptTemplate.from_messages([
                ("system", """基于参考文档回答问题，无相关信息请回答'文档中未找到相关答案'。

参考文档：{context}"""),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}")
            ])
            self.qa_chain = (
                {"context": retriever, "question": lambda x: x["question"], "chat_history": lambda x: x["chat_history"]}
                | prompt
                | self.llm
                | StrOutputParser()
            )
    
    def ask(self, question):
        if not self.qa_chain:
            return "知识库未初始化"
        
        try:
            result = self.qa_chain.invoke({
                "question": question,
                "chat_history": self.chat_history
            })
            self.chat_history.append(HumanMessage(content=question))
            self.chat_history.append(AIMessage(content=result))
            return result
        except Exception as e:
            return f"错误: {str(e)}"

def main():
    print("=" * 60)
    print("RAG问答系统 - 命令行版本")
    print("=" * 60)
    
    rag = RAGQASystem()
    
    docs_folder = "./documents"
    if os.path.exists(docs_folder):
        print(f"\n从 {docs_folder} 加载文档...")
        if rag.build_knowledge_base(docs_folder):
            print("✓ 知识库构建成功")
        else:
            print("✗ 知识库构建失败")
    else:
        print(f"错误: {docs_folder} 文件夹不存在")
        return
    
    print("\n" + "=" * 60)
    print("输入问题进行问答")
    print("输入 'quit' 退出")
    print("=" * 60)
    
    while True:
        question = input("\n问题: ").strip()
        if not question:
            continue
        if question.lower() == 'quit':
            print("再见！")
            break
        
        print("思考中...")
        answer = rag.ask(question)
        print("\n回答:", answer)

if __name__ == "__main__":
    main()
