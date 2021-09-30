FROM ubuntu
RUN apt-get update && apt-get install python3-pip -y
RUN mkdir f-ticket
WORKDIR /f-ticket
ADD src /f-ticket
COPY .env ./
COPY requirements.txt ./
RUN pip install -r /f-ticket/requirements.txt
CMD ["python3","app.py"]