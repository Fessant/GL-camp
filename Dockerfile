FROM python:3.8

COPY . /app/
RUN pip install --no-binary :all: psutil
RUN chmod +x /app/cp.sh
ENTRYPOINT ["bash", "/app/cp.sh"]
CMD ["tail", "-f", "/dev/null"]