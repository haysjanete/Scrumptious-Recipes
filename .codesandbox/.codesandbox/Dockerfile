FROM python:3.10.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "Scrumptious-Recipies.wsgi"]
