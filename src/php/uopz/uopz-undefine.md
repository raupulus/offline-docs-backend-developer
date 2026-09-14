---
title: uopz_undefine
description: Elimina una constante
source_url: https://www.php.net/manual/es/function.uopz-undefine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-undefine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99420
---

uopz_undefine

Elimina una constante

## Descripción

```php
uopz_undefine(string $constant): bool
```php

```php
uopz_undefine(string $class, string $constant): bool
```

Elimina una constante en tiempo de ejecución.

## Parámetros

`class`  
El nombre de la clase que contiene la `constant`

`constant`  
El nombre de una constante existente

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `uopz_undefine`

```php
<?php
define("MY", true);

uopz_undefine("MY");

var_dump(defined("MY"));
?>

   
```

El ejemplo anterior mostrará:

    bool(false)
