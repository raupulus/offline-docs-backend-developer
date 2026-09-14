---
title: interface_exists
description: Verifica si una interfaz ha sido definida
source_url: https://www.php.net/manual/es/function.interface-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/interface-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: 42bd1bfed
order: 6870
---

interface_exists

Verifica si una interfaz ha sido definida

## Descripción

```php
interface_exists(string $interface, [bool $autoload]): bool
```php

Verifica si una interfaz ha sido definida.

## Parámetros

`interface`  
El nombre de la interfaz

`autoload`  
Si se debe llamar a [autoload](#language.oop5.autoload) o no por omisión.

## Valores devueltos

Devuelve `true` si la interfaz proporcionada por el argumento `interface` ha sido definida, `false` en caso contrario.

## Ejemplos

Ejemplo con `interface_exists`

```
<?php
// Verifica si la interfaz existe antes de usarla
if (interface_exists('MyInterface')) {
    class MyClass implements MyInterface
    {
        // Métodos
    }
}

?>

    
```php

## Véase también

`get_declared_interfaces`, `class_implements`, `class_exists`, `enum_exists`
