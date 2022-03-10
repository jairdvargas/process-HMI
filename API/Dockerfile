FROM python:3.9

WORKDIR /app

EXPOSE 5051

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install pipenv
RUN pipenv lock --requirements > paquetesrequeridos.txt
RUN pip install -r paquetesrequeridos.txt

COPY . ./

CMD [ "python", "main.py" ]