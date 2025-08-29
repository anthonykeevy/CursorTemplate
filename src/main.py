#!/usr/bin/env python3
"""
Main application entry point for CursorTemplate.
"""

import os
import sys
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def greet_user(name: Optional[str] = None) -> str:
    """
    Greet the user with a personalized message.
    
    Args:
        name: Optional name to greet. If None, uses environment variable or default.
        
    Returns:
        Greeting message string.
    """
    if name is None:
        name = os.getenv("USER_NAME", "World")
    
    return f"Hello, {name}! Welcome to CursorTemplate! 🚀"


def get_environment_info() -> dict:
    """
    Get information about the current environment.
    
    Returns:
        Dictionary containing environment information.
    """
    return {
        "python_version": sys.version,
        "platform": sys.platform,
        "working_directory": os.getcwd(),
        "environment": os.getenv("ENVIRONMENT", "development"),
    }


def main():
    """Main application function."""
    print("=" * 50)
    print("🎉 CursorTemplate - Python Project Template")
    print("=" * 50)
    
    # Greet the user
    greeting = greet_user()
    print(f"\n{greeting}")
    
    # Display environment information
    env_info = get_environment_info()
    print(f"\n📋 Environment Information:")
    print(f"   Python Version: {env_info['python_version']}")
    print(f"   Platform: {env_info['platform']}")
    print(f"   Working Directory: {env_info['working_directory']}")
    print(f"   Environment: {env_info['environment']}")
    
    print(f"\n✨ Your Python environment is ready for development!")
    print("=" * 50)


if __name__ == "__main__":
    main()
