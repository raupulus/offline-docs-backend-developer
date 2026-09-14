---
title: Ejemplos
source_url: https://www.php.net/manual/es/quickhash.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: 12ff79670
order: 67000
---

## Ejemplos

Ejemplo de Quickhash

```php
<?php
$set = new QuickHashIntSet( 1024, QuickHashIntSet::CHECK_FOR_DUPES );
$set->add( 1 );
$set->add( 3 );

var_dump( $set->exists( 3 ) );
var_dump( $set->exists( 4 ) );

$set->saveToFile( "/tmp/test-set.set" );

$newSet = QuickHashIntSet::loadFromFile(
    "/tmp/test-set.set"
);

var_dump( $newSet->exists( 3 ) );
var_dump( $newSet->exists( 4 ) );
?>

  
```

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(false)
    bool(true)
    bool(false)

Ejemplo de ArrayAccess Quickhash

```php
<?php
$hash = new QuickHashIntHash( 64 );

// Añade y actualiza las entradas de hash.
$hash[3] = 145926;
$hash[3] = 1415926;
$hash[2] = 72;

// Verifica si las claves existen
var_dump( isset( $hash[3] ) );

// Elimina las entradas de hash
unset( $hash[2] );

// Recupera el valor almacenado para un hash
echo $hash[3], "\n";
?>

  
```

Resultado del ejemplo anterior es similar a:

    bool(true)
    1415926

Ejemplo de Iterator Quickhash

```php
<?php
$hash = new QuickHashIntHash( 64 );

// Añade entradas de hash.
$hash[1] = 145926;
$hash[2] = 1415926;
$hash[3] = 72;
$hash[4] = 712314;
$hash[5] = -4234;

foreach( $hash as $key => $value )
{
    echo $key, ' => ', $value, "\n";
}
?>

  
```

Resultado del ejemplo anterior es similar a:

    5 => -4234
    4 => 712314
    1 => 145926
    2 => 1415926
    3 => 72

Ejemplo de valor de string Quickhash

```php
<?php
$hash = new QuickHashIntStringHash( 64 );

// Añade entradas de hash.
$hash[1] = "one million four hundred fifteen thousand nine hundred twenty six";
$hash->add( 2, "one more" );

foreach( $hash as $key => $value )
{
    echo $key, ' => ', $value, "\n";
}
?>

  
```

Resultado del ejemplo anterior es similar a:

    1 => one million four hundred fifteen thousand nine hundred twenty six
    2 => one more
