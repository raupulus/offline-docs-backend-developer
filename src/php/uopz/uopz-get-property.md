---
title: uopz_get_property
description: Devuelve el valor de una propiedad de clase o instancia
source_url: https://www.php.net/manual/es/function.uopz-get-property.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-get-property.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: 18f9cbcbc
order: 99300
---

uopz_get_property

Devuelve el valor de una propiedad de clase o instancia

## Descripción

```php
uopz_get_property(string $class, string $property): mixed
```php

```php
uopz_get_property(object $instance, string $property): mixed
```

Devuelve el valor de una propiedad de clase estática, si `class` es proporcionado, o el valor de una propiedad de instancia, si `instance` es proporcionado.

## Parámetros

`class`  
El nombre de la clase.

`instance`  
La instancia del objeto.

`property`  
El nombre de la propiedad.

## Valores devueltos

Devuelve el valor de la propiedad de clase o instancia, o `null` si la propiedad no está definida.

## Ejemplos

Uso básico de `uopz_get_property`

```php
<?php
class Foo {
    private static $staticBar = 10;
    private $bar = 100;
}
$foo = new Foo;
var_dump(uopz_get_property('Foo', 'staticBar'));
var_dump(uopz_get_property($foo, 'bar'));
?>

   
```

Resultado del ejemplo anterior es similar a:

    int(10)
    int(100)

## Véase también

uopz_set_property
