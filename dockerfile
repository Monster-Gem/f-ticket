FROM ubuntu
RUN apt-get update && apt-get install python3-pip -y
RUN mkdir f-ticket
WORKDIR /f-ticket
ADD src /f-ticket
COPY .env requirements.txt entrypoint.sh ./
RUN pip install -r /f-ticket/requirements.txt
CMD ["/bin/bash", "entrypoint.sh"]