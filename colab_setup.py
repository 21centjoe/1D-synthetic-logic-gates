#!/usr/bin/env python3
"""
Colab Setup Script for 1D Synthetic Logic Gates
Links to: Linux_to_NELOS_OVERLAY_ipynb.ipynb
GitHub: https://github.com/21centjoe/1D-synthetic-logic-gates
"""

import subprocess
import sys

def setup_colab():
    """Install dependencies and configure Gemini API for Colab"""
    
    print("🚀 Setting up Colab environment...")
    
    # Install required packages
    packages = [
        "google-generativeai",
        "pandas",
        "numpy",
        "matplotlib",
        "ipywidgets",
    ]
    
    for package in packages:
        print(f"📦 Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])
    
    print("\n✅ Dependencies installed!")
    print("\n📝 Next steps:")
    print("1. Add GOOGLE_API_KEY to Colab Secrets (🔑 icon on left)")
    print("2. Run this cell to configure Gemini:")
    print("""
from google.colab import userdata
import google.generativeai as genai

api_key = userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
print("✅ Gemini configured!")
    """)
    print("\n📚 Open your notebook:")
    print("https://github.com/21centjoe/1D-synthetic-logic-gates/blob/main/Linux_to_NELOS_OVERLAY_ipynb.ipynb")

if __name__ == "__main__":
    setup_colab()
