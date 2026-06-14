@echo off
echo ========================================
echo RAG问答系统打包脚本
echo ========================================
echo.

echo 正在清理旧的打包文件...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.spec del /q *.spec

echo.
echo 正在打包应用...
pyinstaller --onefile --windowed --name "RAG问答系统" --add-data "requirements.txt;." app.py

echo.
echo ========================================
echo 打包完成！
echo 可执行文件位于: dist\RAG问答系统.exe
echo ========================================
pause
