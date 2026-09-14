---
title: uopz_set_hook
description: Define el hook que se ejecutará al entrar en una función o un método
source_url: https://www.php.net/manual/es/function.uopz-set-hook.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-set-hook.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: 8e242d4d3
order: 99380
---

uopz_set_hook

Define el hook que se ejecutará al entrar en una función o un método

## Descripción

```php
uopz_set_hook(string $function, Closure $hook): bool
```php

```php
uopz_set_hook(string $class, string $function, Closure $hook): bool
```

Define un hook que se ejecutará al entrar en una función o un método.

## Parámetros

`class`  
El nombre de la clase.

`function`  
El nombre de la función o del método.

`hook`  
Una función anónima que se ejecutará al entrar en la función o el método.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Uso básico de `uopz_set_hook`

```php
<?php
function foo() {
    echo 'foo';
}
uopz_set_hook('foo', function () {echo 'bar';});
foo();
?>

   
```

El ejemplo anterior mostrará:

    barfoo

## Véase también

uopz_get_hook

uopz_unset_hook
