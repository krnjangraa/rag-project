import whisper
import os
import json
model = whisper.load_model("base")
output_folder = "transcripts_json"
os.makedirs(output_folder, exist_ok=True)
for aud in os.listdir("audio"):
    if aud.endswith(".mp3"):
        print(f"starting the transcription of {aud} file")
        result = model.transcribe(os.path.join("audio",aud))
        print(f"completed the transcription of {aud} file")
        output_path = os.path.join(output_folder, f"{aud.split('.')[0]}.json")
        
        transcript_segments = []
        print(f"starting seg nikalna of {aud} file")
        for seg in result["segments"]:
            transcript_segments.append({
                "start": seg["start"],
                "end": seg["end"],
                "text": seg["text"].strip()
            })

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(
                {"segments": transcript_segments},
                f,
                ensure_ascii=False,
                indent=4
            )

        print(f"saved {aud} ki transcript")