---
title: mysql_tablename
description: Obtiene el nombre de la tabla de un campo
source_url: https://www.php.net/manual/es/function.mysql-tablename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-tablename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52480
---

mysql_tablename

Obtiene el nombre de la tabla de un campo

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> Consulta SQL:
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> SHOW TABLES
>
> </div>

## Descripción

```php
mysql_tablename(resource $result, int $i): string
```php

Recupera el nombre de tabla desde un resultado dado por `result`.

Esta función está obsoleta. Es preferible usar `mysql_query` para ejecutar una consulta SQL `SHOW TABLES [FROM nombre_bd] [LIKE 'patrón']` en su lugar.

## Parámetros

`result`  
Un `resource` de puntero de resultados que se devuelve desde `mysql_list_tables`.

`i`  
El índice de tipo integer (número de fila/tabla)

## Valores devueltos

El nombre de la tabla en caso de éxito o `false` si ocurre un error.

Use la función `mysql_tablename` para atravesar este puntero de resultados, o cualquier función para obtener tablas, tal como `mysql_fetch_array`.

## Ejemplos

Ejemplo de `mysql_tablename`

```
<?php
mysql_connect("localhost", "usuario_mysql", "contraseña_mysql");
$resultado = mysql_list_tables("mibd");
$número_filas = mysql_num_rows($resultado);
for ($i = 0; $i < $número_filas; $i++) {
    echo "Tabla: ", mysql_tablename($resultado, $i), "\n";
}

mysql_free_result($resultado);
?>

   
```php

## Notas

> [!NOTE]
> La función `mysql_num_rows` puede ser usada para determinar el número de tablas del puntero de resultados.

## Véase también

mysql_list_tables

mysql_field_table

mysql_db_name
