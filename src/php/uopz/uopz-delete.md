---
title: uopz_delete
description: Elimina una función
source_url: https://www.php.net/manual/es/function.uopz-delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99230
---

uopz_delete

Elimina una función

> [!WARNING]
> Esta función ha sido *ELIMINADA* en PECL uopz 5.0.0.

## Descripción

```php
uopz_delete(string $function): void
```php

```php
uopz_delete(string $class, string $function): void
```

Elimina una función o método.

## Parámetros

`class`  
El nombre de la clase.

`function`  
El nombre de la función o método.

## Valores devueltos

## Ejemplos

Ejemplo con `uopz_delete`

```php
<?php
uopz_delete("strlen");

echo strlen("Hello World");
?>

   
```

Resultado del ejemplo anterior es similar a:

    PHP Fatal error: Call to undefined function strlen() in /path/to/script.php on line 4

Ejemplo con `uopz_delete` y una clase

```php
<?php
class My {
    public static function strlen($arg) {
        return strlen($arg);
    }
}

uopz_delete(My::class, "strlen");

echo My::strlen("Hello World");
?>

   
```

Resultado del ejemplo anterior es similar a:

    PHP Fatal error: Call to undefined method My::strlen() in /path/to/script.php on line 10
