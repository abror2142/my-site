FROM python:3

COPY ./requirements.txt /
RUN pip install --timeout=1000 --no-cache-dir -r /requirements.txt

COPY ./entrypoint.sh /

WORKDIR /home/app/backend
COPY . .

EXPOSE 8000
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
