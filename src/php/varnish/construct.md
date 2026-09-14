---
title: VarnishAdmin::__construct
description: Constructor de VarnishAdmin
source_url: https://www.php.net/manual/es/varnishadmin.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/varnish/varnishadmin/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: varnish
translation_status: ready
translation_reviewed: false
translation_revision: 065dd47a9
order: 100950
---

VarnishAdmin::\_\_construct

Constructor de VarnishAdmin

## Descripción

```php
public VarnishAdmin::__construct([array $args])
```php

## Parámetros

`args`  
Argumentos de configuración. Las posibles claves son: VARNISH_CONFIG_IDENT - local varnish instance ident VARNISH_CONFIG_HOST - varnish instance ip VARNISH_CONFIG_PORT - varnish instance port VARNISH_CONFIG_SECRET - varnish instance secret VARNISH_CONFIG_TIMEOUT - connection read timeout VARNISH_CONFIG_COMPAT - varnish major version compatibility

## Valores devueltos

## Ejemplos

Ejemplo con `VarnishAdmin::__construct`

```
<?php
    $args = array(
        VARNISH_CONFIG_HOST => "::1",
        VARNISH_CONFIG_PORT => 6082,
        VARNISH_CONFIG_SECRET => "5174826b-8595-4958-aa7a-0609632ad7ca",
        VARNISH_CONFIG_TIMEOUT => 300,
    );
    $va = new VarnishAdmin($args);
?>

   
```php
