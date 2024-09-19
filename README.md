<h1>Descripción</h1>
https://roadmap.sh/projects/blogging-platform-api
Ejemplo de creación de una API rest sencilla con Django y el modulo django rest framework.
El sistema permite agregar nuevos registros, eliminar y/o editar los existentes, listar uno o todos los registros y filtrar
por una cadena de wildchar.

El sistema utiliza la base de datos SQLite3 por defecto que viene integrada en django, esto debido a que para la sencillez
de la implementacion no era necesario gestionar un servidor de db externo.

La aplicación hace uso del módulo django rest framework para demostrar cómo se puede hacer un CRUD de manera sumamente
sencilla, altamente modificable y con pocas líneas de código.

<h1>USO</h1>
Descarga o clona el proyecto en tu equipo local
Ejecuta el servidor de pruebas de django (py manage.py runserver) y navega a la url que te indica la app (usualmente http://localhost:8000) y agregale "/Blog"
esto te llevará a la página de inicio de la app la cual es la de listar los Post existentes.

Apartir de aquí, la api tiene las siguientes urls:
<h2>A través del método GET</h2>
<ul>
  <li><b>/Blog/</b> => Lista todos los registros de la base de datos</li>
  <li><b>/Blog/x</b> => obtiene el registro con el id "x" de la base de datos</li>
  <li><b>/Blog/search/sss</b> => obtiene todos los registros que contengan la cadena "sss" en el título, en el content o en la category</li>
</ul>
<br>
<h2>A través del método POST</h2>
<ul>
  <li><b>/Blog/</b> => Debe contener en el body del request un json con las variables title, content, category y tags (todas strings)
  Retorna un json con los datos del objeto nuevo creado (incluyendo su id)</li>
</ul>
<br>
<h2>A través del método PUT</h2>
<ul>
  <li><b>/Blog/x </b> => Debe contener en el body del request un json con las <b>modificaciones</b> a las variables title, content, category y tags (todas strings)
    que se desean hacer al registro "x"
    Retorna un json con los datos ya actualizados del objeto (incluyendo su id)</li>
</ul>
<br>
<h2>A traves del metodo DELETE</h2>
<ul>
  <li><b>/Blog/x</b> => elimina el registro con el id "x" de la base de datos</li>
</ul>



