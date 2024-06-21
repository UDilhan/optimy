# Welcome

Here you will find the instructions if you want to test my code :-)

The application is currently running at http://ec2-51-20-255-85.eu-north-1.compute.amazonaws.com/

# Host the application
Simply import the ```template.yml``` file to AWS CloudFormation and fill in the needed parameters during the deployment steps.

Note: the DB password has to be 8 char minimum. You should avoid special symbols in your password (this is not the purpose of the assessment).

Once the stack is deployed, go to the EC2 instance public IP or DNS name. You should see something like this :
```
id: 1 - Name: test1
id: 2 - Name: test2
id: 3 - Name: test3
```
Then you may go to the test section :-)

# Test
The test is processed by Selenium. It will tell you if the DB content is actually displayed on the website or not.

Here is how you can execute it.

1. Checkout the repository
```bash
git checkout https://github.com/UDilhan/optimy
```

2. Go to the tests folder
```bash
cd tests
```

3. Run the test with your EC2 URL : 
```bash
docker build -t my_test .
```

4. Compile the Docker image and then run it with your EC2 URL : 
```bash
docker run --rm my_test python test_selenium.py [EC2 URL HERE]
```

# Grafana

I'm not able to share you the grafana dashboard as there are variables inside so here is a screenshort URL you may check to view the dashboard
[Screenshot URL](https://prnt.sc/-jrEP-sJxzI6)
[Public dashboard not working](https://dilhan.grafana.net/public-dashboards/1e0e263e8d57471db876f946c0d29cac)
