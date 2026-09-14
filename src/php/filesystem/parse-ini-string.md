---
title: parse_ini_string
description: Analiza una cadena de configuración
source_url: https://www.php.net/manual/es/function.parse-ini-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/parse-ini-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: bb54309ef
order: 23900
---

parse_ini_string

Analiza una cadena de configuración

## Descripción

```php
parse_ini_string(string $ini_string, [bool $process_sections], [int $scanner_mode]): array
```php

`parse_ini_string` devuelve la configuración en la cadena `ini_string` en un array asociativo.

La estructura de la cadena debe ser la misma que la del archivo `php.ini`.

> [!WARNING]
> Esta función no debe ser utilizada con entradas no confiables, a menos que `scanner_mode` sea `INI_SCANNER_RAW`, ya que la salida analizada podría contener los valores de constantes sensibles, como constantes que contienen una contraseña de base de datos.

## Parámetros

`ini_string`  
El contenido de tipo ini a analizar.

`process_sections`  
Al activar el argumento `process_sections` con `true`, se obtendrá un array multidimensional, con los nombres de secciones y directivas. El valor por omisión del argumento `process_sections` es `false`

`scanner_mode`  
Puede tomar los valores de las constantes `INI_SCANNER_NORMAL` (por omisión) o `INI_SCANNER_RAW`. Si `INI_SCANNER_RAW` es utilizado, los valores de las opciones no serán analizados.

A partir de PHP 5.6.1 también puede ser especificado como `INI_SCANNER_TYPED`. En este modo los booleanos, null y enteros son preservados tanto como sea posible. Las cadenas de caracteres `"true"`, `"on"` y `"yes"` son convertidas a `true`. `"false"`, `"off"`, `"no"` y `"none"` son considerados como `false`. `"null"` es convertido a `null` en este modo. Además todas las cadenas de caracteres numéricas son convertidas a entero si es posible.

## Valores devueltos

Las directivas son devueltas en forma de array `array` en caso de éxito, y `false` en caso de error.

## Notas

> [!NOTE]
> Existen varias palabras reservadas que no deben ser utilizadas como clave en los archivos .ini. Esto incluye: `null`, `yes`, `no`, `true`, `false`, `on`, `off`, `none`. Los valores `null`, `off`, `no` y `false` son devueltos como "" (cadena vacía) y los valores `on`, `yes` y `true` son devueltos como "1" a menos que el modo `INI_SCANNER_TYPED` sea utilizado. Los caracteres `?{}|&~![()^"` no deben ser utilizados en ninguna parte en las claves, y tienen un significado especial en los valores.

## Véase también

`parse_ini_file`
