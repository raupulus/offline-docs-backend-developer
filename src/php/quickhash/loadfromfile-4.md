---
title: QuickHashStringIntHash::loadFromFile
description: Este método de fábrica crea un hash a partir de un fichero
source_url: https://www.php.net/manual/es/quickhashstringinthash.loadfromfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashstringinthash/loadfromfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67430
---

QuickHashStringIntHash::loadFromFile

Este método de fábrica crea un hash a partir de un fichero

## Descripción

```php
public static QuickHashStringIntHash::loadFromFile(string $filename, [int $size], [int $options]): QuickHashStringIntHash
```php

Este método de fábrica crea un nuevo hash a partir de un fichero de definición en el disco. El formato del fichero se compone de una firma `'QH\0x21\0'`, del número de elementos como entero signado de 32 bits en Endianness del sistema, un entero no signado de 32 bits conteniendo el número de datos de elementos a seguir en caracteres. Estos datos de elementos contienen todas las strings. Sigue otro entero signado de 32 bits conteniendo el número de listas de cubos. Después del encabezado y las strings, los elementos siguen. Están ordenados por lista de cubos de manera que las claves no deben ser hasheadas para restaurar el hash. Para cada lista de cubos, la siguiente información es almacenada (todas en enteros de 32 bits): el índice de la lista de cubos, el número de elementos en esta lista, y luego por parejas de dos enteros no signados de 32 bits los elementos, donde el primero es el índice en la lista de strings conteniendo las claves, y el segundo el valor. Un ejemplo podría ser:

Formato de fichero QuickHash StringIntHash

    00000000  51 48 21 00 02 00 00 00  09 00 00 00 40 00 00 00  |QH!.........@...|
    00000010  4f 4e 45 00 4e 49 4e 45  00 07 00 00 00 01 00 00  |ONE.NINE........|
    00000020  00 00 00 00 00 01 00 00  00 2f 00 00 00 01 00 00  |........./......|
    00000030  00 04 00 00 00 03 00 00  00                       |.........|
    00000039

Formato de fichero QuickHash IntHash

    firma del encabezado ('QH'; tipo de clave: 2; tipo de valor: 1; relleno: \0x00)
    00000000  51 48 21 00

    número de elementos:
    00000004  02 00 00 00

    longitud de valores de string (9 caracteres):
    00000008  09 00 00 00

    número de listas de cubos de hash (esto se configura para hashes como argumento al
    constructor normalmente, 64 en este caso):
    0000000C  40 00 00 00

    valores de string:
    00000010  4f 4e 45 00 4e 49 4e 45  00

    listas de cubos:
      lista de cubos 1 (con clave 7, y 1 elemento):
        encabezado:
        07 00 00 00 01 00 00 00
        elementos (índice de clave: 0 ('ONE'), valor = 0):
        00 00 00 00 01 00 00 00
      lista de cubos 2 (con clave 0x2f, y 1 elemento):
        encabezado:
        2f 00 00 00 01 00 00 00
        elementos (índice de clave: 4 ('NINE'), valor = 3):
        04 00 00 00 03 00 00 00

## Parámetros

`filename`  
El nombre del fichero desde el cual leer el hash.

`size`  
El número de listas de cubos a configurar. El número que se pasa será automáticamente redondeado a la siguiente potencia de dos. También es automáticamente limitado de `4` a `4194304`.

`options`  
Las mismas opciones que el constructor de la clase; excepto que la opción size es ignorada. Se lee desde el formato de fichero (a diferencia de las clases `QuickHashIntHash` y `QuickHashIntStringHash`, donde se calcula automáticamente a partir del número de entradas en el hash.)

## Valores devueltos

Devuelve un nuevo `QuickHashStringIntHash`.

## Ejemplos

Ejemplo de `QuickHashStringIntHash::loadFromFile`

```
<?php
$file = dirname( __FILE__ ) . "/simple.hash.string";
$hash = QuickHashStringIntHash::loadFromFile(
    $file,
    QuickHashStringIntHash::DO_NOT_USE_ZEND_ALLOC
);
foreach( range( 0, 0x0f ) as $key )
{
    $i = 48712 + $key * 1631;
    $k = base_convert( $i, 10, 36 );
    echo $k, ' => ', $hash->get( $k ), "\n";
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    11l4 => 48712
    12uf => 50343
    143q => 51974
    15d1 => 53605
    16mc => 55236
    17vn => 56867
    194y => 58498
    1ae9 => 60129
    1bnk => 61760
    1cwv => 63391
    1e66 => 65022
    1ffh => 66653
    1gos => 68284
    1hy3 => 69915
    1j7e => 71546
    1kgp => 73177
