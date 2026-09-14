---
title: VarnishAdmin::banUrl
description: Prohibe una URL usando una expresión VCL
source_url: https://www.php.net/manual/es/varnishadmin.banurl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/varnish/varnishadmin/banurl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: varnish
translation_status: ready
translation_reviewed: false
translation_revision: a8071d1b7
order: 100920
---

VarnishAdmin::banUrl

Prohibe una URL usando una expresión VCL

## Descripción

```php
public VarnishAdmin::banUrl(string $vcl_regex): int
```php

## Parámetros

`vcl_regex`  
Expresión regular de URL en sintaxis compatible con PCRE. Está basado en el comando de varnish ban.url.

## Valores devueltos

Devuelve el estado de comando varnish.
