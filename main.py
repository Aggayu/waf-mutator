#!/usr/bin/env python3
"""waf-mutator — muta um payload, codifica em hexadecimal e dispara POST contra uma URL."""
import random
import re
import sys

try:
    import requests
except ImportError:
    sys.exit("falta o pacote requests: pip install requests")


def mutar(s):
    """Colapsa espacos e alterna a caixa — muda a assinatura sem perder conteudo."""
    s = re.sub(r"\s+", " ", s).strip()
    return "".join(c.upper() if random.random() < 0.5 else c.lower() for c in s)


def hexificar(s):
    return s.encode("utf-8").hex()


def ofuscar(s):
    return hexificar(mutar(s))


def disparar(url, original):
    payload = ofuscar(original)

    print("=" * 60)
    print("[*] payload original:", original)
    print("[*] payload mutado  :", mutar(original))
    print("[*] enviado em hex  :", payload)
    print("[*] alvo            :", url)
    print("-" * 60)

    try:
        r = requests.post(url, data={"username": payload, "password": "aggayu"}, timeout=5)
        print("[+] status HTTP     :", r.status_code)
        if r.status_code == 200:
            print("[+] passou")
        elif r.status_code == 403:
            print("[+] bloqueado pelo WAF")
        elif r.status_code == 405:
            print("[+] metodo POST nao aceito nesta rota")
        else:
            print("[+] retorno nao mapeado")
    except requests.exceptions.RequestException as e:
        print("[+] sem resposta    :", type(e).__name__)
    print("=" * 60)


def main():
    print("=" * 60)
    print("waf-mutator")
    print("=" * 60)
    while True:
        alvo_string = input("string para ofuscar (Enter para sair): ")
        if not alvo_string:
            break
        url = input("URL alvo (ex: http://httpbin.org): ").strip()
        if not url:
            print("URL vazia, tente de novo.")
            continue
        disparar(url, alvo_string)


if __name__ == "__main__":
    main()
