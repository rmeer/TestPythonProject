# TestPythonProject
Testing alternate deployments

## Web API with Lambda 

1. Create the Lambda function with Python:
This creates a basic HTTP web API, not a webpage.
Deployed Endpoint: https://04qej1765k.execute-api.us-west-2.amazonaws.com/default/TestPythonFunction

The lambda function takes as input 2 parameter in the json format when doing a post to the above endpoint:
{
  "FirstParameter": "hello",
  "SecondParameter": "world"
}

Build a very simple Lambda function:
https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html

The python script and data for the lambda test event is in the scripts folder

1. Create API Gateway to point to the Lambda function

Attach a url to the Lambda so it can be accessed from anywhere:
https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

For API type, REST API was selected
This creates a Lambda Proxy integration where the body is encapsulated, thus the need to extract the body parameter before accessing

## Web page with EC2 instance
