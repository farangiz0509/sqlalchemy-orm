from datetime import datetime
from sqlalchemy import or_
from .models import Student, Score
from .db import get_db

# CREATE
def create_student(first_name: str, last_name: str, birthdate: datetime, bio: str | None = None):
    with get_db() as session:
        student = Student(
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
            bio=bio
        )
        session.add(student)
        session.commit()
        session.refresh(student)
        return student

# READ
def get_students():
    with get_db() as session:
        return session.query(Student).all()

def get_one_student(student_id: int):
    with get_db() as session:
        return session.get(Student, student_id)

def search_students_by_first_name(first_name: str):
    with get_db() as session:
        return session.query(Student).filter(Student.first_name == first_name).all()

def search_students_by_name(name: str):
    with get_db() as session:
        return session.query(Student).filter(
            or_(
                Student.first_name.ilike(f"%{name}%"),
                Student.last_name.ilike(f"%{name}%")
            )
        ).all()

# UPDATE
def update_student(
    student_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
    birthdate: datetime | None = None,
    bio: str | None = None
):
    with get_db() as session:
        student = session.get(Student, student_id)
        if not student:
            return None
        if first_name:
            student.first_name = first_name
        if last_name:
            student.last_name = last_name
        if birthdate:
            student.birthdate = birthdate
        if bio:
            student.bio = bio
        session.commit()
        session.refresh(student)
        return student

# DELETE
def delete_student(student_id: int):
    with get_db() as session:
        student = session.get(Student, student_id)
        if student:
            session.delete(student)
            session.commit()
            return True
        return False

# FILTER
def filter_students_by_gender(gender: str):
    with get_db() as session:
        return session.query(Student).filter_by(gender=gender).all()

def filter_students_by_gpa(min_gpa: float, max_gpa: float):
    with get_db() as session:
        return session.query(Student).filter(Student.gpa.between(min_gpa, max_gpa)).all()

# SORT
def get_sorted_students_by_gpa(by: str = "asc"):
    with get_db() as session:
        if by == "asc":
            return session.query(Student).order_by(Student.gpa.asc()).all()
        else:
            return session.query(Student).order_by(Student.gpa.desc()).all()

# SCORE
def add_score(student_id: int, subject: str, ball: float):
    with get_db() as session:
        student = session.get(Student, student_id)
        if not student:
            return None
        score = Score(subject=subject, ball=ball)
        student.scores.append(score)
        session.commit()
        return score

def get_scores(student_id: int):
    with get_db() as session:
        student = session.get(Student, student_id)
        return student.scores if student else []

# AGGREGATION
def get_student_with_scores():
    with get_db() as session:
        students = session.query(Student).all()
        return [
            {
                "student": student.full_name,
                "total_scores": len(student.scores)
            }
            for student in students
        ]
