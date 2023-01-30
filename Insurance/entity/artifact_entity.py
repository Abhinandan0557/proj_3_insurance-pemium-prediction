#it is used to save training and testing data into artifact folder
#artifact file store all output files

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    # this class is imported in DataTransformation class in data_transformation.py 
    # to access train,test data to do transformation
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str


@dataclass
class DataValidationArtifact:
    report_file_path:str


@dataclass
class DataTransformationArtifact:
    #this class is used in initiate_data_tranfromation function in data_transformattion.py file
    transform_object_path:str
    transformed_train_path:str
    transformed_test_path:str
    target_encoder_path:str