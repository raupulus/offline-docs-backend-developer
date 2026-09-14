---
title: ctype_upper
description: Chequear posibles caracteres en mayúscula
source_url: https://www.php.net/manual/es/function.ctype-upper.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ctype/functions/ctype-upper.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ctype
translation_status: ready
translation_reviewed: false
translation_revision: e20e74073
order: 8540
---

ctype_upper

Chequear posibles caracteres en mayúscula

## Descripción

```php
ctype_upper(mixed $text): bool
```php

Verifica si todos los caracteres en la `string` entregada, `text`, son caracteres en mayúsculas.

## Parámetros

`text`  
La cadena de prueba.

> [!NOTE]
> Si se proporciona un `int` entre -128 y 255 inclusive, este se interpreta como el valor ASCII de un solo carácter (a los valores negativos se les añade 256 para permitir caracteres del rango ASCII extendido). Cualquier otro entero se interpreta como un string que contiene los dígitos decimales del entero.

> [!WARNING]
> A partir de PHP 8.1.0, pasar un argumento que no sea string está obsoleto. En el futuro, el argumento se interpretará como un string en lugar de un punto de código ASCII. Según el comportamiento deseado, el argumento debería convertirse a `string` o se debería realizar una llamada explícita a `chr`.

## Valores devueltos

Devuelve `true` si cada caracter del `text` es una letra mayúscula en la localidad actual. Cuando se llama con una cadena vacía, el resultado será siempre `false`.

## Ejemplos

Un ejemplo de `ctype_upper` (usando la localidad predeterminada)

```
<?php
$cadenas = array('AKLWC139', 'LMNSDO', 'akwSKWsm');
foreach ($cadenas as $caso_prueba) {
    if (ctype_upper($caso_prueba)) {
        echo "La cadena $caso_prueba consiste completamente de letras mayúsculas.\n";
    } else {
        echo "La cadena $caso_prueba no consiste completamente de letras mayúsculas.\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    La cadena AKLWC139 no consiste completamente de signos de letras mayúsculas.
    La cadena LMNSDO consiste completamente de signos de letras mayúsculas.
    La cadena akwSKWsm no consiste completamente de signos de letras mayúsculas.

## Véase también

`ctype_alpha`, `ctype_lower`, `setlocale`, `IntlChar::isupper`
