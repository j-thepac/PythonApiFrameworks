from flask import Flask , request,render_template,json,jsonify,redirect,url_for
from flask_restful import Api,Resource


app=Flask(__name__)
api=Api(app)


class Test(Resource):
    def get(self):return "working"



api.add_resource(Test,"/")

if (__name__ =="__main__"):
    app.run(debug=True)