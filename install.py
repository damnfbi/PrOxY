import subprocess
import sys
import os

def install_requirements():
    print("installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def create_directories():
    print("creating directory structure...")
    os.makedirs("success", exist_ok=True)
    os.makedirs("utils", exist_ok=True)

if __name__ == "__main__":
    install_requirements()
    create_directories()
    print("setup completed successfully")
    print("run 'python main.py' to start scraping")