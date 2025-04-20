# Resume Parser AI

A modern web application that extracts structured information from PDF resumes with high accuracy.

## Overview

Resume Parser AI is a Flask-based web application designed to streamline the process of parsing and managing resumes. It automatically extracts key information such as contact details, skills, and work experience from PDF resumes, making it easier to organize and search through multiple candidates.

The application uses advanced text extraction techniques and pattern matching to reliably parse resume content, storing the structured data in a SQLite database for easy access and searching. With its modern, user-friendly interface, it's perfect for recruiters, HR professionals, or anyone who needs to manage multiple resumes efficiently.

![Resume Parser Screenshot]
(Add a screenshot of your application here)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/resume_parser_AI.git
cd resume_parser_AI

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

```python
# Start the Flask application
python app.py

# The application will be available at http://localhost:5000
```

## Features

- **PDF Resume Upload**: Secure file upload with support for PDF files up to 16MB
- **Intelligent Information Extraction**:
  - Contact information (name, email, phone)
  - Technical skills from a comprehensive database
  - Work experience with company names, dates, and descriptions
- **Modern Web Interface**: Clean, responsive design with real-time parsing results
- **Advanced Search**: Filter resumes by name or specific skills
- **Persistent Storage**: All parsed data is stored in a SQLite database for future access

## Documentation

### Project Structure
```
resume_parser_AI/
│
├── app.py               # Main application file
├── extract.py           # Resume extraction logic
├── database.py          # Database operations
├── static/              # Static files (CSS, JS)
│   ├── styles.css
│   └── script.js
├── templates/           # HTML templates
│   ├── index.html
│   ├── resume_view.html
│   └── search.html
├── uploads/            # PDF upload directory
└── requirements.txt    # Project dependencies
```

### Key Components

1. **Resume Extraction (extract.py)**
   - PDF text extraction using pdfminer.six
   - Pattern matching for contact information
   - Skill detection against a curated technology stack

2. **Database Management (database.py)**
   - SQLAlchemy ORM for database operations
   - Resume data model with structured fields
   - Search functionality implementation

## Configuration

The application uses the following default configuration:
- Server: Flask development server on port 5000
- Database: SQLite (resumes.db)
- Upload Directory: ./uploads
- Maximum File Size: 16MB
- Allowed File Types: PDF

## API Reference

### Main Routes
- `GET /`: Home page with upload form
- `POST /upload`: Handle resume upload and parsing
- `GET /resumes`: View all parsed resumes
- `GET /search`: Search through parsed resumes

## Examples

### Uploading a Resume
1. Visit the home page
2. Click "Choose PDF Resume" or drag and drop a PDF file
3. Click "Upload & Parse"
4. View extracted information immediately

### Searching Resumes
1. Navigate to the Search page
2. Enter a name or comma-separated skills
3. View matching resumes with highlighted relevant information

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM
- [pdfminer.six](https://github.com/pdfminer/pdfminer.six) - PDF text extraction
- [PyPDF2](https://pythonhosted.org/PyPDF2/) - PDF processing
