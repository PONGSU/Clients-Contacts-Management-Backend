A API esta hospedada em https://clients-contacts-manager.onrender.com/api/

Para ver a documentação e rotas acesse: https://clients-contacts-manager.onrender.com/api/docs/

Para acessar a aplicação front end, já integrada com o banco de dados e a API utilize: https://clients-contacts.vercel.app

---------------------------------------------------------------------------------



Se preferir rodar a API Localmente, depois de clonar o repositório, é preciso criar um banco de dados POSTGRESS e configurar um arquivo .env seguindo o exemplo .env.exemple contido na raiz do projeto

Depois é preciso executar os seguintes comandos comandos: 

python -m venv venv

(git bash)
source venv/Scripts/activate 

pip install -r requirements.txt

em seguida para rodar o servidor localmente:

python manage.py runserver

para acessar localmente a documentação da API com suas rotas, acesse: http://127.0.0.1:8000/api/docs/
(127.0.0.1:8000) este endereço pode sofrer alterações e sera confirmado no termial após rodar o comando runserver

para facilitar a interação pode-se usar a aplicação front-end:
https://github.com/PONGSU/Clients-Contacts-Management-FrontEnd
