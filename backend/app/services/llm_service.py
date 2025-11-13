import google.generativeai as genai
import os

#for m in genai.list_models():
    #print(m.name)

# Load API key into Gemini client
genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

def answer_question_from_video(video_path: str, question: str) -> str:
    try:
        # Read video bytes
        with open(video_path, "rb") as f:
            video_bytes = f.read()
            
        # Using Gemini
        model = genai.GenerativeModel("gemini-flash-latest")
        
        # video and question as multimodal input
        response = model.generate_content([
            {"mime_type": "video/mp4", "data": video_bytes},
            question
        ])
        
        return response.text or "(No text returned)"
    
    except Exception as e:
        return f"Error: {str(e)}"