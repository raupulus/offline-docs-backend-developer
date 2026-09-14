---
title: uopz_unset_hook
description: Suprime el hook previamente fijado sobre una función o un método
source_url: https://www.php.net/manual/es/function.uopz-unset-hook.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-unset-hook.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: 8e242d4d3
order: 99430
---

uopz_unset_hook

Suprime el hook previamente fijado sobre una función o un método

## Descripción

```php
uopz_unset_hook(string $function): bool
```php

```php
uopz_unset_hook(string $class, string $function): bool
```

Suprime el hook previamente fijado sobre una función o un método.

## Parámetros

`class`  
El nombre de la clase.

`function`  
El nombre de la función o del método.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Uso básico de `uopz_unset_hook`

```php
<?php
function foo() {
    echo 'foo';
}
uopz_set_hook('foo', function () {echo 'bar';});
foo();
echo PHP_EOL;
uopz_unset_hook('foo');
foo();
?>

   
```

El ejemplo anterior mostrará:

    barfoo
    foo

## Véase también

uopz_set_hook

uopz_get_hook
