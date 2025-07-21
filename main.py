"""
Main entry point for Railway deployment
"""

import sys
import os

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the simple app
from app import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting SMS API on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)