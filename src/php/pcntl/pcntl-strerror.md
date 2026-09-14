---
title: pcntl_strerror
description: Recupera el mensaje de error del sistema asociado con el errno proporcionado
source_url: https://www.php.net/manual/es/function.pcntl-strerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-strerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: false
translation_revision: e7dcfdc34
order: 61400
---

pcntl_strerror

Recupera el mensaje de error del sistema asociado con el errno proporcionado

## Descripción

```php
pcntl_strerror(int $error_code): string
```php

Devuelve el mensaje de error del sistema asociado al `error_code` (`errno`) de la última función pcntl que falló. El parámetro `error_code` puede ser obtenido llamando a `pcntl_get_last_error`.

## Parámetros

`error_code`  
Un número de error (`errno`), devuelto por `pcntl_get_last_error`.

## Valores devueltos

Devuelve el mensaje de error, en forma de string.

## Ejemplos

`pcntl_strerror` ejemplo

Este ejemplo intentará esperar a los procesos hijos en una situación donde no existen procesos hijos, y luego mostrará el mensaje de error correspondiente.

```
<?php
$pid = pcntl_wait($status);
if ($pid === -1) {
    $errno = pcntl_get_last_error();
    $message = pcntl_strerror($errno);
    fwrite(STDERR, 'pcntl_wait falló con errno ' . $errno
           . ': ' . $message . PHP_EOL);
}

   
```php

Resultado del ejemplo anterior es similar a:

    pcntl_wait falló con errno 10: No child processes

## Véase también

pcntl_get_last_error
