from python:3

ADD src/ src/

RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]
