from datetime import datetime
from wafer.constant import trainingpipeline
import os

class TrainingPipelineConfig:
    
    def __init__(self,timestamp = datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%y_%H_%M_%S")
        self.pipelinename = trainingpipeline.PIPELINE_NAME
        self.artifact_dir = os.path.join(trainingpipeline.ARTIFACT_DIR,timestamp)
        self.timestamp = timestamp

class DataIngestionConfig:

    def __init__(self,trainingpipelineconfig:TrainingPipelineConfig):
        self.data_ingestion_file_dir = os.path.join(trainingpipelineconfig.artifact_dir,
                                     trainingpipeline.DATA_INGESTION_FILE_DIR)
        self.feature_store_path = os.path.join(self.data_ingestion_file_dir,
                                    trainingpipeline.DATA_INGESTION_FEATURE_STORE)
        self.train_file_path = os.path.join(self.data_ingestion_file_dir,trainingpipeline.DATA_INGESTION_INGESTED_FILE_PATH,
                                    trainingpipeline.TRAIN_FILE_NAME)
        self.test_file_path = os.path.join(self.data_ingestion_ingested_path,
                                    trainingpipeline.TEST_FILE_NAME)
        self.feature_file_dir = os.path.join(self.data_ingestion_feature_store_path,
                                    trainingpipeline.FILE_NAME)
        self.train_test_split_ratio = trainingpipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    
