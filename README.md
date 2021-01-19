# TestPythonProject
Testing alternate deployments

## Web API with Lambda 

1. Create the Lambda function with Python:
This creates a basic HTTP web API, not a webpage.
Deployed Endpoint can be tested doing a POST to: https://04qej1765k.execute-api.us-west-2.amazonaws.com/default/TestPythonFunction

The lambda function takes as input 2 parameter in the json format when doing a post to the above endpoint:
{
  "FirstParameter": "hello",
  "SecondParameter": "world"
}

Build a very simple Lambda function:
https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html

The python script and data for the lambda test event is in the scripts folder of the project

1. Create API Gateway to point to the Lambda function

Attach a url to the Lambda via api gateway so it can be accessed from anywhere:
https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

For API type, REST API was selected
This creates a Lambda Proxy integration where the body is encapsulated, thus the need to extract the body parameter before accessing

## Web page with EC2 instance

1. Create free tier EC2 instance 
	- Ubuntu 20.04
	- Enable auto-assign IP to get a public IP address
	- Create a new security group with an added Rule of HTTP with Source Anywhere
	- Create new key pair and save the pem file

1. Ssh into EC2 instance
	- pem file is in root of the project: TestPythonProject.pem
	- To login to the sample EC2 instance: ssh -i .ssh/TestPythonProject.pem ubuntu@54.214.109.76

1. Install Python Flask for Ubuntu: https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/
	- make sure to update repositories first: sudo apt update
	- download the main.py file from the root of the project in place of the hello.py
		- copy contents of main.py from the root of the project into the root of the venv instead of creating hello.py

1. Install nginx: https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04
	- dont need to worry about enabling ufw as we are on ec2 instance where security is governed by security groups:     sudo ufw allow 'Nginx HTTP' 
	- test by browsing to your public ip address: http://54.214.109.76
		- should display "Welcome to nginx!
	- No need for Step 5 – Setting Up Server Blocks (Recommended)
	- copy over nginx.conf from the root of the project to /etc/nginx and over-write the existing nginx.conf
	- restart nginx: sudo systemctl restart nginx
	
1. Start the python app
	- make sure you are in your pthon venv and it is active
	- run python main.py
	
1. Browse to your public ip address (http://54.214.109.76) again to enter the two parameters
	
