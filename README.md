Para rodar a API é preciso criar um banco de dados POSTGRESS e configurar um arquivo .env seguindo o exemplo contido no repositório

Depois é preciso executar os seguintes comandos comandos: 

python -m venv venv

(bash)
source venv/Scripts/activate 

pip install -r requirements.txt

em seguida para rodar o servidor localmente:

python manage.py runserver

para acessar a documentação da API com suas rotas, acesse: http://127.0.0.1:8000/api/docs/
(127.0.0.1:8000) este endereço pode sofrer alterações e sera confirmado no termial após rodar o comando runserver

para facilitar a interação pode-se usar a aplicação front-end:
https://github.com/PONGSU/Clients-Contacts-Management-FrontEnd
