from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='OSS Guardian')

@app.route('/scan')
def scan_vulnerabilities():
    # Run a simple vulnerability scan using the safety library
    scan_output = subprocess.check_output(['safety', 'check', '--full-report'])
    
    return render_template('vulnerabilities.html', title='Vulnerability Scan', scan_output=scan_output.decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)
