from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from photo_restorer import predict_image

from dotenv import load_dotenv
import os

load_dotenv()
api_token = os.getenv('REPLICATE_API_TOKEN')

UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Max allowed file size if 16MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url) # returns to home page
        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            full_filename = "." + url_for("static", filename="images/" + filename)
            print(full_filename)
            file.save(full_filename)

            predicted_image_url=predict_image(full_filename)
            return render_template("index.html", filename=filename, restored_img_url=predicted_image_url )

if __name__ == '__main__':
    import main
    main.app.run(debug=True)
