---
title: QuickHashStringIntHash::loadFromString
description: Este método de fábrica crea un hash a partir de una cadena
source_url: https://www.php.net/manual/es/quickhashstringinthash.loadfromstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashstringinthash/loadfromstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67440
---

QuickHashStringIntHash::loadFromString

Este método de fábrica crea un hash a partir de una cadena

## Descripción

```php
public static QuickHashStringIntHash::loadFromString(string $contents, [int $size], [int $options]): QuickHashStringIntHash
```php

Este método de fábrica crea un nuevo hash a partir de una definición en una cadena. El formato es el mismo que el utilizado en "loadFromFile".

## Parámetros

`contents`  
La cadena que contiene un formato serializado del hash.

`size`  
La cantidad de listas de cubos a configurar. El número que se pasa será automáticamente redondeado a la siguiente potencia de dos. También se limita automáticamente de 4 a 4194304.

`options`  
Las mismas opciones que el constructor de la clase; excepto que la opción size es ignorada. Se calcula automáticamente para ser la misma que el número de entradas en el hash, redondeada a la potencia de dos más cercana con un límite máximo de 4194304.

## Valores devueltos

Devuelve un nuevo QuickHashStringIntHash.

## Ejemplos

Ejemplo de `QuickHashStringIntHash::loadFromString`

```
<?php
$contents = file_get_contents( dirname( __FILE__ ) . "/simple.hash.string" );
$hash = QuickHashStringIntHash::loadFromString(
    $contents,
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
