"""Embed files into a llamafile exe as stored, page-aligned zip entries (what zipalign -j0 does)."""
import os, sys, zipfile, struct, shutil
engine, out, *files = sys.argv[1:]
shutil.copyfile(engine, out)
ALIGN = 65536
with zipfile.ZipFile(out, "a", compression=zipfile.ZIP_STORED) as z:
    for path, arcname in (f.split("=") for f in files):
        info = zipfile.ZipInfo(arcname, date_time=(2026, 11, 8, 0, 0, 0))
        info.compress_type = zipfile.ZIP_STORED
        info.external_attr = 0o644 << 16
        info.file_size = os.path.getsize(path)
        start = z.start_dir
        base = start + 30 + len(arcname.encode())
        pad = (-(base + 4)) % ALIGN
        info.extra = struct.pack("<HH", 0xFFFF, pad) + b"\0" * pad
        with open(path, "rb") as src, z.open(info, "w") as dst:
            shutil.copyfileobj(src, dst, 1 << 20)
        print(arcname, "data offset", base + 4 + pad, "aligned", (base + 4 + pad) % ALIGN == 0)
