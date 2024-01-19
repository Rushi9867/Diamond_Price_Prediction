FROM python:3.8-slim-buster
USER root
RUN mkdir /app
COPY . /app/
WORKDIR /app/
RUN pip3 install -r requirements.txt
ENV AIRFLOW_HOME = "/app/airflow"
ENV AIRFLOW__CORE__DAGBAG_IMPORT_TIMEOUT = 1000
ENV AIRFLOW__CORE__ENABLE_XCOM_PICKLING = True
RUN airflow db upgrade
RUN airflow users create -e rushikhandare2203@gmail.com -f rushikesh -l khandare -p admin -r Admin -u admin
RUN chmod 777 start.sh
RUN apt update -y
ENTRYPOINT [ "/bin/sh" ]
CMD ["python3", "app.py"]