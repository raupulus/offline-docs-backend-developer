---
title: uopz_set_return
description: Proporciona un valor de retorno para una función existente
source_url: https://www.php.net/manual/es/function.uopz-set-return.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-set-return.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99410
---

uopz_set_return

Proporciona un valor de retorno para una función existente

## Descripción

```php
uopz_set_return(string $function, mixed $value, [bool $execute]): bool
```php

```php
uopz_set_return(string $class, string $function, mixed $value, [bool $execute]): bool
```

Establece el valor de retorno de la `function` a `value`. Si `value` es una función anónima y `execute` está establecido, la función anónima se ejecutará en lugar de la función original. Es posible llamar a la función original desde la función anónima.

> [!NOTE]
> Esta función reemplaza a uopz_rename.

## Parámetros

`class`  
El nombre de la clase que contiene la función

`function`  
El nombre de una función existente

`value`  
El valor que la función debe devolver. Si se proporciona una función anónima y el flag de ejecución está establecido, la función anónima se ejecutará en lugar de la función original.

`execute`  
Si es verdadero, y se ha proporcionado una función anónima como valor, la función anónima se ejecutará en lugar de la función original.

## Valores devueltos

Devuelve `true` en caso de éxito, de lo contrario `false`.

## Ejemplos

Ejemplo de `uopz_set_return`

```php
<?php
uopz_set_return("strlen", 42);
echo strlen("Banana");
?>

   
```

El ejemplo anterior mostrará:

    42

Ejemplo de `uopz_set_return`

```php
<?php
uopz_set_return("strlen", function($str) { return strlen($str) * 2; }, true );
echo strlen("Banana");
?>

   
```

El ejemplo anterior mostrará:

    12

Ejemplo de `uopz_set_return` con una clase

```php
<?php
class My {
    public static function strlen($arg) {
        return strlen($arg);
    }
}
uopz_set_return(My::class, "strlen", function($str) { return strlen($str) * 2; }, true );
echo My::strlen("Banana");
?>

   
```

El ejemplo anterior mostrará:

    12
