---
title: uopz_flags
description: Recupera o define los flags de una función o clase
source_url: https://www.php.net/manual/es/function.uopz-flags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-flags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99250
---

uopz_flags

Recupera o define los flags de una función o clase

## Descripción

```php
uopz_flags(string $function, [int $flags]): int
```php

```php
uopz_flags(string $class, string $function, [int $flags]): int
```

Recupera o define los flags de una clase o entrada de función en tiempo de ejecución.

## Parámetros

`class`  
El nombre de la clase

`function`  
El nombre de la función. Si `class` es proporcionado y una `string` vacía es pasada como `function`, `uopz_flags` recupera o define los flags de la propia clase.

`flags`  
Un conjunto válido de flags ZEND_ACC\_. Si se omite, `uopz_flags` actúa como recuperador.

## Valores devueltos

Si se definen flags, devuelve los flags antiguos, de lo contrario, devuelve los flags actuales

## Errores/Excepciones

A partir de PHP 7.4.0, si el parámetro `flags` es proporcionado `uopz_flags` emite una `RuntimeException`, si [OPcache](#book.opcache) está activado, y la entrada de clase de `class` o la entrada de función `function` es inmutable.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL uopz 5.0.0 | El parámetro `flags` es ahora opcional. Anteriormente, `ZEND_ACC_FETCH` debía ser pasado para usar `uopz_flags` como recuperador. |

## Ejemplos

Ejemplo con `uopz_flags`

```php
<?php
class Test {
    public function method() {
        return __CLASS__;
    }
}

$flags = uopz_flags("Test", "method");

var_dump((bool) (uopz_flags("Test", "method") & ZEND_ACC_PRIVATE));
var_dump((bool) (uopz_flags("Test", "method") & ZEND_ACC_STATIC));

var_dump(uopz_flags("Test", "method", $flags|ZEND_ACC_STATIC|ZEND_ACC_PRIVATE));

var_dump((bool) (uopz_flags("Test", "method") & ZEND_ACC_PRIVATE));
var_dump((bool) (uopz_flags("Test", "method") & ZEND_ACC_STATIC));
?>

   
```

El ejemplo anterior mostrará:

    bool(false)
    bool(false)
    int(1234567890)
    bool(true)
    bool(true)

Transformar una clase final en no final

```php
<?php
final class MyClass
{
}

$flags = uopz_flags(MyClass::class, '');
uopz_flags(MyClass::class, '', $flags & ~ZEND_ACC_FINAL);
var_dump((new ReflectionClass(MyClass::class))->isFinal());
?>

   
```

El ejemplo anterior mostrará:

    bool(false)
