---
title: La clase SplObjectStorage
source_url: https://www.php.net/manual/es/class.splobjectstorage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: dc6fe404e
order: 85260
---

## Introducción

La clase `SplObjectStorage` proporciona un mapa de objetos o de datos, o bien, ignorando los índices, un conjunto de objetos. Este doble propósito es útil en numerosas situaciones, donde es necesario identificar de manera única objetos.

## Sinopsis de la clase

SeekableSplObjectStorage

implements

Countable

Iterator

Serializable

ArrayAccess

Métodos

## Ejemplos

Ejemplo con `SplObjectStorage`, en forma de conjunto de objetos

```php
<?php
// Un conjunto de objetos
$s = new SplObjectStorage();

$o1 = new stdClass;
$o2 = new stdClass;
$o3 = new stdClass;

$s->attach($o1);
$s->attach($o2);

var_dump($s->contains($o1));
var_dump($s->contains($o2));
var_dump($s->contains($o3));

$s->detach($o2);

var_dump($s->contains($o1));
var_dump($s->contains($o2));
var_dump($s->contains($o3));
?>

    
```

El ejemplo anterior mostrará:

    bool(true)
    bool(true)
    bool(false)
    bool(true)
    bool(false)
    bool(false)

Ejemplo con `SplObjectStorage`, en forma de mapa

```php
<?php
// Un mapa de objetos
$s = new SplObjectStorage();

$o1 = new stdClass;
$o2 = new stdClass;
$o3 = new stdClass;

$s[$o1] = "data for object 1";
$s[$o2] = array(1,2,3);

if (isset($s[$o2])) {
    var_dump($s[$o2]);
}
?>

    
```

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Implementa SeekableIterator, anteriormente solo se implementaba la interfaz Iterator. |
