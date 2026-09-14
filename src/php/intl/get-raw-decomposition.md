---
title: Normalizer::getRawDecomposition
description: Devuelve la propiedad Decomposition_Mapping para el punto de código UTF-8
  dado
source_url: https://www.php.net/manual/es/normalizer.getrawdecomposition.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/normalizer/get-raw-decomposition.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 42140
---

Normalizer::getRawDecomposition

normalizer_get_raw_decomposition

Devuelve la propiedad Decomposition_Mapping para el punto de código UTF-8 dado

## Descripción

Estilo orientado a objetos

```php
public static Normalizer::getRawDecomposition(string $string, [int $form]): string
```php

Estilo procedimental

```php
normalizer_get_raw_decomposition(string $string, [int $form]): string
```

Devuelve la propiedad Decomposition_Mapping, tal como se especifica en la base de datos de caracteres Unicode (UCD), para el punto de código UTF-8 dado.

## Parámetros

`string`  
La cadena de entrada, que debe ser un solo punto de código UTF-8.

## Valores devueltos

Devuelve un `string` que contiene la propiedad Decomposition_Mapping, si está presente en el UCD.

Devuelve `null` si no hay propiedad Decomposition_Mapping para el carácter.

## Ejemplos

Ejemplo de Normalizer::getRawDecomposition

```php
<?php

$result = "";
$strings = [
    "a",
    "\u{FFDA}",
    "\u{FDFA}",
    "",
    "aa",
    "\xF5",
];

foreach ($strings as $string) {
    $decomposition = Normalizer::getRawDecomposition($string);
    // $decomposition = normalizer_get_raw_decomposition($string); Enfoque procedimental

    $error_code = intl_get_error_code();
    $error_message = intl_get_error_message();

    $string_hex = bin2hex($string);
    $result .= "---------------------\n";

    if ($decomposition === null) {
        $result .= "'$string_hex' no tiene mapeo de descomposición\n";
    } else {
        $result .= "'$string_hex' tiene el mapeo de descomposición '" . bin2hex($decomposition) . "'\n";
    }

    $result .= "información de error: '$error_message' ($error_code)\n";
}

echo $result;
?>

   
```

El ejemplo anterior mostrará:

    ---------------------
    '61' no tiene mapeo de descomposición
    información de error: 'U_ZERO_ERROR' (0)
    ---------------------
    'efbf9a' tiene el mapeo de descomposición 'e385a1'
    información de error: 'U_ZERO_ERROR' (0)
    ---------------------
    'efb7ba' tiene el mapeo de descomposición 'd8b5d984d98920d8a7d984d984d98720d8b9d984d98ad98720d988d8b3d984d985'
    información de error: 'U_ZERO_ERROR' (0)
    ---------------------
    '' no tiene mapeo de descomposición
    información de error: 'La cadena de entrada debe tener exactamente un punto de código UTF-8: U_ILLEGAL_ARGUMENT_ERROR' (1)
    ---------------------
    '6161' no tiene mapeo de descomposición
    información de error: 'La cadena de entrada debe tener exactamente un punto de código UTF-8: U_ILLEGAL_ARGUMENT_ERROR' (1)
    ---------------------
    'f5' no tiene mapeo de descomposición
    información de error: 'Punto de código fuera de rango: U_ILLEGAL_ARGUMENT_ERROR' (1)

## Véase también

Normalizer::normalize

Normalizer::isNormalized
