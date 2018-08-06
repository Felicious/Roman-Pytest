FROM python

COPY . /code/
WORKDIR /code

CMD ["python", "./db_helper.py"]