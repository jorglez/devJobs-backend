from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_first():
    return {"message": "La wea jala"}