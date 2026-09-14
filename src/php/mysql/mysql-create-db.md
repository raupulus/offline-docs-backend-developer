---
title: mysql_create_db
description: Crea una base de datos MySQL
source_url: https://www.php.net/manual/es/function.mysql-create-db.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-create-db.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52070
---

mysql_create_db

Crea una base de datos MySQL

> [!WARNING]
> Esta función estaba obsoleta en PHP 4.3.0, y toda la [extensión original MySQL](#book.mysql) fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_query
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::query
>
> </div>

## Descripción

```php
mysql_create_db(string $database_name, [resource $link_identifier]): bool
```php

`mysql_create_db` intenta crear una nueva base de datos en el servidor asociado con el identificador de enlace especificado.

## Parámetros

`database_name`  
El nombre de la base de datos a crear.

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo alternativo de `mysql_create_db`

La función `mysql_create_db` está obsoleta. Es preferible el uso de `mysql_query` para emitir una sentencia `CREATE DATABASE` de sql en su lugar.

```
<?php
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
if (!$enlace) {
    die('No pudo conectarse: ' . mysql_error());
}

$sql = 'CREATE DATABASE mi_bd';
if (mysql_query($sql, $enlace)) {
    echo "La base de datos mi_bd se creó correctamente\n";
} else {
    echo 'Error al crear la base de datos: ' . mysql_error() . "\n";
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    La base de datos mi_bd se creó correctamente

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_createdb`

> [!NOTE]
> Ésta función no estará disponible si la extensión MySQL fue construida con una biblioteca cliente MySQL 4.x.

## Véase también

mysql_query

mysql_select_db
