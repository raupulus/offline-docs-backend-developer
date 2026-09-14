---
title: QuickHashIntStringHash::loadFromFile
description: Este método de fábrica crea un hash a partir de un fichero
source_url: https://www.php.net/manual/es/quickhashintstringhash.loadfromfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintstringhash/loadfromfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67300
---

QuickHashIntStringHash::loadFromFile

Este método de fábrica crea un hash a partir de un fichero

## Descripción

```php
public static QuickHashIntStringHash::loadFromFile(string $filename, [int $size], [int $options]): QuickHashIntStringHash
```php

Este método de fábrica crea un nuevo hash a partir de un fichero de definición en el disco. El formato del fichero consiste en una firma `'QH\0x12\0'`, el número de elementos como un entero signado de 32 bits en Endianness del sistema, un entero no signado de 32 bits conteniendo el número de datos de elementos a seguir en caracteres. Estos datos de elementos contienen todas las strings. Después del encabezado y las strings, los elementos siguen por pares de dos enteros no signados de 32 bits donde el primero es la clave, y el segundo el índice en la string de datos de elementos. Un ejemplo podría ser:

Formato de fichero QuickHash IntString

    00000000  51 48 12 00 02 00 00 00  09 00 00 00 4f 4e 45 00  |QH..........ONE.|
    00000010  4e 49 4e 45 00 01 00 00  00 00 00 00 00 03 00 00  |NINE............|
    00000020  00 04 00 00 00                                    |.....|
    00000025

Formato de fichero QuickHash IntString

    firma del encabezado ('QH'; tipo de clave: 1; tipo de valor: 2; relleno: \0x00)
    00000000  51 48 12 00

    número de elementos:
    00000004  02 00 00 00

    longitud de valores de string (9 caracteres):
    00000008  09 00 00 00

    valores de string:
    0000000C  4f 4e 45 00 4e 49 4e 45  00

    string de datos:
    00000015  01 00 00 00 00 00 00 00  03 00 00 00 04 00 00 00

    clave/valor 1 (clave = 1, índice de string = 0 ("ONE")):
    01 00 00 00  00 00 00 00

    clave/valor 2 (clave = 3, índice de string = 4 ("NINE")):
    03 00 00 00  04 00 00 00

## Parámetros

`filename`  
El nombre del fichero desde el cual leer el hash.

`size`  
La cantidad de listas de cubos a configurar. El número que se pasa será automáticamente redondeado a la siguiente potencia de dos. También está automáticamente limitado de `4` a `4194304`.

`options`  
Las mismas opciones que el constructor de la clase; excepto que la opción size es ignorada. Se calcula automáticamente para ser la misma que el número de entradas en el hash, redondeada a la potencia de dos más cercana con un límite máximo de `4194304`.

## Valores devueltos

Devuelve un nuevo `QuickHashIntStringHash`.

## Ejemplos

Ejemplo de `QuickHashIntStringHash::loadFromFile`

```
<?php
$file = dirname( __FILE__ ) . "/simple.string.hash";
$hash = QuickHashIntStringHash::loadFromFile(
    $file,
    QuickHashIntStringHash::DO_NOT_USE_ZEND_ALLOC
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
