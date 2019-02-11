import os
import subprocess

from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('index.html')

@app.route('/fileuploader', methods = ['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        # file uploaded, now call the shell script 
        subprocess.call("rm -f ./a.out", shell=True)
        retcode = subprocess.call("/usr/bin/g++ walk.cc", shell=True)
        if retcode:
            print("failed to compile walk.cc")
            exit
        subprocess.call("rm -f ./output", shell=True)
        retcode = subprocess.call("./test.sh", shell=True)
        
        print ("Score: " + str(retcode) + " out of 2 correct.")
        print("*************Original submission*************")
        with open('uploads/walk.cc','r') as fs:
            print(fs.read())
        return 'please see the results on console'    

if __name__ == '__main__':
    app.run(debug = True)
