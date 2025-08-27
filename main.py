from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files = []
        for key, value in request.files.items():
            print(key, value)
            # Upload the file
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)  # Sanitized filename
                folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)  # Use makedirs for safety
                file.save(os.path.join(folder_path, filename))
                input_files.append(filename)  # Use sanitized filename
                print(f"Saved file: {filename}")
            # Capture the description and save it to a file
            desc_path = os.path.join(folder_path, "desc.txt")
            with open(desc_path, "w") as f:
                f.write(desc)
        # Write sanitized filenames to input.txt
        input_txt_path = os.path.join(folder_path, "input.txt")
        with open(input_txt_path, "a") as f:
            for fl in input_files:
                f.write(f"file '{fl}'\nduration 1\n")
    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

app.run(debug=True)