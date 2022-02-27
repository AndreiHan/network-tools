FROM python:latest

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN apt-get update && pip install -r requirements.txt && apt-get install -y iputils-ping
# Run the application:
COPY . .
CMD ["python", "main.py"]