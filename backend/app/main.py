from fastapi import FastAPI

app = FastAPI(
    title="AI Code Review System",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "AI Code Review System is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }