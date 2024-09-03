

Este es mi proyecto final para el curso de programación. Se trata de un blog creado con Django, donde los usuarios pueden registrarse, crear posts, editarlos, eliminarlos y, en general, gestionar sus publicaciones. Además, los administradores tienen un panel especial donde pueden gestionar usuarios y posts de manera más avanzada.

Características principales
Autenticación de usuarios: Los usuarios pueden registrarse, iniciar sesión, editar su perfil y cambiar su contraseña. Los administradores tienen la capacidad de otorgar permisos especiales.
Publicación de posts: Los usuarios autenticados pueden crear, editar y eliminar sus propios posts. Los administradores pueden gestionar los posts de todos los usuarios.
Perfil de usuario: Cada usuario tiene un perfil donde puede ver sus datos y editar su información personal, incluyendo la imagen de avatar.
Panel de administración: Los usuarios con permisos is_staff tienen acceso a un panel donde pueden ver un resumen de la actividad del sitio, editar y eliminar posts, y gestionar usuarios.

Instalación
1. Clona el repositorio en tu máquina local:
   git clone https://github.com/tu_usuario/tu_repositorio.git
2. Navega al directorio del proyecto:
   cd tu_repositorio
3. Instala las dependencias:
   pip install -r requirements.txt
4. Realiza las migraciones:
   python manage.py migrate
5. Crea un superusuario para acceder al panel de administración
   python manage.py createsuperuser
6. Ejecuta el servidor de desarrollo:
   python manage.py runserver
7. Accede a la aplicacion:
   Abre tu navegador y ve a http://127.0.0.1:8000/

Uso
Página de inicio: Aquí se muestran los posts más recientes. Los usuarios no autenticados pueden leer los posts, pero necesitan iniciar sesión para ver detalles y crear posts propios.
Panel de usuario: Después de iniciar sesión, los usuarios pueden acceder a su panel, donde ven sus posts y pueden gestionar su perfil.
Panel de administración: Los administradores tienen un panel extra para gestionar usuarios y posts.
Estructura del proyecto
- base/: Contiene las vistas y templates para la funcionalidad principal del blog.
- users/: Maneja todo lo relacionado con la autenticación y gestión de usuarios.
- finalpetri/: es la base del proyecto con las configuraciones.
- media/: es donde se van a guardar las imagenes que usemos para posteos y avatares.
- static/: Archivos estáticos como CSS y JS.

video demostracion de funcionalidad: https://www.loom.com/share/7c1ccd2fabe04a43869bf0a190eb58e8?sid=7b6891c9-8656-4f90-ada2-146886fb22a4

Eso es todo, se que es muy basico pero fue todo un desafio para mi. espero que les guste y que cumpla con todos los requisitos!
Autor: Facundo Petringa
