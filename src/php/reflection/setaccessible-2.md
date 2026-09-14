---
title: ReflectionProperty::setAccessible
description: Define la accesibilidad de una propiedad
source_url: https://www.php.net/manual/es/reflectionproperty.setaccessible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/setaccessible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: e5c8e7add
order: 71770
---

ReflectionProperty::setAccessible

Define la accesibilidad de una propiedad

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] public ReflectionProperty::setAccessible(bool $accessible): void
```php

Activa el acceso a una propiedad protegida o privada mediante los métodos ReflectionProperty::getValue y ReflectionProperty::setValue.

> [!NOTE]
> A partir de PHP 8.1.0, la llamada a este método no tiene ningún efecto; todas las propiedades son accesibles por omisión.

## Parámetros

`accessible`  
`true` para permitir el acceso, o `false`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Este método ha quedado obsoleto, ya que no tiene efecto. |
| 8.1.0 | La llamada a este método no tiene ningún efecto; todas las propiedades son accesibles por omisión. |

## Ejemplos

Definición de una clase simple

```
<?php
class MyClass
{
    private $foo = 'bar';
}
$property = new ReflectionProperty("MyClass", "foo");
$property->setAccessible(true);
$obj = new MyClass();
echo $property->getValue($obj);
echo $obj->foo;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bar
    Fatal error: Uncaught Error: Cannot access private property MyClass::$foo in /in/WJqTv:12

## Véase también

ReflectionProperty::isPrivate, ReflectionProperty::isProtected
