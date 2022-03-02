FROM python:latest

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN apt-get update && pip install -r requirements.txt && apt-get install -y iputils-ping
# Copy Project Files
COPY tools /project/tools
COPY ssh /project/ssh
COPY main.py  /project/
# Run the application:
CMD ["python", "project/main.py"]