import os
from datetime import datetime
from flask import Flask, render_template, request
# from ocr_core import ocr_png
from werkzeug.utils import secure_filename

# Folder to store and later serve the images
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads/')

basedir = os.path.abspath(os.path.dirname(__file__))

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home_page():
	return "Sup"

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
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename + str(datetime.now())))
			# extracted_text = ocr_png(UPLOAD_FOLDER + file.filename + str(datetime.now()))
			# print(extracted_text)
			return 'Successful'
		else:
			return 'Invalid Format'


app.run()
