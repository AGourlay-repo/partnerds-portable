# Partnerds Portable (test)

Testing whether Partnerds can run on a locked-down work computer with **no install and no admin login**, like Notepad++ Portable.

**Test 3 (current):** a simple Partnerds dashboard in your browser, with sample partners, an "Ask Partnerds" chat, and a Settings page. Chat uses the built-in AI on the computer by default. Paste a Claude API key in Settings for smarter answers.

## Try it (Windows)

1. Go to the [latest release](https://github.com/AGourlay-repo/partnerds-portable/releases/latest).
2. Download **Partnerds-Folder.zip** (about 535 MB).
3. Right-click it, choose **Extract All**, and extract it to Documents or Desktop.
4. Open the **Partnerds** folder and double-click **Start Partnerds.cmd**.
5. A black window opens (keep it open) and your browser opens Partnerds a few seconds later.
   - If the browser shows "can't reach this page", wait a few seconds and refresh.
6. Wait until the bottom left says **Built-in AI ready**, go to **Ask Partnerds**, and type `hello`.

### Add your Claude API key

1. Go to **Settings** and pick **Claude (your API key)**.
2. Paste your key and click **Test connection**. If it works, you'll see a short reply.
3. Click **Save**, then try **Ask Partnerds** again. The line above the chat says which AI is answering.

Your key is saved only in that browser on that computer. **Remove key** deletes it.

### One-click version (experimental)

The release also has **Partnerds.exe**, the same thing packed into one file. Double-click it, then open **http://127.0.0.1:8765** in your browser. If it closes right away, use the folder version.

## What's inside

- **Engine:** [llamafile](https://github.com/mozilla-ai/llamafile) 0.10.6 by Mozilla (Apache 2.0). Runs the built-in AI and serves the dashboard with no install.
- **Built-in AI:** [Qwen2.5 0.5B Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF), Q4_K_M (Apache 2.0). Small and basic.
- **Dashboard:** `www/index.html`, one page with no outside downloads. Calls the built-in AI at `/v1/chat/completions` and Claude at `api.anthropic.com` when a key is saved.

Everything runs at `127.0.0.1`, so nothing on the network can reach it.

## Rebuilding the downloads

`packaging/pack.py` packs the engine, the model, the dashboard and the settings in `packaging/args.txt` into one `.exe`:

```bash
python3 packaging/pack.py llamafile-0.10.6-thin Partnerds.exe \
  qwen2.5-0.5b-instruct-q4_k_m.gguf=qwen2.5-0.5b-instruct-q4_k_m.gguf \
  www/index.html=www/index.html \
  packaging/args.txt=.args
```

The folder version is `llamafile.exe` (the engine, renamed), the model, `www/`, and `packaging/Start Partnerds.cmd`.
