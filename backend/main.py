from fastapi import FastAPI

app = FastAPI(title = "AI Commerce Agent")

@app.get("/")
def root():
    return {"message" : "AI Commerce is running "}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
