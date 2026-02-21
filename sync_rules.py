import subprocess
from pathlib import Path
import shutil

def sync_kilo():
    subprocess.run(["rulesync", "generate", "--targets", "kilo", "--features", "rules", "--verbose"], check=True, shell=True)
    src = Path(".rulesync/rules")
    dst = Path(".kilocode/rules")
    dst.mkdir(parents=True, exist_ok=True)
    for f in src.glob("*.md"):
        shutil.copy2(f, dst)
    print("[OK] Kilo rules synced")

if __name__ == "__main__":
    sync_kilo()
