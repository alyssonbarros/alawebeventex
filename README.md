# AlaWeb Eventos

Sistema de Eventos

##Como desenvolver

1. Clone o repositorio
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instãncia com o .env
6. Execute os testes

'''console
git clone git@github.com:alyssonbarros/alawebeventex.git alawebeventex
cd alawebeventex
python -m venv .alawebeventex
source .alawebeventex/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
'''

##Como fazer o deploy

1. Crie uma instãncia no heroku
2. Envie as configurações para o keroku
3. Defina uma SECRET_KEY segura para a instãncia
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

'''console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force

'''