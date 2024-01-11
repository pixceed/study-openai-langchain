# OpenAI LangChain

## Docker 環境構築

イメージ作成
```
docker build -t openai_image build
```

コンテナ作成
```
docker run -it -v `pwd`:/home/ubuntu/workspace -p 8501:8501 --name openai_container openai_image:latest bash
```


