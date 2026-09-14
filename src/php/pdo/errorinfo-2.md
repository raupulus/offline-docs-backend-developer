---
title: PDOStatement::errorInfo
description: Recupera las informaciones sobre el error asociado durante la última
  operación sobre la consulta
source_url: https://www.php.net/manual/es/pdostatement.errorinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/errorinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: 661e6858a
order: 62080
---

PDOStatement::errorInfo

Recupera las informaciones sobre el error asociado durante la última operación sobre la consulta

## Descripción

```php
public PDOStatement::errorInfo(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

PDOStatement::errorInfo devuelve un array que contiene informaciones sobre el error ocurrido durante la última operación ejecutada por este gestor de consultas. El array contiene los siguientes campos:

| Elemento | Información |
|----|----|
| 0 | Código de error SQLSTATE (un identificador de cinco caracteres alfanuméricos definido en el estándar ANSI SQL) |
| 1 | Código de error específico del driver. |
| 2 | Mensaje de error específico del driver. |

## Ejemplos

Muestra los campos de errorInfo() para una conexión PDO_ODBC sobre una base de datos DB2

```
<?php
/* Provoca un error -- la tabla BONES no existe */
$sth = $dbh->prepare('SELECT skull FROM bones');
$sth->execute();

echo "\nPDOStatement::errorInfo():\n";
$arr = $sth->errorInfo();
print_r($arr);
?>

    
```php

El ejemplo anterior mostrará:

    PDOStatement::errorInfo():
    Array
    (
        [0] => 42S02
        [1] => -204
        [2] => [IBM][CLI Driver][DB2/LINUX] SQL0204N  "DANIELS.BONES" is an undefined name.  SQLSTATE=42704
    )

## Véase también

PDO::errorCode, PDO::errorInfo, PDOStatement::errorCode
