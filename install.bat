@echo off
echo ========================================
echo RAG问答系统 - 环境安装脚本
echo ========================================
echo.

echo [步骤 1/4] 检查Python版本...
python --version
if %errorlevel% neq 0 (
    echo [错误] 未检测到Python，请先安装Python 3.8+
    pause
    exit /b 1
)
echo.

echo [步骤 2/4] 创建虚拟环境...
if exist venv (
    echo 虚拟环境已存在，跳过创建
) else (
    python -m venv venv
    echo 虚拟环境创建成功
)
echo.

echo [步骤 3/4] 激活虚拟环境并安装依赖...
call venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
echo.

echo [步骤 4/4] 测试Ollama连接...
python test_ollama.py
echo.

echo ========================================
echo 安装完成！
echo ========================================
echo.
echo 下一步操作：
echo 1. 确保Ollama已安装并运行
echo 2. 下载模型: ollama pull deepseek-r1:7b
echo 3. 下载嵌入模型: ollama pull nomic-embed-text
echo 4. 将PDF/DOCX文档放入 documents 文件夹
echo 5. 运行 start.bat 启动应用
echo.
pause
