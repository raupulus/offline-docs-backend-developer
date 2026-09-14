---
title: mailparse_msg_create
description: Crea un recurso de correo mime
source_url: https://www.php.net/manual/es/function.mailparse-msg-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mailparse/functions/mailparse-msg-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mailparse
translation_status: ready
translation_revision: 01bd007b0
order: 44320
---

mailparse_msg_create

Crea un recurso de correo mime

## Descripción

```php
mailparse_msg_create(): resource
```php

Crea un recurso tipo correo `MIME`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un recurso que puede ser usado para interpretar un mensaje.

## Notas

> [!NOTE]
> Se recomienda llamar a `mailparse_msg_free` en el resultado de esta función, cuando ya no sea necesaria, para evitar fugas de memoria

## Véase también

mailparse_msg_free

mailparse_msg_parse_file
