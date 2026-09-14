---
title: mysql_field_len
description: Devuelve la longitud del campo especificado
source_url: https://www.php.net/manual/es/function.mysql-field-len.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-field-len.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52220
---

mysql_field_len

Devuelve la longitud del campo especificado

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
> \[length\]
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
> \[len\]
>
> </div>

## Descripción

```php
mysql_field_len(resource $result, int $field_offset): int
```php

`mysql_field_len` devuelve la longitud del campo especificado.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

`field_offset`  
La posición numérica del campo. `field_offset` comienza en `0`. Si `field_offset` no existe, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

La longitud del índice del campo especificado en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `mysql_field_len`

```
<?php
$resultado = mysql_query("SELECT id, email FROM people WHERE id = '42'");
if (!$resultado) {
    echo 'No se pudo ejecutar la consulta: ' . mysql_error();
    exit;
}

// Se obtendrá la longitud del campo id tal como está especificado en el esquema
// de la base de datos.
$longitud = mysql_field_len($resultado, 0);
echo $longitud;
?>

   
```php

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_fieldlen`

## Véase también

mysql_fetch_lengths

strlen
