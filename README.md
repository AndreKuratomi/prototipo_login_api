# prototipo_login_api

- [Translations](#translations)
- [About](#about)
- [Links](#links)
- [Instalation](#instalation)
- [Documentation](#documentation)
- [References](#references)

<br>

## Translations

- [Português brasileiro](./.multilingual_readmes/README_pt-br.md)
- [English / Inglês](https://github.com/AndreKuratomi/PrototipoLogin/)

<br>

## About

<b>prototipo_login_api</b> is the <b>PrototipoLogin</b>'s API.

This API uses the language <strong>[Python](https://www.python.org/downloads/)</strong>, its framework <strong>[Django](https://www.djangoproject.com/)</strong>, its lib <strong>[DjangoMail](https://docs.djangoproject.com/en/4.1/topics/email/)</strong>, the database <strong>[PostgreSQL](https://www.postgresql.org/)</strong>, the software <strong>[Docker](https://docs.docker.com/)</strong> and the <strong>[AWS EC2](https://docs.aws.amazon.com/ec2/index.html)</strong> service.

<br>

## Links

AWS S3 [link](http://dev-bi-abkura.com.br.s3-website-us-east-1.amazonaws.com/)

PrototipoLogin's frontend [repository](https://github.com/AndreKuratomi/prototipo_login_api)

<br>

## Instalation:

<h3>0. It is first necessary to have instaled the following devices:</h3>

- The code versioning <b>[Git](https://git-scm.com/downloads)</b>,

- The programming language <b>[Python](https://www.python.org/downloads/)</b>,

- The software <b>[Docker](https://docs.docker.com/)</b>,

- The <b>[PostgreSQL](https://www.postgresql.org/)
</b> database,

- A <b>code editor</b>, also known as <b>IDE</b>. For instance, <strong>[Visual Studio Code (VSCode)](https://code.visualstudio.com/)</strong>,

- <p> And versioning your directory to receive the aplication clone:</p>

```
git init
```

<br>
<h3>1. Clone the repository <b>prototipo_login_api</b> by your machine terminal or by the IDE:</h3>

```
git clone https://github.com/AndreKuratomi/prototipo_login_api.git
```

WINDOWS:

Obs: In case of any mistake similar to this one: 

```
unable to access 'https://github.com/AndreKuratomi/prototipo_login_api.git': SSL certificate problem: self-signed certificate in certificate chain
```

Configure git to disable SSL certification:

```
git config --global http.sslVerify "false"
```

<p>Enter the directory:</p>

```
cd prototipo_login_api
```
<br>

<h3>2. After cloning the repository install:</h3>

<h4>Virtual enviroment* and update its dependencies with the following command:</h4>


LINUX:
```
python3 -m venv venv --upgrade-deps
```

WINDOWS:
```
py -m venv venv --upgrade-deps
```

In case an error like this one is returned just follow the command displayed:

```
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.
```

*It is a good practice to work with virtual enviroments because different projects may need different dependencies. A virtual enviroment is only a separated enviroment from the user machine. If not used, the user's machine may have lots of dependencies intalled that may only be used in a single project.

<br>

<h4>Ativate your virtual enviroment with the command:</h4>

LINUX:
```
source/venv/bin/activate
```

WINDOWS:

On Windows operational system it is necessary to configure the Execution Policy at PowerShell:

```
Get-ExecutionPolicy # to check the Execution policy type
Set-ExecutionPolicy RemoteSigned # to change the type of policy if the command above shows 'Restricted'
```
Obs: It may often be necessary to open PowerShell as administrador for that.

```
.\env\Scripts\activate
```

<br>

<h4>Install its dependencies:</h4>

```
pip install -r requirements.txt
```
<br>

WINDOWS:

In case any error similar to the one bellow be returned:

```
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\andre.kuratomi\\OneDrive - Company\\Área de Trabalho\\tables_to_db_mail_for_finances\\tables_to_db_and_mail_finances\\env\\Lib\\site-packages\\jedi\\third_party\\django-stubs\\django-stubs\\contrib\\contenttypes\\management\\commands\\remove_stale_contenttypes.pyi'
HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths
```

Run cmd as adminstrador with the following command:

```
reg.exe add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f
```

<br>

<h3>3. Open the application on your IDE:</h3>

```
code .
```
<br>


<h3>4. Create <b>.env</b> file at the root directory:</h3>

```
touch .env
```

Inside it we need to put our enviroment variables taking as reference the given file <b>.env.example</b>:

```
DJANGO_SECRET_KEY=secret_key

EMAIL_HOST_USER=user_mail
EMAIL_HOST_PASSWORD=password

POSTGRES_DB=database
POSTGRES_HOST=host
POSTGRES_PASSWORD=password
POSTGRES_USER=user
```

<b>Obs:</b> Do not share info from <b>.env</b> file. It is already mentioned in <b>.gitignore</b> for not being pushed to the repo.

<h3>5. And run Django:</h3>

LINUX:
```
python manage.py runserver
```
or
```
./manage.py runserver
```

WINDOWS:
```
py manage.py runserver
```

<br>


## Documentation

For full description of endpoints and its responses check the insomnia documentation on the link bellow (necessary free login account) click [here](https://insomnia-documentation-mauve.vercel.app/).

<br>

## References

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
