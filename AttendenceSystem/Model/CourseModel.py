from AttendenceSystem.db import db
class CourseModel(db.Model):
    __tablename__="Course"
    c_id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    c_name=db.Column(db.String(100),unique=True)
    AssignSection_rl = db.relationship("AssignSectionModel", back_populates="course_rl")
