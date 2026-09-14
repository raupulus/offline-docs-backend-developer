---
title: oci_error
description: Devuelve el último error de Oracle
source_url: https://www.php.net/manual/es/function.oci-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: ed6de1ae2
order: 57260
---

oci_error

Devuelve el último error de Oracle

## Descripción

```php
oci_error([resource $connection_or_statement]): array
```php

Devuelve el último error de Oracle.

La función debe ser llamada inmediatamente después de que ocurra un error. Los errores son reinicializados después de una consulta exitosa.

## Parámetros

`connection_or_statement`  
Para la mayoría de los errores, el argumento `connection_or_statement` representa un recurso de conexión. Para los errores de conexión con las funciones `oci_connect`, `oci_new_connect` o `oci_pconnect`, `null` debe ser pasado.

## Valores devueltos

Si no se encuentra ningún error, `oci_error` devuelve `false`. De lo contrario, `oci_error` devuelve la información sobre el error en forma de un array asociativo.

| Clave del array | Tipo | Descripción |
|----|----|----|
| `code` | `int` | El número de error de Oracle. |
| `message` | `string` | El texto del error de Oracle. |
| `offset` | `int` | La posición del byte del error en la consulta SQL. Si no hay consulta, `0` será colocado como valor. |
| `sqltext` | `string` | El texto de la consulta SQL. Si no hay consulta, será una cadena vacía. |

Descripción del array devuelto por `oci_error`

## Historial de cambios

| Versión                | Descripción                                  |
|------------------------|----------------------------------------------|
| 8.0.0, PECL OCI8 3.0.0 | `connection_or_statement` ahora es nullable. |

## Ejemplos

Ejemplo de visualización de un mensaje de error de Oracle después de un error de conexión

```
<?php
$conn = oci_connect("hr", "welcome", "localhost/XE");
if (!$conn) {
    $e = oci_error();   // Para los errores oci_connect, no se pasa un manejador de conexión
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}
?>

    
```php

Ejemplo de visualización de un mensaje de error de Oracle después de un error de análisis

```
<?php
$stid = oci_parse($conn, "select ' from dual");  // Note el error con las comillas
if (!$stid) {
    $e = oci_error($conn);  // Para los errores oci_parse, se pasa el manejador de conexión
    trigger_error(htmlentities($e['message']), E_USER_ERROR);
}
?>

    
```php

Ejemplo de visualización de un mensaje de error de Oracle después de un error de ejecución encontrado en una consulta SQL

```
<?php
$stid = oci_parse($conn, "select does_not_exist from dual");
$r = oci_execute($stid);
if (!$r) {
    $e = oci_error($stid);  // Para los errores oci_execute, se pasa el manejador de conexión
    print htmlentities($e['message']);
    print "\n<pre>\n";
    print htmlentities($e['sqltext']);
    printf("\n%".($e['offset']+1)."s", "^");
    print  "\n</pre>\n";
}
?>

    
```php
