FROM python:3.11

WORKDIR /src
COPY . .

RUN python -m pip install --no-cache-dir --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV=prod

CMD ["python3", "-m", "src"]