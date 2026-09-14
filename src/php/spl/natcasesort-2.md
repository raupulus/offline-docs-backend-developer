---
title: ArrayObject::natcasesort
description: Ordena un array utilizando el ordenamiento natural sin distinción de
  mayúsculas y minúsculas
source_url: https://www.php.net/manual/es/arrayobject.natcasesort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/natcasesort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 52e3799c4
order: 81450
---

ArrayObject::natcasesort

Ordena un array utilizando el ordenamiento natural sin distinción de mayúsculas y minúsculas

## Descripción

```php
public ArrayObject::natcasesort(): true
```php

Este método es la versión insensible a la casilla de [ArrayObject::natsort](#arrayobject.natsort).

Este método implementa un algoritmo de ordenamiento que ordena las cadenas alfanuméricas de la misma forma en que lo haría un humano. Esto se describe como un ordenamiento natural.

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `ArrayObject::natcasesort`

```
<?php
$array = array('IMG0.png', 'img12.png', 'img10.png', 'img2.png', 'img1.png', 'IMG3.png');

$arr1 = new ArrayObject($array);
$arr2 = clone $arr1;

$arr1->asort();
echo "Ordenamiento estándar\n";
var_dump($arr1);

$arr2->natcasesort();
echo "\nOrdenamiento natural\n";
var_dump($arr2);
?>

    
```php

El ejemplo anterior mostrará:

    Ordenamiento estándar
    object(ArrayObject)#1 (1) {
      ["storage":"ArrayObject":private]=>
      array(6) {
        [0]=>
        string(8) "IMG0.png"
        [5]=>
        string(8) "IMG3.png"
        [4]=>
        string(8) "img1.png"
        [2]=>
        string(9) "img10.png"
        [1]=>
        string(9) "img12.png"
        [3]=>
        string(8) "img2.png"
      }
    }

    Ordenamiento natural
    object(ArrayObject)#2 (1) {
      ["storage":"ArrayObject":private]=>
      array(6) {
        [0]=>
        string(8) "IMG0.png"
        [4]=>
        string(8) "img1.png"
        [3]=>
        string(8) "img2.png"
        [5]=>
        string(8) "IMG3.png"
        [2]=>
        string(9) "img10.png"
        [1]=>
        string(9) "img12.png"
      }
    }

        

Para más información, ver la página de [comparación de strings en orden natural](https://github.com/sourcefrog/natsort) de Martin Pool.

## Véase también

ArrayObject::asort, ArrayObject::ksort, ArrayObject::natsort, ArrayObject::uasort, ArrayObject::uksort, `natcasesort`
