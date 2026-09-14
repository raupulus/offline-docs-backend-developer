---
title: Pdo\Pgsql::getPid
description: Devuelve el PID del proceso backend que gestiona esta conexión
source_url: https://www.php.net/manual/es/pdo-pgsql.getpid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo/pgsql/getpid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 858400b07
order: 62550
---

Pdo\Pgsql::getPid

Devuelve el PID del proceso backend que gestiona esta conexión

## Descripción

```php
public Pdo\Pgsql::getPid(): int
```php

Devuelve el PID del proceso backend que gestiona esta conexión. Cabe señalar que el PID pertenece a un proceso que se ejecuta en el host del servidor, y no en el host local.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el PID en forma de un `int`.

## Ejemplos

Ejemplo de Pdo\Pgsql::getPid

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
echo $db->getPid();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    12345

## Véase también

pg_get_pid
