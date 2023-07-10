FROM python:3.9

WORKDIR /app

ADD assignment_2.py .

RUN python -m pip install --upgrade pip
RUN pip install flask
EXPOSE 5000

CMD ["python","assignment_2.py"]

