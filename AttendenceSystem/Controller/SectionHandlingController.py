from AttendenceSystem.Model.AssignSectionModel import AssignSectionModel
from AttendenceSystem.Model.AttendenceModel import AttendenceModel
from AttendenceSystem.Model.SectionModel import SectionModel
from AttendenceSystem.Model.CourseModel import CourseModel
from AttendenceSystem.Model.TimeTable import TimeTableModel
from AttendenceSystem.db import db
from flask import request,jsonify
class SectionHandlingController:
    @staticmethod
    def AddCourse():
        data=request.get_json()
        newCourse=CourseModel(**data)
        db.session.add(newCourse)
        db.session.commit()
        db.session.close()
        return jsonify("added"),200
    @staticmethod
    def getAllCourses():
        course=CourseModel.query.all()
        if course:
            return jsonify([str(c.c_name) for c in course]),200
        return jsonify("not available"),404
    @staticmethod
    def addSection():
        data = request.get_json()
        newSection=SectionModel(**data)
        db.session.add(newSection)
        db.session.commit()
        db.session.close()
        return jsonify("added"),200
    @staticmethod
    def getAllSections():
        section=SectionModel.query.all()
        if section:
            return jsonify([
                str(s.s_name)
            for s in section])
        return jsonify("not available"),404
    @staticmethod
    def asignCourseToSection():
        data=request.get_json()
        c_name = data['c_name']
        print(c_name)
        s_name = data['s_name']
        print(s_name)
        corse=CourseModel.query.filter(CourseModel.c_name==c_name).first()
        c_id=corse.c_id
        print(c_id)
        section=SectionModel.query.filter(SectionModel.s_name==s_name).first()
        s_id=section.s_id
        print(s_id)
        check=AssignSectionModel.query.filter(AssignSectionModel.s_id==s_id,AssignSectionModel.c_id==c_id).first()
        newAssign = AssignSectionModel(s_id=s_id,c_id=c_id)
        if check:
            return jsonify("already assigned"),409
        db.session.add(newAssign)
        db.session.commit()
        db.session.close()
        return jsonify("Assigned"), 200
    @staticmethod
    def getTimeTable():
        timtab=TimeTableModel.query.all()
        timetable=[]
        for t in timtab:
            a_id = t.a_id
            t_day = t.t_day
            t_time = t.t_time
            assingsec = AssignSectionModel.query.filter(AssignSectionModel.a_id == a_id).first()
            sec_id = assingsec.s_id
            cor_id = assingsec.c_id
            section = SectionModel.query.filter(SectionModel.s_id == sec_id).first()
            course = CourseModel.query.filter(CourseModel.c_id == cor_id).first()
            s_name = section.s_name
            c_name = course.c_name
            timetable.append({
                "day": str(t_day),
                "time": str(t_time),
                "section": str(s_name),
                "course": str(c_name),
            })
        return jsonify([time for time in timetable]),200
    @staticmethod
    def addNewtimeTable():
        data = request.get_json()
        c_name = data['c_name']
        print(c_name)
        s_name = data['s_name']
        print(s_name)
        corse = CourseModel.query.filter(CourseModel.c_name == c_name).first()
        c_id = corse.c_id
        print(c_id)
        section = SectionModel.query.filter(SectionModel.s_name == s_name).first()
        s_id = section.s_id
        print(s_id)
        time=data['time']
        day=data['day']
        check=TimeTableModel.query.filter(TimeTableModel.t_time==time,TimeTableModel.t_day==day).first()
        assignsection = AssignSectionModel.query.filter(AssignSectionModel.s_id == s_id,AssignSectionModel.c_id == c_id).first()
        a_id = assignsection.a_id
        if check:
            return jsonify("already slot booked"),409
        newTimetable=TimeTableModel(a_id=a_id,t_day=day,t_time=time)
        db.session.add(newTimetable)
        db.session.commit()
        return jsonify("added timetable"),200
