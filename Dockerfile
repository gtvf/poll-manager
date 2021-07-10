FROM python:3.9
EXPOSE 8000
COPY . /poll-manager
WORKDIR /poll-manager
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]