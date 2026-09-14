---
title: La clase SplStack
source_url: https://www.php.net/manual/es/class.splstack.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splstack.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 4d17b7b49
order: 85480
---

## Introducción

La clase SplStack proporciona la funcionalidad principal de una pila implementada mediante una lista doblemente enlazada estableciendo el modo iterador a `SplDoublyLinkedList::IT_MODE_LIFO`.

## Sinopsis de la clase

SplStack

extends

SplDoublyLinkedList

Constantes heredadas

Métodos heredados

## Ejemplos

Ejemplo de `SplStack`

```php
<?php
$q = new SplStack();
$q[] = 1;
$q[] = 2;
$q[] = 3;
foreach ($q as $elem)  {
 echo $elem."\n";
}
?>

     
```

El ejemplo anterior mostrará:

    3
    2
    1
