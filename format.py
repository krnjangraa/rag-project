import json 
import os
i=0
for files in os.listdir("transcripts_json"):
    i+=1
    with open(os.path.join("transcripts_json",files),"r") as f:
        data=json.load(f)
        texts=[]
        title = os.path.splitext(files)[0]
        for segment in data["segments"]:
            segment["title"]=title
            segment["number"]=i
            texts.append(segment["text"])
        data["title"]=title
        data["number"]=i
        data["text"]=texts
    with open(os.path.join("transcripts_json",files),"w") as f:
        json.dump(data,f, indent=4)


