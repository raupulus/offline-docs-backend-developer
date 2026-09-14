---
title: odbc_execute
description: Ejecuta una consulta SQL preparada
source_url: https://www.php.net/manual/es/function.odbc-execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98800
---

odbc_execute

Ejecuta una consulta SQL preparada

## Descripción

```php
odbc_execute(Odbc\Result $statement, [array $params]): bool
```php

Ejecuta una consulta SQL preparada por `odbc_prepare`.

## Parámetros

`statement`  
The ODBC result object desde `odbc_prepare`.

`params`  
Los valores del parámetro `params` serán sustituidos en las variables de consulta de la consulta preparada. Los elementos de este array serán convertidos a string al llamar a esta función.

Todo parámetro de `params` que comience y termine con comillas simples será considerado como un nombre de fichero a leer y enviado a la base de datos, con la variable de consulta apropiada.

Si se desea almacenar un string que comience y termine realmente con comillas, se debe añadir un espacio al inicio o al final del string, para evitar que este parámetro sea confundido con un nombre de fichero. Si esto no es posible en el contexto de la aplicación, se deberá utilizar la función `odbc_exec`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |
| 8.0.0 | El parámetro `flags`, sin uso, ha sido eliminado. |

## Ejemplos

Ejemplo con `odbc_execute` y `odbc_prepare`

En el script siguiente, `$success` solo será posible si los tres parámetros de myproc son parámetros de tipo IN:

```
<?php
$a = 1;
$b = 2;
$c = 3;
$stmt    = odbc_prepare($conn, 'CALL myproc(?,?,?)');
$success = odbc_execute($stmt, array($a, $b, $c));
?>

    
```php

Si se necesita llamar a un procedimiento almacenado utilizando parámetros INOUT o OUT, la solución es utilizar una extensión nativa de la base de datos (por ejemplo [oci8](#ref.oci8) para Oracle).

## Véase también

`odbc_prepare`
