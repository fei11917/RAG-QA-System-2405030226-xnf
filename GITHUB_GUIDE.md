# GitHub仓库创建与提交指南

## 步骤1：创建GitHub仓库

1. 登录GitHub账号
2. 点击右上角的 "+" 按钮，选择 "New repository"
3. 填写仓库信息：
   - Repository name: `RAG-QA-System-姓名-学号`
   - Description: 基于LangChain和Ollama的本地知识库问答系统
   - 选择 Public（公开）
   - 不要勾选 "Add a README file"（我们已经有了）
   - 不要勾选 "Add .gitignore"（我们已经有了）
4. 点击 "Create repository"

## 步骤2：初始化本地Git仓库

在项目根目录打开命令行，执行以下命令：

```bash
# 初始化Git仓库
git init

# 添加所有文件到暂存区
git add .

# 创建第一次提交
git commit -m "初始提交：RAG问答系统完整代码"

# 添加远程仓库
git remote add origin https://github.com/你的用户名/RAG-QA-System-姓名-学号.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

## 步骤3：验证提交

1. 刷新GitHub仓库页面
2. 确认所有文件都已上传
3. 检查README.md是否正确显示

## 需要提交的文件

确保以下文件都已提交：

- [x] app.py - Streamlit Web应用
- [x] rag_cli.py - 命令行版RAG问答
- [x] knowledge_base.py - 知识库构建模块
- [x] test_ollama.py - Ollama测试脚本
- [x] requirements.txt - 项目依赖
- [x] README.md - 项目说明文档
- [x] QUICKSTART.md - 快速开始指南
- [x] TEST_REPORT.md - 测试报告
- [x] .gitignore - Git忽略文件
- [x] config.ini - 配置文件
- [x] install.bat - 安装脚本
- [x] start.bat - 启动脚本
- [x] build.bat - 打包脚本
- [x] RAG_QA_System.spec - PyInstaller配置
- [x] documents/README.md - 文档说明

## 注意事项

1. **不要提交以下文件/文件夹**：
   - venv/ (虚拟环境)
   - __pycache__/ (Python缓存)
   - chroma_db/ (向量数据库)
   - temp_docs/ (临时文件)
   - build/ (打包临时文件)
   - dist/ (打包输出文件)
   - *.pyc (编译文件)

2. **确保.gitignore文件存在**，它会自动忽略不需要提交的文件

3. **文档样例**：
   - 如果有示例文档，可以放在 documents/ 文件夹
   - 但不要提交过大的文档文件

## 更新仓库

如果后续有修改，使用以下命令更新：

```bash
# 查看修改状态
git status

# 添加修改的文件
git add .

# 提交修改
git commit -m "更新说明"

# 推送到GitHub
git push
```

## 仓库地址示例

```
https://github.com/你的用户名/RAG-QA-System-张三-2025011
```

## 提交检查清单

- [ ] 仓库命名格式正确
- [ ] 所有必需文件已提交
- [ ] README.md内容完整
- [ ] 代码可以正常运行
- [ ] 没有提交敏感信息
- [ ] .gitignore配置正确
