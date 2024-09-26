## prototipo_login_api

- [Traduções](#traduções)
- [Sobre](#sobre)
- [Links](#links)
- [Instalação](#instalação)
- [Documentação](#documentação)
- [Referências](#referências)

<br>

## Traduções

- [English / Inglês](./.multilingual_readmes/README_en-uk.md)
- [Português brasileiro](https://github.com/AndreKuratomi/prototipo_login_api/tree/pt_br)

<br>

## Sobre

<b>prototipo_login_api</b> é uma API para login de fornecedores a seus relatórios Power-BI filtrando por período de assinatura. O superusuario consegue visualizar todos eles em seu dashboard.

Os usuários também podem trocar de senha caso desejem. Para mais informações conferir no repositório [front](https://github.com/AndreKuratomi/PrototipoLogin).

Esta aplicação utiliza o framework <b>Django</b>, a lib <strong>DjangoMail</strong>, o software <b>Docker</b> e o serviço AWS <strong>EC2</strong>.
<br>

## Links

AWS S3 [link](http://dev-bi-abkura.com.br.s3-website-us-east-1.amazonaws.com/)

Repositório [frontend](https://github.com/AndreKuratomi/prototipo_login_api)

<br>

## Instalação

<h3>0. Primeiramente, é necessário já ter instalado na própria máquina:</h3>

- O versionador de codigo <b>[Git](https://git-scm.com/downloads)</b>,

- A linguagem de programação <b>[Python](https://www.python.org/downloads/)</b> e pacotes essenciais como <b>[asdf](https://asdf-vm.com/guide/getting-started.html)</b> e <b>[asdf-python](https://github.com/danhper/asdf-python)</b>,

- Um <b>editor de código</b>, conhecido também como <b>IDE</b>. Por exemplo, o <b>[Visual Studio Code (VSCode)](https://code.visualstudio.com/)</b>,

- O software <b>[Docker](https://docs.docker.com/)</b>,

- O banco de dados <b>[PostgreSQL](https://www.postgresql.org/)
</b>,

- Uma <b>ferramenta cliente de API REST</b>. Por exemplo, o <b>[Insomnia](https://insomnia.rest/download)</b> ou o <b>[Postman](https://www.postman.com/product/rest-client/)</b>,

- <p> E versionar o diretório para receber o clone da aplicação:</p>

```
git init
```

<br>

<h3>1. Fazer o clone do reposítório <b>prototipo_login_api</b> na sua máquina pelo terminal do computador ou pelo do IDE:</h3>

```
git clone https://github.com/AndreKuratomi/prototipo_login_api.git
```

WINDOWS:

Obs: Caso apareca algum erro semelhante a este: 

```
unable to access 'https://github.com/AndreKuratomi/prototipo_login_api.git': SSL certificate problem: self-signed certificate in certificate chain
```

Configure o git para desabilitar a certificação SSL:

```
git config --global http.sslVerify "false"
```


<p>Entrar na pasta criada:</p>

```
cd prototipo_login_api
```
<br>

<h3>2. Após feito o clone do repositório, instalar:</h3>

<h4>O ambiente virtual* e atualizar suas dependências com o seguinte comando:</h4>

LINUX:
```
python3 -m venv venv --upgrade-deps
```

WINDOWS:
```
py -m venv venv --upgrade-deps
```

Caso seja retornado algum erro semelhante a este basta seguir as instruções:

```
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.
```

*É interessante seguir esta prática porque diferentes projetos exigem diferentes dependências. Um ambiente virtual nada mais é do que um ambiente separado da sua máquina. Caso contrário, a máquina do usuário pode se encher de dependências que serão utilizadas apenas em um único projeto.

<h4>Ative o seu ambiente virtual com o comando:</h4>

LINUX:
```
source/venv/bin/activate
```

WINDOWS:

No sistema operacional Windows é necessário antes configurar o Execution Policy do PowerShell:

```
Get-ExecutionPolicy # para verificar o tipo de política de execução
Set-ExecutionPolicy RemoteSigned # para alterar o tipo de política se o comando acima mostrar 'Restricted'
```
Obs: Eventualmente, pode ser necessário abrir o PowerShell como administrador.

```
.\venv\Scripts\activate
```


<h4>Instalar suas dependências:</h4>

```
pip install -r requirements.txt
```

WINDOWS:

Caso seja retornado algum erro semelhante a este:

```
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\andre.kuratomi\\OneDrive - Company\\Área de Trabalho\\prototipo_login_api\\prototipo_login_api\\env\\Lib\\site-packages\\jedi\\third_party\\django-stubs\\django-stubs\\contrib\\contenttypes\\management\\commands\\remove_stale_contenttypes.pyi'
HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths
```

Rode no cmd como adminstrador o seguinte comando:

```
reg.exe add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f
```
<br>

<h3>3. Abrir a aplicação no IDE:</h3>

```
code .
```

<br>

<h3>4. Feitas as instalações precisamos criar nosso arquivo de variáveis de ambiente, o <b>.env</b>, no diretório raiz:</h3>

```
touch .env
```

Dentro dele precisamos definir nossas variáveis de ambiente tendo como base o arquivo <b>.env.example</b>:

```
DJANGO_SECRET_KEY=secret_key

EMAIL_HOST_USER=user_mail
EMAIL_HOST_PASSWORD=password

POSTGRES_DB=database
POSTGRES_HOST=host
POSTGRES_PASSWORD=password
POSTGRES_USER=user
```

<b>Obs:</b> as informações contidas no arquivo <b>.env</b> não devem ser compartilhadas. O arquivo já consta no <b>.gitignore</b> para não constar no repositório.

<h3>4. E executá-la:</h3>

LINUX:
```
python manage.py runserver
```
ou
```
./manage.py runserver
```

WINDOWS:
```
py manage.py runserver
```

<br>

## Documentação

Para ter acesso às descrições, detalhes das rotas e seus retornos, conferir documentação completa neste [link](https://insomnia-documentation-mauve.vercel.app/).

<br>

## Referências

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
- [PostgreSQL](https://www.postgresql.org/)
