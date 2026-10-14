from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import create_tables
from routes.reviews import router as reviews_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables on startup
    try:
        create_tables()
        print("Database tables created or verified successfully.")
    except Exception as e:
        print(f"Warning during database initialization: {e}")
    yield 
    print("Application shutdown. Cleanup tasks completed.")

app = FastAPI(
    title="Rangmanch Reviews API",
    description="Theatre Reviews API for Pune Rangmanch",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for frontend integrations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reviews_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Rangmanch Reviews API!",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
def health():
    return {"status": "ok"}