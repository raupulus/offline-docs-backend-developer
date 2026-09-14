---
title: ReflectionExtension::getINIEntries
description: Recupera las entradas ini de la extensión
source_url: https://www.php.net/manual/es/reflectionextension.getinientries.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/getinientries.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70230
---

ReflectionExtension::getINIEntries

Recupera las entradas ini de la extensión

## Descripción

```php
public ReflectionExtension::getINIEntries(): array
```php

Recupera las entradas ini de la extensión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array asociativo donde las claves son las entradas ini, y los valores los valores de dichas entradas.

## Ejemplos

Ejemplo con ReflectionExtension::getINIEntries

```
<?php
$ext = new ReflectionExtension('mysql');

print_r($ext->getINIEntries());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [mysql.allow_persistent] => 1
        [mysql.max_persistent] => -1
        [mysql.max_links] => -1
        [mysql.default_host] =>
        [mysql.default_user] =>
        [mysql.default_password] =>
        [mysql.default_port] =>
        [mysql.default_socket] =>
        [mysql.connect_timeout] => 60
        [mysql.trace_mode] =>
        [mysql.allow_local_infile] => 1
        [mysql.cache_size] => 2000
    )

## Véase también

`ini_get_all`, ReflectionExtension::getConstants
