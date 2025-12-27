# from fastapi import FastAPI
# from main import signup,login
# app = FastAPI()
#
# @app.get("/")
# def welcome():
#     return {"message": "Welcome"}
# @app.post("/signup")
# def register():
#     return signup()


from fastapi import FastAPI
from Controller.UserController import signup as signup_ctrl, login as login_ctrl
from Model.UserModel import User

app = FastAPI()

@app.post("/signup")
def signup_route(user: User):
    return signup_ctrl(user)

@app.post("/login")
def login_route(user: User):
    return login_ctrl(user)
