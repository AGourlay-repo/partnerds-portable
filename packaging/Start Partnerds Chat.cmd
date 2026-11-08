@echo off
title Partnerds Chat Test
cd /d "%~dp0"
llamafile.exe -m qwen2.5-0.5b-instruct-q4_k_m.gguf -c 4096 --temp 0.7 -sys "You are Partnerds, a friendly assistant for non-profit partnership staff. Keep answers short."
pause
