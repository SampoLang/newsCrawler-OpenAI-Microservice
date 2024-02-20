from fastapi import FastAPI
#create main instance of FastAPI
app = FastAPI()
#decorator to define the path and method
@app.get("/")
def read_root():
    return {"Hello": "World"}
