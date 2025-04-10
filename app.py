import boto3
import zipfile
import changes by pratham 

LAMBDA_FUNCTION_NAME = "helloLambdaBoto3"
ROLE_ARN = "arn:aws:iam::123456789012:role/lambda-execution-role"  # replace with your actual role ARN

# 1. Create ZIP file
def create_zip():
    with zipfile.ZipFile('function.zip', 'w') as zipf:
        zipf.write('lambda_function.py')

# 2. Create Lambda function
def create_lambda():
    create_zip()
    with open("function.zip", "rb") as f:
        zipped_code = f.read()

    client = boto3.client('lambda')

    response = client.create_function(
        FunctionName=LAMBDA_FUNCTION_NAME,
        Runtime='python3.12',
        Role=ROLE_ARN,
        Handler='lambda_function.lambda_handler',
        Code=dict(ZipFile=zipped_code),
        Timeout=15,
        Publish=True
    )

    print("Lambda function created:")
    print(response)

if __name__ == "__main__":
    create_lambda()

