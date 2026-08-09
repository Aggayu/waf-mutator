# ---------------------------------------------------------------------------
# Ferramenta: Red Team WAF Validation Tool (Dynamic Polymorphic Injector)
# Desenvolvido por: Dext33
# Autor Exclusivo: Dext33
# Finalidade: Auditoria de Segurança Autorizada e Fins Educacionais
# ---------------------------------------------------------------------------

import re
import requests

def codifica_hexadecimal(string):
    return string.encode('utf-8').hex()

def substitui_caracteres(string, caracteres_proibidos):
    return ''.join(c for c in string if c not in caracteres_proibidos)

def polimorfiza_string(string):
    substituicao_caracteres = {
        r'\w': '',
        r'\d': '',
        r'\s': '',
    }
    for padrao, substituto in substituicao_caracteres.items():
        string = re.sub(padrao, substituto, string)
    return string

def aplica_codificação_hexadecimal(string):
    return codifica_hexadecimal(string)

def ofusca_string(string):
    string_polimorfizada = polimorfiza_string(string)
    string_hex = aplica_codificação_hexadecimal(string_polimorfizada)
    string_substituido = substitui_caracteres(string_hex, ['/', '\\', ':', ';', '"', "'"])
    return string_substituido

def executar_disparo_dinamico(url_alvo, payload_original):
    """
    Processa a string do usuário através do motor polimórfico
    e realiza o envio imediato via HTTP POST para a URL inserida.
    """
    print("\n" + "="*60)
    print("[*] PROCESSANDO ANÁLISE DE RED TEAM")
    print("="*60)
    
    # Aplica as regras matemáticas de ofuscação criadas por Dext33
    payload_ofuscado = ofusca_string(payload_original)
    
    print(f"[+] Payload Original : {payload_original}")
    print(f"[+] String Ofuscada  : {payload_ofuscado}")
    print(f"[+] URL Alvo         : {url_alvo}")
    print("-" * 60)
    print("[*] Enviando requisição HTTP POST...")

    dados_requisicao = {
        'username': payload_ofuscado,
        'password': 'validacao_segura_dext33'
    }

    try:
        # Realiza o disparo para a URL que o usuário digitou no terminal
        resposta = requests.post(url_alvo, data=dados_requisicao, timeout=5)
        status = resposta.status_code
        
        if status == 200:
            resultado = "💥 PASSOU (O WAF aceitou ou não detectou o padrão)"
        elif status == 403:
            resultado = "🛡️ BLOQUEADO (O WAF identificou e barrou o acesso)"
        elif status == 405:
            resultado = "❌ MÉTODO REJEITADO (O servidor não aceita requisições POST nesta rota)"
        else:
            resultado = f"❓ RETORNO HTTP {status}"

    except requests.exceptions.RequestException:
        status = "ERR"
        resultado = "🚨 TIMEOUT/DROP (O Firewall derrubou a conexão completamente)"

    print(f"[+] Status HTTP      : {status}")
    print(f"[+] Resultado Final  : {resultado}")
    print("="*60 + "\n")

def main():
    print("=" * 60)
    print("🛡️ SUÍTE DE VALIDAÇÃO POLIMÓRFICA WAF - POR DEXT33 🛡️")
    print("=" * 60)
    
    while True:
        # Pergunta 1: Captura a string de teste
        payload = input("Digite a string para ofuscar (ou Enter para sair): ")
        if not payload:
            print("[*] Encerrando ferramenta.")
            break
            
        # Pergunta 2: Captura a URL alvo dinamicamente
        url = input("Digite a URL do alvo que deseja testar (Ex: http://httpbin.org): ")
        if not url:
            print("[!] Erro: A URL do alvo não pode ficar vazia. Tente novamente.\n")
            continue

        # Executa a engine completa
        executar_disparo_dinamico(url, payload)

if __name__ == '__main__':
    main()
