---
title: La clase WeakMap
source_url: https://www.php.net/manual/es/class.weakmap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/weakmap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 4320
---

## Introducción

Un `WeakMap` es un array asociativo (o diccionario) que acepta objetos como claves. Sin embargo, a diferencia del similar `SplObjectStorage`, un objeto en una clave de `WeakMap` no contribuye al número de referencias del objeto. En otras palabras, si, en un momento dado, la única referencia restante a un objeto es la clave de un `WeakMap`, el objeto será recolectado y eliminado del `WeakMap`. Su principal caso de uso es la construcción de cachés de datos derivados de un objeto que no necesitan ser conservados más tiempo que el objeto.

`WeakMap` implementa ArrayAccess, Traversable (vía IteratorAggregate), y Countable, de modo que, en la mayoría de los casos, puede ser utilizado de la misma manera que un array asociativo.

## Sinopsis de la clase

final

WeakMap

implements

ArrayAccess

Countable

IteratorAggregate

Métodos

## Ejemplos

Ejemplo de uso de un `Weakmap`

```php
      
<?php
$wm = new WeakMap();

$o = new stdClass;

class A {
    public function __destruct() {
        echo "Dead!\n";
    }
}

$wm[$o] = new A;

var_dump(count($wm));
echo "Unsetting...\n";
unset($o);
echo "Done\n";
var_dump(count($wm));

     
```

El ejemplo anterior mostrará:

          
    int(1)
    Unsetting...
    Dead!
    Done
    int(0)
