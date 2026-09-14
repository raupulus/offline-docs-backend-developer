---
title: Session::getDefaultSchema
description: Devuelve el nombre del esquema predeterminado
source_url: https://www.php.net/manual/es/mysql-xdevapi-session.getdefaultschema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/session/getdefaultschema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 6d310c441
order: 54040
---

Session::getDefaultSchema

Devuelve el nombre del esquema predeterminado

## Descripción

```php
public mysql_xdevapi\Session::getDefaultSchema(): mysql_xdevapi\Schema
```php

Recupera el esquema por defecto que se suele establecer en el URI de conexión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El esquema por defecto definido por la conexión, o `null` si no se ha establecido ninguno.

## Ejemplos

Ejemplo de `mysql_xdevapi\Session::getSchema`

```
<?php
$uri = "mysqlx://testuser:testpasswd@localhost:33160/testx?ssl-mode=disabled";
$session = mysql_xdevapi\getSession($uri);

$schema = $session->getDefaultSchema();
echo $schema->getName();
?>

   
```php

El ejemplo anterior mostrará:

    testx
