# Padrão de Projeto Proxy

## Introdução

O padrão de projeto proxy é um padrão estrutural que nos fornece um substituto para um outro objeto (surrogate) ou marcador da localização de outro objeto para controlar o acesso a esse objeto.

## Motivações

Uma das principais motivações desse padrão de projeto é adiar o custo integral de sua inicialização até o momento que de fato precisemos dele, armazenar os dados em cache e fazer o controle de acesso.

## Executando a aplicação

Para executar a aplicação observe os passos abaixo.

```
git clone https://github.com/marte2050/pattern-design-proxy .

docker compose up -d

cd pattern-design-proxy

poetry shell

fastapi dev main.py
```

Para fazer o teste da aplicação execute o comando curl conforme exemplo abaixo:

```
curl -o /dev/null -s -w "Tempo total: %{time_total}s\n" localhost:8000/100

curl -o /dev/null -s -w "Tempo total: %{time_total}s\n" localhost:8000/100
```

Perceba que na primeira chamada a API levou-se aproximadamente 10 segundos isso se deve ao fato da aplicação não encontrar-se em cache ainda. Já ao executar a segunda chamada os dados já estão estão armazenados em cache.