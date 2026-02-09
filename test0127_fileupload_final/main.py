from fastapi import FastAPI,UploadFile,File
from pathlib import Path
from fastapi.responses import HTMLResponse, FileResponse
import shutil


app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {"png","jpg","jpeg","gif","webp"}
MAX_FILE_SIZE = 10 * 1024 * 1024    ## 10mb

@app.get("/", response_class=HTMLResponse)
def main():
    html= """
    <body>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file" />
            <button type ="submit">등록</button>
        </form>
    </body>   
    """
    return html

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        "message": "업로드 완료",
        "filename": file.filename,
    }
## upload 확인하는 방법 : http://localhost:8000/upload

@app.get("/download")
async def download_image(filename: str):
    file_path = UPLOAD_DIR / filename
    return FileResponse(path=file_path, filename=filename)