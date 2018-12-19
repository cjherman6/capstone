from flask import Flask, request
import boto3

app = Flask(__name__)

bucket_name = 'capstone-bucket-galvd83'

@app.route('/')
def index():
    return '''<form method=POST enctype=multipart/form-data action='upload'>
    <input type=file name=myfile>
    <input type=submit>
    </form>'''

@app.route('/upload',methods=['POST'])
def upload():
    s3 = boto3.resource('s3')
    s3.Bucket(bucket_name).put_object(Key='example.py',Body=request.files['myfile'])

    return '<h1>File saved to S3</h1>'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
