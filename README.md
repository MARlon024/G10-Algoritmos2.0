### GRUPO 10 - BANQUITO
**INTEGRANTES:**
-👨 Canecillas Contreras, Juan Mariano
-👨 Castillo Carranza Jose Richard
-👨 Durand Caracuzma, Marlon
-👨 Espinoza Fabian, Josue Marcelo
-👩 Peña Manuyama, Dafna Nicole

#### INSTALACIÓN PARA WINDOWS 

🔖 Desde la terminal instalar los modulos necesarios: *pip install -r requirements.txt *
🔖Para visualizar la base de datos puede usar la extension en Visual Studio Code *SQLite*  o tener instalado *DB Browser for SQLite*

#### INSTALACIÓN PARA LINUX

🔖 Desde la terminal instalar los modulos necesarios: *pip install -r requirements.txt *
🔖 Desde la terminal instalar sqlite3: *sudo apt install sqlite3*
🔖Para visualizar la base de datos puede usar la extension en Visual Studio Code *SQLite*  o tener instalado DB Browser for SQLite desde la terminal: *sudo apt-get install sqlitebrowser*

#### EJECUCIÓN de *Banquito* en la terminal

🔖 Ejecutar el archivo *Bank_new/main.py *
🔖 Loguearse como Recepcionista o Plataforma (credenciales en *banquito.db/personal*)

 ##### PLATAFORMA - FUNCIONALIDADES
	🏷️Registrar nuevo cliente
	🏷️Bloquear tarjeta de débito
	🏷️Cancelar cuenta bancaria
 ##### RECEPCIONISTA - FUNCIONALIDADES
	🏷️Solicitar tarjeta de débito
	🏷️Efectuar transacciones (retiro, deposito, pago de servicios)

🔖 Para los funciones de retiro, deposito o pago de servicios se generara un comprobante. Para visualizarlo dirigirse a la carpeta comprobantes

#### EJECUCIÓN de *Banquito* en el framework *Django* como interfaz para *Banca por internet*

🔖 Dentro de la carpeta *SB2* migrar los archivos con: *python manage.py migrate*
🔖 Dentro de la carpeta *SB2* ejecutar el servidor con: *python manage.py runserver*
🔖 Leer las instruccion presentes en la terminal o dirigirse a la siguiente ruta en su navegador: *127.0.0.1:8000*
🔖 Elegir 

#### FUNCIONALIDADES QUE NO SE IMPLEMENTARON

🔖 Bloquear tarjeta de débito de la carpeta *Bank_new*
🔖 Implementar los archivos de la carpeta *Bank_new* al framework Django en los archivos de la carpeta *SB2* 