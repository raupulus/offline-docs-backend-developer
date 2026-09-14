---
title: odbc_prepare
description: Prepara una orden para su ejecución
source_url: https://www.php.net/manual/es/function.odbc-prepare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-prepare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98990
---

odbc_prepare

Prepara una orden para su ejecución

## Descripción

```php
odbc_prepare(Odbc\Connection $odbc, string $query): Odbc\Result
```php

Prepara una orden para su ejecución. The ODBC result object puede ser utilizado más tarde para ejecutar la orden con `odbc_execute`.

Algunas bases de datos (como IBM DB2, MS SQL Server y Oracle) soportan los procedimientos almacenados que aceptan los tipos de parámetros IN, INOUT y OUT como se definen en las especificaciones ODBC. Sin embargo, el driver unificado ODBC soporta actualmente únicamente el tipo de parámetros IN para los procedimientos almacenados.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`query`  
La consulta a preparar.

## Valores devueltos

Devuelve un objeto de resultado ODBC si la orden SQL ha sido preparada con éxito. Retorna `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo con `odbc_prepare` y `odbc_execute`

En el código siguiente, `$res` solo será válido si los tres parámetros para myproc son parámetros IN:

```
<?php
$a = 1;
$b = 2;
$c = 3;
$stmt = odbc_prepare($conn, 'CALL myproc(?,?,?)');
$res  = odbc_execute($stmt, array($a, $b, $c));
?>

    
```php

Si necesita llamar a un procedimiento almacenado que utilice parámetros INOUT o OUT, se recomienda utilizar la extensión nativa de su base de datos (por ejemplo [oci8](#ref.oci8) para Oracle).

## Véase también

`odbc_execute`
