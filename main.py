from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/')
def home():
    data = "hello Sai kumar"
    return jsonify({"name":data})

if __name__ =="__main__":
    app.run(debug=True)