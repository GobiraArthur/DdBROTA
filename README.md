# Backend Diário de bordo

O projeto objetiva a implementação de um diário de bordo direcionado aos registros e controle de ocorrências dos ônibus durante as viagens. Os registros serão disponibilizados em versões desktop e mobile para os motoristas e fiscais de ocorrências. O projeto [Backend-DdB](https://github.com/GobiraArthur/DdBROTA) possibilitará o registro de ocorrências de forma remota por meio dos frameworks <b>Django e Kivy</b>.

## 📖 Sobre o projeto

O objetivo da funcionalidade backend é a configuração dos CRUDs de Incidentes, Telefones Emergenciais e Manutenções da API. Com os contextos das informações presentes nos bancos de dados, em Django, para o CRUD de vistorias e <b>registros das ocorrências relatadas pelos motoristas e/ou fiscais de veículos</b>. A comunicação com o banco de dados será em Django e a exibição será realizada por meio do API Kivy framework, o que permitirá maior <b>agilidade na elaboração dos registros de ocorrências</b> os quais passarão a ser via API, em substituição aos registros preenchidos manualmente. 

Consulte **[Implantação](https://github.com/GobiraArthur/DdBROTA)** para saber como implantar o projeto.

## 📚 Tecnologias utilizadas

- <b> Python 3.11.5 & [Django](https://www.djangoproject.com/download/5.0.8/tarball/) 5.0.6.</b> 
- <b>API e Interfaces Interativas</b> <small>| Kivy.</small>

## 📋 Pré-requisitos

Ferramentas a serem instaladas no seu ambiente de desenvolvimento:

- <b>Python</b> (versão 3.11.5 ou superior).
- <b>Django</b> (versão 5.0.6 ou superior).
- <b>Kivy</b> (versão 2.x ou superior).
- <b>Git</b> para clonar o repositório.

## 🛠 Configuração do ambiente

Execute os comandos a seguir para instalar as bibliotecas necessárias para o funcionamento do projeto backend:

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