---
title: Session::getSchema
description: Devuelve un nuevo objeto esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.getschema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/getschema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54050
---

Session::getSchema

Devuelve un nuevo objeto esquema

## Descripción

```php
public mysql_xdevapi\Session::getSchema(string $schema_name): mysql_xdevapi\Schema
```php

Un nuevo objeto Schema para el nombre de esquema proporcionado.

## Parámetros

`schema_name`  
El nombre del esquema (base de datos) para el cual se obtiene un objeto Schema.

## Valores devueltos

Un objeto Schema.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::getSchema`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$schema  = $session->getSchema("addressbook");

print_r($schema);

   
```php

Resultado del ejemplo anterior es similar a:

    mysql_xdevapi\Schema Object
    (
        [name] => addressbook
    )
