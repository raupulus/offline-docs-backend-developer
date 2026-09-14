---
title: PDOStatement::getAttribute
description: Recupera un atributo de consulta
source_url: https://www.php.net/manual/es/pdostatement.getattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/getattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 661e6858a
order: 62140
---

PDOStatement::getAttribute

Recupera un atributo de consulta

## Descripción

```php
public PDOStatement::getAttribute(int $name): mixed
```php

Recupera un atributo de la consulta. Actualmente, no existen atributos genéricos, sino especificaciones del driver:

- `PDO::ATTR_CURSOR_NAME` (especificación de Firebird y ODBC): Recupera el nombre del cursor para `UPDATE ... WHERE CURRENT OF`.

Tenga en cuenta que los atributos específicos del controlador *no deben* utilizarse con otros controladores.

## Parámetros

`name`  
El atributo a consultar.

## Valores devueltos

Devuelve el valor del atributo.

## Véase también

PDO::getAttribute, PDO::setAttribute, PDOStatement::setAttribute
