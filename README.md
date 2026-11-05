# waf-mutator

Script interativo em Python que recebe uma string, codifica em hexadecimal e dispara um POST contra uma URL para ver se passa por um WAF.

Projeto de estudo, de agosto de 2024.

## Uso

git clone https://github.com/Aggayu/waf-mutator.git
cd waf-mutator
python3 main.py

Digite a string: ' OR 1=1 --
Digite a URL: http://httpbin.org

Saída: payload original, versão em hexadecimal, URL e resposta HTTP.

## Limites

- Só codificação hexadecimal; não há mutação aleatória.
- Não detecta WAF: mostra o código HTTP e o corpo.
- Sem TLS, proxy ou cookies.

MIT
