---
title: array_diff
description: Calcula la diferencia entre arrays
source_url: https://www.php.net/manual/es/function.array-diff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-diff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 2e60c5134
order: 5250
---

array_diff

Calcula la diferencia entre arrays

## Descripción

```php
array_diff(array $array, array ...$arrays): array
```php

`array_diff` compara el array `array` con uno o más arrays y devuelve los valores del array `array` que no están presentes en los otros arrays.

## Parámetros

`array`  
El array desde el cual comparar

`arrays`  
Arrays a comparar

## Valores devueltos

Devuelve un `array` que contiene todas las entidades del array `array` que no están presentes en ninguno de los otros arrays. Las claves del array `array` son preservadas.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función puede ser llamada ahora con un solo parámetro. Anteriormente, al menos dos parámetros eran necesarios. |

## Ejemplos

Ejemplo con `array_diff`

```
<?php
$array1 = array("a" => "green", "red", "blue", "red");
$array2 = array("b" => "green", "yellow", "red");
$result = array_diff($array1, $array2);

print_r($result);
?>

    
```php

Los valores múltiples en `array1` serán todos tratados de la misma forma. Esto mostrará:

    Array
    (
        [1] => blue
    )

Dos elementos son considerados iguales si y solo si `(string) $elem1 === (string) $elem2` ; es decir, cuando la [representación de string ](#language.types.string.casting) es la misma.

Ejemplo con la función `array_diff` con tipos que no coinciden

```
     
<?php
// Esto generará una advertencia ya que un array no puede ser convertido a string.
$source = [1, 2, 3, 4];
$filter = [3, 4, [5], 6];
$result = array_diff($source, $filter);

// Mientras que esto es correcto, ya que los objetos pueden ser convertidos a string.
class S {
  private $v;

  public function __construct(string $v) {
    $this->v = $v;
  }

  public function __toString() {
    return $this->v;
  }
}

$source = [new S('a'), new S('b'), new S('c')];
$filter = [new S('b'), new S('c'), new S('d')];

$result = array_diff($source, $filter);

// $result ahora contiene una instancia de S('a');
var_dump($result);
?>

    
```php

Para utilizar una función de comparación alternativa, consulte la función `array_udiff`.

## Notas

> [!NOTE]
> Tenga en cuenta que esta función solo verifica una dimensión de un array multidimensional. Por supuesto, se pueden verificar dimensiones más profundas utilizando `array_diff($array1[0], $array2[0]);`.

## Véase también

`array_diff_assoc`, `array_udiff`, `array_intersect`, `array_intersect_assoc`
