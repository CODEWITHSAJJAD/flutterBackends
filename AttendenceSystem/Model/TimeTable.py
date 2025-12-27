from AttendenceSystem.db import db
class TimeTableModel(db.Model):
    __tablename__="TimeTable"
    t_id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    a_id=db.Column(db.Integer,db.ForeignKey("AssignSection.a_id"))
    t_day=db.Column(db.String(10))
    t_time=db.Column(db.String(20))
    AssignSection_rl=db.relationship("AssignSectionModel",back_populates="TimeTable_rl")
    Attendence_rl=db.relationship("AttendenceModel",back_populates="TimeTable_rl")
