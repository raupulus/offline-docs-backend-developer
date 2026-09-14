---
title: QuickHashIntSet::exists
description: Este método verifica si una clave forma parte del conjunto
source_url: https://www.php.net/manual/es/quickhashintset.exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/quickhash/quickhashintset/exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: quickhash
translation_status: ready
translation_reviewed: false
translation_revision: bfe06c36e
order: 67170
---

QuickHashIntSet::exists

Este método verifica si una clave forma parte del conjunto

## Descripción

```php
public QuickHashIntSet::exists(int $key): bool
```php

Este método verifica si una entrada con la clave proporcionada existe en el conjunto.

## Parámetros

`key`  
La clave de la entrada a verificar si existe en el conjunto.

## Valores devueltos

Devuelve `true` cuando la entrada es encontrada, o `false` cuando la entrada no es encontrada.

## Ejemplos

Ejemplo de `QuickHashIntSet::exists`

```
<?php
//genera 200000 elementos
$array = range( 0, 199999 );
$existingEntries = array_rand( array_flip( $array ), 180000 );
$testForEntries = array_rand( array_flip( $array ), 1000 );
$foundCount = 0;

echo "Creando conjunto: ", microtime( true ), "\n";
$set = new QuickHashIntSet( 100000 );
echo "Añadiendo elementos: ", microtime( true ), "\n";
foreach( $existingEntries as $key )
{
     $set->add( $key );
}

echo "Realizando 1000 pruebas: ", microtime( true ), "\n";
foreach( $testForEntries as $key )
{
     $foundCount += $set->exists( $key );
}
echo "Hecho, $foundCount encontrados: ", microtime( true ), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Creando conjunto: 1263588703.0748
    Añadiendo elementos: 1263588703.0757
    Realizando 1000 pruebas: 1263588703.7851
    Hecho, 898 encontrados: 1263588703.7897
