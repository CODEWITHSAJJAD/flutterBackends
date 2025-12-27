from AttendenceSystem.db import db
class AssignStudentModel(db.Model):
    __tablename__="AssignStudent"
    as_id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    username=db.Column(db.String(50),db.ForeignKey("User.username"))
    a_id=db.Column(db.Integer,db.ForeignKey("AssignSection.a_id"))
    AssignSection_rl=db.relationship("AssignSectionModel",back_populates="AssignStudent_rl")
    User_rl=db.relationship("UserModel",back_populates="AssignStudent_rl")
    Attendence_rl=db.relationship("AttendenceModel",back_populates="AssignStudent_rl")