FROM python:3.10
# pra imagem evitar de utilizar os arquivos .pyc no containerENV PYTHONDONTWRITEBYTECODE 1
# joga os logs de erro direto pro terminal de logs do containerENV PYTHONNUNBUFFERED 1
COPY ./requirements.txt .
RUN pip install -U pipRUN pip install -r requirements.txt
WORKDIR /code
COPY . /code/