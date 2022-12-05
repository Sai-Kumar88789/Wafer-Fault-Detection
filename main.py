from flask import Flask,jsonify,request
from wafer.pipeline.trainingpipeline import TrainingPipeline
from wafer.exception import WaferException

app = Flask(__name__)

@app.route('/')
def home():
    data = "hello Sai kumar"
    return jsonify({"name":data})

@app.route("/train")
def train_route():
    try:

        trainingpipeline = TrainingPipeline()
        status  = trainingpipeline.is_pipeline_running
        if status:
            training_details = "training pipeline run successfull!!"
        else:
            training_details = "training pipeline run failed!!"
        return jsonify({"training status":training_details})
    except Exception as e:
        return jsonify({"error":"error occured"})

if __name__ =="__main__":
    app.run(debug=True)