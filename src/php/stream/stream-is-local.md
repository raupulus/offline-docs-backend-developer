---
title: stream_is_local
description: Verifica si un flujo es local
source_url: https://www.php.net/manual/es/function.stream-is-local.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-is-local.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 88010
---

stream_is_local

Verifica si un flujo es local

## Descripción

```php
stream_is_local(resource $stream): bool
```php

`stream_is_local` verifica si el flujo o la URL `stream_or_url` es local al sistema o no.

## Parámetros

`stream`  
El `resource` de flujo o la URL a verificar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `stream_is_local`

Ejemplo simple.

```
<?php
var_dump(stream_is_local("http://example.com"));
var_dump(stream_is_local("/etc"));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    bool(false)
    bool(true)
