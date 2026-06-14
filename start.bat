@echo off
echo ========================================
echo RAG问答系统启动脚本
echo ========================================
echo.

echo 正在检查Ollama服务...
curl -s http://localhost:11434/api/tags >nul 2>&1
if %errorlevel% neq 0 (
    echo [警告] Ollama服务未运行
    echo 请先启动Ollama服务: ollama serve
    echo.
)

echo 正在启动Streamlit应用...
echo.
streamlit run app.py

pause
