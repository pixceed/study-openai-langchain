# ベースイメージ
FROM python:3.10-slim

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

# ワークスペース定義
ENV HOME /home/ubuntu
WORKDIR /home/ubuntu/workspace