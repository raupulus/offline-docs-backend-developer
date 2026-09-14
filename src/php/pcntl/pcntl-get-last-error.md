---
title: pcntl_get_last_error
description: Recupera el número del error generado por la última función pcntl utilizada
source_url: https://www.php.net/manual/es/function.pcntl-get-last-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-get-last-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: false
translation_revision: 4ac5624be
order: 61240
---

pcntl_get_last_error

Recupera el número del error generado por la última función pcntl utilizada

## Descripción

```php
pcntl_get_last_error(): int
```php

Recupera el número de error (`errno`) definido por la última función \*\*pcntl\*\* que haya fallado. El mensaje de error del sistema asociado al número de error puede ser verificado con la función `pcntl_strerror`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de error (`errno`) definido por la última función pcntl que haya fallado. Si no se ha encontrado ningún error, se devuelve 0.

## Ejemplos

`pcntl_get_last_error` example

Este ejemplo intentará esperar a los procesos hijos en una situación donde no existen procesos hijos, y luego mostrará el mensaje de error correspondiente.

```
<?php
$pid = pcntl_wait($status);
if ($pid === -1) {
    $errno = pcntl_get_last_error();
    $message = pcntl_strerror($errno);
    fwrite(STDERR, 'pcntl_wait failed with errno ' . $errno
           . ': ' . $message . PHP_EOL);
}

   
```php

Resultado del ejemplo anterior es similar a:

    pcntl_wait failed with errno 10: No child processes

## Véase también

pcntl_strerror
