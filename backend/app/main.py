from fastapi import FastAPI

app = FastAPI(title="DocuSense")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "DocuSense"}