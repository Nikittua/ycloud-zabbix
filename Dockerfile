FROM ubuntu
COPY app app/
RUN apt update && apt install -y curl && apt install -y python3 && apt install -y python3-pip
RUN pip install -r /app/imports.txt
RUN curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
RUN echo 'source /root/yandex-cloud/completion.zsh.inc' >>  ~/.zshrc
WORKDIR /app
ENTRYPOINT ["/usr/bin/python3", "main.py"]
