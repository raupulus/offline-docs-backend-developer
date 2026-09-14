---
title: get_include_path
description: Lee el valor de la directiva de configuración include_path
source_url: https://www.php.net/manual/es/function.get-include-path.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/get-include-path.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 8dd14a886
order: 38880
---

get_include_path

Lee el valor de la directiva de configuración include_path

## Descripción

```php
get_include_path(): string
```php

Lee el valor de la directiva de configuración [include_path](#ini.include-path).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la ruta, en forma de `string`, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `get_include_path`

```
<?php
echo get_include_path();

// O utilizar ini_get()
echo ini_get('include_path');
?>

    
```php

## Véase también

`ini_get`, `restore_include_path`, `set_include_path`, `include`
