# Prueba técnica Gabriel

1.  Clonar el repositorio
2.  Posicionarse en la carpeta raiz del proyecto por `cd .\FinancieraG\ `
3.  Ejecutar el comando `docker-compose up`
4.  En el docker compose se encuentran listados dos servicios que deberian inicializarse despues de ejecutar el comando `docker-compose up `estos servicios son `web` y `database` , verificar que estan conrriendo con el comando `docker-compose ps`

5.  Ejecutar el comando `docker-compose exec -i -t web bash` para poder ejecutar las migraciones de la basede datos dentro del contenedor del servidor web, esto abrira una consola

![image](https://github.com/user-attachments/assets/be9e803c-d712-4992-96b2-6b251f068d28)  
6. Ejecutar el comando `python manage.py migrate` ![image](https://github.com/user-attachments/assets/398b4af5-948f-4bc7-919b-161893939fea)

7.  Crear un super usuario para poder ingresar en el admin de django si se desea con `python manage.py createsuper user `
8.  realizar un `docker-compose down` y luego `docker-compose up` para inicializar el servidor nuevamente
    ![image](https://github.com/user-attachments/assets/6a1cfabb-2ea6-40d4-aaa1-a1075fbc5fd9)

9.  Ingresar al navegador ` [localhost:8000](http://localhost:8000/)`

![image](https://github.com/user-attachments/assets/55a2d614-e91d-439b-8ccb-25a4b430bac1)
