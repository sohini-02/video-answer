import os
from uuid import uuid4
from fastapi import UploadFile

UPLOAD_DIR = "videos"

def save_upload_file(file: UploadFile) -> tuple[str, str]:
    #Create folder if missing
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    
    #Generate unique video ID
    video_id = str(uuid4())
    
    #Extract extension (.mp4, .mov, etc.)
    ext = os.path.splitext(file.filename)[1]
    
    #Construct filename
    new_filename = f"{video_id}{ext}"
    
    #Full path on disk
    file_path = os.path.join(UPLOAD_DIR, new_filename)
    
    #Save file to disk
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
        
    return video_id, file_path