---
title: apache_get_modules
description: Devuelve la lista de módulos Apache cargados
source_url: https://www.php.net/manual/es/function.apache-get-modules.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/functions/apache-get-modules.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_reviewed: true
translation_revision: f3b9d85f7
order: 4740
---

apache_get_modules

Devuelve la lista de módulos Apache cargados

## Descripción

```php
apache_get_modules(): array
```php

Devuelve la lista de módulos Apache cargados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` que contiene los módulos Apache cargados.

## Ejemplos

Ejemplo con `apache_get_modules`

```
<?php
print_r(apache_get_modules());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => core
        [1] => http_core
        [2] => mod_so
        [3] => sapi_apache2
        [4] => mod_mime
        [5] => mod_rewrite
    )
