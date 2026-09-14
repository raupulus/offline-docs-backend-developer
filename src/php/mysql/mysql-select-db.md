---
title: mysql_select_db
description: Seleccionar una base de datos MySQL
source_url: https://www.php.net/manual/es/function.mysql-select-db.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-select-db.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52450
---

mysql_select_db

Seleccionar una base de datos MySQL

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_select_db
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::\_\_construct
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> (parte de dsn)
>
> </div>

## Descripción

```php
mysql_select_db(string $database_name, [resource $link_identifier]): bool
```php

Establece la base de datos activa actual en el servidor asociado con el identificador de enlace especificado. Cada llamada posterior a `mysql_query` será ejecutada en la base de datos activa.

## Parámetros

`database_name`  
El nombre de la base de datos que va a ser seleccionada.

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo `mysql_select_db`

```
<?php

$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_myql');
if (!$enlace) {
    die('No se pudo conectar : ' . mysql_error());
}

// Hacer que foo sea la base de datos actual
$bd_seleccionada = mysql_select_db('foo', $enlace);
if (!$bd_seleccionada) {
    die ('No se puede usar foo : ' . mysql_error());
}
?>

   
```php

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_selectdb`

## Véase también

mysql_connect

mysql_pconnect

mysql_query
