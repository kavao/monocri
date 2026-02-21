import shutil
from pathlib import Path

def howto_init():
    src = Path("_how_to.example")
    dst = Path("_how_to")

    if not src.exists():
        print(f"Error: Source directory '{src}' does not exist.")
        return

    if not dst.exists():
        print(f"Creating destination directory '{dst}'...")
        dst.mkdir(parents=True, exist_ok=True)

    print(f"Copying template files from '{src}' to '{dst}' (without overwriting existing files)...")

    # Copy files that don't exist in destination
    for item in src.iterdir():
        if item.is_file():
            target_path = dst / item.name
            if not target_path.exists():
                print(f"  Copying {item.name}")
                shutil.copy2(item, target_path)
            else:
                print(f"  Skipping {item.name} (already exists)")

    print("\nInitialization finished.")

if __name__ == "__main__":
    howto_init()
