---
title: Session::dropSchema
description: Elimina un esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.dropschema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/dropschema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54020
---

Session::dropSchema

Elimina un esquema

## Descripción

```php
public mysql_xdevapi\Session::dropSchema(string $schema_name): bool
```php

Elimina un esquema (base de datos).

## Parámetros

`schema_name`  
El nombre del esquema a eliminar.

## Valores devueltos

`true` si el esquema es eliminado, o `false` si no existe o no puede ser eliminado.

Un nivel de error `E_WARNING` es generado si el esquema no existe.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::dropSchema`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->dropSchema("addressbook");

$session->close();
?>

   
```php
