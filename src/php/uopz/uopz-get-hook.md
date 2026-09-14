---
title: uopz_get_hook
description: Devuelve el hook previamente definido en una función o método
source_url: https://www.php.net/manual/es/function.uopz-get-hook.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-get-hook.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: '475439775'
order: 99280
---

uopz_get_hook

Devuelve el hook previamente definido en una función o método

## Descripción

```php
uopz_get_hook(string $function): Closure
```php

```php
uopz_get_hook(string $class, string $function): Closure
```

Devuelve el hook previamente definido en una función o método.

## Parámetros

`class`  
El nombre de la clase.

`function`  
El nombre de la función o método.

## Valores devueltos

Devuelve el hook previamente definido en una función o método, o `null` si ningún hook ha sido definido.

## Ejemplos

Uso básico de `uopz_get_hook`

```php
<?php
function foo() {
    echo 'foo';
}
uopz_set_hook('foo', function () {echo 'bar';});
var_dump(uopz_get_hook('foo'));
?>

   
```

Resultado del ejemplo anterior es similar a:

    object(Closure)#2 (0) {
    }

## Véase también

uopz_set_hook

uopz_unset_hook
