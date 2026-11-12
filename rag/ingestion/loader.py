from pathlib import Path

def get_content():
    current_dir = Path(__file__).resolve().parent
    source_path = current_dir.parent.parent / "source" / "source.txt"
    with open(source_path, "r", encoding="utf-8") as source:
        return source.read()