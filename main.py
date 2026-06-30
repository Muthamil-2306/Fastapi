# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI

app = FastAPI()

# Use a dictionary instead of a list
store = {}

@app.get("/")
def getting():
    print("method work")
    return {"message": "GET method works"}

@app.post("/inserting")
def adding(key: str, value: str):
    store[key] = value
    return store

@app.put("/updating")
def updating(key: str, value: str):
    if key in store:
        store[key] = value
        return store
    return {"error": "Key not found"}

@app.delete("/deleting")
def deleting(key: str):
    if key in store:
        store.pop(key)
        return store
    return {"error": "Key not found"}

    
    


#Start Command
#uvicorn main:app --host 0.0.0.0 --port $PORT