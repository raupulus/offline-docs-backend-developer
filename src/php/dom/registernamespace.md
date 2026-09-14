---
title: DOMXPath::registerNamespace
description: Registra el espacio de nombres con el objeto DOMXPath
source_url: https://www.php.net/manual/es/domxpath.registernamespace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domxpath/registernamespace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 14330
---

DOMXPath::registerNamespace

Registra el espacio de nombres con el objeto

DOMXPath

## Descripción

```php
public DOMXPath::registerNamespace(string $prefix, string $namespace): bool
```php

Registra `namespace` y `prefix` con el objeto DOMXPath.

## Parámetros

`prefix`  
El prefijo.

`namespace`  
La URI del espacio de nombres.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
