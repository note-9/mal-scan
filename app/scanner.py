import hashlib

BAD_PATTERNS = [b"<?php", b"eval(", b"PowerShell", b"vbaProject"]

def quick_scan(file_path: str) -> dict:
    with open(file_path, "rb") as f:
        data = f.read()

    found = [p for p in BAD_PATTERNS if p in data]

    return {
        "sha256": hashlib.sha256(data).hexdigest(),
        "size_bytes": len(data),
        "bad_patterns": [p.decode(errors="ignore") for p in found],
        "num_found": len(found),
        "verdict": "MALICIOUS" if found else "CLEAN"
    }
