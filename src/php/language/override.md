---
title: La clase Override
source_url: https://www.php.net/manual/es/class.override.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/attributes/override.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 77325b622
order: 2960
---

## Introducción

Este atributo se utiliza para indicar que un método o una propiedad está destinado a sobrescribir un método o una propiedad de una clase padre o que implementa un método o una propiedad definido en una interfaz.

Si no existe ningún método o propiedad con el mismo nombre en una clase padre o en una interfaz implementada, se emitirá un error de compilación.

El atributo solo puede ser utilizado con el método [\_\_construct()](#object.construct), que está excluido de las verificaciones de firma.

## Sinopsis de la clase

\#\[\Attribute\]

final

Override

Métodos

## Historial de cambios

| Versión | Descripción                                  |
|---------|----------------------------------------------|
| 8.5.0   | `Override` puede ser aplicado a propiedades. |

## Ejemplos

Uso con métodos

```php
<?php

class Base {
    protected function foo(): void {}
}

final class Extended extends Base {
    #[\Override]
    protected function boo(): void {}
}

?>

    
```

Resultado del ejemplo anterior en PHP 8.3 es similar a:

    Fatal error: Extended::boo() has #[\Override] attribute, but no matching parent method exists

Uso con propiedades

```php
<?php

class Base {
    protected string $foo;
}

final class Extended extends Base {
    #[\Override]
    protected string $boo;
}

?>

    
```

La salida del ejemplo anterior en PHP 8.5 es similar a:

    Fatal error: Extended::$boo has #[\Override] attribute, but no matching parent property exists

## Véase también

Visión general de los atributos
