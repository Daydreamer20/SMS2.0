"""
Simple SMS API for Railway deployment
"""

import os
import psycopg2
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="SMS API", version="1.0.0")

# Database connection
DATABASE_URL = os.environ.get("DATABASE_URL")

class SMSMessage(BaseModel):
    phone: str
    message: str

@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "SMS API is running", "status": "ok"}

@app.get("/health")
def health_check():
    """Health check endpoint for Railway"""
    try:
        # Test database connection if available
        if DATABASE_URL:
            conn = psycopg2.connect(DATABASE_URL)
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            cursor.close()
            conn.close()
            db_status = "connected"
        else:
            db_status = "no_database_configured"
        
        return {
            "status": "healthy",
            "database": db_status,
            "message": "Service is running"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "connection_failed",
            "error": str(e)
        }

@app.post("/send-sms")
def send_sms(sms: SMSMessage):
    """Send SMS endpoint (placeholder)"""
    return {
        "status": "success",
        "message": f"SMS would be sent to {sms.phone}: {sms.message}",
        "phone": sms.phone
    }

@app.get("/init-db")
def init_database():
    """Initialize database tables"""
    if not DATABASE_URL:
        raise HTTPException(status_code=500, detail="No database URL configured")
    
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        
        # Create a simple messages table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id SERIAL PRIMARY KEY,
                phone VARCHAR(20) NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return {
            "status": "success",
            "message": "Database initialized successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to initialize database: {str(e)}")

@app.get("/env")
def show_environment() -> Dict[str, Any]:
    """Show environment variables (excluding sensitive ones)"""
    env_vars = {}
    for key, value in os.environ.items():
        # Skip sensitive variables
        if any(sensitive in key.lower() for sensitive in ["password", "secret", "key", "token"]):
            env_vars[key] = "***REDACTED***"
        else:
            env_vars[key] = value
    return {"environment_variables": env_vars}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting server on port {port}")
    print(f"Database URL exists: {bool(DATABASE_URL)}")
    uvicorn.run(app, host="0.0.0.0", port=port)