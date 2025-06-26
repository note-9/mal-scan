import uuid
import os
from fastapi import UploadFile

UPLOAD_DIR = 'uploads'
def save_file(file: UploadFile) -> tuple[str, str]:
    file_id = str(uuid.uuid4())
    extension = file.filename.split('.')[-1]
    saved_path = os.path.join(UPLOAD_DIR, f"{file_id}.{extension}")

    with open(saved_path, "wb") as out_file:
        content = file.file.read()
        out_file.write(content)

    return file_id, saved_path