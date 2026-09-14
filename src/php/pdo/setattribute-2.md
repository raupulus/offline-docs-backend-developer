---
title: PDOStatement::setAttribute
description: Establece un atributo de consulta
source_url: https://www.php.net/manual/es/pdostatement.setattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/setattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 661e6858a
order: 62190
---

PDOStatement::setAttribute

Establece un atributo de consulta

## Descripción

```php
public PDOStatement::setAttribute(int $attribute, mixed $value): bool
```php

Establece un atributo de la consulta. Actualmente, no se definen atributos genéricos, sino especificaciones del driver:

- `PDO::ATTR_CURSOR_NAME` (especificidad de Firebird y ODBC): Establece el nombre del cursor para `UPDATE ... WHERE CURRENT OF`.

Tenga en cuenta que los atributos específicos del controlador *no deben* utilizarse con otros controladores.

## Parámetros

`attribute`  
El atributo a modificar.

`value`  
El valor para establecer el `attribute`, puede requerir un tipo específico según el atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

PDO::getAttribute, PDO::setAttribute, PDOStatement::getAttribute
