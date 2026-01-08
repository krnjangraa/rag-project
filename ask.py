import numpy as np
import pandas as pd 
import json 
import requests
from sklearn.metrics.pairwise import cosine_similarity

def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed", json={
        "model":"bge-m3",
        "input":text_list
    })
    return r.json()["embeddings"]
df=pd.read_json("output_chunks.json")
incoming=input("Ask a question:")
sim=cosine_similarity(np.vstack(df["embedding"]),np.vstack(create_embedding([incoming])))
top=5
max_indx=sim.flatten().argsort()[::-1][0:top]
new_df=df.loc[max_indx]
prompt=f'''
here are video chunks data containing chunk id, start time, end time , text at that time, video number, embedding :
{new_df[["start","end","text","number","chunk_id"]].to_json()}
-------------------------------------------------------------------------------------------------------------------------------------
{incoming}
User asked this question related to the video chunks you have to tell where and how much content is taught where (in the video at which 
time stamp) and guide the user to go to that particular video , if user asks unrealted course tell him u can only give answers regarding 
the data in videos given
'''

with open("prompt.txt", "w") as f:
    f.write(prompt)



