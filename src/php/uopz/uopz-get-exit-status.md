---
title: uopz_get_exit_status
description: Devuelve el último estado de salida definido
source_url: https://www.php.net/manual/es/function.uopz-get-exit-status.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-get-exit-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: 961ac1b44
order: 99270
---

uopz_get_exit_status

Devuelve el último estado de salida definido

## Descripción

```php
uopz_get_exit_status(): mixed
```php

Devuelve el último estado de salida definido, es decir, el valor pasado a `exit`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función devuelve el último estado de salida, o `null` si `exit` no ha sido llamada.

## Ejemplos

Ejemplo de `uopz_get_exit_status`

```
<?php
exit(123);
echo uopz_get_exit_status();?>

   
```php

El ejemplo anterior mostrará:

    123

## Notas

> [!CAUTION]
> [OPcache](#book.opcache) optimiza el código muerto después de una salida incondicional.

## Véase también

uopz_allow_exit
