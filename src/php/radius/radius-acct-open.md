---
title: radius_acct_open
description: Crea un manejador Radius para el conteo
source_url: https://www.php.net/manual/es/function.radius-acct-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-acct-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67540
---

radius_acct_open

Crea un manejador Radius para el conteo

## Descripción

```php
radius_acct_open(): resource
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un manejador en caso de tener éxito, `false` en caso de error. Esta función falla solamente si hay insuficiencia de memoria.

## Ejemplos

`radius_acct_open` example

```
<?php
$res = radius_acct_open ()
    or die ("No se pudo crear un manejador handle");
print "Manejador creado exitosamente";
?>

   
```php
