---
title: unpack
description: Desempaqueta datos desde una cadena binaria
source_url: https://www.php.net/manual/es/function.unpack.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/unpack.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 5fabd0788
order: 47290
---

unpack

Desempaqueta datos desde una cadena binaria

## Descripción

```php
unpack(string $format, string $string, [int $offset]): array
```php

Desempaqueta los datos `data` desde una cadena binaria con el formato `format`.

Los datos desempaquetados se almacenan en un array. Para ello, debe asignarse un nombre a cada formato utilizado y separarlos con una barra (/). Si se proporciona un argumento de repetición, entonces cada una de las claves del array tendrá un número de secuencia detrás del nombre proporcionado.

Se han realizado modificaciones para alinear el comportamiento de esta función con Perl : El código "a" ya no elimina los bytes NULL finales., El código "A" ahora elimina todos los espacios en blanco ASCII finales (espacio, tabulación, nuevas líneas, retorno de carro, y bytes NULL)., Se ha añadido el código "Z" para las cadenas rellenas con caracteres NULL, y elimina los bytes NULL finales.

## Parámetros

`format`  
Consulte la función `pack` para una explicación de los códigos de formato.

`string`  
Los datos empaquetados.

`offset`  
La posición donde comenzar el desempaquetado.

## Valores devueltos

Devuelve un array asociativo que contiene los elementos desempaquetados de una cadena binaria, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | Los tipos `float` y `double` soportan tanto la orientación Big Endian como Little Endian. |
| 7.1.0 | Se ha añadido el argumento opcional `offset`. |

## Ejemplos

Ejemplo con `unpack`

```
<?php
$binarydata = "\x04\x00\xa0\x00";
$array = unpack("cchars/nint", $binarydata);
print_r($array);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [chars] => 4
        [int] => 160
    )

Ejemplo con `unpack` y un argumento de repetición

```
 
 <?php
$binarydata = "\x04\x00\xa0\x00";
$array = unpack("c2chars/nint", $binarydata);
print_r($array);
?>
 
     
```php

El ejemplo anterior mostrará:

    Array
    (
        [chars1] => 4
        [chars2] => 0
        [int] => 40960
    )

## Notas

> [!CAUTION]
> Debe tenerse en cuenta que PHP maneja los valores internamente en forma firmada. Si se desempaqueta un valor que es tan grande como el tamaño utilizado internamente por PHP, el resultado será un número negativo, incluso si se ha desempaquetado con la opción `"no firmado"`.

> [!CAUTION]
> Si no se nombra un elemento, se utilizan los índices numéricos a partir de `1`. Tenga en cuenta que si tiene más de un elemento sin nombre, algunos datos se sobrescriben porque la numeración se reinicia a partir de `1` para cada elemento.
>
> <div class="example">
>
> <div class="title">
>
> Ejemplo con `unpack` con claves no nombradas
>
> </div>
>
> ```
> <?php
> $binarydata = "\x32\x42\x00\xa0";
> $array = unpack("c2/n", $binarydata);
> var_dump($array);
> ?>
>
>      
> ```
>
> El ejemplo anterior mostrará:
>
>     array(2) {
>       [1]=>
>       int(160)
>       [2]=>
>       int(66)
>     }
>
>          
>
> Observe que el primer valor desde el especificador `c` es sobrescrito por el primer valor desde el especificador `n`.
>
> </div>

## Véase también

`pack`
