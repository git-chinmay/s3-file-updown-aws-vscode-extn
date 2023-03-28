# s3-file-updown-aws-vscode-extn
 Uploading Downloading File S3 using VS Code extention.


## Steps
- SAM CLI Install (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- AWS CLI Install (https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- AWS Toolkit for VS Code install and Configure
- Create project folder
- Click on AWS Eplorer and right click on Lambda and select Create a SAM Lambda Function
- Create an empty lambda in AWS Console(Bcz if there is no lambda present then SAM will not deploy)
- Go to your hello_world folder and under app.py(considering you have selected python as runtime for your lambda) write your lambda function
- Go to template.yml file and add make sure the Runtime is correct(It should be AWS supported).
Example:- Let your laptop runs with python3.10 and AWS can support upto 3.9. If you choose runtime 3.10 i template.yml then the deploy will fail
If you choose runtime as 3.9 then build will fail as it will not find the python 3.9 in your system while packaging the code.
- To deploy the Lambda, right click on your template.yml and selct upload lambda.

Note: This blog contains steps for creating and deploying a SAM application. Although the blog is oudated now as AWS changed its approach a lot still good to refer to get you started.


## Status
This repo is not completed. Current lambda just only printing a line. file upload/download not yet tested.