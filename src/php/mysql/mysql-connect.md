---
title: mysql_connect
description: Abre una conexión al servidor MySQL
source_url: https://www.php.net/manual/es/function.mysql-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52060
---

mysql_connect

Abre una conexión al servidor MySQL

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_connect
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::\_\_construct
>
> </div>

## Descripción

```php
mysql_connect([string $server], [string $username], [string $password], [bool $new_link], [int $client_flags]): resource
```php

Abre o reutiliza una conexión a un servidor MySQL.

## Parámetros

`server`  
El servidor MySQL. También se puede incluir un número de puerto. P.ej. "nombre_anfitrión:puerto" o una ruta a un socket local, p.ej. ":/ruta/al/socket" para el servidor local.

Si la directiva PHP [ mysql.default_host](#ini.mysql.default-host) no está definida (por defecto), el valor por defecto es 'localhost:3306'. En [safe mode SQL](#ini.sql.safe-mode), éste parámetro es ignorado y siempre se usa el valor 'localhost:3306'.

`username`  
El nombre de usuario. El valor por defecto está definido por [mysql.default_user](#ini.mysql.default-user). En [safe mode SQL](#ini.sql.safe-mode), éste parámetro es ignorado y se usa el nombre de usuario que posee el proceso del servidor.

`password`  
La contraseña. El valor por defecto está definido por [mysql.default_password](#ini.mysql.default-password). En [safe mode SQL](#ini.sql.safe-mode), éste parámetro es ignorado y se usa la contraseña vacía.

`new_link`  
Si se realiza una segunda llamada a `mysql_connect` con los mismos argumentos, un nuevo enlace no será establecido, pero en su lugar, será devuelto el identificador de enlace del enlace ya abierto. El parámetro `new_link` modifica éste comportamiento y hace que `mysql_connect` siempre abra un nuevo enlace, aun si `mysql_connect` fue llamada antes con los mismos parámetros. En [safe mode SQL](#ini.sql.safe-mode), éste parámetro es ignorado.

`client_flags`  
El parámetro `client_flags` puede ser una combinación de las siguientes constantes: 128 (habilita el manejo de `LOAD DATA LOCAL`), `MYSQL_CLIENT_SSL`, `MYSQL_CLIENT_COMPRESS`, `MYSQL_CLIENT_IGNORE_SPACE` o `MYSQL_CLIENT_INTERACTIVE`. Lea la sección sobre [???](#mysql.client-flags) para más información. En [safe mode SQL](#ini.sql.safe-mode), éste parámetro es ignorado.

## Valores devueltos

Devuelve un identificador de enlace de MySQL en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `mysql_connect`

```
<?php
$enlace =  mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
if (!$enlace) {
    die('No pudo conectarse: ' . mysql_error());
}
echo 'Conectado satisfactoriamente';
mysql_close($enlace);
?>

   
```php

Ejemplo de `mysql_connect` usando la sintaxis `nombre_anfitrión:puerto`

```
<?php
// nos  conectamos a ejemplo.com y al puerto 3307
$enlace = mysql_connect('ejemplo.com:3307',  'usuario_mysql', 'contraseña_mysql');
if  (!$enlace) {
    die('No pudo conectarse: ' . mysql_error());
}
echo 'Conectado satisfactoriamente';
mysql_close($enlace);

// nos conectamos a ejemplo.com y al puerto 3307
$enlace = mysql_connect('127.0.0.1:3307', 'usuario_mysql',  'contraseña_mysql');
if (!$enlace) {
    die('No pudo conectarse: ' . mysql_error());
}
echo 'Conectado satisfactoriamente';
mysql_close($enlace);
?>

   
```php

Ejemplo de `mysql_connect` usando la sintaxis ":/rota/al/socket"

```
<?php
// nos  conectamos a localhost y a la toma ej. /tmp/mysql.sock

// variante 1: omitir el localhost
$enlace = mysql_connect(':/tmp/mysql', 'usuario_mysql',  'contraseña_mysql');
if (!$enlace) {
    die('No pudo conectarse: ' . mysql_error());
}
echo 'Conectado satisfactoriamente';
mysql_close($enlace);

// variante 2: con localhost
$enlace = mysql_connect('localhost:/tmp/mysql.sock',  'usuario_mysql', 'contraseña_mysql');
if  (!$enlace) {
    die('No pudo conectarse: ' . mysql_error());
}
echo 'Conectado  satisfactoriamente';
mysql_close($enlace);
?>

   
```php

## Notas

> [!NOTE]
> Siempre que se especifique "localhost" o "localhost:puerto" como servidor, la biblioteca cliente de MySQL invalidará esto e intentará conectarse a un socket local (llamada tubería en Windows). Si se quiere usar TCP/IP, se ha de utilizar "127.0.0.1" en lugar de "localhost". Si la biblioteca cliente de MySQL intenta conectarse al socket local erróneo, se debería establecer el ruta correcta como [mysql.default_host](#ini.mysql.default-host) en `php.ini` y dejar el campo del servidor en blanco.

> [!NOTE]
> El enlace al servidor se cerrará tan pronto finalice la ejecución del script, a menos que se cierre antes por una llamada explícita a `mysql_close`.

> [!NOTE]
> El error "Can't create TCP/IP socket (10106)" normalmente significa que la directiva de configuración [variables_order](#ini.variables-order) no contiene el carácter `E`. En Windows, si el entorno no es copiadola variable de entorno `SYSTEMROOT` no estará disponible y PHP tendrá problemas al cargar Winsock.

## Véase también

mysql_pconnect

mysql_close
