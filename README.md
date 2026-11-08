# Partnerds Portable (test)

A tiny test: can a work computer run Partnerds' own AI with **no install and no admin login**, like Notepad++ Portable?

This first version is just a chat window with a very small AI model built in. It runs entirely on the computer. Nothing is sent to the internet.

## Try it (Windows)

1. Go to the [latest release](https://github.com/AGourlay-repo/partnerds-portable/releases/latest).
2. Download **Partnerds-Chat-Test.exe** (about 535 MB).
3. Double-click it.
   - If Windows says "Windows protected your PC", click **More info**, then **Run anyway**.
4. A black window opens and loads the model (give it 10 to 30 seconds).
5. Type `hello` and press Enter.

**If it answers, it works.** Close the window to quit.

### If the .exe gets blocked

Try the backup version:

1. Download **Partnerds-Chat-Folder.zip** from the same release.
2. Right-click it, choose **Extract All**, and extract it somewhere you can save files, like Documents or Desktop.
3. Open the folder and double-click **Start Partnerds Chat.cmd**.

### What to note down

- Did it open at all? If not, what message did Windows show?
- Did it answer "hello"?
- Roughly how long did it take to answer?

## What's inside

- **Chat engine:** [llamafile](https://github.com/mozilla-ai/llamafile) 0.10.6 by Mozilla (Apache 2.0). One file that runs on Windows, Mac and Linux with no install.
- **AI model:** [Qwen2.5 0.5B Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF), Q4_K_M (Apache 2.0). Small enough to run on an ordinary work laptop. It's good for a "hello" test and quick answers, not deep work.

## Rebuilding the download

`packaging/pack.py` puts the engine, the model and the settings in `packaging/args.txt` into one `.exe`:

```bash
python3 packaging/pack.py llamafile-0.10.6-thin Partnerds-Chat-Test.exe \
  qwen2.5-0.5b-instruct-q4_k_m.gguf=qwen2.5-0.5b-instruct-q4_k_m.gguf \
  packaging/args.txt=.args
```
