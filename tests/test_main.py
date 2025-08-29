"""
Tests for the main application module.
"""

import pytest
import os
import sys
from unittest.mock import patch

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import greet_user, get_environment_info


class TestGreetUser:
    """Test cases for the greet_user function."""
    
    def test_greet_user_with_name(self):
        """Test greeting with a specific name."""
        result = greet_user("Alice")
        assert result == "Hello, Alice! Welcome to CursorTemplate! 🚀"
    
    def test_greet_user_without_name(self):
        """Test greeting without a name (should use default)."""
        result = greet_user()
        assert result == "Hello, World! Welcome to CursorTemplate! 🚀"
    
    def test_greet_user_with_none(self):
        """Test greeting with None (should use default)."""
        result = greet_user(None)
        assert result == "Hello, World! Welcome to CursorTemplate! 🚀"
    
    @patch.dict(os.environ, {'USER_NAME': 'TestUser'})
    def test_greet_user_with_env_variable(self):
        """Test greeting with environment variable."""
        result = greet_user()
        assert result == "Hello, TestUser! Welcome to CursorTemplate! 🚀"


class TestGetEnvironmentInfo:
    """Test cases for the get_environment_info function."""
    
    def test_get_environment_info_structure(self):
        """Test that environment info returns expected structure."""
        result = get_environment_info()
        
        assert isinstance(result, dict)
        assert "python_version" in result
        assert "platform" in result
        assert "working_directory" in result
        assert "environment" in result
    
    def test_get_environment_info_python_version(self):
        """Test that python_version is correctly set."""
        result = get_environment_info()
        assert result["python_version"] == sys.version
    
    def test_get_environment_info_platform(self):
        """Test that platform is correctly set."""
        result = get_environment_info()
        assert result["platform"] == sys.platform
    
    def test_get_environment_info_working_directory(self):
        """Test that working directory is correctly set."""
        result = get_environment_info()
        assert result["working_directory"] == os.getcwd()
    
    @patch.dict(os.environ, {'ENVIRONMENT': 'production'})
    def test_get_environment_info_with_env_variable(self):
        """Test environment info with environment variable set."""
        result = get_environment_info()
        assert result["environment"] == "production"
    
    def test_get_environment_info_default_environment(self):
        """Test environment info with default environment."""
        # Clear any existing ENVIRONMENT variable
        with patch.dict(os.environ, {}, clear=True):
            result = get_environment_info()
            assert result["environment"] == "development"


if __name__ == "__main__":
    pytest.main([__file__])
