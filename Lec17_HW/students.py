# from dotenv import load_dotenv
# import os - for .env не вийшло щось трошки
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    subject_id = Column(Integer, ForeignKey("subject.id"))

    subject = relationship("Subject", back_populates="students")

    def __str__(self):
        return f"This is {self.id} student {self.name}. Age: {self.age}. Subject_id: {self.subject_id}"

    def __repr__(self):
        return f"This is {self.id} student {self.name}. Age: {self.age}. Subject_id: {self.subject_id}"


class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True)
    subject_name = Column(String)

    students = relationship("Student", back_populates="subject")

    def __str__(self):
        return f"This is {self.subject_name} subject. Id: {self.id}"

    def __repr__(self):
        return f"This is {self.subject_name} subject. Id: {self.id}"


def db_conect():
    DATABASE_URI = "postgresql://{user}:{password}@{host}:{port}/{database}"

    engine = create_engine(
        DATABASE_URI.format(
            host="localhost",
            database="postgres",
            user="postgres",
            password=1111,
            port=5433,
        )
    )
    return engine


def add_info(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    subject_names = ["English", "Spanish", "Chinese", "Math", "History", "Science"]

    for sub_name in subject_names:
        subject = Subject(subject_name=sub_name)
        session.add(subject)

    session.commit()
    session.query(Subject).all()
    from random import randint, choice

    random_names = [
        "Victoria",
        "Oleksandr",
        "Maria",
        "Kseniia",
        "Alina",
        "Anastasiia",
        "Arsen",
        "Ilya",
        "Oksana",
        "Yevhenii",
        "Dmytro",
        "Kate",
    ]

    for _ in range(10):
        student = Student(
            name=choice(random_names), age=randint(18, 25), subject_id=randint(1, 6)
        )
        session.add(student)

    session.commit()
    session.query(Student).all()

    result = session.query(Student, Subject).join(Subject).all()
    return result, session


def print_res_1(result):
    for student, subject in result:
        print(student.id, student.name, student.age, subject.id, subject.subject_name)


class StudentSubjects(Base):
    __tablename__ = "student_subjects"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    student_name = Column(Integer, ForeignKey("student.name"))
    student_age = Column(Integer, ForeignKey("student.age"))
    subject_name = Column(Integer, ForeignKey("subject.subject_name"))

    student = relationship("Student", foreign_keys=[student_id])
    subject = relationship("Subject", foreign_keys=[subject_name])


def print_res_2(result, session):
    for student, subject in result:
        student_subject_obj = StudentSubjects(
            student_id=student.id,
            student_name=student.name,
            student_age=student.age,
            subject_name=subject.subject_name,
        )
        session.add(student_subject_obj)

    session.query(StudentSubjects).all()
    session.query(Student).filter(Student.subject_id == "1").all()


if __name__ == "__main__":
    engine = db_conect()
    result, session = add_info(engine)
    print_res_1(result)
    print_res_2(result, session)
