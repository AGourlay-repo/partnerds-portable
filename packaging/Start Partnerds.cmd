@echo off
title Partnerds - keep this window open while you use Partnerds
cd /d "%~dp0"
echo Starting Partnerds. Your browser will open in a few seconds.
echo Keep this window open while you use Partnerds. Close it to quit.
start "" cmd /c "ping -n 6 127.0.0.1 >nul & start http://127.0.0.1:8765"
llamafile.exe --server --host 127.0.0.1 --port 8765 --path www -m qwen2.5-0.5b-instruct-q4_k_m.gguf -c 4096
pause
