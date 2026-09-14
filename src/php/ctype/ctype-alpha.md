---
title: ctype_alpha
description: Chequear posibles caracteres alfabéticos
source_url: https://www.php.net/manual/es/function.ctype-alpha.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ctype/functions/ctype-alpha.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ctype
translation_status: ready
translation_reviewed: false
translation_revision: e20e74073
order: 8460
---

ctype_alpha

Chequear posibles caracteres alfabéticos

## Descripción

```php
ctype_alpha(mixed $text): bool
```php

Verifica si todos los caracteres en la `string` entregada,`texto`, son alfabéticos. En la localización `C` estándar las letras se limitan a `[A-Za-z]` y `ctype_alpha` es equivalente a `(ctype_upper($texto) || ctype_lower($texto))` si \$texto es un caracter sencillo, aunque otros idiomas usan letras que no son consideradas como mayúsculas ni minúsculas.

## Parámetros

`text`  
El string de prueba.

> [!NOTE]
> Si se proporciona un `int` entre -128 y 255 inclusive, este se interpreta como el valor ASCII de un solo carácter (a los valores negativos se les añade 256 para permitir caracteres del rango ASCII extendido). Cualquier otro entero se interpreta como un string que contiene los dígitos decimales del entero.

> [!WARNING]
> A partir de PHP 8.1.0, pasar un argumento que no sea string está obsoleto. En el futuro, el argumento se interpretará como un string en lugar de un punto de código ASCII. Según el comportamiento deseado, el argumento debería convertirse a `string` o se debería realizar una llamada explícita a `chr`.

## Valores devueltos

Devuelve `true` si cada caracter de `texto` es una letra de la localización actual, `false` de lo contrario. Cuando se llama con una cadena vacía, el resultado será siempre `false`.

## Ejemplos

Un ejemplo de `ctype_alpha` (usando la localización predeterminada)

```
<?php
$cadenas = array('KjgWZC', 'arf12');
foreach ($cadenas as $caso_prueba) {
    if (ctype_alpha($caso_prueba)) {
        echo "La cadena $caso_prueba consiste completamente de letras.\n";
    } else {
        echo "La cadena $caso_prueba no consiste completamente de letras.\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    La cadena KjgWZC consiste completamente de letras.
    La cadena arf12 no consiste completamente de letras.

## Véase también

`ctype_upper`, `ctype_lower`, `setlocale`, `IntlChar::isalpha`
