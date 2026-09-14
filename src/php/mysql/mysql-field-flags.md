---
title: mysql_field_flags
description: Obtiene las banderas asociadas al campo especificado de un resultado
source_url: https://www.php.net/manual/es/function.mysql-field-flags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-field-flags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52210
---

mysql_field_flags

Obtiene las banderas asociadas al campo especificado de un resultado

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_fetch_field_direct
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> \[flags\]
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDOStatement::getColumnMeta
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> \[flags\]
>
> </div>

## Descripción

```php
mysql_field_flags(resource $result, int $field_offset): string
```php

`mysql_field_flags` devuelve las banderas del campo especificado. Las banderas son reportadas como una sola palabra por bandera, separada por un solo espacio, por lo que se puede dividir el valor devuelto usando `explode`.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

`field_offset`  
La posición numérica del campo. `field_offset` comienza en `0`. Si `field_offset` no existe, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Devuelve un string de banderas asociadas con el resultado o `false` si ocurre un error.

Las siguientes banderas son reportadas si la versión de MySQL es suficientemente actual para soportarlas: `"not_null"`, `"primary_key"`, `"unique_key"`, `"multiple_key"`, `"blob"`, `"unsigned"`, `"zerofill"`, `"binary"`, `"enum"`, `"auto_increment"` y `"timestamp"`.

## Ejemplos

Un ejemplo de `mysql_field_flags`

```
<?php
$resultado = mysql_query("SELECT id, email FROM people WHERE id = '42'");
if (!$resultado) {
    echo 'No se pudo ejecutar la consulta: ' . mysql_error();
    exit;
}
$banderas = mysql_field_flags($resultado, 0);

echo $banderas;
print_r(explode(' ', $banderas));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    not_null primary_key auto_increment
    Array
    (
        [0] => not_null
        [1] => primary_key
        [2] => auto_increment
    )

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_fieldflags`

## Véase también

mysql_field_type

mysql_field_len
