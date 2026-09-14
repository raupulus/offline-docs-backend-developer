---
title: PDO::errorInfo
description: Devuelve las informaciones asociadas al error durante la última operación
  sobre la base de datos
source_url: https://www.php.net/manual/es/pdo.errorinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/errorinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: 661e6858a
order: 61870
---

PDO::errorInfo

Devuelve las informaciones asociadas al error durante la última operación sobre la base de datos

## Descripción

```php
public PDO::errorInfo(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

PDO::errorInfo devuelve un array que contiene informaciones sobre el error ocurrido durante la última operación ejecutada por este manejador de base de datos. El array contiene los siguientes campos:

| Elemento | Información |
|----|----|
| 0 | Código de error SQLSTATE (un identificador alfanumérico de cinco caracteres definido en el estándar ANSI SQL). |
| 1 | Código de error específico del driver. |
| 2 | Mensaje de error específico del driver. |

> [!NOTE]
> Si el código de error SQLSTATE no está definido o si no hay un error específico del driver, el elemento siguiente al elemento 0 será definido a `null`.

PDO::errorInfo devuelve únicamente las informaciones de los errores para las operaciones ejecutadas directamente sobre un manejador de base de datos. Si se crea un objeto PDOStatement con la función PDO::prepare o la función PDO::query y se invoca un error sobre el manejador de consulta, PDO::errorInfo no devolverá el error desde el manejador de consulta. Se debe llamar a la función PDOStatement::errorInfo para devolver las informaciones sobre el error para una operación ejecutada sobre un manejador de consulta particular.

## Ejemplos

Muestra los campos de errores para una conexión PDO_ODBC sobre una base de datos DB2

```
<?php
/* Provoca un error -- sintaxis SQL incorrecta */
$stmt = $dbh->prepare('sintaxis sql incorrecta');
if (!$stmt) {
   echo "\nPDO::errorInfo():\n";
   print_r($dbh->errorInfo());
}
?>

    
```php

El ejemplo anterior mostrará:

    PDO::errorInfo():
    Array
    (
        [0] => 42S02
        [1] => -204
        [2] => [IBM][CLI Driver][DB2/LINUX] SQL0204N  "DANIELS.BONES" is an undefined name.  SQLSTATE=42704
    )

## Véase también

PDO::errorCode, PDOStatement::errorCode, PDOStatement::errorInfo
