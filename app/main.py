from fastapi import FastAPI

app=FastAPI(
    title="AI Powered DevSecOps Assistant",
    description="AI assistant for CI/CD diagnostics and security analysis",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "AI-powered DevSecOps Assistant is running!"
    }

@app.get("/health")
def health():
    return{"status":"healthy"}