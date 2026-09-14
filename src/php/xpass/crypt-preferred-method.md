---
title: crypt_preferred_method
description: Devuelve el prefijo del método de hash preferido
source_url: https://www.php.net/manual/es/function.crypt-preferred-method.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xpass/functions/crypt-preferred-method.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xpass
translation_status: ready
translation_reviewed: true
translation_revision: 7b9d57fa4
order: 104040
---

crypt_preferred_method

Devuelve el prefijo del método de hash preferido

## Descripción

```php
crypt_preferred_method(): string
```php

Devuelve el prefijo del método de hash preferido.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una cadena con el prefijo, o `null` en caso de error.

## Ejemplos

Un ejemplo de `crypt_preferred_method`

```
<?php
var_dump(crypt_preferred_method());
?>

   
```php

El ejemplo anterior mostrará:

    string(3) "$y$"

## Véase también

crypt_gensalt
