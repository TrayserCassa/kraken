FROM python:3.10.9-alpine3.17

WORKDIR /

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY templates/ templates/
COPY app.py .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
