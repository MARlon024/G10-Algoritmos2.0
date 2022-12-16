# G10
# Integrantes:

# Espinoza Fabian, Josue Marcelo
# Canecillas Contreras, Juan Mariano
# Castillo Carranza Jose Richard
# Durand Caracuzma, Marlon
# Peña Manuyama, Dafna Nicole

# Repositorio: https://github.com/MARlon024/G10-Algoritmos2.0

# Requerimientos:

# PARA WINDOWS:
# Python 3.10.7
# Base Datos : "DB Browser for SQLite Version 3.12.2"
# Instalar el modulo cryptography en la carpeta scripts de python - pip install cryptography


# PARA LINUX:
# Python 3.10.7
# Instalar sqlite3 - sudo apt install sqlite3
# Visualizar base de datos
# Opcion1 (Visual Studio Code) - Instalar la extension sqlite
# opcion2 - instalar DB Browser for SQLite Version 3.12.2 - sudo apt-get install sqlitebrowser

# Pasos:
# El recepcionista debe loguearse (Consultar tabla recepcionista)
# Una vez logueado
#   Se le mostrará un menú de opciones para que el recepcionista pueda realizar las operaciones correspondientes:
#   El programa empezará a ejecutarse de acuerdo a la opción
#   Se cierra el programa

# DJANGO

# Requerimientos:

# pip install django
# pip install django-bootstrap4
# pip install django-bootstrap-themes

# Pasos:
# Dirigirse a la carpeta SB2
# Migrar el archivo manage: python manage.py migrate
# Luego, correr el servidor: python manage.py runserver
# En la web registrarse e iniciar sesion.
# Luego se dirige automaticamente al index del usuario, en la pantalla se mostrara el numero de cuenta, su saldo, y tipo de cuenta.
# En el parte izquierda en el index del usuario se muestra algunas operaciones que el usuario puede realizar.
# Otras funciones las cuales se han agregado vendrían a ser los siguientes:
# Imprimir el voucher: Cómo se sabe,cuando algún cliente siempre realiza una operación como alguna transacción,se le da un # voucher sobre la operación realizada con sus respectivos detalles.En este caso,lo que hicimos,fue pasar el mensaje # mostrado al formato csv para luego transformarlo a pdf,ya que no se podía hacerlo directamente.Además,una vez ya creado # el pdf del voucher,el archivo csv pasaría a eliminarse con el fin de evitar la acumalación de archivos innecesarios y el # consumo de memoria.
# Bloqueo y eliminación de datos en la BBDD: El primero de ellos es bloqueo de tarjeta, el cual sirve en los casos que el # usuario haya perdido su tarjeta o que haya tal vez vencido u otro caso. En la cual, una vez que esta función sea # solicitada,el usuario no podrá realizar alguna operación con su tarjeta,ya que su estado pasaría de “Activo” a # “Bloqueado”. Cabe recalcar que una vez bloqueada una tarjeta,el usuario tendrá que solicitar una nueva. Desafiliar cuenta # es otro de los casos y su principal objetivo vendría a ser eliminar al cliente de la base de datos,ya que el cliente se # ha desafiliado del banco. Por lo tanto, todos sus datos pasarán a retirarse del sistema bancario.

# En el README: instrucciones claras y concisas de cómo ejecutar su proyecto. Indicar que comandó correr para instalar # dependencias de ser necesario. Dichas instrucciones no deben pasar de 4 pasos.
# El personal del banco al entrar a la aplicación, observará dos opciones por lo cual este tendrá que escoger como # recepcionista o plataforma, puesto que cada empleado realiza diferentes funciones. Una vez que el personal haya iniciado # sesión dependiendo el caso, se le mostrará un menú con sus respectivas funciones a realizar.
# Por un lado, el recepcionista tiene como funciones: “Solicitar tarjeta de débito” y “Transferencias''. Al solicitar # tarjeta de débito, se le solicitará al cliente su número de cuenta que se le ha sido otorgado al crear su cuenta y se le # genera su tarjeta. De igual manera en transferencias, se le solicitará al cliente su número de cuenta y luego se le # imprimirá su voucher con sus respectivos detalles de la operación realizada en un PDF que se guardará en la carpeta del # mismo nombre.
# Por otro lado, el personal de plataforma tiene como funciones: “Registrar nuevo cliente” , “Bloqueo de tarjeta de débito” # y "Cancelar cuenta". En registrar un nuevo cliente, se le solicitará al cliente sus datos personales para así poder # registrarlo en la base de datos y generar su número de cuenta también. En bloqueo de tarjeta de débito, se le solicitará # al cliente su número de cuenta que está afiliado a su tarjeta así como la clave de la tarjeta también, una vez ya # introducidos los datos, la tarjeta pasará a bloquearse. Por último en cancelar cuenta, el cliente brindará su número de # cuenta para luego sus datos sean retirados de la base de datos.
# En el apartado de Django en la web debe registrarse e iniciar sesión, luego se redirecciona al index del usuario, en la # pantalla se mostrará el número de cuenta, su saldo, y tipo de cuenta. En la parte izquierda en el index del usuario se # muestran algunas operaciones que el usuario puede realizar transacciones, depósito, retiro, editar datos. Y si quiere # cerrar la sesión se dirige a la barra de arriba.
# Comandos y librerías a descargar:
# pip install pdfkit
# pip install os
# pip install pandas
# wkhtmltopdf.exe para poder transformar un string a pdf
# pip install django
# pip install django-bootstrap4
# pip install django-bootstrap-themes
# Base Datos : "DB Browser for SQLite Version 3.12.2"
# Instalar el módulo cryptography en la carpeta scripts de python - pip install cryptography
# SB2 ES LA CARPETA DE DJANGO, LA CUAL NO PUDO ACOPLARSE :(
