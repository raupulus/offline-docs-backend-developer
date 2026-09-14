---
title: stream_isatty
description: Verifica si un flujo es un TTY
source_url: https://www.php.net/manual/es/function.stream-isatty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-isatty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: e4a3ece42
order: 88020
---

stream_isatty

Verifica si un flujo es un TTY

## Descripción

```php
stream_isatty(resource $stream): bool
```php

Determina si el flujo `stream` se refiere a un dispositivo de tipo terminal válido. Esta es una versión más portable de `posix_isatty`, ya que también funciona en sistemas Windows.

## Parámetros

`stream`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `stream_isatty`

Este comando puede ser utilizado para determinar si un flujo de salida / error estándar es redirigido a un fichero.

```
     php -r "var_export(stream_isatty(STDERR));"
    
```php

Resultado del ejemplo anterior es similar a:

         true
        

```
     php -r "var_export(stream_isatty(STDERR));" 2>output.txt
    
```php

Resultado del ejemplo anterior es similar a:

         false
