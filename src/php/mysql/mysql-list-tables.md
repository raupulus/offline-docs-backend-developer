---
title: mysql_list_tables
description: Lista las tablas de una base de datos MySQL
source_url: https://www.php.net/manual/es/function.mysql-list-tables.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-list-tables.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_reviewed: false
translation_revision: 15d88bef8
order: 52370
---

mysql_list_tables

Lista las tablas de una base de datos MySQL

> [!WARNING]
> Esta función estaba obsoleta en PHP 4.3.0, y toda la [extensión original MySQL](#book.mysql) fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> Consulta SQL:
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> SHOW TABLES FROM dbname
>
> </div>

## Descripción

```php
mysql_list_tables(string $database, [resource $link_identifier]): resource
```php

Lista las tablas de una base de datos MySQL especificada.

Esta función está deprecada. Es preferible utilizar la función `mysql_query` para ejecutar la consulta SQL `SHOW TABLES [FROM db_name] [LIKE 'pattern']` en su lugar.

## Parámetros

`database`  
El nombre de la base de datos

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Un puntero de resultados `resource` en caso de éxito o `false` si ocurre un error.

Utilice la función `mysql_tablename` para recorrer este puntero de resultados o cualquier otra función para los resultados de tablas, como la función `mysql_fetch_array`.

## Ejemplos

Ejemplo de alternativa a `mysql_list_tables`

```
<?php
$dbname = 'mysql_dbname';

if (!mysql_connect('mysql_host', 'mysql_user', 'mysql_password')) {
   echo 'No es posible conectarse a MySQL';
   exit;
}

$sql = "SHOW TABLES FROM $dbname";
$result = mysql_query($sql);

if (!$result) {
   echo "Error DB, no es posible listar las tablas\n";
   echo 'Error MySQL : ' . mysql_error();
   exit;
}

while ($row = mysql_fetch_row($result)) {
   echo "Tabla : {$row[0]}\n";
}

mysql_free_result($result);
?>

   
```php

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_listtables`

## Véase también

mysql_list_dbs

mysql_tablename
