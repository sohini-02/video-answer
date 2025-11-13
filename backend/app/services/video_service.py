#store in_memory 
video_store = {}

def register_video(video_id: str, filename: str, file_path: str):
    video_store[video_id] = {
        "filename": filename,
        "file_path": file_path,
        "status": "ready"
    }
    
def get_video(video_id: str):
    return video_store.get(video_id)