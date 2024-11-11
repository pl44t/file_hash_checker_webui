# File Hash Checker WebUI

This is a simple web application that allows users to upload any file and check its hash values (MD5, SHA-1, SHA-256, and SHA-512). The application is built using Python and Flask.

## Features

- **File Upload**: Upload any file to compute its hash values.
- **Hash Calculations**: Supports MD5, SHA-1, SHA-256, and SHA-512 hash algorithms.
- **User-Friendly Web Interface**: Built with Flask to provide an intuitive web interface.

## Requirements

- Python 3.x
- Flask

## Installation

1. **Clone this repository:**

```
   git clone https://github.com/yourusername/file-hash-checker-webui.git
   cd file-hash-checker-webui
```
2. **Install required packages:**
```
    pip install Flask
```
3. **Run the application:**
 ```
    python app.py
```

4. **Access the application:** Open a browser and navigate to http://localhost:5004 (or replace localhost with your server IP if hosting remotely).

## Usage

1. **Upload a File:** Use the upload button to select and upload any file from your computer.

2. **View Hash Results:** Once uploaded, the application will calculate and display the hash values (MD5, SHA-1, SHA-256, SHA-512) for the file.

## Project Structure

- app.py: Main application file that contains the Flask server and hash calculation logic.
- templates/: Folder containing the HTML template for the web UI.
- uploads/: Folder for temporary uploaded files which are cleared after hashing.

## Configuration

To change the application's default port, modify the last line in app.py:
```app.run(host='0.0.0.0', port=5004, debug=True)```

Replace  ```5004``` with the port number you prefer.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request with your enhancements.