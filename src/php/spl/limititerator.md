---
title: La clase LimitIterator
source_url: https://www.php.net/manual/es/class.limititerator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/limititerator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 4d17b7b49
order: 82600
---

## Introducción

La clase `LimitIterator` permite iterar sobre una parte limitada de entidades desde un `Iterator`.

## Sinopsis de la clase

LimitIterator

extends

IteratorIterator

Métodos

Métodos heredados

## Ejemplos

Ejemplo de uso de `LimitIterator`

```php
<?php

// Crear un iterador a limitar
$fruits = new ArrayIterator(array(
    'apple',
    'banana',
    'cherry',
    'damson',
    'elderberry'
));

// Bucle sobre los 3 primeros frutos únicamente
foreach (new LimitIterator($fruits, 0, 3) as $fruit) {
    var_dump($fruit);
}

echo "\n";

// Bucle desde el 3º fruto hasta el último
// Nota: la clave comienza en cero para apple
foreach (new LimitIterator($fruits, 2) as $fruit) {
    var_dump($fruit);
}

?>

    
```

El ejemplo anterior mostrará:

    string(5) "apple"
    string(6) "banana"
    string(6) "cherry"

    string(6) "cherry"
    string(6) "damson"
    string(10) "elderberry"
