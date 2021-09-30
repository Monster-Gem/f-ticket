# Flying Tickets

## Team

- Gustavo Alves Pacheco (11821ECP011)
- Lucas Resende Carneiro (11811ECP009)

## Running Instructions

Run the project with:

```shell
docker compose up -d
```

## Documentation

### Database Diagram

![](/docs/uml.jpg)

The database used was Mongodb, using flask-mongoengine and mongoengine as communication with flask.

### Routes Documentation

You can import [this file](/docs/insomnia.har) into [Insomnia](https://insomnia.rest) to have all routes listed, along with examples.

### Users

Some endpoints requires the user to be an admin, while others, a normal one. To avoid register directly on the database, we already provided an admin. A normal user is registered using Sign Up.

```
email: eliot@gmail.com
password: qwerty
```

### Scripts

The database already have some data, created using the seeds folder.
