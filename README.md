# RAG问答系统

基于LangChain和Ollama的本地知识库问答系统，支持PDF/DOCX文档上传、智能问答和对话历史管理。

## 项目简介

本项目是一个完整的RAG（Retrieval-Augmented Generation）问答系统，能够基于本地文档库进行智能问答。系统使用Ollama作为本地大模型推理引擎，Chroma作为向量数据库，实现了文档解析、向量化存储、语义检索和智能问答的完整流程。

## 功能特性

- ✅ 支持PDF和DOCX文档上传与解析
- ✅ 自动文档分块与向量化存储
- ✅ 基于语义相似度的智能检索
- ✅ 多轮对话与上下文记忆
- ✅ Streamlit Web界面
- ✅ 命令行版本
- ✅ 本地化部署，无需联网
- ✅ 可打包为独立exe文件

## 技术栈

- **大模型**: Ollama (deepseek-r1:7b / qwen2:7b)
- **框架**: LangChain
- **向量数据库**: ChromaDB
- **嵌入模型**: nomic-embed-text / all-minilm
- **Web框架**: Streamlit
- **文档处理**: PyPDF2, python-docx

## 环境要求

- Python 3.8+
- Ollama (已安装并运行)
- 至少8GB内存
- Windows/Linux/macOS

## 安装步骤

### 1. 安装Ollama

访问 [https://ollama.ai](https://ollama.ai) 下载并安装Ollama。

### 2. 下载模型

```bash
# 下载deepseek-r1:7b模型
ollama pull deepseek-r1:7b

# 或下载qwen2:7b模型
ollama pull qwen2:7b

# 下载嵌入模型
ollama pull nomic-embed-text
```

### 3. 创建虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境 (Windows)
venv\Scripts\activate

# 激活虚拟环境 (Linux/macOS)
source venv/bin/activate
```

### 4. 安装依赖

```bash
pip install -r requirements.txt
```

### 5. 测试Ollama连接

```bash
python test_ollama.py
```

## 使用方法

### Web界面版本

```bash
streamlit run app.py
```

然后在浏览器中打开 `http://localhost:8501`

### 命令行版本

```bash
python rag_cli.py
```

## 项目结构

```
RAG-QA-System/
├── app.py                  # Streamlit Web应用
├── rag_cli.py              # 命令行版RAG问答
├── knowledge_base.py       # 知识库构建模块
├── test_ollama.py          # Ollama API测试脚本
├── requirements.txt        # 项目依赖
├── build.bat               # Windows打包脚本
├── RAG_QA_System.spec      # PyInstaller配置文件
├── README.md               # 项目说明文档
├── documents/              # 文档存放目录（需自行创建）
├── chroma_db/              # 向量数据库存储目录（自动生成）
└── temp_docs/              # 临时文档目录（自动生成）
```

## 使用流程

### 1. 准备文档

在项目根目录创建 `documents` 文件夹，放入PDF或DOCX格式的文档。

### 2. 构建知识库

#### Web界面方式：
1. 启动应用后，在左侧边栏点击"上传文档"
2. 选择PDF或DOCX文件
3. 点击"构建知识库"按钮

#### 命令行方式：
```bash
python rag_cli.py
```
系统会自动从 `documents` 文件夹读取文档并构建知识库。

### 3. 开始问答

在对话框中输入问题，系统会基于知识库内容生成回答。

## 核心功能说明

### 文档处理

- 支持PDF和DOCX格式
- 自动提取文本内容
- 使用RecursiveCharacterTextSplitter进行分块
  - chunk_size: 1000
  - chunk_overlap: 200

### 向量化存储

- 使用Ollama嵌入模型（nomic-embed-text）
- Chroma向量数据库持久化存储
- 支持增量更新

### 智能检索

- 基于语义相似度检索
- 默认返回最相关的3个文本块
- 显示参考来源

### 对话管理

- 多轮对话上下文记忆
- 对话历史展示
- 支持清空历史

## 打包为exe文件

### 使用打包脚本

```bash
# Windows系统
build.bat
```

### 手动打包

```bash
pyinstaller --onefile --windowed --name "RAG问答系统" app.py
```

打包完成后，可执行文件位于 `dist/RAG问答系统.exe`

## 测试结果

### 相关问题测试（5个）

1. **问题**: 什么是自然语言处理？
   - **回答质量**: ✓ 准确引用文档内容，解释清晰

2. **问题**: 自然语言处理有哪些应用？
   - **回答质量**: ✓ 列举了多个应用场景，有文档支持

3. **问题**: 什么是词向量？
   - **回答质量**: ✓ 定义准确，举例恰当

4. **问题**: 深度学习在NLP中有什么作用？
   - **回答质量**: ✓ 解释详细，引用相关内容

5. **问题**: 什么是Transformer模型？
   - **回答质量**: ✓ 描述准确，有文档依据

### 无关问题测试（2个）

1. **问题**: 今天天气怎么样？
   - **回答**: "文档中未找到相关答案"
   - **结果**: ✓ 正确识别无关问题

2. **问题**: 如何做红烧肉？
   - **回答**: "文档中未找到相关答案"
   - **结果**: ✓ 正确识别无关问题

## 常见问题

### Q: Ollama连接失败怎么办？
A: 确保Ollama服务正在运行，可以通过 `ollama serve` 启动服务。

### Q: 模型下载速度慢怎么办？
A: 可以尝试使用镜像源或下载较小的模型。

### Q: 内存不足怎么办？
A: 尝试使用较小的模型（如7b版本），或减少文档数量。

### Q: 如何更换模型？
A: 在Web界面的左侧边栏选择其他模型，或在代码中修改model_name参数。

## 注意事项

1. 首次运行需要下载嵌入模型，可能需要较长时间
2. 大文件处理可能需要等待
3. 建议使用Chrome或Edge浏览器获得最佳体验
4. 打包的exe文件需要在有Ollama服务的机器上运行

## 许可证

MIT License

## 作者信息

- 姓名: [您的姓名]
- 学号: [您的学号]
- 项目地址: [GitHub仓库地址]

## 致谢

感谢LangChain、Ollama、Streamlit等开源项目提供的支持。
