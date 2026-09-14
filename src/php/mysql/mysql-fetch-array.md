---
title: mysql_fetch_array
description: Recupera una fila de resultados como un array asociativo, un array numérico
  o como ambos
source_url: https://www.php.net/manual/es/function.mysql-fetch-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-fetch-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52150
---

mysql_fetch_array

Recupera una fila de resultados como un array asociativo, un array numérico o como ambos

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_fetch_array
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDOStatement::fetch
>
> </div>

## Descripción

```php
mysql_fetch_array(resource $result, [int $result_type]): array
```php

Devuelve un array que corresponde a la fila recuperada y mueve el puntero de datos interno hacia delante.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

`result_type`  
El tipo de array que va a ser devuelto. Es una constante y puede tomar los siguientes valores: `MYSQL_ASSOC`, `MYSQL_NUM`, y `MYSQL_BOTH`.

## Valores devueltos

Devuelve un array de cadenas que corresponde a la fila recuperada, o `false` si no hay más filas. El tipo del array retornado depende de como esté definido `result_type`. Al utilizar `MYSQL_BOTH` (predeterminado), se obtendrá un array con ambos índices: asociativos y numéricos. Al utilizar `MYSQL_ASSOC`, se obtienen solo los índices asociativos (tal como funciona `mysql_fetch_assoc`). Al utilizar `MYSQL_NUM`, se obtienen solo los índices numéricos (tal como funciona `mysql_fetch_row`).

Si dos o más columnas del resultado tienen el mismo nombre de campo, la última columna tomará precedencia. Para acceder a la/s otra/s columna/s con el mismo nombre, se deberá usar el índice numérico de la columna o crear un alias para la columna. Para las columnas con alias, no se puede acceder al contenido con el nombre de la columna original.

## Ejemplos

Consulta con nombres de campos duplicados con alias

```
SELECT tabla1.campo AS foo, tabla2.campo AS bar FROM tabla1, tabla2

   
```php

`mysql_fetch_array` con `MYSQL_NUM`

```
<?php
mysql_connect("localhost", "usuario_mysql", "contraseña_mysql") or
    die("No se pudo conectar: " . mysql_error());
mysql_select_db("mibd");

$resultado = mysql_query("SELECT id, nombre FROM mitabla");

while ($fila = mysql_fetch_array($resultado, MYSQL_NUM)) {
    printf("ID: %s  Nombre: %s", $fila[0], $fila[1]);
}

mysql_free_result($resultado);
?>

   
```php

`mysql_fetch_array` con `MYSQL_ASSOC`

```
<?php
mysql_connect("localhost", "usuario_mysql", "contraseña_mysql") or
    die("No se pudo conectar: " . mysql_error());
mysql_select_db("mibd");

$resultado = mysql_query("SELECT id, nombre FROM mitabla");

while ($fila = mysql_fetch_array($resultado, MYSQL_ASSOC)) {
    printf("ID: %s  Nombre: %s", $fila["id"], $fila["nombre"]);
}

mysql_free_result($resultado);
?>

   
```php

`mysql_fetch_array` con `MYSQL_BOTH`

```
<?php
mysql_connect("localhost", "usuario_mysql", "contraseña_mysql") or
    die("No se pudo conectar: " . mysql_error());
mysql_select_db("mibd");

$resultado = mysql_query("SELECT id, nombre FROM mitabla");

while ($fila = mysql_fetch_array($resultado, MYSQL_BOTH)) {
    printf ("ID: %s  Nombre: %s", $fila[0], $fila["nombre"]);
}

mysql_free_result($resultado);
?>

   
```php

## Notas

> [!NOTE]
> Una cosa importante a tener en cuenta es que el uso de `mysql_fetch_array` *no es significativamente* más lento que el uso de `mysql_fetch_row`, aunque provee un valor añadido considerable.

> [!NOTE]
> Los nombres de los campos devueltos por esta función son *sensibles a la case*.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Véase también

mysql_fetch_row

mysql_fetch_assoc

mysql_data_seek

mysql_query
