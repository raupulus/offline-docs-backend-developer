---
title: QuickHashIntSet::loadFromString
description: Este método de fábrica crea un conjunto a partir de una string
source_url: https://www.php.net/manual/es/quickhashintset.loadfromstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintset/loadfromstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67200
---

QuickHashIntSet::loadFromString

Este método de fábrica crea un conjunto a partir de una string

## Descripción

```php
public static QuickHashIntSet::loadFromString(string $contents, [int $size], [int $options]): QuickHashIntSet
```php

Este método de fábrica crea un nuevo conjunto a partir de una string. El formato del fichero consiste en enteros de 32 bits con signo empaquetados juntos en el orden de bytes que el sistema en el que se ejecuta el código utiliza.

## Parámetros

`contents`  
La string que contiene un formato serializado del conjunto.

`size`  
La cantidad de listas de cubos a configurar. El número que se pasa será automáticamente redondeado a la siguiente potencia de dos. También está automáticamente limitado de `4` a `4194304`.

`options`  
Las mismas opciones que el constructor de la clase; excepto que la opción de tamaño es ignorada. Se calcula automáticamente para ser el mismo que el número de entradas en el conjunto, redondeado a la potencia de dos más cercana con un límite máximo de `4194304`.

## Valores devueltos

Devuelve un nuevo `QuickHashIntSet`.

## Ejemplos

Ejemplo de `QuickHashIntSet::loadFromString`

```
<?php
$contents = file_get_contents( dirname( __FILE__ ) . "/simple.set" );
$set = QuickHashIntSet::loadFromString(
    $contents,
    QuickHashIntSet::DO_NOT_USE_ZEND_ALLOC
);
foreach( range( 0, 0x0f ) as $key )
{
    printf( "Key %3d (%2x) is %s\n",
        $key, $key,
        $set->exists( $key ) ? 'set' : 'unset'
    );
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Key   0 ( 0) is unset
    Key   1 ( 1) is set
    Key   2 ( 2) is set
    Key   3 ( 3) is set
    Key   4 ( 4) is unset
    Key   5 ( 5) is set
    Key   6 ( 6) is unset
    Key   7 ( 7) is set
    Key   8 ( 8) is unset
    Key   9 ( 9) is unset
    Key  10 ( a) is unset
    Key  11 ( b) is set
    Key  12 ( c) is unset
    Key  13 ( d) is set
    Key  14 ( e) is unset
    Key  15 ( f) is unset
