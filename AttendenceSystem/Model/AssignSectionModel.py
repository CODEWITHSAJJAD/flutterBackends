from AttendenceSystem.db import db
class AssignSectionModel(db.Model):
    __tablename__="AssignSection"
    a_id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    c_id=db.Column(db.Integer,db.ForeignKey("Course.c_id"))
    s_id=db.Column(db.Integer,db.ForeignKey("Section.s_id"))
    sec_rl=db.relationship("SectionModel",back_populates="AssignSection_rl")
    course_rl=db.relationship("CourseModel",back_populates="AssignSection_rl")
    TimeTable_rl=db.relationship("TimeTableModel",back_populates="AssignSection_rl")
    AssignStudent_rl=db.relationship("AssignStudentModel",back_populates="AssignSection_rl")