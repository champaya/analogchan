# ベースイメージとして公式のPythonイメージを使用
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# OpenCV用に必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# 必要なファイルをコピー
COPY . /app/

# Pythonの依存関係をインストール
RUN pip install -r requirements.txt