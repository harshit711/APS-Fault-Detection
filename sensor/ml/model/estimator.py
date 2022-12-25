from sensor.exception import SensorException
import os, sys
from sensor.constant.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME

class TargetValueMapping:
    def __init__(self):
        self.neg: int = 0
        self.pos: int = 1
        # neg and pos are values in the target variable

    def to_dict(self):
        return self.__dict__

    def reverse_mapping(self):
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))

class SensorModel:
    def __init__(self,preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise SensorException(e, sys)

    def predict(self, x):
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise SensorException(e, sys)

class ModelResolver:
    def __init__(self, model_dir=SAVED_MODEL_DIR):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise SensorException(e, sys)

    def get_best_model_path(self,)-> str:
        try:
            timestamps = list(map(int, os.listdir(self.model_dir)))
            latest_timestamp = max(timestamps)
            latest_model_path = os.path.join(self.model_dir, f"{str(latest_timestamp)}", MODEL_FILE_NAME)
            return latest_model_path
        except Exception as e:
            raise SensorException(e, sys)

    def is_model_exists(self)->bool:
        try:
            if not os.path.exists(self.model_dir):
                return False
            
            timestamps = os.listdir(self.model_dir)
            if len(timestamps) == 0:
                return False
            
            latest_model_path = self.get_best_model_path()
            print(latest_model_path)
            if not os.path.exists(latest_model_path):
                return False
            print(latest_model_path)

            return True
        except Exception as e:
            raise SensorException(e, sys)