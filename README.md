# diario-de-bordo-backend-desktop-mobile-componentes-API

O projeto objetiva a implementação de um diário de bordo direcionado aos registros e controle de ocorrências dos ônibus durante as viagens. Os registros serão disponibilizados em versões desktop e mobile para os motoristas e fiscais de ocorrências. O projeto [Backend-DdB](https://github.com/GobiraArthur/DdBROTA) possibilitará o registro de ocorrências de forma remota por meio dos frameworks <b>Django, Angular e Kivy</b>.

## 📖 Sobre o projeto

O objetivo da funcionalidade frontend é a exibição das telas de endpoints, em Angular, com os contextos das informações presentes nos bancos de dados, em Django, para o CRUD de vistorias e <b>registros das ocorrências relatadas pelos motoristas e/ou fiscais de veículos</b>. A comunicação entre o backend e frontend será realizada por meio do API Kivy framework, o que permitirá maior <b>agilidade na elaboração dos registros de ocorrências</b> os quais passarão a ser via API em substituição aos registros preenchidos manualmente. 

Consulte **[Implantação](https://github.com/GobiraArthur/DdBROTA)** para saber como implantar o projeto.

## 📚 Tecnologias utilizadas

- <b>Frontend</b> <small>| , HTML5, CSS3 & [Angular CLI](https://github.com/angular/angular-cli) version 17.0.3 para construção das páginas dinâmicas de cadastro nas versões Web e Mobile.</small>
- <b>Backend</b> <small>| Python 3.11.5 & [Django](https://www.djangoproject.com/download/5.0.8/tarball/) 5.0.6.</small>
- <b>API e Interfaces Interativas</b> <small>| Kivy.</small>

## 📋 Pré-requisitos

Ferramentas a serem instaladas no seu ambiente de desenvolvimento:

- <b>Python</b> (versão 3.11.5 ou superior).
- <b>Django</b> (versão 5.0.6 ou superior).
- <b>Kivy</b> (versão 2.x ou superior).
- <b>Git</b> para clonar o repositório.

## 🛠 Configuração

Execute os comandos a seguir para instalar as bibliotecas necessárias para o funcionamento do projeto frontend:

- <b>Instale o Python 3 e o Django:</b>
```
sudo apt update
```
```
sudo apt install python3 python3-pip
```
```
pip install django
```
- <b>Instale o Kivy:</b>
```
pip install kivy
```
- <b>Navegue até a pasta do backend e instale as dependências:</b>
```
cd backend
```
```
pip install -r requirements.txt
```
- <b>Rode as migrações do banco de dados:</b>
```
python manage.py migrate
```
- <b>Inicie o servidor Django:</b>
```
python manage.py runserver
```

## ⚙️ Executando os testes

<strong><span style="color: red;">Ao final do projeto</span></strong>

### 🔩 Analise os testes de ponta a ponta

<strong><span style="color: red;">Ao final do projeto, se necessário</span></strong>

## 🛠️ Construído com

<strong><span style="color: red;">Verificar em reunião</span></strong>

## ✒️ Autores

* **Arthur Gobira** - [desenvolvedor](https://github.com/GobiraArthur)
* **Jose Ulian Cardoso** - [desenvolvedor](https://github.com/ulian18TIC18)
* **Leane Soares** - [desenvolvedor](https://github.com/Leane212)
* **Nairan Santos** - [desenvolvedor](https://github.com/nairansantos)
* **Paulo Cabral** - [líder Tech/desenvolvedor](https://github.com/xpcjunior)
* **Rafaela Britto** - [desenvolvedor](https://github.com/rcfbritto)