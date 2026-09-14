---
title: ReflectionMethod::setAccessible
description: Define la accesibilidad del método
source_url: https://www.php.net/manual/es/reflectionmethod.setaccessible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionmethod/setaccessible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: e5c8e7add
order: 71090
---

ReflectionMethod::setAccessible

Define la accesibilidad del método

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] public ReflectionMethod::setAccessible(bool $accessible): void
```php

Activa la invocación de métodos protegidos y privados mediante el método ReflectionMethod::invoke.

> [!NOTE]
> A partir de PHP 8.1.0, la llamada a este método no tiene ningún efecto; todas las propiedades son accesibles por defecto.

## Parámetros

`accessible`  
`true` para permitir la accesibilidad, o `false`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Este método ha quedado obsoleto, ya que no tiene efecto. |
| 8.1.0 | La llamada a este método no tiene ningún efecto; todos los métodos son invocables por defecto. |

## Ejemplos

Definición de una clase simple

```
<?php
class MyClass
{
    private function foo()
    {
        return 'bar';
    }
}
$method = new ReflectionMethod("MyClass", "foo");
$method->setAccessible(true);
$obj = new MyClass();
echo $method->invoke($obj);
echo $obj->foo();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bar
    Fatal error: Uncaught Error: Call to private method MyClass::foo() from global scope in /in/qdaZS:16

## Véase también

ReflectionMethod::isPrivate, ReflectionMethod::isProtected
