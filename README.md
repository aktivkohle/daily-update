# Receive emailed updates of changes to a municipality website involving certain keywords

So the application is the following - plans for new factories or buildings in your neighbourhood, which possibly pollute or ruin the ambiance are lodged with the local council. The plans are not necessarily more widely advertised, and the law is that if the plans are visible on the municipal website for 90 days and nobody says anything, permission is deemed to be granted. 

So what I have made here is a Python app that scrapes the table on the website once or twice a day with pandas, searches for search terms predefined in the config.py file (not in repository obviously), and then sends an email to several recipients who live in the area. The number of matching lines is also in the email. The schedule is managed by the Python library APScheduler and then a delay of a random number of minutes is added on top to make the daily traffic seem perhaps more human. The Python files have been put in a Docker container and deployed on an Amazon nano instance for under €5 per month.    

## Dockerising and Deploying

This was very detailed, a mix of command line and AWS gui to dockerise the application and deploy it correctly with the Amazon container service ECS. This is a note-to-self so I remember what I did in case it needs to be repeated one day..

To dockerize the Python files in this directory type:
`docker build -t daily_update .`

To run the docker container type:
`docker run daily_update`

`docker images` and `docker ps -a` let you see the image and container on your local machine.

There is a certain amount of setting up in AWS - an instance needs to go into a Cluster, it needs an IAM role attached, and the repositoiries in ECS need permissions attached.

### Here is then the procedure to get it from your local machine into ECS and deploy it.

Assuming you have the AWS command line interface installed and credentials stored..

`aws ecr get-login --no-include-email --region eu-central-1`

then copy and paste back in the terminal that gigantic docker login command that gets returned

`docker tag  allrecipients:latest  478310531824.dkr.ecr.eu-central-1.amazonaws.com/ecs-repo-1:latest`

`docker push 478310531824.dkr.ecr.eu-central-1.amazonaws.com/ecs-repo-1:latest`

Go to AWS click on EC2 container service. When you click on repository you should see in there what was just pushed, check the time stamp. Ensuring there is a running instance in the 'cluster', create a 'task definition' for the link to the repo and then go into the cluster and tell it to run the task. Do not mix up 'task' and 'service' - task is what you want, service is possibly a collection of tasks. 
