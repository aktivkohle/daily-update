FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY emailResult.py ./
COPY config.py ./
COPY scrape_and_send.py ./
COPY scheduler.py ./

CMD [ "python", "./scheduler.py" ]