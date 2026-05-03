"""
Backend API entry point. FastAPI app with /api/health and clean router registration.
Run with: uvicorn backend.app:app --reload
"""
from fastapi import FastAPI

app = FastAPI(
    title="MindixoAI API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


def register_routers(app: FastAPI) -> None:
    """Register API routers from backend modules. Extend here for new modules."""
    # Example: app.include_router(some_router, prefix="/api/some", tags=["some"])
    pass


# Apply router registration (no-op until modules add API routers)
register_routers(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=True)
