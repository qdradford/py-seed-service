from python:3

ADD / src/

RUN ls src/

RUN pip install -r ./src/requirements.txt

CMD ["python", "./src/src/main.py"]
