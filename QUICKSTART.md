# 快速开始指南

## 第一步：安装Ollama

1. 访问 https://ollama.ai 下载Ollama
2. 安装完成后，打开命令行，运行以下命令下载模型：

```bash
ollama pull deepseek-r1:7b
ollama pull nomic-embed-text
```

## 第二步：安装Python环境

1. 双击运行 `install.bat` 脚本
2. 等待安装完成

或者手动安装：

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

## 第三步：测试Ollama连接

```bash
python test_ollama.py
```

如果看到"Ollama API连接成功"，说明环境配置正确。

## 第四步：准备文档

1. 将PDF或DOCX文档放入 `documents` 文件夹
2. 建议至少准备5份与"自然语言处理技术"相关的文档

## 第五步：启动应用

### Web界面版本（推荐）

双击运行 `start.bat` 或在命令行运行：

```bash
streamlit run app.py
```

然后在浏览器中打开 http://localhost:8501

### 命令行版本

```bash
python rag_cli.py
```

## 第六步：使用系统

### Web界面使用流程

1. 在左侧边栏点击"上传文档"，选择PDF或DOCX文件
2. 点击"构建知识库"按钮
3. 在对话框中输入问题
4. 查看回答和参考来源

### 命令行使用流程

1. 将文档放入 `documents` 文件夹
2. 运行 `python rag_cli.py`
3. 系统会自动构建知识库
4. 输入问题进行问答

## 常见问题

### Q: Ollama连接失败？

A: 确保Ollama服务正在运行：
```bash
ollama serve
```

### Q: 模型下载慢？

A: 可以尝试使用国内镜像或下载较小的模型。

### Q: 内存不足？

A: 尝试使用较小的模型，或减少文档数量。

### Q: 如何打包为exe？

A: 运行 `build.bat` 脚本，打包后的文件在 `dist` 文件夹中。

## 项目文件说明

| 文件名 | 说明 |
|--------|------|
| app.py | Streamlit Web应用主程序 |
| rag_cli.py | 命令行版RAG问答程序 |
| knowledge_base.py | 知识库构建模块 |
| test_ollama.py | Ollama API测试脚本 |
| requirements.txt | 项目依赖列表 |
| install.bat | 环境安装脚本 |
| start.bat | 应用启动脚本 |
| build.bat | 打包脚本 |
| README.md | 项目说明文档 |
| TEST_REPORT.md | 测试报告 |

## 技术支持

如有问题，请查看 README.md 文档或提交Issue。
