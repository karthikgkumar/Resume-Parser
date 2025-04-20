from sqlalchemy import create_engine, Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Resume(Base):
    __tablename__ = 'resumes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    skills = Column(JSON)
    work_experience = Column(JSON)
    raw_text = Column(Text)

class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///resumes.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def save_resume(self, data):
        session = self.Session()
        resume = Resume(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            skills=data['skills'],
            work_experience=data['work_experience']
        )
        session.add(resume)
        session.commit()
        resume_id = resume.id
        session.close()
        return resume_id
    
    def get_all_resumes(self):
        session = self.Session()
        resumes = session.query(Resume).all()
        session.close()
        return [
            {
                'id': r.id,
                'name': r.name,
                'email': r.email,
                'phone': r.phone,
                'skills': r.skills,
                'work_experience': r.work_experience
            }
            for r in resumes
        ]
    
    def search_resumes(self, query=None, skills=None):
        session = self.Session()
        results = session.query(Resume)
        
        if query:
            results = results.filter(Resume.name.ilike(f'%{query}%'))
        
        if skills and skills[0]:  # Check if skills list is not empty
            for skill in skills:
                # This is a simple implementation - in production, you'd want to use a proper JSON query
                results = results.filter(Resume.skills.like(f'%{skill.strip()}%'))
        
        resumes = results.all()
        session.close()
        return [
            {
                'id': r.id,
                'name': r.name,
                'email': r.email,
                'phone': r.phone,
                'skills': r.skills,
                'work_experience': r.work_experience
            }
            for r in resumes
        ]
