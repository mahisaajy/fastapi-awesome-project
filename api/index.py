import sys
from pathlib import Path

# Add parent directory to Python path so we can import main.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import app
