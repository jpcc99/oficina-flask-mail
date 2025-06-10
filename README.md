# Oficina de Flask e Flask-Mail

Este repositório contém os materiais para uma oficina sobre envio de e-mails em aplicações Flask utilizando a extensão Flask-Mail.

## Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)
- Conta de e-mail para testes (recomendado: Gmail ou serviço com SMTP)

## Configuração do Ambiente

### 1. Clone o repositório
```bash
git clone https://github.com/jpcc99/oficina-flask-mail.git
cd oficina-flask-mail
```

### 2. Crie e ative um ambiente virtual (recomendado)
#### No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### No Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install flask flask-mail
```

## Configuração do Aplicativo

```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=seuemail@gmail.com
MAIL_PASSWORD=suasenha
MAIL_DEFAULT_SENDER=seuemail@gmail.com
```

**Observação:** Para contas Gmail, você pode precisar criar uma "Senha de App" ou habilitar "Acesso a app menos seguro".

## Executando a Aplicação

```bash
python app.py
```

O servidor Flask será iniciado em `http://localhost:5000`.

## Dúvidas e Suporte

Para dúvidas durante a oficina, entre em contato com o instrutor ou abra uma issue neste repositório.
