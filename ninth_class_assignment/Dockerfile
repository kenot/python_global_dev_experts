FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y \
    libc6 \
    libnss3 \
    libpam0g \
    libcap2-bin \
    libselinux1 \
    passwd && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY get_user.py .

ENV USER=tdinkov

CMD ["python", "./get_user.py"]