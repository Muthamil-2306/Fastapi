# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI


app = FastAPI()


lst=[]


@app.get("/")
def getting():
    print("method  work")
    return "get method was work"
@app.post("/inserting")
def addind(inp:str):
    a="vebbox"
    lst.append(inp)
    return lst
@app.put("/updating")
def up(ind:int,inp:str):
    lst[ind] = inp
    return lst
@app.delete("/deleting")
def dele(ind:int):
    lst.pop(ind)
    return lst
    
    
    


#Start Command
#uvicorn main:app --host 0.0.0.0 --port $PORT