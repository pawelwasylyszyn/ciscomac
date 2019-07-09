FROM python:2
ADD macquery.py /
ENTRYPOINT [ "python" ,"/macquery.py" ]
CMD []
