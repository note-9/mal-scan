from sqlmodel import Session, SQLModel, create_engine, select
from app.models import File

engine = create_engine("sqlite:///scanner.db")
SQLModel.metadata.create_all(engine)

def add_file_record(file_id: str, filename: str):
    with Session(engine) as session:
        session.add(File(id=file_id, filename=filename))
        session.commit()

def update_file_report(file_id: str, report: dict):
    with Session(engine) as session:
        file = session.exec(select(File).where(File.id == file_id)).first()
        file.report = report
        file.status = "DONE"
        session.add(file)
        session.commit()

def get_status(file_id: str):
    with Session(engine) as session:
        file = session.exec(select(File).where(File.id == file_id)).first()
        return file.status

def get_report(file_id: str):
    with Session(engine) as session:
        file = session.exec(select(File).where(File.id == file_id)).first()
        return file.report
