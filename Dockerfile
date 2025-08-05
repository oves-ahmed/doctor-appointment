FROM python:3.10
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN apt-get update
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]
