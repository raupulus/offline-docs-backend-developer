---
title: Problemas con bases de datos
source_url: https://www.php.net/manual/es/faq.databases.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: faq/databases.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: faq
translation_status: ready
translation_reviewed: false
translation_revision: b8e1b1357
order: 1440
---

## Problemas con bases de datos

Esta sección contiene preguntas comunes sobre la relación entre PHP y bases de datos. Sí, PHP puede acceder a prácticamente cualquier base de datos disponible hoy en día.

**Q:** He escuchado que es posible acceder a Microsoft SQL Server desde PHP. ¿Cómo?

**A:** En máquinas Unix se puede usar [PDO_ODBC](#ref.pdo-odbc) o la [API ODBC Unificada](#book.uodbc).

En máquinas Windows se puede usar [PDO_SQLSRV](#ref.pdo-sqlsrv) o [SQLSRV](#book.sqlsrv).

Consulte también la respuesta de la siguiente pregunta.

**Q:** ¿Puedo acceder a bases de datos Microsoft Access?

**A:** Si está corriendo PHP en una máquina Unix y desea comunicarse con MS Access en Windows, necesitará controladores ODBC para Unix. [OpenLink Software](http://www.openlinksw.com/) tiene controladores ODBC basados en Unix que tienen esa capacidad.

Otra alternativa consiste en usar un servidor SQL que tenga controladores ODBC Windows y usarlo para almacenar los datos, a los cuales puede acceder desde Microsoft Access (usando ODBC) y PHP (usando los controladores incorporados), o usar un formato de archivo intermedio que Access y PHP entiendan, como archivos planos o bases de datos dBase. Sobre este punto, Tim Hayes de OpenLink Software escribe:

> Usar otra base de datos como intermediario no es una buena idea, cuando es posible usar ODBC desde PHP directamente a su base de datos, es decir, con los controladores de OpenLink. Si realmente necesita usar un formato de archivo intermedio, OpenLink ha lanzado ahora Virtuoso (un motor de bases de datos virtual) para NT, Linux y otras plataformas Unix. Por favor visite nuestro [sitio web](http://www.openlinksw.com/) para una descarga gratuita.

Una opción que ha sido probada con éxito es usar MySQL y sus controladores MyODBC en Windows y sincronizar las bases de datos. Steve Lawrence escribe:

- Instale MySQL en su plataforma de acuerdo a las instrucciones de MySQL. La última versión disponible se encuentra en <http://www.mysql.com/>. No se requiere ninguna configuración especial, exceptuando al momento de configurar una base de datos, y al configurar la cuenta de usuario, debe poner % en el campo de host, o el nombre del host del equipo Windows desde el que desea acceder a MySQL. Anote su nombre de servidor, nombre de usuario y contraseña.

- Descargue el controlador MyODBC para Windows desde el sitio de MySQL. Instálelo en su equipo Windows. Es posible probar su operación con las utilidades incluidas con este programa.

- Cree un usuario o dsn de sistema en su administrador de ODBC, ubicado en el panel de control. Cree un nombre dsn, ingrese su nombre de host, nombre de usuario, contraseña, puerto, etc. para su base de datos MySQL configurada en el paso 1.

- Instale Access usando la instalación completa, esto asegura que tenga las elementos adicionales apropiados... por lo menos requerirá el soporte ODBC y el gestor de tablas enlazadas.

- ¡Ahora la parte divertida! Cree una nueva base de datos Access. En la ventana de tabla use el clic derecho y seleccione Enlazar Tablas, o bajo la opción del menú de archivo, seleccione Obtener Datos Externos y luego Enlazar Tablas. Cuando el cuadro de navegación de archivos aparezca, seleccione archivos de tipo: ODBC. Seleccione dsn de Sistema y el nombre de su dsn creado en el paso 3. Seleccione la tabla a enlazar, presione Aceptar, y ¡listo! ¡Ahora es posible abrir la tabla y agregar/eliminar/editar datos en su servidor MySQL! También es posible construir consultas, importar/exportar tablas a MySQL, construir formularios y reportes, etc.

Consejos y Trucos:

- Es posible construir sus tablas en Access y exportarlas a MySQL, y luego enlazarlas de vuelta. Esto facilita la rápida creación de tablas.

- Cuando se crean tablas en Access, es necesario tener una clave primaria definida para tener acceso de escritura a la tabla en Access. Asegúrese de crear una clave primaria en MySQL antes de enlazar en Access.

- Si modifica una tabla en MySQL, es necesario re-enlazarla en Access. Diríjase a Herramientas\>Adiciones\>Gestor de Tablas Enlazadas, vaya a su DSN ODBC, y seleccione la tabla a re-enlazar desde allí. También es posible transladar su fuente dsn allí, simplemente active el cuadro de verificación "siempre preguntar por una ubicación nueva" antes de presionar Aceptar.
