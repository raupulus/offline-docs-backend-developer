---
title: VarnishAdmin::setParam
description: Establece los parámetros de configuración en la instancia varnish actual
source_url: https://www.php.net/manual/es/varnishadmin.setparam.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/varnish/varnishadmin/setparam.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: varnish
translation_status: ready
translation_reviewed: false
translation_revision: 53242ee66
order: 101030
---

VarnishAdmin::setParam

Establece los parámetros de configuración en la instancia varnish actual

## Descripción

```php
public VarnishAdmin::setParam(string $name, string $value): int
```php

## Parámetros

`name`  
Nombre del parámetro de configuración varnish.

`value`  
Valor del parámetro de configuración varnish.

## Valores devueltos

Devuelve el estado de comando varnish.
