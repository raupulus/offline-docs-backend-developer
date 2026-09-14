---
title: posix_strerror
description: Recuperar el mensaje de error del sistema asociado con el errno dado
source_url: https://www.php.net/manual/es/function.posix-strerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-strerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65460
---

posix_strerror

Recuperar el mensaje de error del sistema asociado con el errno dado

## Descripción

```php
posix_strerror(int $error_code): string
```php

Devuelve el mensaje de error del sistema POSIX asociado con el `error_code`. Es posible obtener el parámetro `error_code` llamando la función `posix_get_last_error`.

## Parámetros

`error_code`  
Un número de error POSIX, devuelto por `posix_get_last_error`. Si se define como 0, entonces se devuelve la cadena "Success".

## Valores devueltos

Devuelve el mensaje de error, como una cadena.

## Ejemplos

Ejemplo de `posix_strerror`

Este ejemplo intentará matar un proceso que no existe, luego imprimirá el mensaje de error correspondiente.

```
<?php
posix_kill(50,SIGKILL);
echo posix_strerror(posix_get_last_error())."\n";
?>

    
```php

Resultado del ejemplo anterior es similar a:

    No such process

## Véase también

`posix_get_last_error`
