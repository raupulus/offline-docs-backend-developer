---
title: Error::__construct
description: Construir el objeto error
source_url: https://www.php.net/manual/es/error.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/error/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 3fc56d76d
order: 3160
---

Error::\_\_construct

Construir el objeto error

## Descripción

```php
public Error::__construct([string $message], [int $code], [Throwable $previous])
```php

Construye el Error.

## Parámetros

`message`  
El mensaje de error.

`code`  
El código de error.

`previous`  
El objeto Throwable anterior empleado para la cadena de excepciones.

## Notas

> [!NOTE]
> El parámetro `message` *NO* es seguro a nivel binario.
