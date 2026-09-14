---
title: uopz_set_property
description: Establece el valor de una propiedad de clase existente o de instancia
source_url: https://www.php.net/manual/es/function.uopz-set-property.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-set-property.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: 415ff8a05
order: 99400
---

uopz_set_property

Establece el valor de una propiedad de clase existente o de instancia

## Descripción

```php
uopz_set_property(string $class, string $property, mixed $value): void
```php

```php
uopz_set_property(object $instance, string $property, mixed $value): void
```

Establece el valor de una propiedad de clase estática existente, si se proporciona `class`, o el valor de una propiedad de instancia (sin importar si la propiedad de instancia ya existe), si se proporciona `instance`.

## Parámetros

`class`  
El nombre de la clase.

`instance`  
La instancia del objeto.

`property`  
El nombre de la propiedad.

`value`  
El valor a asignar a la propiedad.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Uso básico de `uopz_set_property`

```php
<?php
class Foo {
   private static $staticBar;
   private $bar;
   public static function testStaticBar() {
      return self::$staticBar;
   }
   public function testBar() {
      return $this->bar;
   }
}
$foo = new Foo;
uopz_set_property('Foo', 'staticBar', 10);
uopz_set_property($foo, 'bar', 100);
var_dump(Foo::testStaticBar());
var_dump($foo->testBar());
?>

   
```

El ejemplo anterior mostrará:

    int(10)

## Véase también

uopz_get_property
