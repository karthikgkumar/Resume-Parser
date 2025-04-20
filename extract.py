import PyPDF2
import re
from pdfminer.high_level import extract_text

class ResumeParser:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def extract_text_from_pdf(self):
        return extract_text(self.file_path)
    
    def extract_email(self, text):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        return emails[0] if emails else None
    
    def extract_phone(self, text):
        phone_pattern = r'\b(?:\+\d{1,3}[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b'
        phones = re.findall(phone_pattern, text)
        return phones[0] if phones else None
    
    def extract_name(self, text):
        # Get first two lines of text
        first_lines = text.split('\n')[:2]
        # Simple heuristic: First line that's not an email and doesn't contain common headers
        for line in first_lines:
            line = line.strip()
            if line and '@' not in line and not any(header in line.lower() for header in ['resume', 'cv', 'curriculum vitae']):
                return line
        return None
    
    def extract_skills(self, text):
        # Common programming languages and technologies
        common_skills = {
            "python", "java", "javascript", "html", "css", "sql", "react",
            "angular", "vue", "node", "express", "django", "flask", "spring",
            "docker", "kubernetes", "aws", "azure", "git", "agile", "scrum",
            "c++", "c#", "ruby", "php", "swift", "kotlin", "rust", "golang",
            "mongodb", "postgresql", "mysql", "redis", "elasticsearch",
            "jenkins", "circleci", "travis", "jira", "confluence",
            "tensorflow", "pytorch", "pandas", "numpy", "scikit-learn",
            "machine learning", "deep learning", "ai", "artificial intelligence",
            "data science", "data analysis", "data visualization",
            "rest api", "graphql", "microservices", "devops", "ci/cd"
        }
        
        # Find skills in text
        text_lower = text.lower()
        found_skills = set()
        
        # Look for exact matches
        for skill in common_skills:
            if skill in text_lower:
                found_skills.add(skill)
                
        return list(found_skills)
    
    def extract_work_experience(self, text):
        experience = []
        # Look for date patterns and company names
        lines = text.split('\n')
        date_pattern = r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}\b'
        
        current_company = None
        current_dates = None
        current_description = []
        
        for line in lines:
            dates = re.findall(date_pattern, line)
            if dates:
                if current_company:
                    experience.append({
                        'company': current_company,
                        'dates': current_dates,
                        'description': ' '.join(current_description)
                    })
                current_dates = line.strip()
                current_company = None
                current_description = []
            elif current_dates and not current_company and line.strip():
                current_company = line.strip()
            elif current_company and line.strip():
                current_description.append(line.strip())
        
        # Add the last experience
        if current_company:
            experience.append({
                'company': current_company,
                'dates': current_dates,
                'description': ' '.join(current_description)
            })
            
        return experience
    
    def extract(self):
        text = self.extract_text_from_pdf()
        return {
            'name': self.extract_name(text),
            'email': self.extract_email(text),
            'phone': self.extract_phone(text),
            'skills': self.extract_skills(text),
            'work_experience': self.extract_work_experience(text)
        }
