# Taller de Django!

En este taller, creamos nuestro propio blog en Django. Para ver más sobre el evento: http://devconchile.org/

## Configuración

Con python y virtualenv instalados, crea tu entorno:

    $ virtualenv venv
    $ source venv/bin/activate
    (venv) $

Ahora, instalemos los requirements del proyecto:

    (venv) $ pip install -r requirements.txt

## Migrations

Corramos las migrations:

    (venv) $ ./manage.py migrate

## Development Server

    (venv) $ ./manage.yp runserver 8000

Listo! Ahi podrás abrir http://localhost:8000/ para ver nuestro blog!
