FROM python:3.7

WORKDIR /flask

COPY ./api /flask

RUN pip install --upgrade pip pipenv

RUN pipenv install --system

CMD ["python", "helpdesk_rest.py"]

CMD ["gunicorn","-w", "4", "-b", "0.0.0.0:3030", "helpdesk:app"]
