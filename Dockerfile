FROM python:3.9.2-alpine3.13
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]