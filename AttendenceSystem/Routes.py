from AttendenceSystem.Controller.SectionHandlingController import SectionHandlingController
from AttendenceSystem.Controller.StudentHandlingController import StudentHandlingController
from AttendenceSystem.db import db,init_db
from AttendenceSystem.Controller.UserHandlingController import UserHandlingController
from AttendenceSystem.Model.CourseModel import CourseModel
from AttendenceSystem.Model.SectionModel import SectionModel
from AttendenceSystem.Model.ClaimModel import ClaimModel
from AttendenceSystem.Model.AttendenceModel import AttendenceModel
from AttendenceSystem.Model.AssignSectionModel import AssignSectionModel
from AttendenceSystem.Model.AssignStudentModel import AssignStudentModel
from AttendenceSystem.Model.TimeTable import TimeTableModel
from flask import Flask, jsonify
app = Flask(__name__)
init_db(app)

with app.app_context():
    db.create_all()
    print("created")
@app.route('/')
def welcome():
    return jsonify("welcome"),200
@app.route('/login',methods=['POST'])
def login():
    return UserHandlingController.login()
@app.route('/addCourse',methods=['POST'])
def addCourse():
    return SectionHandlingController.AddCourse()
@app.route('/getCourses',methods=['GET'])
def getCourses():
    return SectionHandlingController.getAllCourses()
@app.route('/addSection',methods=['POST'])
def addSection():
    return SectionHandlingController.addSection()
@app.route('/getSections',methods=['GET'])
def getSection():
    return SectionHandlingController.getAllSections()
@app.route('/asignCourseToSection',methods=['POST'])
def asignCourseToSection():
    return SectionHandlingController.asignCourseToSection()
@app.route('/asignStudent',methods=['POST'])
def asignStudent():
    return StudentHandlingController.assignStudent()
@app.route('/gettimetable',methods=['GET'])
def timetable():
    return SectionHandlingController.getTimeTable()
@app.route('/addTimeTable',methods=['POST'])
def addtimeTable():
    return SectionHandlingController.addNewtimeTable()

@app.route('/getStudents',methods=['POST'])
def getStudents():
    return StudentHandlingController.getStudents()

@app.route('/markAttendence',methods=['POST'])
def markAttendence():
    return StudentHandlingController.markAttendence()

@app.route('/getAttendence',methods=['POST'])
def getAttendence():
    return StudentHandlingController.getAttendence()

@app.route('/addClaim',methods=['POST'])
def addClaim():
    return StudentHandlingController.claimAttendence()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)