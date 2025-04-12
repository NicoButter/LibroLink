![background_librolink_3](https://github.com/user-attachments/assets/e1e92f9f-7012-48e6-abf7-8b43982ce107)
# 📚 LibroLink

**LibroLink** es un sistema de gestión de bibliotecas desarrollado con Django. Está diseñado para facilitar tanto la **búsqueda de libros** como la **administración de socios**, todo a través de una interfaz web intuitiva, moderna y responsive.

---

## 🔍 Características Principales

- 🔎 **Búsqueda de Libros**: Filtrado por título, autor, ISBN, y más.
- 📚 **Gestión de Libros**: Alta, baja y modificación de libros para administradores.
- 👥 **Gestión de Usuarios**: Autenticación mediante login/logout y sistema de roles.
- 📱 **Diseño Responsivo**: Adaptado para escritorio, tablet y móvil.
- ⏱️ **Interactividad Dinámica**: Actualización en tiempo real de datos como fecha y hora (¡gracias JS!).

---

## 🧰 Tecnologías Utilizadas

- ⚙️ **Backend**: Django
- 🧱 **Base de Datos**: PostgreSQL
- 🎨 **Frontend**: HTML5, CSS3
- 🧠 **Interactividad**: JavaScript vanilla
- 🖥️ **Entorno de Desarrollo**: VSCode sobre openSUSE 💚🐧

---

## 🚀 Instalación y Ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/librolink.git
   ```

2. Crear un entorno virtual e instalar dependencias:
   ```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Configurar la base de datos PostgreSQL según `settings.py`.

4. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

5. Crear un superusuario (para el panel admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Iniciar el servidor:
   ```bash
   python manage.py runserver
   ```

7. Acceder desde tu navegador en:  
   [http://localhost:8000](http://localhost:8000)

---

## 📸 LibroLink

> [background_librolink_3](https://github.com/user-attachments/assets/c0ee833a-dac3-47b1-895b-b35fc5c222a0)
---

## 🤝 Contribuciones

¿Tenés ideas para mejorar LibroLink? ¡Las contribuciones son más que bienvenidas!  
Podés hacer un fork del proyecto, crear una nueva rama, y enviar un pull request.

---

## 📬 Contacto

📌 **Autor**: Nicolás Butterfield  
📧 **Email**: [nicobutter@gmail.com](mailto:nicobutter@gmail.com)

---

## 🧠 Fun Fact

**LibroLink** es tan organizado que si un libro está fuera de su lugar… el sistema lanza una excepción `LibroNoEncontradoException`, y un bibliotecario Jedi aparece mágicamente para devolvértelo al estante correcto. 📖✨🔦

> "Que el `queryset` te acompañe..." 🙏🧘‍♂️

---
