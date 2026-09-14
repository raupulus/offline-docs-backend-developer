---
title: iterator_apply
description: Llama a una función para todos los elementos de un iterador
source_url: https://www.php.net/manual/es/function.iterator-apply.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/iterator-apply.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 60809ebcf
order: 82220
---

iterator_apply

Llama a una función para todos los elementos de un iterador

## Descripción

```php
iterator_apply(Traversable $iterator, callable $callback, [array $args]): int
```php

Llama a una función para todos los elementos de un iterador.

## Parámetros

`iterator`  
El objeto iterador a iterar.

`callback`  
La función de devolución de llamada a invocar para cada elemento. Esta función solo recibe los argumentos `args` proporcionados, por lo que es nullaria por defecto. Si `count($args) === 3`, por ejemplo, la función es ternaria.

> [!NOTE]
> La función debe devolver `true` para continuar iterando a través del iterador nombrado por el parámetro `iterator`.

`args`  
Un array `array` de argumentos; cada elemento de `args` se pasa a la función de devolución de llamada `callback` como argumento separado.

## Valores devueltos

Devuelve el número de iteraciones.

## Ejemplos

Ejemplo con `iterator_apply`

```
<?php
function print_caps(Iterator $iterator) {
    echo strtoupper($iterator->current()) . "\n";
    return TRUE;
}

$it = new ArrayIterator(array("Apples", "Bananas", "Cherries"));
iterator_apply($it, "print_caps", array($it));
?>

    
```php

El ejemplo anterior mostrará:

    APPLES
    BANANAS
    CHERRIES

## Véase también

`array_walk`
