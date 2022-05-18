FROM python:latest
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py
CMD [ "python3", "app.py"]
EXPOSE 5000