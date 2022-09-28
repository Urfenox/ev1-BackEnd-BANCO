# ev1-BackEnd-BANCO


# Banco "Piramide" en Django
Evaluación N°1 Programación Back-End 2022

## Funcionamiento
Primero debe, a traves de linea de comandos, iniciar el servidor.
	- `py manage.py runserver`
Luego diríjase a "http://127.0.0.1:8000/" para visualizar el sitio web.

## Explicación
El proyecto raíz es EV1. La aplicación principal de EV1 es Banco.

Aplicaciones
- Banco es la aplicación principal.

### settings.py
Dentro de [settings.py](https://github.com/Urfenox/ev1-BackEnd-BANCO/blob/master/EVA1/settings.py) se debe declarar la aplicación L34.
```python
	INSTALLED_APPS = [
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'Banco'
	]
```
Declaramos los templates (carpeta `templates`) de Banco en settings.py L56.
```python
TEMPLATES = [
{
	'BACKEND': 'django.template.backends.django.DjangoTemplates',
	'DIRS': [os.path.join(BASE_DIR, 'templates')],
	'APP_DIRS': True,
	'OPTIONS': {
		'context_processors': [
			'django.template.context_processors.debug',
			'django.template.context_processors.request',
			'django.contrib.auth.context_processors.auth',
			'django.contrib.messages.context_processors.messages',
			],
		},
},
]
```
Y finalmente los recursos de static. settings.py L120.
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```
### urls.py
Para que al momento de entrar al sitio web tengamos directamente la página principal, debemos declaras las urls para cargar las vistas.

Importamos las vistas desde nuestra aplicación `Banco`.
```python
from  Banco  import  views  as  app
```
Y luego declaramos las direcciones URLS que queramos habitar con nuestras vistas.
```python
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', app.mostrarHogar),
	path('Galeria', app.mostrarGaleria),
	path('Registro', app.mostrarRegistro),
	path('About', app.mostrarAbout),
	path('Consultas', app.mostrarConsultas)
]
```
(Nota: cuando pones `path('', app.mostrarHogar))` el `''` quiere decir página principal raíz. Cuando pongas la "http://127.0.0.1:8000/", la vista que se mostrara será `app.mostrarHogar`.

### Aplicación Banco
Ahora solo queda crear los templates y direccionar cada URL a su respectiva vista.
Dentro de [views.py](https://github.com/Urfenox/ev1-BackEnd-BANCO/blob/master/Banco/views.py) podemos declarar las vistas a renderizar cuando se llame a una URL.

### Templates
Finalmente, toda esta ok. Solo queda dirigirse a las URLS indicadas.

 - http://127.0.0.1:8000/ (index.html)
 - http://127.0.0.1:8000/Galeria (galeria.html)
 - http://127.0.0.1:8000/Registro (registro.html)
 - http://127.0.0.1:8000/About (about.html)
 - http://127.0.0.1:8000/Consultas (consultas.html)

#### Redirecciones.
### Statics
Los recursos dentro de la carpeta `static` pueden estar como tú desees.
Luego, cuando quieras usar un recurso, solo le pones `/static/<ruta o nombre de recurso>`.
También lo puedes hacer con las llaves `{% load static %}` y `{% static 'my_app/example.jpg' %}`, pero es muy incómodo.
### Rutas
Simplemente, poner `href="Galeria"` te dirigirá a http://127.0.0.1:8000/Galeria.
Para ir a index.html, basta poner `href=""` y eso te dirigirá a http://127.0.0.1:8000/.
Si pones `href="/"` eso recargará la página actual.
