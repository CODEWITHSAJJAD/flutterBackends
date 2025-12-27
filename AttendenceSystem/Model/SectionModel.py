from AttendenceSystem.db import db
class SectionModel(db.Model):
    __tablename__="Section"
    s_id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    s_name=db.Column(db.String(20),unique=True)
    AssignSection_rl=db.relationship("AssignSectionModel",back_populates="sec_rl")