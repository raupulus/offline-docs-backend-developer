---
title: ArrayObject::asort
description: Ordena los elementos por valor
source_url: https://www.php.net/manual/es/arrayobject.asort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/asort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 2ca090342
order: 81360
---

ArrayObject::asort

Ordena los elementos por valor

## Descripción

```php
public ArrayObject::asort([int $flags]): true
```php

Ordena las entradas en orden ascendente, de tal manera que la correlación entre las claves y las valores sea conservada.

El uso principal es durante el ordenamiento de arrays asociativos donde el orden de los elementos es importante.

> [!NOTE]
> Si dos miembros se comparan como iguales, mantienen su orden original. Anterior a PHP 8.0.0, su orden relativo en el array ordenado no está definido.

## Parámetros

`flags`  
El segundo parámetro opcional `flags` puede ser utilizado para modificar el comportamiento de ordenación utilizando estos valores:

Tipo de banderas de ordenación:

- `SORT_REGULAR` - compara los elementos normalmente; los detalles son descritos en la sección de los [operadores de comparación](#language.operators.comparison)

- `SORT_NUMERIC` - compara los elementos numéricamente

- `SORT_STRING` - compara los elementos como strings

- `SORT_LOCALE_STRING` - compara los elementos como strings, basado en la configuración regional actual. Esto utiliza la configuración regional, que puede ser cambiada utilizando `setlocale`

- `SORT_NATURAL` - compara los elementos como strings utilizando el "orden natural" como `natsort`

- `SORT_FLAG_CASE` - puede ser combinado (OR a nivel de bits) con `SORT_STRING` o `SORT_NATURAL` para ordenar strings sin tener en cuenta la mayúscula/minúscula

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `ArrayObject::asort`

```
<?php
$fruits = array("d" => "limón", "a" => "naranja", "b" => "plátano", "c" => "manzana");
$fruitArrayObject = new ArrayObject($fruits);
$fruitArrayObject->asort();

foreach ($fruitArrayObject as $key => $val) {
    echo "$key = $val\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    b = plátano
    d = limón
    a = naranja
    c = manzana

        

Las frutas han sido ordenadas en orden alfabético, y su clave asociada ha sido conservada.

## Véase también

ArrayObject::ksort, ArrayObject::natsort, ArrayObject::natcasesort, ArrayObject::uasort, ArrayObject::uksort, `asort`
