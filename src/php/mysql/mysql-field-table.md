---
title: mysql_field_table
description: Obtiene el nombre de la tabla en la que está el campo especificado
source_url: https://www.php.net/manual/es/function.mysql-field-table.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-field-table.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52250
---

mysql_field_table

Obtiene el nombre de la tabla en la que está el campo especificado

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
> \[table\] o \[orgtable\]
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
> \[table\]
>
> </div>

## Descripción

```php
mysql_field_table(resource $result, int $field_offset): string
```php

Devuelve el nombre de la tabla en la que está el campo especificado.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

`field_offset`  
La posición numérica del campo. `field_offset` comienza en `0`. Si `field_offset` no existe, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

El nombre de la tabla en caso de éxito.

## Ejemplos

Un ejemplo de `mysql_field_table`

```
<?php

$consulta = "SELECT account.*, country.* FROM account, country WHERE country.name = 'Portugal' AND account.country_id = country.id";

// obtener el resultado desde la BD
$resultado = mysql_query($consulta);

// Lista el nombre de la tabla y luego el nombre del campo
for ($i = 0; $i < mysql_num_fields($resultado); ++$i) {
    $tabla = mysql_field_table($resultado, $i);
    $campo = mysql_field_name($resultado, $i);

    echo  "$tabla: $campo\n";
}

?>

   
```php

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_fieldtable`

## Véase también

mysql_list_tables
