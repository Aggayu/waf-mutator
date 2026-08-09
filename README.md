# 🛡️ WAF Polymorphic Obfuscator & Injector (Dynamic)
> **Desenvolvido por:** [Dext33](https://github.com) | **Versão:** 2.0.0 | **Licença:** MIT

Uma suíte automatizada de engenharia de segurança ofensiva (Red Team) unificada em um único script interativo. A ferramenta foi projetada para realizar transformações matemáticas polimórficas em strings e realizar disparos de validação HTTP POST contra URLs parametrizadas dinamicamente pelo operador.

---

## 📁 Estrutura de Arquivos Essenciais

*   **`main.py`**: O núcleo do ecossistema. Contém as rotinas matemáticas de ofuscação (RegEx dinâmico e codificação hexadecimal) e a interface interativa de linha de comando que gerencia as entradas de strings e URLs em tempo real.
*   **`README.md`**: Documentação e manual técnico do repositório.
*   **`LICENSE`**: Termos legais de direitos autorais da Licença MIT atribuídos a Dext33.

---

## 🚀 Instruções de Uso

### 1. Clonagem e Acesso
```bash
git clone https://github.com/waf-polymorphic-obfuscator.git
cd waf-polymorphic-obfuscator
```

### 2. Inicialização Interativa
```bash
python3 main.py
```

### 3. Exemplo de Execução
```text
Digite a string para ofuscar (ou Enter para sair): ' OR 1=1 --
Digite a URL do alvo que deseja testar (Ex: http://httpbin.org): http://httpbin.org

============================================================
[*] PROCESSANDO ANÁLISE DE RED TEAM
============================================================
[+] Payload Original : ' OR 1=1 --
[+] String Ofuscada  : 273d2d2d
[+] URL Alvo         : http://httpbin.org
------------------------------------------------------------
[+] Status HTTP      : 200
[+] Resultado Final  : 💥 PASSOU (O WAF aceitou ou não detectou o padrão)
============================================================
```

---

## ⚖️ Aviso de Isenção de Responsabilidade

O conteúdo e as ferramentas fornecidos neste repositório são estritamente para **fins educacionais, acadêmicos e de auditoria de segurança autorizada (Pentest)**. O autor não se responsabiliza pelo uso indevido, danos ou atividades ilícitas executadas com esta implementação.

---

## 📝 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações sobre os direitos garantidos a **Dext33**.
