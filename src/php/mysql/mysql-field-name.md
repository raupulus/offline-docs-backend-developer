---
title: mysql_field_name
description: Obtiene el nombre del campo especificado de un resultado
source_url: https://www.php.net/manual/es/function.mysql-field-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-field-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52230
---

mysql_field_name

Obtiene el nombre del campo especificado de un resultado

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
> \[name\] o \[orgname\]
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
> \[name\]
>
> </div>

## Descripción

```php
mysql_field_name(resource $result, int $field_offset): string
```php

`mysql_field_name` devuelve el nombre del índice del campo especificado.

## Parámetros

`result`  
El `resource` de resultado que está siendo evaluado. Este resultado proviene de una llamada a `mysql_query`.

`field_offset`  
La posición numérica del campo. `field_offset` comienza en `0`. Si `field_offset` no existe, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

El nombre del índice del campo especificado en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `mysql_field_name`

```
<?php
/* La tabla usuarios consiste de tres campos:
 *   user_id
 *   username
 *   password.
 */
$enlace = mysql_connect('localhost', 'usuario_mysql', 'contraseña_mysql');
if (!$enlace) {
    die('No se pudo conectar al servidor MySQL: ' . mysql_error());
}
$nombre_bd = 'mibd';
$bd_seleccionada = mysql_select_db($nombre_bd, $enlace);
if (!$bd_seleccionada) {
    die("No se pudo establecer $nombre_bd: " . mysql_error());
}
$resultado = mysql_query('select * from usuarios', $enlace);

echo mysql_field_name($resultado, 0) . "\n";
echo mysql_field_name($resultado, 2);
?>

   
```php

El ejemplo anterior mostrará:

    user_id
    password

## Notas

> [!NOTE]
> Los nombres de los campos devueltos por esta función son *sensibles a la case*.

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `mysql_fieldname`

## Véase también

mysql_field_type

mysql_field_len
