FROM python:3.8

COPY . /app/
RUN pip install --no-binary :all: psutil

CMD ["tail", "-f", "/dev/null"]