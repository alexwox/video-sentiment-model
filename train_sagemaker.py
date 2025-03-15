from sagemaker.pytorch import PyTorch
from sagemaker.debugger import TensorBoardOutputConfig

def start_training():
    tensorborad_config = TensorBoardOutputConfig(
        s3_output_path="s3://alexwox-sentiment-analysis-saas/tensorboard",
        container_local_output_path="/opt/ml/output/tensorboard"
    )
    
    estimator = PyTorch(
        entry_point="train.py",
        source_dir="training",
        role="arn:aws:iam::361769561370:role/sentiment-analysis-execution-role",
        framework_version="2.5.1",
        py_version="py311",
        instance_count = 1,
        instance_type = "ml.g5.xlarge",
        hyperparameters = {
            "batch-size": 32,
            "epochs": 25,
        },
        tensorborad_config=tensorborad_config
    )
    
    #Start training
    estimator.fit({
        "training": "s3://alexwox-sentiment-analysis-saas/dataset/train",
        "validation": "s3://alexwox-sentiment-analysis-saas/dataset/dev",
        "test": "s3://alexwox-sentiment-analysis-saas/dataset/test"
    })

if __name__ == "__main__":
    start_training()