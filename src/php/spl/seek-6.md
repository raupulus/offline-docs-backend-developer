---
title: SplObjectStorage::seek
description: Busca un iterador en una posición
source_url: https://www.php.net/manual/es/splobjectstorage.seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 434557c58
order: 85210
---

SplObjectStorage::seek

Busca un iterador en una posición

## Descripción

```php
public SplObjectStorage::seek(int $offset): void
```php

Busca en una posición dada en el iterador.

## Parámetros

`offset`  
La posición a buscar.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una `OutOfBoundsException` si el `offset` no es accesible.

## Ejemplos

Ejemplo de SplObjectStorage::seek

Busca la posición 2 en el iterador.

```
<?php
class Test {
    public function __construct(public string $marker) {}
}

$a = new Test("a");
$b = new Test("b");
$c = new Test("c");

$storage = new SplObjectStorage();
$storage[$a] = "first";
$storage[$b] = "second";
$storage[$c] = "third";

$storage->seek(2);
var_dump($storage->key());
var_dump($storage->current());
?>

   
```php

El ejemplo anterior mostrará:

    int(2)
    object(Test)#3 (1) {
      ["marker"]=>
      string(1) "c"
    }

## Véase también

SeekableIterator
