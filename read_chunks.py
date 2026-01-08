import requests
import pandas as pd 
import json 
import os
def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed", json={
        "model":"bge-m3",
        "input":text_list
    })
    return r.json()["embeddings"]

jsons=os.listdir("transcripts_json")
chunk_id=0
my_dict=[]
for json_file in jsons:
    with open(os.path.join("transcripts_json",json_file)) as f:
        content=json.load(f)
    print(f"Creating embedding for {json_file}")
    text_list=(chunk["text"] for chunk in content["segments"])
    embedding=create_embedding(list(text_list))

    for i, chunk in enumerate(content["segments"]):
        chunk["chunk_id"]=chunk_id
        chunk["embedding"]=embedding[i]
        chunk_id+=1
        my_dict.append(chunk)

df=pd.DataFrame.from_records(my_dict)


print(df)
        





