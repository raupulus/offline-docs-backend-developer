---
title: uopz_rename
description: Cambia el nombre de una función en tiempo de ejecución
source_url: https://www.php.net/manual/es/function.uopz-rename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-rename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99360
---

uopz_rename

Cambia el nombre de una función en tiempo de ejecución

> [!WARNING]
> Esta función ha sido *ELIMINADA* en PECL uopz 5.0.0.

## Descripción

```php
uopz_rename(string $function, string $rename): void
```php

```php
uopz_rename(string $class, string $function, string $rename): void
```

Cambia el nombre de la función `function` a `rename`.

> [!NOTE]
> Si ambas funciones existen, sus nombres serán intercambiados.

## Parámetros

`class`  
El nombre de la clase que contiene la función

`function`  
El nombre de una función existente

`rename`  
El nuevo nombre de la función

## Valores devueltos

## Ejemplos

Ejemplo con `uopz_rename`

```php
<?php
uopz_rename("strlen", "original_strlen");

echo original_strlen("Hello World");
?>

   
```

El ejemplo anterior mostrará:

    11

Ejemplo con `uopz_rename` y una clase

```php
<?php
class My {
    public function strlen($arg) {
        return strlen($arg);
    }
}

uopz_rename(My::class, "strlen", "original_strlen");

echo My::original_strlen("Hello World");
?>

   
```

El ejemplo anterior mostrará:

    11
