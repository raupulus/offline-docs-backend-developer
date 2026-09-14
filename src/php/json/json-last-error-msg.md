---
title: json_last_error_msg
description: Devuelve el mensaje del último error ocurrido durante la llamada a la
  función json_validate(), json_encode() o json_decode()
source_url: https://www.php.net/manual/es/function.json-last-error-msg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/json/functions/json-last-error-msg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: json
translation_status: ready
translation_reviewed: false
translation_revision: 811ad2ca0
order: 42850
---

json_last_error_msg

Devuelve el mensaje del último error ocurrido durante la llamada a la función json_validate(), json_encode() o json_decode()

## Descripción

```php
json_last_error_msg(): string
```php

Devuelve el string de error del último llamado a `json_validate`, `json_encode` o `json_decode`, que no haya especificado `JSON_THROW_ON_ERROR`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el mensaje de error en caso de éxito, o `"No error"` si no ha ocurrido ningún error, o `false` si ocurre un error.

## Véase también

`json_last_error`
