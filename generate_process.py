import os 
from text_to_audio import text_to_speech_file
import time
import subprocess


def text_to_audio(folder):
    print("TTA - ", folder)
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
    print(text, folder)
    text_to_speech_file(text, folder)


def create_reel(folder):
    input_txt = os.path.join("user_uploads", folder, "input.txt").replace("\\", "/")
    audio_mp3 = os.path.join("user_uploads", folder, "audio.mp3").replace("\\", "/")
    output_mp4 = os.path.join("static", "reels", f"{folder}.mp4").replace("\\", "/")
    command = (
        f'ffmpeg -f concat -safe 0 -i "{input_txt}" -i "{audio_mp3}" '
        f'-vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" '
        f'-c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p "{output_mp4}"'
    )
    print(f"Running FFmpeg command: {command}")
    subprocess.run(command, shell=True, check=True)
    print(f"CR - Created reel for: {folder}")

if __name__ == "__main__":
    while True:
        print("Processing queue...")
        with open("done.txt", "r") as f:
            done_folders = f.readlines()

        done_folders = [f.strip() for f in done_folders]
        folders = os.listdir("user_uploads") 
        for folder in folders:
            if(folder not in done_folders): 
                text_to_audio(folder) 
                create_reel(folder) 
                with open("done.txt", "a") as f:
                    f.write(folder + "\n")
        time.sleep(4)