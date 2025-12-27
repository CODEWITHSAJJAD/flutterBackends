from AttendenceSystem.db import db
class ClaimModel(db.Model):
    __tablename__="Claim"
    cl_id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    atten_id=db.Column(db.Integer,db.ForeignKey("Attendence.atten_id"))
    cl_status=db.Column(db.Integer)
    Attendence_rl=db.relationship("AttendenceModel",back_populates="Claim_rl")