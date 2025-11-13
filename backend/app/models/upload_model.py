from pydantic import BaseModel

class UploadResponse(BaseModel):
    video_id: str
    filename: str
    path: str