# Receive emailed updates of changes to a municipality website involving certain keywords

A certain website is scraped once per day a random number of seconds after the same time of day, certain keywords are searched and matching lines emailed. The thing is, you don't want to remember to push a button every day, so you should just receive an email. This small set of scripts here includes what is needed to put the app in a docker container and deploy it. I have it running in a nano instance for under €5 per month.

An interesting Python package APScheduler has been used to do the daily send. The municipal website is in table form and it scrapes very nicely with Pandas.

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

Go to AWS click on EC2 container service. When you click on repository you should see in there what was just pushed, check the time stamp. Ensuring there is a running instance in the 'cluster', create a 'task definition' for the link to the repo and then go into the cluster and tell it to run the task. 
