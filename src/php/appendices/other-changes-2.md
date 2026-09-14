---
title: Otros cambios
source_url: https://www.php.net/manual/es/migration71.other-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration71/other-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 4360f13f4
order: 500
---

## Otros cambios

## Avisos y advertencias sobre operaciones aritméticas con strings inválidos

Se han introducido nuevos errores `E_WARNING` y `E_NOTICE` cuando se fuerzan strings no válidos utilizando operadores que esperan números (`+` `-` `*` `/` `**` `%` `<<` `>>` `|` `&` `^`) o sus asignaciones equivalentes. Se emite un `E_NOTICE` cuando el string comienza con un valor numérico pero contiene caracteres no numéricos al final, y se emite un `E_WARNING` cuando el string no contiene un valor numérico.

```php
<?php
'1b' + 'something';

   
```

El ejemplo anterior mostrará:

    Notice: A non well formed numeric value encountered in %s on line %d
    Warning: A non-numeric value encountered in %s on line %d

## Advertencia en caso de desbordamiento de la secuencia de escape octal

Anteriormente, las secuencias de escape octales de tres octetos en strings desbordaban silenciosamente. Ahora siguen desbordando, pero se emitirá un `E_WARNING`.

```php
<?php
var_dump("\500");

   
```

El ejemplo anterior mostrará:

    Warning: Octal escape sequence overflow \500 is greater than \377 in %s on line %d
    string(1) "@"

## Corrección de las inconsistencias de `$this`

Aunque `$this` se considera una variable especial en PHP, le faltaban controles adecuados para asegurar que no se utilizara como nombre de variable o reasignada. Esto se ha rectificado para asegurar que `$this` no se pueda usar como una variable definida por el usuario, reasignar a un valor diferente o globalizar.

## Generación de ID de sesión sin hashing

Los IDs de sesión ya no se les aplicará un hash al generarse. Con este cambio, se eliminan los siguientes cuatro parámetros ini:

- `session.entropy_file`

- `session.entropy_length`

- `session.hash_function`

- `session.hash_bits_per_character`

Y se añaden los siguientes dos parámetros ini:

- `session.sid_length` - define la longitud del ID de sesión, por defecto 32 caracteres para la retrocompatibilidad.

- `session.sid_bits_per_character` - define el número de bits a registrar por caracter (es decir, aumenta el intervalo de caracteres que se pueden utilizar en el ID de sesión), por defecto 4 para la retrocompatibilidad.

## Modificaciones aplicadas a la gestión de los ficheros INI

`precision`  
Si el valor se establece en -1, entonces se utiliza el modo dtoa 0. El valor por defecto sigue siendo 14.

`serialize_precision`  
Si el valor se establece en -1, entonces se utiliza el modo dtoa 0. El valor -1 ahora se utiliza por defecto.

`gd.jpeg_ignore_warning`  
El valor por defecto de este parámetro `php.ini` se ha modificado a 1, por lo que los avisos de libjpeg se ignoran de forma predeterminada.

`opcache.enable_cli`  
El valor por defecto de este parámetro `php.ini` se modificó a 1 (activado) en PHP 7.1.2, y se cambió de nuevo a 0 (desactivado) en PHP 7.1.7.

## Generación de ID de sesión únicamente con un CSPRNG

Los ID de sesión ahora se generarán únicamente mediante un CSPRNG (Crypto Secure Pseudo Random Number Generator).

## Mensajes de `TypeError` más informativos cuando se permite `null`

Las excepciones `TypeError` para las verificaciones de tipo arg_info ahora proporcionarán mensajes de error más informativos. Si el tipo del parámetro o el tipo de retorno acepta `null` (ya sea teniendo un valor por defecto de `null` o siendo un tipo nullable), entonces el mensaje de error mencionará esto con un mensaje "must be ... or null" o "must ... or be null."
