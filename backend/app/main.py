from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from app.utils.file_utils import save_upload_file
from app.services.video_service import register_video, get_video
from app.services.llm_service import answer_question_from_video
from app.models.ask_model import AskRequest
from app.models.upload_model import UploadResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"} 

@app.post("/api/videos", response_model=UploadResponse)
async def upload_video(file: UploadFile = File(...)):
    
    print("MAIN.PY LOCATION:", os.path.abspath(__file__))
    
    print("UPLOAD ENDPOINT HIT")
    
    #validate file type
    if not file.content_type or not file.content_type.startswith("video/"):
        print("NOT A VIDEO")
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a video file.")
    
    #save video
    video_id, file_path = save_upload_file(file)
    print("VIDEO SAVED:", video_id, file_path)
    
    #store it in memory 
    register_video(video_id, file.filename, file_path)
    print("REGISTERED VIDEO")
    
    response = {
        "video_id": video_id,
        "filename": file.filename,
        "path": file_path
    }
    
    print("RETURNING:", response)
    return response
    
@app.post("/api/videos/{video_id}/ask")
async def ask_about_video(video_id: str, request: AskRequest):
    video = get_video(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found.")
    
    #Call mock LLM
    answer = answer_question_from_video(video["file_path"], request.question)
    
    return {"answer": answer}