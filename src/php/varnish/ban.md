---
title: VarnishAdmin::ban
description: Prohibe URLs usando una expresión VCL
source_url: https://www.php.net/manual/es/varnishadmin.ban.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/varnish/varnishadmin/ban.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: varnish
translation_status: ready
translation_reviewed: false
translation_revision: a8071d1b7
order: 100910
---

VarnishAdmin::ban

Prohibe URLs usando una expresión VCL

## Descripción

```php
public VarnishAdmin::ban(string $vcl_regex): int
```php

## Parámetros

`vcl_regex`  
expresión VCL de Varnish. Se basa en el comando de prohibición de varnish.

## Valores devueltos

Devuelve el estado de comando de varnish.
