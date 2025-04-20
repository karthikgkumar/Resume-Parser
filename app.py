from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
import os
from extract import ResumeParser
from database import Database

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'pdf'}

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database
db = Database()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['resume']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Parse resume
        parser = ResumeParser(filepath)
        resume_data = parser.extract()
        
        # Save to database
        resume_id = db.save_resume(resume_data)
        
        return jsonify({
            'success': True,
            'resume_id': resume_id,
            'data': resume_data
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/resumes')
def view_resumes():
    resumes = db.get_all_resumes()
    return render_template('resume_view.html', resumes=resumes)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    skills = request.args.get('skills', '').split(',')
    results = db.search_resumes(query, skills)
    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
