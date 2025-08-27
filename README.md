# AI Reel Creator

## Description
AI Reel Creator is a Flask web app that generates social media video reels from user-uploaded images and text. It uses the ElevenLabs API for text-to-speech and FFmpeg to create 1080x1920 MP4 videos with audio narration.

## Features
- Upload images and text to create reels
- AI-generated audio from text
- Automated video creation
- Gallery to view reels

## Technologies
- Python, Flask
- ElevenLabs API
- FFmpeg
- HTML, Bootstrap

## Setup
1. Clone: `git clone https://github.com/your-username/ai-reel-creator.git`
2. Create a "user_uploads" file to store the pictures,Ai audio, Input.txt.
3. Install: `pip install -r requirements.txt`
4. Add ElevenLabs API key in `config.py`
5. Install FFmpeg and add to PATH
6. Run: `python main.py` and `python generate_process.py`

## Usage
- Go to `/create` to upload images and text
- View reels at `/gallery`
