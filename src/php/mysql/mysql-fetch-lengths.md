---
title: mysql_fetch_lengths
description: Obtiene la longitud de cada salida en un resultado
source_url: https://www.php.net/manual/es/function.mysql-fetch-lengths.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-fetch-lengths.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52180
---

mysql_fetch_lengths

Obtiene la longitud de cada salida en un resultado

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_fetch_lengths
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDOStatement::getColumnMeta
>
> </div>

## Descripción

```php
mysql_fetch_lengths(resource $result): array
```php

Devuelve un array que corresponde a las longitudes de cada campo de la última fila recuperada por MySQL.

`mysql_fetch_lengths` almacena las longitudes de cada columna del resultado en la última fila devuelta mediante `mysql_fetch_row`, `mysql_fetch_assoc`, `mysql_fetch_array`, y `mysql_fetch_object` en un array, comenzando desde el índice 0.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

## Valores devueltos

Un `array` de longitudes en caso de éxito o `false` si ocurre un error.

## Ejemplos

Un ejemplo de `mysql_fetch_lengths`

```
<?php
$resultado = mysql_query("SELECT id,email FROM people WHERE id = '42'");
if (!$resultado) {
    echo 'No se pudo ejecutar la consulta: ' . mysql_error();
    exit;
}
$fila       = mysql_fetch_assoc($resultado);
$longitudes = mysql_fetch_lengths($resultado);

print_r($fila);
print_r($longitudes);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [id] => 42
        [email] => user@example.com
    )
    Array
    (
        [0] => 2
        [1] => 16
     )

## Véase también

mysql_field_len

mysql_fetch_row

strlen
