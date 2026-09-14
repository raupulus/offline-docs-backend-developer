---
title: odbc_setoption
description: Modifica los parámetros ODBC
source_url: https://www.php.net/manual/es/function.odbc-setoption.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-setoption.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 99060
---

odbc_setoption

Modifica los parámetros ODBC

## Descripción

```php
odbc_setoption(Odbc\Connection $odbc, int $which, int $option, int $value): bool
```php

`odbc_setoption` permite acceder a las opciones ODBC para una conexión particular o un resultado de consulta. Fue escrita para ayudar a la resolución de problemas relacionados con los controladores ODBC problemáticos. Será necesario utilizar `odbc_setoption` si se es un programador ODBC y se comprenden los diversos efectos de las opciones disponibles. Asimismo, se necesitará un buen manual de referencia para comprender las opciones y su uso. Diferentes versiones de controladores admiten diferentes versiones de opciones.

Dado que los efectos pueden variar de un controlador a otro, el uso de `odbc_setoption` en scripts destinados a ser entregados al público está muy fuertemente desaconsejado. Además, ciertas opciones ODBC no están disponibles porque deben ser fijadas antes del establecimiento de la conexión. Sin embargo, si en un caso bien específico, `odbc_setoption` permite utilizar PHP sin que el jefe obligue a usar un producto comercial, entonces no importa.

## Parámetros

`odbc`  
Un identificador de conexión, o un identificador de resultado, para el cual se desea modificar opciones. Para SQLSetConnectOption(), es un identificador de conexión. Para SQLSetStmtOption(), es un identificador de resultado.

`which`  
Función ODBC a utilizar. El valor debe ser 1 para SQLSetConnectOption() y 2 para SQLSetStmtOption().

`option`  
La opción a definir.

`value`  
El valor para el parámetro `option` dado.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` espera ahora una instancia de `Odbc\Connection` o de `Odbc\Result`; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `odbc_setoption`

```
<?php
// 1. La opción 102 de SQLSetConnectOption() es SQL_AUTOCOMMIT.
// 1 de SQL_AUTOCOMMIT es SQL_AUTOCOMMIT_ON.
//    Este ejemplo tiene el mismo efecto que
//    odbc_autocommit($conn, true);

odbc_setoption($conn, 1, 102, 1);

// 2. Opción 0 de SQLSetStmtOption() es SQL_QUERY_TIMEOUT.
//    Este ejemplo fija el tiempo límite a 30 segundos.

$result = odbc_prepare($conn, $sql);
odbc_setoption($result, 2, 0, 30);
odbc_execute($result);
?>

    
```php
