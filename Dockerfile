FROM python

ADD db_helper.py /

CMD ["python", "db_helper.py"]