FROM python:3.7.6-buster

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY covid.csv /app/

COPY *.py /app/
RUN chmod a+x *.py

CMD ["./main.py"]