from datetime import datetime
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/time")
def get_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
