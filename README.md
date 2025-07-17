# 🎬 BlogPelículas — Proyecto Django
Este proyecto es parte de la entrega final del curso de Programación en Python de CoderHouse. Se trata de una aplicación estilo blog desarrollada con Django, que permite gestionar películas, directores y críticas, junto con funcionalidades de búsqueda y sistema de usuarios.

## 🧩 ¿Qué se puede hacer?
- Cargar una nueva película  
- Cargar un director  
- Cargar una crítica  
- Buscar películas por su título  
- Ver el listado completo y el detalle de cada película  
- Acceder a la sección “Acerca de mí”  
- Registrarse, iniciar sesión, cerrar sesión y acceder al perfil de usuario

## 🚀 ¿En qué orden se prueba?
1. Cargar directores  
2. Cargar películas vinculadas a esos directores  
3. Agregar críticas para cada película  
4. Utilizar la búsqueda por título  
5. Probar navegación entre vistas y sistema de login

## 🛠️ ¿Cómo se usa?
1. Clonar o descargar el proyecto  
2. Activar el entorno virtual  
3. Instalar dependencias necesarias:  
   pip install django  
   pip install ckeditor  
4. En la terminal, correr:  
   python manage.py makemigrations  
   python manage.py migrate  
   python manage.py runserver  
5. Abrir el navegador y acceder a: http://localhost:8000/

## 📍 Rutas principales
- /crear_director/ → Cargar directores  
- /crear/ → Cargar películas  
- /crear_critica/ → Cargar críticas  
- /buscar_pelicula/ → Buscar películas por nombre  
- /cuentas/registro/ → Crear una cuenta  
- /cuentas/login/ → Iniciar sesión  
- /cuentas/logout/ → Cerrar sesión  
- /cuentas/perfil/ → Ver perfil del usuario  
- /about/ → Ver sección Acerca de mí

## 📂 Estructura relevante
BlogPeliculas/  
├── BlogPeliculas/  
│   └── static/css/style.css  
├── peliculas/  
│   └── templates/peliculas/  
│       ├── base.html  
│       ├── crear_pelicula.html  
│       ├── editar_pelicula.html  
│       ├── borrar_pelicula.html  
│       ├── lista_peliculas.html  
│       ├── detalle_pelicula.html  
│       ├── crear_director.html  
│       ├── crear_critica.html  
│       ├── buscar_pelicula.html  
│       └── about.html  
├── cuentas/  
│   └── templates/cuentas/  
│       ├── registro.html  
│       ├── login.html  
│       └── perfil.html

## 💡 Notas técnicas
- Se utiliza herencia de plantillas con base.html  
- Todos los formularios están protegidos con {% csrf_token %}  
- La búsqueda de películas se realiza usando coincidencia parcial (icontains)  
- Se usa LoginRequiredMixin y @login_required en vistas sensibles  
- Se aplicó un estilo básico a través de CSS en style.css 


Facundo Sosa · CoderHouse · 2025
