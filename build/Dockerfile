# ベースイメージ
FROM ubuntu:22.04

# 日本語表示用環境設定
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# aptモジュールインストール
RUN apt-get update
RUN apt-get install -y python3.10
RUN apt-get install -y python3-pip
RUN apt-get install -y less vim sudo wget curl git

# 環境変数を設定

# https://www.lifewithpython.com/2021/05/python-docker-env-vars.html
# 非空なら .pyc を生成しない
ENV PYTHONDONTWRITEBYTECODE 1
# 非空なら標準出力・標準エラーのストリームのバッファリングを行わない
ENV PYTHONUNBUFFERED 1

# パッケージインストール
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install openai
RUN pip install langchain
RUN pip install tiktoken
RUN pip install chromadb

# 環境変数設定
ENV PYTHONPATH "${PYTHONPATH}:/home/ubuntu/workspace/src"

## 権限定義 ##
# user_name, user_id, group_name, group_idを変更する
ARG user_name=ubuntu
ARG user_id=1000
ARG group_name=ubuntu
ARG group_id=1000

RUN groupadd -g ${group_id} ${group_name}
RUN useradd -u ${user_id} -g ${group_id} -d /home/${user_name} --create-home --shell /usr/bin/bash ${user_name}
RUN echo "${user_name} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN chown -R ${user_name}:${group_name} /home/${user_name}

# ワークスペース定義
USER ubuntu
ENV HOME /home/ubuntu
WORKDIR /home/ubuntu/workspace