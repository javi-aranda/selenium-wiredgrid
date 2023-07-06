FROM python:3.8

COPY requirements /tmp
WORKDIR /tmp
RUN echo "Installing requirements"
RUN pip install -r requirements.txt

WORKDIR /code
RUN echo "Starting proxy server..."
ENTRYPOINT ["./selenium-proxy/entrypoint.sh"]