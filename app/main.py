from flask import Flask, request
from manager import Mega
import uuid


app = Flask(__name__)

loggedIn = False
loggingIn = False
manager =  Mega()

@app.post("/login/")
def login():
    global loggedIn
    global loggingIn
    body = request.form
    loggingIn = True
    loggedIn = False
    manager.login(body.get("email"), body.get("password"))
    loggedIn = True
    loggingIn = False
    return { "result": "Success" }
    
@app.get("/logged_in/")
def login_get():
    global loggedIn
    global loggingIn
    return { "loggedIn": loggedIn, "loggingIn": loggingIn }
    
@app.get("/exists/")
def exists():
    global loggedIn
    if not loggedIn:
        return { "error": "Not logged in" }
    path = request.args.get("path")
    return { "result": manager.does_file_exist(path) }

@app.put("/upload/")
def upload():
    global loggedIn
    global safeUUID
    if not loggedIn:
        return { "result": "not logged in." }
    local_path = f"/tmp/{request.form['path'].split('/')[-1]}"
    with open(local_path, "wb+") as file:
        request.files.get("file").save(file)
    manager.upload_file(request.form["path"], local_path)
    return { "result": "success" }
    
@app.get("/list_dir/")
def list_dir():
    global loggedIn
    if not loggedIn:
        return { "error": "Not logged in" }
    path = request.args.get("path")
    return { "result": manager.list_dir(path) }
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, use_reloader=False)