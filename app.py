from flask import Flask, render_template, request, jsonify, make_response
from flask_socketio import SocketIO, emit, send
import os
from datetime import datetime
from ocr_core import getTextFromFile, SampleText
from werkzeug.utils import secure_filename
import hashlib, random

# Folder to store and later serve the images
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads/')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
socketio = SocketIO(app)

@app.route('/')
def home_page():
	return "Sup"

@app.route('/debug')
def debug_page():
	return render_template('index.html')

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_page():
	if request.method == 'POST':
		# Check if there is a file in the request
		if 'file' not in request.files:
			return 'File not present'
		file = request.files['file']
		# If no file is selected
		if file.filename == '':
			return 'No file selected'
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			stamp = datetime.now()
			uniqueCode = str(hashlib.sha256((str(stamp) + str(random.getrandbits(256))).encode('utf-8')).hexdigest()) + '.' + filename.rsplit('.', 1)[1].lower()
			# print(uniqueCode)
			uniqueCode = secure_filename(uniqueCode)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], uniqueCode))
			# print(UPLOAD_FOLDER + str(uniqueCode))
			return make_response(jsonify(unique_code = uniqueCode),200)
		else:
			return make_response(jsonify(message = "Invalid Type"),400)

#Event listener message
@socketio.on('message')
def handleMessage(message):
    print('Message: ' + message)
    send(message)

@socketio.on('ocr_request')
def handleGetText(message):
	print('Code : ', message)
	try:
		extracted_text = getTextFromFile(os.path.join(UPLOAD_FOLDER + message))
		emit('ocr_response', extracted_text)
	except:
		send('Invalid Code')

if __name__ == '__main__':
	socketio.run(app,host='0.0.0.0',port=8080, debug = True)
