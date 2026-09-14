---
title: enum_exists
description: Verifica si la enumeración está definida
source_url: https://www.php.net/manual/es/function.enum-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/enum-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_reviewed: false
translation_revision: 42bd1bfed
order: 6760
---

enum_exists

Verifica si la enumeración está definida

## Descripción

```php
enum_exists(string $enum, [bool $autoload]): bool
```php

Esta función verifica si la [enum](#language.enumerations) dada ha sido definida o no.

## Parámetros

`enum`  
El nombre de la enum. El nombre se toma en cuenta sin tener en cuenta las mayúsculas y minúsculas.

`autoload`  
Si se debe llamar [autoload](#language.oop5.autoload) por omisión.

## Valores devueltos

Retorna `true` si `enum` es una enum definida, `false` en caso contrario.

## Ejemplos

Ejemplo de `enum_exists`

```
<?php
// Verifica que la enum exista antes de intentar usarla
if (enum_exists(Suit::class)) {
    $myclass = Suit::Hearts;
}
?>

    
```php

## Véase también

`function_exists`, `class_exists`, `interface_exists`, `get_declared_classes`
