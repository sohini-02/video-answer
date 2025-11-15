# 🎥 Video Answering System  
AI-powered video understanding using FastAPI + Google Gemini

This project is a full-stack AI application that allows users to **upload a video** and **ask natural language questions** about what is happening in that video.  
The backend uses **FastAPI** and **Gemini 2.0 Flash** to analyze video content and return intelligent, context-aware answers.

---

## Features

### Video Upload  
Upload `.mp4` videos directly through the backend API or from the upcoming frontend UI.

### AI Video Question Answering  
Ask any natural-language question about an uploaded video.  
Uses Google’s latest **Gemini Flash** model to interpret the video and respond with accurate, detailed answers.

### Modular Architecture  
- Clean folder structure  
- Separate services for LLM + video storage  
- Easy to extend (summaries, frame extraction, subtitles, etc.)

### Ready for Frontend Integration  
The `frontend/` folder is prepared for:
- Simple HTML/CSS/JS  
- or React + Vite + Tailwind

---

## Tech Stack

### Backend
- Python 3.11
- FastAPI
- Uvicorn
- Google Generative AI SDK (Gemini)
- python-dotenv

### Frontend (To Be Built)
- React or HTML/CSS/JS

---

## Project Structure

video-answer/
│
├── backend/
│ ├── app/
│ │ ├── main.py # FastAPI entrypoint
│ │ ├── models/
│ │ │ ├── upload_model.py # Response model for video upload
│ │ │ └── ask_model.py # Request model for Q&A
│ │ ├── services/
│ │ │ ├── video_service.py # Saving + registering videos
│ │ │ └── llm_service.py # Gemini model integration
│ │ └── init.py
│ │
│ ├── videos/ # Uploaded videos (auto-created)
│ ├── venv/ # Virtual environment (ignored)
│ └── .env # Contains GEMINI_API_KEY (ignored)
│
├── frontend/ # UI will be built here
│
└── README.md


Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/sohini-02/video-answer.git
cd video-answer/backend

2. Create a virtual environment
python -m venv venv

Activate it:
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

pip freeze > requirements.txt

4. Add your Gemini API key
Create:
backend/.env

Add your key:
GEMINI_API_KEY=YOUR_REAL_KEY_HERE

5. Run the FastAPI server

From inside the backend/ folder:

uvicorn app.main:app --reload
API will be live at:
http://127.0.0.1:8000

Interactive Swagger docs:
http://127.0.0.1:8000/docs


📌 API Documentation
🔹 POST /api/videos
Upload a video.

Form Data
file: .mp4 file

Response
{
  "video_id": "example-uuid",
  "filename": "sample.mp4",
  "path": "videos/example-uuid.mp4"
}
🔹 POST /api/videos/{video_id}/ask

Ask a question about a previously uploaded video.
{
  "question": "What is the person doing?"
}
Response Example
{
  "answer": "The person is sitting at a desk adjusting their camera."
}

Environment Variables

Your backend requires:
GEMINI_API_KEY=your_key_here


Optional future variables:

MODEL_NAME=gemini-2.0-flash
VIDEO_FOLDER=videos

🔮 Future Enhancements: 
> Video summarization feature
> Speech-to-text transcription
> Keyframe extraction
> Full UI (React + Tailwind)
> Deployment to Railway / Render / Cloud Run
> Support for local LLMs
> Database for video metadata and Q/A logs

🧑‍💻 Contributing
Pull requests and suggestions are welcome!

📄 License
MIT License.

✨ Author
Sohini Mazumder
Building intelligent multimodal AI tools for real video understanding.