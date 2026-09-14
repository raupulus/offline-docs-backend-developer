---
title: session_decode
description: Decodifica la información de sesión desde una cadena de sesión codificada
source_url: https://www.php.net/manual/es/function.session-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 4de6272a1
order: 73760
---

session_decode

Decodifica la información de sesión desde una cadena de sesión codificada

## Descripción

```php
session_decode(string $data): bool
```php

`session_decode` decodifica la información de sesión serializada proporcianda en `data`, y rellena la variable superglobal \$\_SESSION con el resultado.

Por defecto, el método de deserialización usado es interno a PHP, y no es el mismo que `unserialize`. El método de serialización se puede establecer con [session.serialize_handler](#ini.session.serialize-handler).

## Parámetros

`data`  
Los datos codificados a alamcenar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`session_encode`, [session.serialize_handler](#ini.session.serialize-handler)
