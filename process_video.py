import os 
import subprocess

input_folder="video"
output_folder="audio"
os.makedirs(output_folder,exist_ok=True)

for vid in os.listdir(input_folder):
    if vid.lower().endswith(".mp4"):
        input_path=os.path.join(input_folder,vid)
        aud=os.path.splitext(vid)[0]+".mp3"
        output_path=os.path.join(output_folder,aud)

        command=[
            "ffmpeg",
            "-i", input_path,
            output_path
        ]
        print(f"Converting {input_path} to {output_path}")
        subprocess.run(command)
print("All videos are converted to mp3")
