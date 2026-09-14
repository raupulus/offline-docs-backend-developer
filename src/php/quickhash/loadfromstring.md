---
title: QuickHashIntHash::loadFromString
description: Este método de fábrica crea un hash a partir de una string
source_url: https://www.php.net/manual/es/quickhashinthash.loadfromstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashinthash/loadfromstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67080
---

QuickHashIntHash::loadFromString

Este método de fábrica crea un hash a partir de una string

## Descripción

```php
public static QuickHashIntHash::loadFromString(string $contents, [int $options]): QuickHashIntHash
```php

Este método de fábrica crea un nuevo hash a partir de una definición en una string. El formato de fichero consiste en enteros de 32 bits con signo empaquetados juntos en el Endianness que el sistema en el que se ejecuta el código utiliza. Para cada elemento de hash, hay dos enteros de 32 bits con signo almacenados juntos. El primero de cada elemento es la clave, y el segundo es el valor perteneciente a la clave.

## Parámetros

`contents`  
La string que contiene un formato serializado del hash.

`options`  
Las mismas opciones que el constructor de la clase; con la excepción de la opción size que es ignorada. Se calcula automáticamente para ser la misma que el número de entradas en el hash, redondeada a la potencia de dos más cercana con un límite máximo de `4194304`.

## Valores devueltos

Devuelve un nuevo `QuickHashIntHash`.

## Ejemplos

Ejemplo de `QuickHashIntHash::loadFromString`

```
<?php
$contents = file_get_contents( dirname( __FILE__ ) . "/simple.hash" );
$hash = QuickHashIntHash::loadFromString(
    $contents,
    QuickHashIntHash::DO_NOT_USE_ZEND_ALLOC
);
foreach( range( 0, 0x0f ) as $key )
{
    printf( "Key %3d (%2x) is %s\n",
        $key, $key,
        $hash->exists( $key ) ? 'set' : 'unset'
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
