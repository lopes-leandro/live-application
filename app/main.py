from fastapi import FastAPI

app = FastAPI(
    title="Live Application"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}