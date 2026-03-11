FROM python:3.11

RUN useradd -m appuser

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

COPY requirements.txt .

RUN pip config set global.progress_bar off && \
  pip install -r requirements.txt < /dev/null

COPY . .

RUN chown -R appuser:appuser /app

USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]