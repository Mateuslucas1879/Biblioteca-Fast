/* Para fazer uma instalação do FastAPi com poetry */
    poetry install
    poetry add 'fastapi[standard]'


/*  Habilitar o ambiente virtual, para que o python consiga enxergar nossas dependências instaladas.
O poetry tem um comando específico para isso: */

    poetry shell

/* Agora com o ambiente virtual ativo,
podemos iniciar nosso servidor FastAPI para iniciar nossa aplicação */

    fastapi dev biblioteca_fast/app.py


/* Também é possível executar os comandos sem entrar no shell do ambiente virtual.
 É mais verboso, mas funciona bem: */

    poetry run fastapi dev biblioteca_fast/app.py

/* As ferramentas escolhidas são:

taskipy: ferramenta usada para criação de comandos. Como executar a aplicação, rodar os testes, etc.
pytest: ferramenta para escrever e executar testes
ruff: Uma ferramenta que tem duas funções no nosso código:
Um analisador estático de código (um linter), para dizer se não estamos infringindo alguma boa prática de programação;
Um formatador de código. Para seguirmos um estilo único de código. Vamos nos basear na PEP-8.
Para instalar essas ferramentas que usaremos em desenvolvimento, podemos usar um grupo de dependências (--group dev no poetry) focado nelas, para não serem instaladas quando nossa aplicação estiver em produção:

   poetry add --group dev pytest pytest-cov taskipy ruff

