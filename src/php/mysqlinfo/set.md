---
title: Plugins y drivers MySQL
source_url: https://www.php.net/manual/es/set.mysqlinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqlinfo/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqlinfo
translation_status: ready
translation_reviewed: false
translation_revision: 7cff4d34f
order: 56110
---

## Introducción

Existen varias APIs PHP para acceder a una base de datos MySQL. Los usuarios pueden elegir entre las extensiones [mysqli](#book.mysqli) o [PDO_MySQL](#ref.pdo-mysql).

Esta guía explica la [terminología](#mysqlinfo.terminology) utilizada para describir cada una de ellas, proporciona información sobre [la elección de la API](#mysqlinfo.api.choosing) a utilizar, así como información que ayuda a elegir la [biblioteca MySQL a utilizar](#mysqlinfo.library.choosing) con la API.

## Visión general de la terminología

Esta sección proporciona una introducción a las opciones disponibles al desarrollar una aplicación PHP que debe interactuar con una base de datos MySQL.

**¿Qué es una API?**

Una interfaz de programación de aplicaciones, o API, define las clases, los métodos, las funciones y las variables que su aplicación necesita para realizar las tareas deseadas. En el caso de las aplicaciones PHP que necesitan comunicarse con bases de datos, las APIs necesarias suelen exponerse a través de extensiones PHP.

Las APIs pueden ser procedimentales u orientadas a objetos. Con una API procedimental, se llaman funciones para realizar las tareas, con una API orientada a objetos, se instancian las clases, luego se llaman los métodos en los objetos resultantes. La segunda interfaz es generalmente preferida ya que es más moderna y permite organizar mejor el código fuente.

Al escribir aplicaciones PHP que necesitan conectarse a un servidor MySQL, hay varias opciones de API disponibles. Este documento abordará lo que está disponible, y cómo elegir la mejor solución para su aplicación.

**¿Qué es un conector?**

En la documentación de MySQL, el término *conector* se refiere a la parte del programa que permite a su aplicación conectarse al servidor de base de datos MySQL. MySQL proporciona conectores para muchos lenguajes, incluyendo PHP.

Si su aplicación PHP necesita comunicarse con un servidor de base de datos, debe escribir su código PHP para realizar tareas como conectarse al servidor de base de datos, consultar la base de datos y otras tareas relacionadas con la base de datos. El programa es requerido para proporcionar la API a utilizar por su aplicación PHP, pero también para gestionar la comunicación entre su aplicación y el servidor de base de datos, utilizando bibliotecas intermedias si es necesario. Este programa suele denominarse conector, ya que permite a su aplicación *conectarse* al servidor de base de datos.

**¿Qué es un driver?**

Un driver es una parte de programa cuyo objetivo es comunicarse con un tipo específico de servidor de base de datos. El driver también puede llamar a una biblioteca, como la biblioteca cliente MySQL o el driver nativo MySQL. Estas bibliotecas implementan el protocolo de bajo nivel utilizado para comunicarse con el servidor de base de datos MySQL.

Por ejemplo, la capa de abstracción de base de datos [PHP Data Objects (PDO)](#mysqli.overview.pdo) puede utilizar uno de los drivers específicos de base de datos. Uno de estos drivers disponibles es el driver PDO MYSQL, que proporciona una interfaz con el servidor MySQL.

A veces, las personas utilizan los términos conector y driver de manera intercambiable, lo que puede causar confusión. En la documentación de MySQL, el término “driver” se reserva al programa que proporciona la parte específica de la base de datos de un conector.

**¿Qué es una extensión?**

En la documentación de PHP, se encuentra otro término - *extensión*. El código PHP está compuesto por un núcleo, con extensiones opcionales que permiten extender las funcionalidades del núcleo. Las extensiones PHP relacionadas con bases de datos, como la extensión `mysqli` se implementan utilizando el framework de extensiones PHP.

Típicamente, una extensión expone una API al programador PHP, permitiéndole algunas facilidades durante la programación. Sin embargo, algunas extensiones que utilizan el framework de extensión PHP no exponen ninguna API al programador PHP.

La extensión driver PDO MySQL, por ejemplo, no expone ninguna API al programador PHP, pero proporciona una interfaz a la capa PDO.

Los términos API y extensión no deben considerarse como significando lo mismo, ya que una extensión no expone necesariamente una API al programador.

## Elegir una API

PHP ofrece diferentes APIs para conectarse a MySQL. A continuación, se encuentran las APIs proporcionadas por las extensiones mysqli y PDO. Cada ejemplo de código crea una conexión a un servidor MySQL que se ejecuta en el dominio "example.com", utilizando el nombre de usuario "user", la contraseña "password". Y se ejecuta una consulta para saludar al usuario.

Comparación de las APIs MySQL

```php
<?php
// mysqli
$mysqli = new mysqli("example.com", "user", "password", "database");
$result = $mysqli->query("SELECT '¡Hola, querido usuario de MySQL!' AS _message FROM DUAL");
$row = $result->fetch_assoc();
echo htmlentities($row['_message']);

// PDO
$pdo = new PDO('mysql:host=example.com;dbname=database', 'user', 'password');
$statement = $pdo->query("SELECT '¡Hola, querido usuario de MySQL!' AS _message FROM DUAL");
$row = $statement->fetch(PDO::FETCH_ASSOC);
echo htmlentities($row['_message']);

    
```

**Comparación de funcionalidades**

El rendimiento global de las dos extensiones puede considerarse idéntico. Sin embargo, el rendimiento de la extensión constituye solo una fracción del tiempo total de ejecución de una solicitud web PHP. A menudo, el impacto es inferior al 0.1%.

|  | ext/mysqli | PDO_MySQL |
|----|----|----|
| Introducida en la versión de PHP | 5.0 | 5.1 |
| Incluida con PHP 7.x y 8.x | Sí | Sí |
| Estado de desarrollo | Activo | Activo |
| Ciclo de vida | Activo | Activo |
| Recomendado para nuevos proyectos | Sí | Sí |
| Interfaz orientada a objetos | Sí | Sí |
| Interfaz procedimental | Sí | No |
| La API soporta consultas no bloqueantes, asíncronas con mysqlnd | Sí | No |
| Conexiones persistentes disponibles | Sí | Sí |
| La API soporta juegos de caracteres | Sí | Sí |
| La API soporta consultas preparadas del lado del servidor | Sí | Sí |
| La API soporta consultas preparadas del lado del cliente | No | Sí |
| La API soporta procedimientos almacenados | Sí | Sí |
| La API soporta consultas múltiples | Sí | La mayoría |
| La API soporta transacciones | Sí | Sí |
| Las transacciones pueden controlarse con SQL | Sí | Sí |
| Soporta todas las funcionalidades de MySQL 5.1+ | Sí | La mayoría |

## Elegir una biblioteca

Las extensiones PHP mysqli y PDO_MySQL son envolventes ligeras de una biblioteca cliente C. Las extensiones pueden utilizar la biblioteca [mysqlnd](#book.mysqlnd), o la biblioteca `libmysqlclient`. La elección de la biblioteca se realiza en el momento de la compilación.

La biblioteca mysqlnd forma parte de la distribución de PHP. Ofrece funcionalidades como conexiones perezosas, caché de consultas, que no están disponibles con libmysqlclient, por lo que se recomienda utilizar la biblioteca interna mysqlnd. Ver la [documentación de mysqlnd](#book.mysqlnd) para obtener más información, así como una lista de las funcionalidades que ofrece.

Comando de configuración para el uso de mysqlnd o libmysqlclient

```php
// Recomendado, compilación con mysqlnd
$ ./configure --with-mysqli=mysqlnd --with-pdo-mysql=mysqlnd

// Alternativamente recomendado, compilación con mysqlnd
$ ./configure --with-mysqli --with-pdo-mysql

// No recomendado, compilación con libmysqlclient
$ ./configure --with-mysqli=/path/to/mysql_config --with-pdo-mysql=/path/to/mysql_config

    
```

Comparación de las instrucciones preparadas

```php
<?php
// mysqli
$mysqli = new mysqli("example.com", "usuario", "contraseña", "base de datos");
$statement = $mysqli->prepare("SELECT District FROM City WHERE Name=?");
$statement->execute(["Amersfoort"]);
$result = $statement->get_result();
$row = $result->fetch_assoc();
echo htmlentities($row['District']);

// PDO
$pdo = new PDO('mysql:host=example.com;dbname=base de datos', 'usuario', 'contraseña');
$statement = $pdo->prepare("SELECT District FROM City WHERE Name=?");
$statement->execute(["Amersfoort"]);
$row = $statement->fetch(PDO::FETCH_ASSOC);
echo htmlentities($row['District']);

    
```

**Comparación de funcionalidades de las bibliotecas**

Se recomienda utilizar la biblioteca [mysqlnd](#book.mysqlnd) en lugar de la biblioteca cliente servidor MySQL (libmysqlclient). Ambas bibliotecas son soportadas y mejoradas continuamente.

|  | Driver nativo MySQL ([mysqlnd](#book.mysqlnd)) | Biblioteca cliente servidor MySQL (`libmysqlclient`) |
|----|----|----|
| Forma parte de la distribución de PHP | Sí | No |
| Introducido en versión de PHP | 5.3.0 | N/A |
| Licencia | Licencia PHP 3.01 | Doble licencia |
| Estado de desarrollo | Activo | Activo |
| Ciclo de vida | Sin fin anunciado | Sin fin anunciado |
| Compilado por defecto (para todas las extensiones MySQL) | Sí | No |
| Soporte del protocolo de compresión | Sí | Sí |
| Soporte de SSL | Sí | Sí |
| Soporte de pipes nombrados | Sí | Sí |
| Consultas no bloqueantes, asíncronas | Sí | No |
| Estadísticas de rendimiento | Sí | No |
| LOAD LOCAL INFILE respeta la [directiva open_basedir](#ini.open-basedir) | Sí | No |
| Uso del sistema de gestión de memoria nativo de PHP (es decir, sigue los límites de memoria de PHP) | Sí | No |
| Devuelve las columnas numéricas en forma de double (COM_QUERY) | Sí | No |
| Devuelve las columnas numéricas en forma de string (COM_QUERY) | Sí | Sí |
| API del plugin | Sí | Limitada |
| Reconexión automática | No | Opcional |
