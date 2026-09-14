---
title: uopz_redefine
description: Redefinir una constante
source_url: https://www.php.net/manual/es/function.uopz-redefine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-redefine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99350
---

uopz_redefine

Redefinir una constante

## Descripción

```php
uopz_redefine(string $constant, mixed $value): bool
```php

```php
uopz_redefine(string $class, string $constant, mixed $value): bool
```

Redefine la constante `constant` proporcionada, a `value`.

## Parámetros

`class`  
El nombre de la clase que contiene la constante

`constant`  
El nombre de la constante

`value`  
El nuevo valor de la constante; debe ser un tipo válido para una constante

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `uopz_redefine`

```php
<?php
define("MY", 100);

uopz_redefine("MY", 1000);

echo MY;
?>

   
```

El ejemplo anterior mostrará:

    1000
