---
title: pack
description: Compacta datos en una cadena binaria
source_url: https://www.php.net/manual/es/function.pack.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/pack.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: ad0f1eaa6
order: 47140
---

pack

Compacta datos en una cadena binaria

## Descripción

```php
pack(string $format, mixed ...$values): string
```php

Compacta los argumentos `args` en una cadena binaria, siguiendo el formato `format`.

El concepto proviene de Perl y todo el formato funciona de la misma forma que en Perl, pero algunos formatos aún faltan (como "`u`").

Tenga en cuenta que la distinción entre signado y no signado solo afecta a la función `unpack`, mientras que la función `pack` proporcionará el mismo resultado para ambos formatos.

## Parámetros

`format`  
La `string` `format` consiste en códigos de formato seguidos por un argumento repetidor opcional. El repetidor puede ser un valor entero o `*` para una repetición hasta el final de los datos de entrada. Para a, A, h, H, el repetidor especifica cuántos caracteres de un dato se toman, para @, es la posición absoluta donde se insertan los próximos datos, para todo lo demás, el repetidor especifica cuántos argumentos de datos son consumidos y compactados en la cadena binaria resultante.

Los formatos actualmente aceptados son:

| Código | Descripción |
|----|----|
| a | NUL - Una cadena completada con `null` |
| A | SPACE - Una cadena completada con un espacio |
| h | Cadena hexadecimal h, bit de menor peso en primer lugar |
| H | Cadena hexadecimal H, bit de mayor peso en primer lugar |
| c | Carácter signado |
| C | Carácter no signado |
| s | entero corto signado (siempre 16 bits, orden de bytes dependiente de la máquina) |
| S | entero corto no signado (siempre 16 bits, orden de bytes dependiente de la máquina) |
| n | entero corto no signado (siempre 16 bits, orden de bytes big endian) |
| v | entero corto no signado (siempre 16 bits, orden de bytes little endian) |
| i | entero signado (tamaño y orden de bytes dependientes de la máquina) |
| I | entero no signado (tamaño y orden de bytes dependientes de la máquina) |
| l | entero largo signado (siempre 32 bits, orden de bytes dependiente de la máquina) |
| L | entero largo no signado (siempre 32 bits, orden de bytes dependiente de la máquina) |
| N | entero largo no signado (siempre 32 bits, orden de bytes big endian) |
| V | entero largo no signado (siempre 32 bits, orden de bytes little endian) |
| q | entero doblemente largo signado (siempre 64 bits, orden de bytes dependiente de la máquina) |
| Q | entero doblemente largo no signado (siempre 64 bits, orden de bytes dependiente de la máquina) |
| J | entero doblemente largo no signado (siempre 64 bits, orden de bytes big endian) |
| P | entero doblemente largo no signado (siempre 64 bits, orden de bytes little endian) |
| f | número de coma flotante (tamaño y representación dependientes de la máquina) |
| g | número de coma flotante (tamaño dependiente de la máquina, orden de bytes little endian) |
| G | número de coma flotante (tamaño dependiente de la máquina, orden de bytes big endian) |
| d | número de coma flotante doble (tamaño y representación dependientes de la máquina) |
| e | número de coma flotante doble (tamaño dependiente de la máquina, orden de bytes little endian) |
| E | número de coma flotante doble (tamaño dependiente de la máquina, orden de bytes big endian) |
| x | carácter NUL |
| X | Retrocede un carácter |
| Z | La cadena terminada por NUL (ASCIIZ) será completada con el valor NULL |
| @ | Rellena con NUL hasta la posición absoluta |

Caracteres de formato para `pack`

`values`  

## Valores devueltos

Devuelve una `string` binaria que contiene los datos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ya no devuelve `false` en caso de error. |
| 7.2.0 | Los tipos `float` y `double` admiten Big Endian y Little Endian. |
| 7.0.15, 7.1.1 | Se han añadido los códigos "e", "E", "g" y "G" para activar la compatibilidad con el orden de bytes para los números de coma flotante de simple y doble precisión. |

## Ejemplos

Ejemplo con `pack`

```
<?php
$binarydata = pack("nvc*", 0x1234, 0x5678, 65, 66);
?>

    
```php

La cadena binaria resultante tendrá 6 bytes de longitud, y contendrá la secuencia 0x12, 0x34, 0x78, 0x56, 0x41, 0x42.

## Notas

> [!CAUTION]
> Los códigos de formato `q`, `Q`, `J` y `P` no están disponibles en las versiones de PHP de 32 bits.

> [!CAUTION]
> Tenga en cuenta que PHP almacena internamente los valores `int` como valores signados dependientes de la máquina. Las operaciones sobre enteros que llevan a números fuera del espacio de definición del `int` serán almacenados como `float`. Al empaquetar estos flotantes en enteros, se convierten al tipo entero. Esto puede llevar potencialmente a una representación inesperada de los bytes.
>
> El caso más clásico es el empaquetado de números no signados que serían representables en el tipo `int` si este fuera no signado. En los sistemas con un `int` de 32 bits, la conversión resulta en un byte idéntico al que si el tipo `int` fuera no signado (aunque esto sigue dependiendo de la implementación no signada a signada, del estándar C). En los sistemas con un `int` de 64 bits, el `float` no suele tener una mantisa lo suficientemente amplia para contener el valor sin pérdida de precisión. Si estos sistemas también poseen un tipo C nativo `int` de 64 bits (la mayoría de los \*NIX no lo tienen), la única forma de usar el formato de empaquetado `I` en valores altos es crear valores `int` negativos con la misma representación de bytes que la valor no signado deseado correspondiente.

## Véase también

`unpack`
