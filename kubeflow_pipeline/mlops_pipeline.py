import kfp
from kfp import dsl # domain-specific language

#### Components for the Kubeflow Pipeline
def data_preprocessing_op():
    return dsl.ContainerOp(
        name='Data Processing',
        image='htai99/my-mlops-ap:latest',
        command=['python', 'src/data_processing.py']
    )


def model_training_op():
    return dsl.ContainerOp(
        name='Model Training',
        image='htai99/my-mlops-ap:latest',
        command=['python', 'src/model_training.py']
    )

#### Pipeline starts here...
@dsl.pipeline(
    name='MLOPS Pipeline',
    description='A pipeline to preprocess data, train a model, and deploy it.'
)
def mlops_pipeline():
    # Step 1: Data Preprocessing
    data_preprocessing = data_preprocessing_op()

    # Step 2: Model Training
    model_training = model_training_op().after(data_preprocessing)


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(
        mlops_pipeline, "mlops_pipeline.yaml"
    )