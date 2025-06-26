from fastapi import FastAPI, UploadFile, BackgroundTasks
from app import storage, scanner, db

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile, background_tasks: BackgroundTasks):
    file_id, path = storage.save_file(file)
    db.add_file_record(file_id, file.filename)
    background_tasks.add_task(run_scan, file_id, path)
    return {"file_id": file_id, "message": "File uploaded successfully"}

def run_scan(file_id: str, file_path: str):
    report = scanner.quick_scan(file_path)
    db.update_file_report(file_id, report)

@app.get("/status/{file_id}")
def check_status(file_id: str):
    return {"status": db.get_status(file_id)}

@app.get("/report/{file_id}")
def get_report(file_id: str):
    return db.get_report(file_id)
