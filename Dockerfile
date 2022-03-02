FROM python:slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN apt-get update && apt-get install -y build-essential && pip install -r requirements.txt && apt-get install -y iputils-ping

# Copy Project Files
COPY tools /tools/
COPY ssh /ssh/
COPY main.py  ./
# Run the application:
CMD ["python", "main.py"]