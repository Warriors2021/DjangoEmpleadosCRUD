<h1>API REST de CRUD para una tabla de empleados y departamento con una relación de muchos a uno en Django</h1>
<p>Este proyecto utiliza Django para la creación de una API REST que implementa un CRUD y se puede utilizar como un microservicio. Además, utiliza una implementación de base de datos como PostgreSQL, la cual debe ser configurada antes de configurar este poryecto.</p>

<h2>Clonar este proyecto</h2>

<pre><code>git clone  https://github.com/Warriors2021/DjangoEmpleadosCRUD.git
</code></pre>

<h2>Variables de entorno</h2>
<p>Para configurar la aplicación, es necesario establecer las siguientes variables de entorno:</p>
<ul>
  <li><code>DATABASE_NAME</code>: El nombre de la base de datos que ya se ha creado.</li>
  <li><code>DATABASE_USER</code>: El nombre de usuario, por defecto es <strong>"postgres"</strong>, o el que se ha creado para la base de datos.</li>
  <li><code>DATABASE_PASSWORD</code>: La contraseña del usuario de la base de datos.</li>
  <li><code>DATABASE_HOST</code>: La dirección IP donde se encuentra ejecutándose la base de datos PostgreSQL.</li>
  <li><code>DATABASE_PORT</code>: El puerto por el que la base de datos está escuchando.</li>
</ul>

<h2>Creación de entorno virtual</h2>

<p>De esta forma creamos un entorno virtual:</p>

<pre><code>virtualenv venv
</code></pre>

<h2>requirements.txt</h2>

<p>Estos son los requerimientos que necesitamos:</p>

<pre><code>django==4.1.7
djangorestframework==3.14.0
python-dotenv==1.0.0
psycopg-binary==3.1.8
psycopg2==2.9.5
</code></pre>

<h2>Instalación necesaria para Linux y poder que funcione con la base de datos PostgreSQL</h2>

<p>Configuración basada en Linux Ubuntu:</p>

<pre><code> sudo apt-get update && apt-get install -y gcc libpq-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
</code></pre>

<h2>Instalación de requerimientos en el entorno virtual</h2>

<p>De esta forma instalamos el archivo requirements.txt:</p>

<pre><code>pip install -r requirements.txt
</code></pre>

<h2>Ejecución de migraciones</h2>

<p>En este proyecto solo necesitamos ejecutar las migraciones ya que el makemigrations está por defecto en el proyecto:</p>

<pre><code>python manage.py migrate
</code></pre>


<h2>Ejecución de API REST</h2>
<p>Para ejecutar nuestra API REST y que esté escuchando en http://localhost:8000, podemos usar el siguiente comando:</p>
<pre><code>python manage.py runserver
</code></pre>
<p>Si deseamos modificar el puerto para que se ejecute, por ejemplo, en http://0.0.0.0:1234, podemos usar el siguiente comando:</p>
<pre><code>python manage.py runserver 0.0.0.0:1234
</code></pre>
<h2>Endpoints disponibles</h2>
<ul>
  <li><code>http://localhost:8000/api/departamentos/</code></li>
  <li><code>http://localhost:8000/api/departamentos/int:pk/</code></li>
  <li><code>http://localhost:8000/api/empleados/</code></li>
  <li><code>http://localhost:8000/api/empleados/int:pk/</code></li>
</ul>
<h2>Creación de departamento</h2>
<p>Para crear y gestionar departamentos, se pueden usar los siguientes endpoints:</p>
<ul>
  <li><code>http://localhost:1234/api/departamentos/</code>: En este endpoint se pueden crear y visualizar los departamentos existentes mediante los métodos <strong>GET</strong> y <strong>POST</strong>.</li>
  <li><code>http://localhost:1234/api/departamentos/int:pk/</code>: En este endpoint se pueden actualizar y eliminar departamentos existentes mediante los métodos <strong>UPDATE</strong> y <strong>DELETE</strong>.</li>
</ul>
<h2>Creación de empleados</h2>
<p>Para crear y gestionar empleados, se pueden usar los siguientes endpoints:</p>
<ul>
  <li><code>http://localhost:1234/api/empleados/</code>: En este endpoint se pueden crear y visualizar los empleados existentes y, adicionalmente, asignarles un departamento de los anteriormente creados mediante los métodos <strong>GET</strong> y <strong>POST</strong>.</li>
  <li><code>http://localhost:1234/api/empleados/int:pk/</code>: En este endpoint se pueden actualizar y eliminar empleados existentes y el departamento asignado mediante los métodos <strong>UPDATE</strong> y <strong>DELETE</strong>.</li>
</ul>
<h2>Imagen Docker</h2>
<p>La imagen Docker se encuentra disponible en el siguiente enlace: https://hub.docker.com/r/1121931934/empleadoscrud</p>







