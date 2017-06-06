# Receive emailed updates of changes to a municipality website involving certain keywords

A certain website is scraped once per day a random number of seconds after the same time of day, certain keywords are searched and matching lines emailed. 

To dockerize the python files type:
`docker build -t daily_update .`

To run the docker container type:
`docker run daily_update`