---
title: Session::createSchema
description: Crear un nuevo esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.createschema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/createschema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 54010
---

Session::createSchema

Crear un nuevo esquema

## Descripción

```php
public mysql_xdevapi\Session::createSchema(string $schema_name): mysql_xdevapi\Schema
```php

Crear un nuevo esquema.

## Parámetros

`schema_name`  
El nombre del esquema a crear.

## Valores devueltos

Un objeto Schema en caso de éxito, y lanza una excepción en caso de fallo.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::createSchema`

```
<?php
$uri  = 'mysqlx://happyuser:password@127.0.0.1:33060/';
$sess = mysql_xdevapi\getSession($uri);

try {

    if ($schema = $sess->createSchema('fruit')) {
        echo "Info: I created a schema named 'fruit'\n";
    }

} catch (Exception $e) {

   echo $e->getMessage();

}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Info: I created a schema named 'fruit'
