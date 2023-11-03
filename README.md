# Sistema de controle de acesso com Interface Web e API REST
### 1. Nomes dos membros do grupo:

* Lecio Alves
* Matheus

### 2. Explicação do sistema:

O sistema é composto de um servidor web com interface em html, uma API e um banco de dados. 
Os usuários do sistema são os usuários das fechadura e um administrador.
As fechaduras interagem com a API através do protocolo HTTP. Ao usar uma fechadura, os usuários devem apresentar suas credenciais no dispositivo Fechadura o qual fará uma requisição ao Servidor através da API HTTP, tendo como resposta se aquele usuário tem ou não a permissão para ingresso na sala, protegida pela fechadura.
O Servidor possui uma Interface web para cadastro de usuários. Ela possui o usuário admin que é fixo e pré-definido desde sua criação e instanciação. Este usuário pode cadastrar e remover, usuários e fechaduras, além de cadastrar permissões para os usuários.
Este sistema foi construído na linguagem Python utilizando o ORM (Object Relational Mapping), é uma técnica que abstrai o banco de dados em objetos. O banco de dados se encontra em database/models.py e possui operações de inserção e remoção que estão em database/operations.py 
A pasta api contém a definição do endpoint para acesso das fechaduras ao sistema, cuja lógica de negócio é definida em uma classe.


### 3. Eexplicação das tecnologias utilizadas.
* Debian 9 64 Bit - Sistema operacional utilizado
* Python 3.5 - Linguagem de programação
* Python pip - Gerenciador de pacotes da linguagem Python
* Python 3 Virtual Environment - Ambiente virtual para isolar pacotes instalados pelo Python pip
* Python Flask - Framework em Python para desenvolvimento de sistemas web
* Python Flask-restful - Pacote em Python para expressar APIs REST
* SQLAlchemy - Framework em Python que implementa banco de dados com interface ORM (Object Relational Mapping)


## Desenvolvimento no Linux (Debian 9 64 Bit):
### Dependências:
* Desenvolvido no Debian 9 64-bit
* Python 3.5
* Python pip
* Python 3 Virtual Environment


```bash
sudo apt install python3.5 python3-venv python3-pip
```

### Configurando o ambiente:
1. Criação:    `python3 -m venv ./venv`
2. Ativalção:  `source venv/bin/activate`
3. Dependências do sistema: `pip install -r requirements.txt`

### Executando:
1. Ativando ambiente:  `source venv/bin/activate`
2. Executando: `make`
3. Desativando ambiente: `deactivate`



