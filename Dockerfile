# 현 프로젝트에서 사용한 python 버전의 base image
FROM python:3.9-slim-buster
# .pyc 파일 생성 금지
ENV PYTHONDONTWRITEBYTECODE = 1
# 버퍼링 제거
ENV PYTHONUNBUFFERED = 1

RUN apt-get update && apt-get install -y gcc libpq-dev python3-dev

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "category.wsgi:application"]
EXPOSE 8000