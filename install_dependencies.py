#!/usr/bin/env python3
"""
DADBOT v4 Portable - Dependency Installer
Run this script to install all required Python packages.
"""

import subprocess
import sys
import os

def main():
    print("=" * 60)
    print("DADBOT v4 Portable - Installing Dependencies")
    print("=" * 60)
    print()
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    requirements_file = os.path.join(script_dir, 'requirements.txt')
    
    # Upgrade pip first
    print("Upgrading pip...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    
    # Install from requirements.txt
    print("\nInstalling dependencies from requirements.txt...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
    
    print()
    print("=" * 60)
    print("All dependencies installed successfully!")
    print("=" * 60)
    print()
    print("You can now run the application with:")
    print("  - Double-click START_DADBOT.bat")
    print("  - Or run: python run.py")
    print()
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
