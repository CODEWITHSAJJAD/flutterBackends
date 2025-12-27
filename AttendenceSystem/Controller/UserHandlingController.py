from AttendenceSystem.Model.UserModel import UserModel
from flask import request,jsonify
class UserHandlingController:
    @staticmethod
    def login():
        try:
            data = request.get_json()
            user = data['user']
            pwd = data['pwd']
            result = UserModel.query.filter(UserModel.username == user, UserModel.password == pwd).first()
            if result:
                return jsonify({"role":result.role,"username":user}), 200
            return jsonify("invalid username or password"), 404
        except Exception as e:
            return jsonify(str(e)),500
