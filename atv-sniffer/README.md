# Packet Sniffer com Página de Login

Um sniffer de pacotes simples em Python com uma pa´gina de login de teste para gerar tráfego HTTP, desenvolvido para fins acadêmicos.

## Visão geral

- **Sniffer**: Faz a captura de pacotes TCP/UDP e mostra os IPS, portas e payloads de origem e destino.
- **Login Page**: Uma página HTML simples, estilizada com Tailwind CSS, que envia requests de login via método POST para testar o sniffer.

## Requerimentos

- Python 3.x
- Lib Scapy (`pip install scapy`)
- Navegador Web (para página de login)
- Privilégios root/admin (para o sniffer)

## Instalação

1. Clone o repositório:
git clone https://github.com/majusalins/atv-sniffer.git
cd atv-sniffer

2. Instale as dependências do Python:
pip install -r sniffer/requirements.txt

## Como Testar

1. Em um terminal, execute o sniffer:
sudo python3 sniffer/sniffer.py -v

2. Em outro terminal, acesse a pasta do projeto e inicie o servidor web:
python3 -m http.server 8000 --directory web

3. Acesse http://localhost:8000 no seu navegador.

4. Preencha o formulário e envie.

5. Observe a saída no terminal do sniffer.
