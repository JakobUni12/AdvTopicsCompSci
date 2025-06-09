from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pwd = request.form.get('password')
    if user == 'admin' and pwd == 'admin':
        return jsonify(status="success")
    return jsonify(status="failure"), 403

@app.route('/firmware', methods=['POST'])
def firmware_upload():
    f = request.files.get('file')
    if f:
        f.save(f"./uploads/{f.filename}")
        return jsonify(status="uploaded")
    return jsonify(status="no file"), 400

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        ssl_context=('certs/server.crt', 'certs/server.key')
    )
