---
title: get_class_methods
description: Devuelve los nombres de los métodos de una clase
source_url: https://www.php.net/manual/es/function.get-class-methods.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/get-class-methods.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: 5ea9b57cb
order: 6780
---

get_class_methods

Devuelve los nombres de los métodos de una clase

## Descripción

```php
get_class_methods(object $object_or_class): array
```php

Devuelve los nombres de los métodos de una clase.

## Parámetros

`object_or_class`  
El nombre de la clase o una instancia de objeto

## Valores devueltos

Devuelve un array que contiene los nombres de los métodos de la clase `object_or_class`. En caso de error, se devuelve `null`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | El argumento `object_or_class` solo acepta ahora objetos o nombres de clase válidos. |

## Ejemplos

Ejemplo con `get_class_methods`

```
<?php

class myclass {
    // constructor
    function __construct()
    {
        return(true);
    }

    // método 1
    function myfunc1()
    {
        return(true);
    }

    // método 2
    function myfunc2()
    {
        return(true);
    }
}

$class_methods = get_class_methods('myclass');
// o
$class_methods = get_class_methods(new myclass());

foreach ($class_methods as $method_name) {
    echo "$method_name\n";
}

?>

    
```php

El ejemplo anterior mostrará:

    __construct
    myfunc1
    myfunc2

## Véase también

`get_class`, `get_class_vars`, `get_object_vars`
