from fastapi import FastAPI

app = FastAPI(
    title="Aegis API",
    description="AI Agent Red Teaming & Certification Platform",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "project": "Aegis",
        "message": "AI Agent Red Teaming & Certification Platform"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "version": "1.0.0"
    }