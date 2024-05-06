FROM python:3.8.13-slim
WORKDIR /usr/src/kali

RUN pip install --upgrade pip
RUN pip install django djangorestframework django-cors-headers

COPY ./requirements.txt .
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "/usr/src/kali/entrypoint.sh" ]