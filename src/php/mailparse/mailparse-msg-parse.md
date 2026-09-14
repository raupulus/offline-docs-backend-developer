---
title: mailparse_msg_parse
description: Procesar datos incrementalmente sobre un búfer
source_url: https://www.php.net/manual/es/function.mailparse-msg-parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mailparse/functions/mailparse-msg-parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mailparse
translation_status: ready
translation_reviewed: false
translation_revision: 01bd007b0
order: 44410
---

mailparse_msg_parse

Procesar datos incrementalmente sobre un búfer

## Descripción

```php
mailparse_msg_parse(resource $mimemail, string $data): bool
```php

Procesa datos incrementalmente al interior del recurso de correo mime entregado.

Esta función le permite secuenciar porciones de un archivo en pedazos, en lugar de leer y procesarlo en su totalidad.

## Parámetros

`mimemail`  
Un recurso `MIME` válido.

`data`  
> [!NOTE]
> El último trozo de `data` debe terminar con una nueva línea (`CRLF`); de lo contrario, no se analizará la última línea del mensaje.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
