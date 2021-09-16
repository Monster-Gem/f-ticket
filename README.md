# Flying Tickets

It's recommended that you create a virtual environment. After that, to install the required packages, run:

```shell
pip install -r requirements.txt
```

Create a `.env` file on the root directory for this project, containing:

```
DATABASE_NAME={database_name}
DATABASE_HOST={database_host}
DATABASE_PORT={database_port}
```

Run the project with: 

```shell
cd src
flask run
```