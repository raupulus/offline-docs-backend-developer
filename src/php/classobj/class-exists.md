---
title: class_exists
description: Verifica si una clase ha sido definida
source_url: https://www.php.net/manual/es/function.class-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/class-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: 42bd1bfed
order: 6750
---

class_exists

Verifica si una clase ha sido definida

## Descripción

```php
class_exists(string $class, [bool $autoload]): bool
```php

Esta función verifica si una clase dada ha sido definida.

## Parámetros

`class`  
El nombre de la clase. Se busca de manera insensible a la casse.

`autoload`  
Si se debe llamar a [autoload](#language.oop5.autoload) por omisión.

## Valores devueltos

Devuelve `true` si `class` es una clase definida, `false` en caso contrario.

## Ejemplos

Ejemplo con `class_exists`

```
<?php
// Verifica que la clase existe antes de usarla
if (class_exists('MyClass')) {
    $myclass = new MyClass();
}

?>

    
```php

Ejemplo con el argumento `autoload`

```
<?php
spl_autoload_register(function ($class_name) {
    include $class_name . '.php';

    // Verifica si el include ha declarado la clase
    if (!class_exists($class_name, false)) {
        throw new LogicException("No se puede cargar la clase: $class_name");
    }
});

if (class_exists(MyClass::class)) {
    $myclass = new MyClass();
}

?>

    
```php

## Véase también

`function_exists`, `enum_exists`, `interface_exists`, `get_declared_classes`
