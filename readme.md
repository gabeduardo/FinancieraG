# Prueba técnica Gabriel

1.  Clonar el repositorio
2.  Posicionarse en la carpeta raiz del proyecto por `cd .\FinancieraG\ `
3.  Ejecutar el comando `docker-compose up`
4.  En el docker compose se encuentran listados dos servicios que deberian inicializarse despues de ejecutar el comando `docker-compose up `estos servicios son `web` y `database` , verificar que estan conrriendo con el comando `docker-compose ps`
5.  Ejecutar el comando `docker-compose exec -i -t web bash` para poder ejecutar las migraciones de la basede datos dentro del contenedor del servidor web, esto abrira una consola
6.  Ejecutar el comando `python manage.py migrate`
7.  Crear un super usuario para poder ingresar en el admin de django si se desea con `python manage.py createsuper user `
8.  realizar un `docker-compose down` y luego `docker-compose up` para inicializar el servidor nuevamente
9.  Ingresar al navegador ` [localhost:8000](http://localhost:8000/)`
