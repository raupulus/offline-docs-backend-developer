---
title: mysql_num_rows
description: Obtener el número de filas de un conjunto de resultados
source_url: https://www.php.net/manual/es/function.mysql-num-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-num-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52390
---

mysql_num_rows

Obtener el número de filas de un conjunto de resultados

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_num_rows
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_stmt_num_rows
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDOStatement::rowCount
>
> </div>

## Descripción

```php
mysql_num_rows(resource $result): int
```php

Recupera el número de filas de un conjunto de resultados. Este comando es únicamente válido para sentencias como SELECT o SHOW que retornan un conjunto de resultados real. Para recuperar el número de filas afectadas por una consulta INSERT, UPDATE, REPLACE o DELETE, use `mysql_affected_rows`.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

## Valores devueltos

El número de filas de un conjunto de resultados en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `mysql_num_rows`

```
<?php

$enlace = mysql_connect("localhost", "usuario_mysql", "contraseña_mysql");
mysql_select_db("basedatos", $enlace);

$resultado = mysql_query("SELECT * FROM tabla1", $enlace);
$número_filas = mysql_num_rows($resultado);

echo "$número_filas Filas\n";

?>

   
```php

## Notas

> [!NOTE]
> Si se utiliza `mysql_unbuffered_query`, `mysql_num_rows` no retornará el valor correcto hasta que se hayan recuperado todas las filas del conjunto de resultados.

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_numrows`

## Véase también

mysql_affected_rows

mysql_connect

mysql_data_seek

mysql_select_db

mysql_query
