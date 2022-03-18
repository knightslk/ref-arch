FROM python

RUN pip install -U Flask

WORKDIR /app

COPY svr.py .

ENV FLASK_APP=svr
ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0
