# Tienda-online
proyecto en django sobre una tienda virtual

instalacion:
1) Clonar o descargar el proyecto
2) crear un entorno virtual:
  "python -m venv nombredelentorno"
3) Copiar el proyecto dentro del entorno y activarlo (situados en la carpeta base ejecutar el comando):
    ".\Scripts\activate"
4) Ubicarse dentro de la carpeta que contiene el archivo "requirement.txt", ejecutar el comando: "pip install -r requirement.txt"
5) Dentro del directorio 'dnmshoes' realizar las migraciones:
  python manage.py migrate,
  python manage.py makemigrations secciones
  python manage.py migrate
6) Ejecutar el servidor de prueba
  python manage.py runserver
