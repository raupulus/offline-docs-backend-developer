---
title: MessageFormatter::getErrorCode
description: Lee el último código de error de la última operación
source_url: https://www.php.net/manual/es/messageformatter.geterrorcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/messageformatter/get-error-code.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 42060
---

MessageFormatter::getErrorCode

msgfmt_get_error_code

Lee el último código de error de la última operación

## Descripción

Estilo orientado a objetos

```php
public MessageFormatter::getErrorCode(): int
```php

Estilo procedimental

```php
msgfmt_get_error_code(MessageFormatter $formatter): int
```

Lee el último código de error de la última operación.

## Parámetros

`formatter`  
Un objeto de formateador de mensajes `MessageFormatter`

## Valores devueltos

El código de error, una de las valores UErrorCode. El valor inicial es U_ZERO_ERROR.

## Véase también

`msgfmt_get_error_message`, `intl_get_error_code`, `intl_is_failure`
