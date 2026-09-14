---
title: PDOStatement::errorCode
description: Recupera las informaciones sobre el error asociado durante la última
  operación sobre la consulta
source_url: https://www.php.net/manual/es/pdostatement.errorcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/errorcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 661e6858a
order: 62070
---

PDOStatement::errorCode

Recupera las informaciones sobre el error asociado durante la última operación sobre la consulta

## Descripción

```php
public PDOStatement::errorCode(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Idéntico a PDO::errorCode, excepto que PDOStatement::errorCode recupera únicamente los códigos de error para las operaciones sobre los objetos PDOStatement.

## Ejemplos

Determina la categoría del error que ocurre

```
<?php
/* Provoca un error -- la tabla BONES no existe */
$err = $dbh->prepare('SELECT skull FROM bones');
$err->execute();

echo "\nPDOStatement::errorCode(): ";
print $err->errorCode();
?>

    
```php

El ejemplo anterior mostrará:

    PDOStatement::errorCode(): 42S02

## Véase también

PDO::errorCode, PDO::errorInfo, PDOStatement::errorInfo
