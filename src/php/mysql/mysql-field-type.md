---
title: mysql_field_type
description: Obtiene el tipo del campo especificado de un resultado
source_url: https://www.php.net/manual/es/function.mysql-field-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-field-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52260
---

mysql_field_type

Obtiene el tipo del campo especificado de un resultado

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
> \[type\]
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
> \[driver:decl_type\] o \[pdo_type\]
>
> </div>

## Descripción

```php
mysql_field_type(resource $result, int $field_offset): string
```php

`mysql_field_type` es similar a la función `mysql_field_name`. Los argumentos son idénticos, pero se devuelve en su lugar el tipo de campo.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

`field_offset`  
La posición numérica del campo. `field_offset` comienza en `0`. Si `field_offset` no existe, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

El tipo de campo devuelto será uno de los siguientes: `"int"`, `"real"`, `"string"`, `"blob"`, y otros tal como se detalla en [la documentación de MySQL](http://dev.mysql.com/doc/).

## Ejemplos

Ejemplo de `mysql_field_type`

```
<?php
mysql_connect("localhost", "nombre_usuario_mysql", "cotraseña_mysql");
mysql_select_db("mysql");
$resultado = mysql_query("SELECT * FROM func");
$campos    = mysql_num_fields($resultado);
$filas     = mysql_num_rows($resultado);
$tabla     = mysql_field_table($resultado, 0);
echo "Su tabla '" . $tabla . "' tiene " . $campos . " campos y " . $filas . " registro/s\n";
echo "La tabla tiene los siguientes campos:\n";
for ($i=0; $i < $campos; $i++) {
    $tipo     = mysql_field_type($resultado, $i);
    $nombre   = mysql_field_name($resultado, $i);
    $longitud = mysql_field_len($resultado, $i);
    $banderas = mysql_field_flags($resultado, $i);
    echo $tipo . " " . $nombre . " " . $longitud . " " . $banderas . "\n";
}
mysql_free_result($resultado);
mysql_close();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Su tabla 'func' tiene 4 campos y 1 registro/s
    La tabla tiene los siguientes campos:
    string name 64 not_null primary_key binary
    int ret 1 not_null
    string dl 128 not_null
    string type 9 not_null enum

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_fieldtype`

## Véase también

mysql_field_name

mysql_field_len
