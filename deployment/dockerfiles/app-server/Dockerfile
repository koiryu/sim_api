# debianベースのpythonイメージをベースとする
FROM python:3.10-slim-buster

# 設定ファイルの転送(適当な場所が思いつかないので/app直下)
RUN mkdir -p /app/config
COPY requirements.txt /app/requirements.txt
COPY config/gunicorn_settings.py /app/config/gunicorn_settings.py
COPY sim_api.py /app/sim_api.py

# パッケージのインストール
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

EXPOSE 9876
# cdにあたるコマンド
WORKDIR /app

# run実行時のコマンド
# ENTRYPOINT->CMDでCMDはrunのときの引数で上書きすることが可能
ENTRYPOINT [ "gunicorn", "sim_api:app" ]
CMD [ "-c", "/app/config/gunicorn_settings.py" ]
