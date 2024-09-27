FROM python:3.12

WORKDIR /code

COPY requirements.txt .

RUN pip install crewai

RUN pip install 'crewai[tools]'

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 80

CMD ["fastapi", "run", "main.py", "--port", "80"]

