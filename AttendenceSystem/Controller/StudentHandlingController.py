import json
import os

from AttendenceSystem.Model.ClaimModel import ClaimModel
from AttendenceSystem.Model.CourseModel import CourseModel
from AttendenceSystem.Model.SectionModel import SectionModel
from AttendenceSystem.Model.AssignSectionModel import AssignSectionModel
from AttendenceSystem.Model.AttendenceModel import AttendenceModel
from AttendenceSystem.Model.TimeTable import TimeTableModel
from AttendenceSystem.db import db
from flask import request,jsonify
from AttendenceSystem.Model.AssignStudentModel import AssignStudentModel
from AttendenceSystem.Model.UserModel import UserModel
from datetime import datetime
class StudentHandlingController:
    @staticmethod
    def assignStudent():
        data = request.form['student']
        image = request.files['Image']
        photos_dir = 'photos'
        if not os.path.exists(photos_dir):
            os.makedirs(photos_dir)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        extension = image.filename.split('.')[-1] if '.' in image.filename else 'jpg'
        unique_filename = f"{timestamp}.{extension}"
        save_path = os.path.join(photos_dir, unique_filename)
        image.save(save_path)
        path_data = {"image": save_path}

        jsondata=json.loads(data)
        username=jsondata['username']
        c_name = jsondata['c_name']
        print(c_name)
        s_name = jsondata['s_name']
        print(s_name)
        corse = CourseModel.query.filter(CourseModel.c_name == c_name).first()
        c_id = corse.c_id
        print(c_id)
        section = SectionModel.query.filter(SectionModel.s_name == s_name).first()
        s_id = section.s_id
        print(s_id)
        assignsection=AssignSectionModel.query.filter(AssignSectionModel.s_id==s_id,AssignSectionModel.c_id==c_id).first()
        a_id=assignsection.a_id
        if a_id and username and image:
            newStudentAssign=AssignStudentModel(username=username,a_id=a_id)
            existing=AssignStudentModel.query.filter(AssignStudentModel.username==username,AssignStudentModel.a_id==a_id).first()
            if not existing:
                db.session.add(newStudentAssign)
                UserModel.query.filter(UserModel.username==username).update(path_data)
                db.session.commit()
                return jsonify("student assigned"),200
            return jsonify("already assigned"),409
        return jsonify("incomplete parameters"),204

    @staticmethod
    def getStudents():
        try:
            data = request.get_json()
            section = data['section']
            course = data['course']
            day = data["day"]
            time = data["time"]
            students = db.session.query(
                UserModel.username,
                UserModel.image,
                AssignStudentModel.as_id,
                TimeTableModel.t_id
            ).join(
                AssignStudentModel, UserModel.username == AssignStudentModel.username
            ).join(
                AssignSectionModel, AssignStudentModel.a_id == AssignSectionModel.a_id
            ).join(
                TimeTableModel, AssignSectionModel.a_id == TimeTableModel.a_id
            ).join(
                SectionModel, AssignSectionModel.s_id == SectionModel.s_id
            ).join(
                CourseModel, AssignSectionModel.c_id == CourseModel.c_id
            ).filter(
                SectionModel.s_name == section,
                CourseModel.c_name == course,
                TimeTableModel.t_day == day,
                TimeTableModel.t_time == time
            ).all()

            if students:
                stud_list = []
                for s in students:
                    stud_list.append({
                        "Name": s.username,
                        "image": s.image,
                        "Section": section,
                        "Course": course,
                        "Day": day,
                        "Time": time,
                        "as_id": s.as_id,
                        "t_id": s.t_id,
                    })
                return jsonify(stud_list), 200

            return jsonify({"message": "No students found matching the criteria"}), 404

        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @staticmethod
    def markAttendence():
        try:
            date=datetime.utcnow()
            date=str(date.strftime("%Y-%m-%d"))
            Attendence=request.get_json()
            for a in Attendence:
                a["atten_date"]=date
                newAttendence=AttendenceModel(**a)
                db.session.add(newAttendence)
                db.session.commit()
            return jsonify("attendence updated"),200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def getAttendence():
        try:
            data = request.get_json()
            username = data.get("user")
            if not username:
                return jsonify({"error": "Username is required"}), 400
            attendance = db.session.query(
                AttendenceModel,
                CourseModel.c_name,
                SectionModel.s_name
            ).join(
                AssignStudentModel, AttendenceModel.as_id == AssignStudentModel.as_id
            ).join(
                UserModel, AssignStudentModel.username == UserModel.username
            ).join(
                AssignSectionModel, AssignStudentModel.a_id == AssignSectionModel.a_id
            ).join(
                CourseModel, AssignSectionModel.c_id == CourseModel.c_id
            ).join(
                SectionModel, AssignSectionModel.s_id == SectionModel.s_id
            ).filter(
                UserModel.username == username
            ).all()

            if not attendance:
                return jsonify({"message": "No attendance found"}), 404

            result = []
            for att, course_name, section_name in attendance:
                result.append({
                    "atten_id":att.atten_id,
                    "date": att.atten_date,
                    "course": course_name,
                    "section": section_name,
                    "attendance": "Present" if att.a_state == 1 else "Absent"
                })

            return jsonify(result), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500
    @staticmethod
    def claimAttendence():
        try:
            data = request.get_json()
            data["cl_status"]=0
            newClaim=ClaimModel(**data)
            db.session.add(newClaim)
            db.session.commit()
            return jsonify("claim updated"),200
        except Exception as e:
            return jsonify( str(e)), 500