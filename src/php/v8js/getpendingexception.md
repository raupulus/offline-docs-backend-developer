---
title: V8Js::getPendingException
description: Devuelve la excepción de Javascript no capturada pendiente
source_url: https://www.php.net/manual/es/v8js.getpendingexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/v8js/v8js/getpendingexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: v8js
translation_status: ready
translation_revision: '475439775'
order: 100360
---

V8Js::getPendingException

Devuelve la excepción de Javascript no capturada pendiente

## Descripción

```php
public V8Js::getPendingException(): V8JsException
```php

Devuelve cualquier excepción de Javascript no capturada pendiente de una o varias llamadas anteriores a `V8Js::executeString`, en forma de `V8JsException`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un objeto `V8JsException` o `null`.
