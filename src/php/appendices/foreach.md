---
title: Cambios relacionados con foreach
source_url: https://www.php.net/manual/es/migration70.incompatible.foreach.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/incompatible/foreach.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 285e7e31e
order: 300
---

## Cambios relacionados con [`foreach`](#control-structures.foreach)

Se han realizado cambios menores en el comportamiento de la estructura de control [`foreach`](#control-structures.foreach), principalmente en la gestión del puntero interno del array y la modificación del array mientras se recorre.

### [`foreach`](#control-structures.foreach) ya no modifica el puntero interno del array

Antes de PHP 7, el puntero interno del array se modificaba mientras se recorría un array con [`foreach`](#control-structures.foreach). Esto ya no es así, como se muestra en el siguiente ejemplo:

```php
<?php
$array = [0, 1, 2];
foreach ($array as &$val) {
    var_dump(current($array));
}
?>

   
```

Resultado del ejemplo anterior en PHP 5:

    int(1)
    int(2)
    bool(false)

       

Resultado del ejemplo anterior en PHP 7:

    int(0)
    int(0)
    int(0)

### [`foreach`](#control-structures.foreach) por valor trabaja sobre una copia del array

Al utilizar el modo predeterminado (por valor), [`foreach`](#control-structures.foreach) ahora trabaja sobre una copia del array en lugar del array original. Esto significa que los cambios realizados en el array mientras se recorre no afectarán los valores que se están iterando.

### Se ha mejorado el comportamiento de [`foreach`](#control-structures.foreach) por referencia

Al recorrer un array por referencia, [`foreach`](#control-structures.foreach) ahora identifica mejor los cambios realizados en el array durante la iteración. Por ejemplo, si se añaden valores a un array mientras se recorre, estos nuevos valores también se iterarán:

```php
<?php
$array = [0];
foreach ($array as &$val) {
    var_dump($val);
    $array[1] = 1;
}
?>

   
```

Resultado del ejemplo anterior en PHP 5:

    int(0)

       

Resultado del ejemplo anterior en PHP 7:

    int(0)
    int(1)

### Iteración de objetos no-`Traversable`

La iteración de un objeto no-`Traversable` ahora es idéntica a la iteración de un array por referencia. Como resultado, la [mejora en el comportamiento cuando se modifica un array durante su iteración](#migration70.incompatible.foreach.by-ref) también se aplica cuando se añaden o eliminan propiedades de un objeto.
