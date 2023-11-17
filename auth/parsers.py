from flask_restx import reqparse


login_args = reqparse.RequestParser()
login_args.add_argument('email', location="form", required=True)
login_args.add_argument('password', location="form", required=True)