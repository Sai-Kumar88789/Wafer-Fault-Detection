from wafer.entity.config_entity import DataIngestionConfig
from wafer.entity.artifact_entity import DataIngestionArtifact

class DataIngestion:

    def __init__(self,dataingestionconfig:DataIngestionConfig):
        self.dataingestionconfig = dataingestionconfig

    def initate_data_ingestion(self) -> DataIngestionArtifact:
        pass
    
