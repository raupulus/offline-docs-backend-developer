---
title: ArrayObject::natsort
description: Ordena los elementos con un tri natural
source_url: https://www.php.net/manual/es/arrayobject.natsort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/natsort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 52e3799c4
order: 81460
---

ArrayObject::natsort

Ordena los elementos con un tri natural

## Descripción

```php
public ArrayObject::natsort(): true
```php

Este método implementa un algoritmo de ordenación que coloca las strings alfanuméricas en el mismo orden que un humano utilizaría, manteniendo la correlación entre las claves y los valores. Esto se denomina tri natural. Por ejemplo, el tri natural se distingue del tri informático, tal como se utiliza en [ArrayObject::asort](#arrayobject.asort), como se ilustra a continuación.

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

Ejemplo con `ArrayObject::natsort`

```
<?php
$array = array("img12.png", "img10.png", "img2.png", "img1.png");

$arr1 = new ArrayObject($array);
$arr2 = clone $arr1;

$arr1->asort();
echo "Tri estándar\n";
var_dump($arr1);

$arr2->natsort();
echo "\nTri en orden natural\n";
var_dump($arr2);
?>

    
```php

El ejemplo anterior mostrará:

    Tri estándar
    object(ArrayObject)#1 (1) {
      ["storage":"ArrayObject":private]=>
      array(4) {
        [3]=>
        string(8) "img1.png"
        [1]=>
        string(9) "img10.png"
        [0]=>
        string(9) "img12.png"
        [2]=>
        string(8) "img2.png"
      }
    }

    Tri en orden natural
    object(ArrayObject)#2 (1) {
      ["storage":"ArrayObject":private]=>
      array(4) {
        [3]=>
        string(8) "img1.png"
        [2]=>
        string(8) "img2.png"
        [1]=>
        string(9) "img10.png"
        [0]=>
        string(9) "img12.png"
      }
    }

        

Para más información, véase el sitio de Martin Pool [`Natural Order String Comparison`](https://github.com/sourcefrog/natsort).

## Véase también

ArrayObject::asort, ArrayObject::ksort, ArrayObject::natcasesort, ArrayObject::uasort, ArrayObject::uksort, `natsort`
