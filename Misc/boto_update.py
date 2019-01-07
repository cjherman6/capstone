from flask import Flask, request, render_template
import boto3
import predict_function as pf
import recommender_function as rf

from flask import Flask, request 
import boto3

app = Flask(__name__)

@app.route('/')
def index():
    return '''<form method=POST enctype=multipart/form-data action="upload">
    <input type=file name=myfile>
    <input type=submit>
    </form>'''

@app.route('/upload', methods=['POST'])
def upload():
    s3 = boto3.resource('s3')

    s3.Bucket('capstone-bucket-galvd83').put_object(Key='myfile.jpg',Body=request.files['myfile'])

    return '<h1>File saved to S3</h1>'

if __name__ == '__main__':
    app.run(debug=True)