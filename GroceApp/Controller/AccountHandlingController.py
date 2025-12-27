from flask import request,jsonify
from GroceApp.Model.UserAccounrModel import UserAccountModel
from Router import username
from db import db
import json
class AccountHandlingController:
    @staticmethod
    def Signup():
        try:
            username = request.form['userName']
            password = request.form['password']
            role = request.form['role']
            city = request.form['city']
            newuser = UserAccountModel(userName=username, password=password, role=role, city=city)
            check = UserAccountModel.query.filter(UserAccountModel.userName == username).first()
            if not check:
                db.session.add(newuser)
                db.session.commit()
                return jsonify(f"{username} signup completed"), 200
            return jsonify(f"{username} already exist"), 409
        except Exception as e:
            return jsonify(f"Error:{e}"),500

    @staticmethod
    def Signupformobject():
        try:
            user=request.form['user']
            jsonuser=json.loads(user)
            newuser = UserAccountModel(**jsonuser)
            check = UserAccountModel.query.filter(UserAccountModel.userName == username).first()
            if not check:
                db.session.add(newuser)
                db.session.commit()
                return jsonify(f"{username} signup completed"), 200
            return jsonify(f"{username} already exist"), 409
        except Exception as e:
            return jsonify(f"Error:{e}"), 500
    @staticmethod
    def Login():
        try:
            username = request.form['userName']
            password = request.form['password']
            user = UserAccountModel.query.filter(UserAccountModel.userName == username,UserAccountModel.password==password).first()
            if user:
                return jsonify({
                    "username":user.userName,
                    "role":user.role,
                    "profile":user.profileImagePath}), 200
            return jsonify("invalid username or password"),404
        except Exception as e:
            return jsonify(f"Error:{e}"), 500