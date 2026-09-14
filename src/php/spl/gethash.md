---
title: SplObjectStorage::getHash
description: Calcular un identificador único (hash) para los objetos contenidos
source_url: https://www.php.net/manual/es/splobjectstorage.gethash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/gethash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 85100
---

SplObjectStorage::getHash

Calcular un identificador único (hash) para los objetos contenidos

## Descripción

```php
public SplObjectStorage::getHash(object $object): string
```php

Este método calcula un identificador para los objetos añadidos a un objeto `SplObjectStorage`.

La implementación en la clase `SplObjectStorage` devuelve el mismo valor que la función `spl_object_hash`.

El objeto de almacenamiento nunca contendrá más de un objeto con el mismo identificador. Por lo tanto, se puede usar para implementar un conjunto (una colección de valores únicos) donde la cualidad de un objeto de ser único está determinada por el valor devuelto por esta función.

## Parámetros

`object`  
El objeto cuyo identificador va a ser calculado.

## Valores devueltos

Un `string` con el identificador calculado.

## Errores/Excepciones

Se lanza una excepción de tipo `RuntimeException` cuando el valor devuelto no es un `string`.

## Ejemplos

Ejemplo de `SplObjectStorage::getHash`

```
<?php
class OneSpecimenPerClassStorage extends SplObjectStorage {
    public function getHash($o) {
        return get_class($o);
    }
}
class A {}

$s = new OneSpecimenPerClassStorage;
$o1 = new stdClass;
$o2 = new stdClass;
$o3 = new A;

$s[$o1] = 1;
//$o2 es considerado igual a $o1, por lo que el valor es reemplazado
$s[$o2] = 2;
$s[$o3] = 3;

//estos objetos son considerados iguales a los objetos anteriores
//por lo que se pueden usar para acceder a los valores almacenados en ellos
$p1 = new stdClass;
$p2 = new A;
echo $s[$p1], "\n";
echo $s[$p2], "\n";
?>

    
```php

Resultado del ejemplo anterior es similar a:

    2
    3

## Véase también

`spl_object_hash`
