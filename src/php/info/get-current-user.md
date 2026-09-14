---
title: get_current_user
description: Devuelve el nombre del propietario del script actual
source_url: https://www.php.net/manual/es/function.get-current-user.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/get-current-user.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 8dd14a886
order: 38850
---

get_current_user

Devuelve el nombre del propietario del script actual

## Descripción

```php
get_current_user(): string
```php

Devuelve el nombre del propietario del script actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre del usuario, en forma de `string`.

## Ejemplos

Ejemplo con `get_current_user`

```
<?php
echo 'Propietario del script actual : ' . get_current_user();
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Propietario del script actual : SYSTEM

## Véase también

`getmyuid`, `getmygid`, `getmypid`, `getmyinode`, `getlastmod`
