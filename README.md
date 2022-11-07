## PROTOTIPO-LOGIN-API

- [Sobre](#sobre)
- [Instalação](#instalação)
- [Documentação](#documentação)
- [Termos de uso](#termos-de-uso)
- [Referências](#referências)

<br>

# Sobre

<b>PrototipoLogin-API</b> é uma aplicação de login de fornecedores a seus relatórios Power-BI. Esta aplicação utiliza o framework Django.
<br>


Link AWS:

http://dev-bi-abkura.com.br.s3-website-us-east-1.amazonaws.com/

Repositório frontend:

https://github.com/AndreKuratomi/PrototipoLogin

# Instalação

<h5>0. Primeiramente, é necessário já ter instalado na própria máquina:</h5>

- Um <b>editor de código</b>, conhecido também como <b>IDE</b>. Por exemplo, o <b>[Visual Studio Code (VSCode)](https://code.visualstudio.com/)</b>.

- Uma <b>ferramenta cliente de API REST</b>. Por exemplo, o <b>[Insomnia](https://insomnia.rest/download)</b> ou o <b>[Postman](https://www.postman.com/product/rest-client/)</b>.

- <b>Python</b> e pacotes essenciais como <b>[asdf](https://asdf-vm.com/guide/getting-started.html)</b> e <b>[asdf-python](https://github.com/danhper/asdf-python)</b>.

- <p> E versionar o diretório para receber o clone da aplicação:</p>

```
git init
```

<br>
<h5>1. Fazer o clone do reposítório <span>PrototipoLogin-API</span> na sua máquina pelo terminal do computador ou pelo do IDE:</h5>

```
git clone https://github.com/AndreKuratomi/PrototipoLogin-API.git
```

<p>Entrar na pasta criada:</p>

```
cd PrototipoLogin-API
```

Após feito o clone do repositório PrototipoLogin-API, instalar:

O ambiente virtual e atualizar suas dependências com o seguinte comando:

```
python -m venv venv --upgrade-deps
```

Ative o seu ambiente virtual com o comando:

```
source/venv/bin/activate
```

Instalar suas dependências:

```
pip install -r requirements.txt
```

E rodar a aplicação:

```
code .
```
<br>

<h5>2. Feitas as instalações precisamos criar nosso arquivo de variáveis de ambiente, o <span style="text-decoration: underline">.env</span>:</h5>

```
touch .env
```

Dentro dele precisamos definir nossas variáveis de ambiente:

```
EMAIL_HOST_USER=user_mail
EMAIL_HOST_PASSWORD=password

POSTGRES_DB=database
POSTGRES_HOST=host
POSTGRES_PASSWORD=password
POSTGRES_USER=user
```

<b>Obs:</b> as informações contidas no arquivo <b>.env</b> não devem ser compartilhadas. O arquivo já consta no <b>.gitignore</b> para não ser subido no repositório.

# Documentação

Para ter acesso às descrições, detalhes das rotas e seus retornos, conferir documentação completa no link a seguir:

https://insomnia-documentation-mauve.vercel.app/

# Termos de uso

Esse projeto atende a fins exclusivamente didáticos e sem nenhum intuito comercial.

# Referências

- [AWS EC2](https://docs.aws.amazon.com/ec2/index.html)
- [AWS EC2 (Docker)](https://stackoverflow.com/questions/53974488/how-to-delete-and-recreate-a-postgres-database-using-a-single-docker-command)
- [Bcrypt](https://github.com/kelektiv/node.bcrypt.js)
- [Django](https://www.djangoproject.com/)
- [DjangoMail](https://docs.djangoproject.com/en/4.1/topics/email/)
- [Django Rest framework](https://www.django-rest-framework.org/#)
- [Docker](https://docs.docker.com/)
- [Dotenv](https://www.npmjs.com/package/dotenv)
- [Insomnia-documenter](https://www.npmjs.com/package/insomnia-documenter)
- [Insomnia-documenter (quick tutorial)](https://www.youtube.com/watch?v=pq2u3FqVVy8)
- [JWT](https://github.com/auth0/node-jsonwebtoken)

