---
title: SchemaObject::getSchema
description: Devuelve el objeto esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-schemaobject.getschema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schemaobject/getschema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53970
---

SchemaObject::getSchema

Devuelve el objeto esquema

## Descripción

```php
abstract mysql_xdevapi\SchemaObject::getSchema(): mysql_xdevapi\Schema
```php

Utilizado por otros objetos para recuperar un objeto esquema.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El objeto esquema actual.

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
