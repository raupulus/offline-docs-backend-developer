---
title: SqlStatementResult::getWarnings
description: Devuelve las advertencias de la última operación
source_url: https://www.php.net/manual/es/mysql-xdevapi-sqlstatementresult.getwarnings.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/sqlstatementresult/getwarnings.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 286ab7c12
order: 54310
---

SqlStatementResult::getWarnings

Devuelve las advertencias de la última operación

## Descripción

```php
public mysql_xdevapi\SqlStatementResult::getWarnings(): array
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de objetos Warning de la última operación. Cada objeto define un 'message' de error, un 'nivel' de error y un 'code' de error. Un array vacío es devuelto si no hay errores.

## Ejemplos

Ejemplo de `mysql_xdevapi\SqlStatementResult::getWarnings`

```
<?php

/* ... */

?>

   
```php
