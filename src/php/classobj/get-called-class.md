---
title: get_called_class
description: El nombre de la clase en "Late Static Binding"
source_url: https://www.php.net/manual/es/function.get-called-class.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/get-called-class.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: fe33a5685
order: 6770
---

get_called_class

El nombre de la clase en "Late Static Binding"

## Descripción

```php
get_called_class(): string
```php

Devuelve el nombre de la clase desde la cual se ha llamado a un método estático, tal como lo determina el Late Static Binding.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre de la clase.

## Errores/Excepciones

Si `get_called_class` se invoca desde fuera de una clase, se lanza una `Error`. Anteriormente a PHP 8.0.0, se generaba un error de nivel `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Invocar esta función desde fuera de una clase lanza ahora una `Error`. Anteriormente, se generaba un `E_WARNING` y la función devolvía `false`. `false`. |

## Ejemplos

Ejemplo con `get_called_class`

```
<?php

class foo {
    static public function test() {
        var_dump(get_called_class());
    }
}

class bar extends foo {
}

foo::test();
bar::test();

?>

    
```php

El ejemplo anterior mostrará:

    string(3) "foo"
    string(3) "bar"

## Véase también

`get_parent_class`, `get_class`, `is_subclass_of`
