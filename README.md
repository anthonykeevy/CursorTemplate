# CursorTemplate

A Python project template for rapid development with Cursor IDE.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/anthonykeevy/CursorTemplate.git
   cd CursorTemplate
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows:
   .\venv\Scripts\Activate.ps1
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📁 Project Structure

```
CursorTemplate/
├── src/                    # Source code
│   ├── __init__.py
│   └── main.py
├── tests/                  # Test files
│   ├── __init__.py
│   └── test_main.py
├── venv/                   # Virtual environment (created locally)
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🛠️ Development

### Running the Application
```bash
python src/main.py
```

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black src/ tests/
```

### Linting
```bash
flake8 src/ tests/
```

## 🔧 Configuration

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your configuration values.

## 📝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

If you have any questions or need help, please open an issue on GitHub.
