---
title: get_parent_class
description: Devuelve el nombre de la clase padre de un objeto
source_url: https://www.php.net/manual/es/function.get-parent-class.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/get-parent-class.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: 7cec82fec
order: 6860
---

get_parent_class

Devuelve el nombre de la clase padre de un objeto

## Descripción

```php
get_parent_class([object $object_or_class]): string
```php

Obtiene el nombre de la clase padre para un objeto o una clase.

## Parámetros

`object_or_class`  
El objeto o el nombre de la clase probado.

## Valores devueltos

Devuelve el nombre de la clase padre de la cual `object_or_class` es una instancia o el nombre.

Si el objeto no tiene padre o si la clase proporcionada no existe, `false` será devuelto.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Llamar a `get_parent_class` sin argumento genera ahora un aviso `E_DEPRECATED` ; previamente, llamar a esta función dentro de una clase devolvía el nombre de esta clase. |
| 8.0.0 | El parámetro `object_or_class` acepta ahora solo objetos o nombres de clase válidos. |

## Ejemplos

Ejemplo con `get_parent_class`

```
<?php

class Papa {
    function __construct()
    {
    // un poco de código
    }
}

class Hijo extends Papa {
    function __construct()
    {
        echo "Soy el hijo de " , get_parent_class($this) , "\n";
    }
}

class Hijo2 extends papa {
    function __construct()
    {
        echo "Yo también soy el hijo de " , get_parent_class('hijo2') , "\n";
    }
}

$foo = new Hijo();
$bar = new Hijo2();

?>

    
```php

El ejemplo anterior mostrará:

    Soy el hijo de Papa
    Yo también soy el hijo de Papa

## Véase también

`get_class`, `is_subclass_of`, `class_parents`
