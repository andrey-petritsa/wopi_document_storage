FROM python
WORKDIR /app
COPY . .
CMD ["python", "simple_http_server_main.py"]