---
title: mysql_get_host_info
description: Obtener información del anfitrión de MySQL
source_url: https://www.php.net/manual/es/function.mysql-get-host-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-get-host-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52290
---

mysql_get_host_info

Obtener información del anfitrión de MySQL

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_get_host_info
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::getAttribute
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> con
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> attribute
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> como
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::ATTR_CONNECTION_STATUS
>
> </div>

## Descripción

```php
mysql_get_host_info([resource $link_identifier]): string
```php

Describe el tipo de conexión en uso, incluyendo el nombre del servidor anfitrión.

## Parámetros

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Devuelve un string que describe el tipo de conexión MySQL en uso, o o `false` si ocurre un error.

## Ejemplos

Ejemplo de `mysql_get_host_info`

```
<?php
$enlace = mysql_connect("localhost", "usuario_mysql", "contraseña_mysql");
if (!$enlace) {
    die("No pudo conectarse: " . mysql_error());
}
printf("Información del anfitrión de MySQL: %s\n", mysql_get_host_info());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Información del anfitrión de MySQL: Localhost via UNIX socket

## Véase también

mysql_get_client_info

mysql_get_proto_info

mysql_get_server_info
