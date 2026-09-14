---
title: La clase SplFixedArray
source_url: https://www.php.net/manual/es/class.splfixedarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfixedarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 17ebcd2ea
order: 84850
---

## Introducción

la clase SplFixedArray proporciona la funcionalidad principal de un array. La principal diferencia entre SplFixedArray y un array normal de PHP es que la clase SplFixedArray es de longitud fija y sólo permite enteros dentro del rango de índices. La ventaja es que usa menos memoría que un `array` estándar.

## Sinopsis de la clase

SplFixedArray

implements

IteratorAggregate

ArrayAccess

Countable

JsonSerializable

Métodos

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Los accesos fuera de los límites en `SplFixedArray` ahora lanzan excepciones de tipo OutOfBoundsException en lugar de RuntimeException. Dado que OutOfBoundsException es una clase hija de RuntimeException, no se produce ningún cambio de comportamiento al intentar capturar esas excepciones. |
| 8.2.0 | Se han añadido los métodos mágicos SplFixedArray::\_\_serialize y SplFixedArray::\_\_unserialize a `SplFixedArray`. |
| 8.1.0 | `SplFixedArray` ahora implementa JsonSerializable. |
| 8.0.0 | `SplFixedArray` ahora implementa IteratorAggregate. Anteriormente, se implementaba Iterator en su lugar. |

## Ejemplos

Ejemplo de uso `SplFixedArray`

```php
<?php
// Inicializar el array con una longitud fija
$array = new SplFixedArray(5);

$array[1] = 2;
$array[4] = "foo";

var_dump($array[0]); // NULL
var_dump($array[1]); // int(2)

var_dump($array["4"]); // string(3) "foo"

// Aumentar el tamaño del array a 10
$array->setSize(10);

$array[9] = "asdf";

// Reducir el tamaño de un array a 2
$array->setSize(2);

// Las siguientes líneas lanzan una RuntimeException: Index invalid or out of range (Índice inválido o fuera de rango)
try {
    var_dump($array["non-numeric"]);
} catch(RuntimeException $re) {
    echo "RuntimeException: ".$re->getMessage()."\n";
}

try {
    var_dump($array[-1]);
} catch(RuntimeException $re) {
    echo "RuntimeException: ".$re->getMessage()."\n";
}

try {
    var_dump($array[5]);
} catch(RuntimeException $re) {
    echo "RuntimeException: ".$re->getMessage()."\n";
}
?>

     
```

El ejemplo anterior mostrará:

    NULL
    int(2)
    string(3) "foo"
    RuntimeException: Index invalid or out of range
    RuntimeException: Index invalid or out of range
    RuntimeException: Index invalid or out of range
