from AttendenceSystem.db import db
class UserModel(db.Model):
    __tablename__="User"
    username=db.Column(db.String(50),primary_key=True)
    password=db.Column(db.String(50),nullable=False)
    role=db.Column(db.Integer,nullable=False)
    image=db.Column(db.String(100))
    AssignStudent_rl=db.relationship("AssignStudentModel",back_populates="User_rl")
