---
title: uopz_function
description: Crea una función en tiempo de ejecución
source_url: https://www.php.net/manual/es/function.uopz-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99260
---

uopz_function

Crea una función en tiempo de ejecución

> [!WARNING]
> Esta función ha sido *ELIMINADA* en PECL uopz 5.0.0.

## Descripción

```php
uopz_function(string $function, Closure $handler, [int $modifiers]): void
```php

```php
uopz_function(string $class, string $function, Closure $handler, [int $modifiers]): void
```

Crea una función en tiempo de ejecución.

## Parámetros

`class`  
El nombre de la clase que debe recibir la nueva función

`function`  
El nombre de la función

`handler`  
La closure de la función

`modifiers`  
Los modificadores de la función; por omisión, copiados o ZEND_ACC_PUBLIC

## Valores devueltos

## Ejemplos

Ejemplo con `uopz_function`

```php
<?php
uopz_function("my_strlen", function($arg) {
    return strlen($arg);
});
echo my_strlen("Hello World");
?>

   
```

El ejemplo anterior mostrará:

    11

Ejemplo con `uopz_function` y una clase

```php
<?php
class My {}

uopz_function(My::class, "strlen", function($arg) {
    return strlen($arg);
}, ZEND_ACC_STATIC);

echo My::strlen("Hello World");
?>

   
```

El ejemplo anterior mostrará:

    11
