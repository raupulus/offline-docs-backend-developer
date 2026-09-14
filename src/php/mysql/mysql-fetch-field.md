---
title: mysql_fetch_field
description: Obtiene la información de una columna de un resultado y la devuelve como
  un objeto
source_url: https://www.php.net/manual/es/function.mysql-fetch-field.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-fetch-field.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52170
---

mysql_fetch_field

Obtiene la información de una columna de un resultado y la devuelve como un objeto

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_fetch_field
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
mysql_fetch_field(resource $result, [int $field_offset]): object
```php

Devuelve un objeto que contiene la información de los campos. Esta función puede ser usada para obtener información sobre campos en el resultado de la consulta proporcionada.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

`field_offset`  
El índice numérico del campo. Si el índice del campo no se especifica, se recuperará el siguiente campo que aún no haya recuperado esta función. Los índices de `field_offset` comienzan en `0`.

## Valores devueltos

Devuelve un `object` que contiene la información del campo. Las propiedades del objeto son:

- name - nombre de la columna

- table - nombre de la tabla a la que pertenece la columna, el cual es el sobrenombre si alguno está definido

- max_length - longitud máxima de la columna

- not_null - 1 si la columna no puede ser `null`

- primary_key - 1 si la columna es una clave primaria

- unique_key - 1 si la columna es una clave única

- multiple_key - 1 si la colmuna es una clave no única

- numeric - 1 si la columna es numérica

- blob - 1 si la columna es un BLOB

- type - el tipo de la columna

- unsigned - 1 si la columna es sin signo

- zerofill - 1 si la columna es rellena de ceros

## Ejemplos

Ejemplo de `mysql_fetch_field`

```
<?php
$conexión = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
if (!$conexión) {
    die('No se pudo conectar: ' . mysql_error());
}
mysql_select_db('basedatos');
$resultado = mysql_query('select * from table');
if (!$resultado) {
    die('Falló la consulta: ' . mysql_error());
}
/* obtener los metadatos de la columna */
$i = 0;
while ($i < mysql_num_fields($resultado)) {
    echo "Información de la columna $i:<br />\n";
    $metadatos = mysql_fetch_field($resultado, $i);
    if (!$metadatos) {
        echo "No hay información disponible<br />\n";
    }
    echo "<pre>
blob:         $metadatos->blob
max_length:   $metadatos->max_length
multiple_key: $metadatos->multiple_key
name:         $metadatos->name
not_null:     $metadatos->not_null
numeric:      $metadatos->numeric
primary_key:  $metadatos->primary_key
table:        $metadatos->table
type:         $metadatos->type
unique_key:   $metadatos->unique_key
unsigned:     $metadatos->unsigned
zerofill:     $metadatos->zerofill
</pre>";
    $i++;
}
mysql_free_result($resultado);
?>

   
```php

## Notas

> [!NOTE]
> Los nombres de los campos devueltos por esta función son *sensibles a la case*.

> [!NOTE]
> Si se usa un alias para los campos o los nombres de tablas en la consulta SQL se devolverá el nombre del alias. El nombre original se puede recuperar, por ejemplo, usando mysqli_result::fetch_field.

## Véase también

mysql_field_seek
