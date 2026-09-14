---
title: posix_get_last_error
description: Recuperar el número de error establecido por la última función posix
  que ha fallado
source_url: https://www.php.net/manual/es/function.posix-get-last-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-get-last-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_revision: f8854f6a6
order: 65150
---

posix_get_last_error

Recuperar el número de error establecido por la última función posix que ha fallado

## Descripción

```php
posix_get_last_error(): int
```php

Recupera el número de error establecido por la última función posix que falló. El mensaje de error del sistema asociado con el valor errno puede ser consultado con `posix_strerror`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el valor errno (número de error) definido por la última función posix que haya fallado. Si no existe un error, se devuelve 0.

## Ejemplos

Ejemplo de `posix_get_last_error`

Este ejemplo intenta matar un id de proceso inexistente, lo cual establecerá el error más reciente. Entonces el valor errno será impreso.

```
<?php
posix_kill(999459,SIGKILL);
echo 'Su error devuelto fue '.posix_get_last_error(); //Su error devuelto fue ___
?>

    
```php

## Véase también

`posix_strerror`
