---
title: get_class
description: Devuelve el nombre de la clase de un objeto
source_url: https://www.php.net/manual/es/function.get-class.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/get-class.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: 4f36c26a7
order: 6800
---

get_class

Devuelve el nombre de la clase de un objeto

## Descripción

```php
get_class([object $object]): string
```php

Devuelve el nombre de la clase del objeto `obj`.

## Parámetros

`object`  
El objeto probado.

> [!NOTE]
> Pasar explícitamente `null` en `object` ya no es permitido desde PHP 7.2.0 y emite una `E_WARNING`. A partir de PHP 8.0.0, se emite una `TypeError` cuando `null` es utilizado.

## Valores devueltos

Devuelve el nombre de la clase de la cual `object` es una instancia.

Si `object` es una instancia de una clase que existe en un espacio de nombres, el nombre con el espacio de nombres de la clase será devuelto.

## Errores/Excepciones

Si `get_class` es llamada con algo que no sea un objeto, se levanta una `TypeError`. Anteriormente a PHP 8.0.0, se emitía una advertencia de nivel `E_WARNING`.

Si `get_class` es llamado sin argumento fuera de una clase, se levanta una `Error`. Anteriormente a PHP 8.0.0, se emitía una advertencia de nivel `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Llamar a `get_class` sin argumento ahora desencadena una advertencia `E_DEPRECATED`; previamente, llamar a esta función dentro de una clase devolvía el nombre de esa clase. |
| 8.0.0 | Llamar a esta función desde fuera de una clase ahora lanza una `Error`. Anteriormente, se generaba un `E_WARNING` y la función devolvía `false`. |
| 7.2.0 | Anteriormente a esta versión, el valor por omisión para `object` era `null` y tenía el mismo efecto que no pasar ningún valor. Ahora `null` ya no es el valor por omisión para `object`, y ya no es una entrada válida. |

## Ejemplos

Ejemplo con `get_class`

```
<?php

class foo {
    function name()
    {
        echo "Mi nombre es " , get_class($this) , "\n";
    }
}

// creación de un objeto
$bar = new foo();

// Llamada externa
echo "Su nombre es " , get_class($bar) , "\n";

// Llamada interna
$bar->name();

?>

    
```php

El ejemplo anterior mostrará:

    Su nombre es foo
    Mi nombre es foo

Uso de `get_class` en una superclase

```
<?php

abstract class bar {
    public function __construct()
    {
        var_dump(get_class($this));
        var_dump(get_class());
    }
}

class foo extends bar {
}

new foo;

?>

    
```php

El ejemplo anterior mostrará:

    string(3) "foo"
    string(3) "bar"

Uso de `get_class` con espacios de nombres de clase

```
<?php

namespace Foo\Bar;

class Baz {
    public function __construct()
    {

    }
}

$baz = new \Foo\Bar\Baz;

var_dump(get_class($baz));
?>

    
```php

El ejemplo anterior mostrará:

    string(11) "Foo\Bar\Baz"

## Véase también

`get_called_class`, `get_parent_class`, `gettype`, `get_debug_type`, `is_subclass_of`
