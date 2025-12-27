from AttendenceSystem.db import db
class AttendenceModel(db.Model):
    __tablename__="Attendence"
    atten_id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    atten_date=db.Column(db.String(20))
    t_id=db.Column(db.Integer,db.ForeignKey("TimeTable.t_id"))
    as_id=db.Column(db.Integer,db.ForeignKey("AssignStudent.as_id"))
    a_state=db.Column(db.Integer)
    TimeTable_rl=db.relationship("TimeTableModel",back_populates="Attendence_rl")
    AssignStudent_rl=db.relationship("AssignStudentModel",back_populates="Attendence_rl")
    Claim_rl=db.relationship("ClaimModel",back_populates="Attendence_rl")