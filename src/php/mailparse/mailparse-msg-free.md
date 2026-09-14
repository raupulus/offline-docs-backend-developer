---
title: mailparse_msg_free
description: Libera un recurso MIME
source_url: https://www.php.net/manual/es/function.mailparse-msg-free.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mailparse/functions/mailparse-msg-free.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mailparse
translation_status: ready
translation_revision: 01bd007b0
order: 44360
---

mailparse_msg_free

Libera un recurso MIME

## Descripción

```php
mailparse_msg_free(resource $mimemail): bool
```php

Libera un recurso `MIME`.

## Parámetros

`mimemail`  
Un recurso `MIME` válido reservado por `mailparse_msg_create` o `mailparse_msg_parse_file`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

mailparse_msg_create

mailparse_msg_parse_file
