from flask import Flask, request, render_template, flash
import os
import hashlib

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def calculate_hash(file_path):
    hash_funcs = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512,
    }
    hashes = {}
    
    with open(file_path, "rb") as f:
        file_content = f.read()
        for name, func in hash_funcs.items():
            hash_obj = func()
            hash_obj.update(file_content)
            hashes[name] = hash_obj.hexdigest()
    
    return hashes

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/check', methods=['POST'])
def check_file():
    if 'file' not in request.files:
        flash('No file provided')
        return render_template('upload.html')
    
    file = request.files['file']

    if file.filename == '':
        flash('No file selected')
        return render_template('upload.html')

    # Save the file
    filename = file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Calculate the file's hashes
    calculated_hashes = calculate_hash(filepath)

    # Delete the uploaded file after showing the hashes
    os.remove(filepath)

    # Render the template with the calculated hashes
    return render_template('upload.html', calculated_hashes=calculated_hashes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)
