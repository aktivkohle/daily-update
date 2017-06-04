A certain website is scraped once per day a random number of seconds after the same time of day, certain keywords are searched and matching lines emailed. 

To dockerize the python files type:
docker build -t scrape_and_send .

To run the docker container type:
$ docker run scrape_and_send