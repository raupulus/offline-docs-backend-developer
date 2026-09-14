---
title: QuickHashIntHash::loadFromFile
description: Este método de fábrica crea un hash a partir de un fichero
source_url: https://www.php.net/manual/es/quickhashinthash.loadfromfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashinthash/loadfromfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67070
---

QuickHashIntHash::loadFromFile

Este método de fábrica crea un hash a partir de un fichero

## Descripción

```php
public static QuickHashIntHash::loadFromFile(string $filename, [int $options]): QuickHashIntHash
```php

Este método de fábrica crea un nuevo hash a partir de un fichero de definición en disco. El formato de fichero consiste en una firma `'QH\0x11\0'`, el número de elementos como un entero de 32 bits con signo en Endianness de sistema, seguido de enteros de 32 bits con signo empaquetados juntos en el Endianness que el sistema en el que se ejecuta el código utiliza. Para cada elemento de hash, hay dos enteros de 32 bits con signo almacenados. El primero de cada elemento es la clave, y el segundo es el valor perteneciente a la clave. Un ejemplo podría ser:

Formato de fichero QuickHash IntHash

    00000000  51 48 11 00 02 00 00 00  01 00 00 00 01 00 00 00  |QH..............|
    00000010  03 00 00 00 09 00 00 00                           |........|
    00000018

Formato de fichero QuickHash IntHash

    firma de encabezado ('QH'; tipo de clave: 1; tipo de valor: 1; relleno: \0x00)
    00000000  51 48 11 00

    número de elementos:
    00000004  02 00 00 00

    cadena de datos:
    00000000  01 00 00 00 01 00 00 00  03 00 00 00 09 00 00 00

    clave/valor 1 (clave = 1, valor = 1)
    01 00 00 00  01 00 00 00

    clave/valor 2 (clave = 3, valor = 9)
    03 00 00 00  09 00 00 00

## Parámetros

`filename`  
El nombre del fichero desde el cual leer el hash.

`options`  
Las mismas opciones que el constructor de la clase; con la excepción de la opción size que es ignorada. Se calcula automáticamente para ser la misma que el número de entradas en el hash, redondeada a la potencia de dos más cercana con un límite máximo de `4194304`.

## Valores devueltos

Devuelve un nuevo `QuickHashIntHash`.

## Ejemplos

Ejemplo de `QuickHashIntHash::loadFromFile`

```
<?php
$file = dirname( __FILE__ ) . "/simple.hash";
$hash = QuickHashIntHash::loadFromFile(
    $file,
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
