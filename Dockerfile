FROM python:3
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY config.json .
COPY main.py .
CMD ["python", "./main.py"]