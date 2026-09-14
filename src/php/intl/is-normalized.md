---
title: Normalizer::isNormalized
description: Comprueba si el string proporcionado ya está en el formato de normalización
  especificado
source_url: https://www.php.net/manual/es/normalizer.isnormalized.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/normalizer/is-normalized.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 42150
---

Normalizer::isNormalized

normalizer_is_normalized

Comprueba si el string proporcionado ya está en el formato de normalización especificado

## Descripción

Estilo orientado a objetos

```php
public static Normalizer::isNormalized(string $string, [int $form]): bool
```php

Estilo procedimental

```php
normalizer_is_normalized(string $string, [int $form]): bool
```

Verifica si una cadena está normalizada.

## Parámetros

`string`  
La cadena a normalizar.

`form`  
Una de las formas de normalización.

## Valores devueltos

`true` si la cadena está normalizada, y `false` en caso contrario o si hay un error.

## Ejemplos

Ejemplo con `normalizer_is_normalized`, en estilo procedimental

```php
<?php
$char_A_ring = "\xC3\x85"; // 'LATIN CAPITAL LETTER A WITH RING ABOVE' (U+00C5)
$char_combining_ring_above = "\xCC\x8A";  // 'COMBINING RING ABOVE' (U+030A)

$char_orig = 'A' . $char_combining_ring_above;
$char_norm = normalizer_normalize( 'A' . $char_combining_ring_above, Normalizer::FORM_C );

echo ( normalizer_is_normalized($char_orig, Normalizer::FORM_C) ) ? "normalized" : "not normalized";
echo '; ';
echo ( normalizer_is_normalized($char_norm, Normalizer::FORM_C) ) ? "normalized" : "not normalized";
?>

   
```

Ejemplo con `normalizer_is_normalized`, en estilo orientado a objetos

```php
<?php
$char_A_ring = "\xC3\x85"; // 'LATIN CAPITAL LETTER A WITH RING ABOVE' (U+00C5)
$char_combining_ring_above = "\xCC\x8A";  // 'COMBINING RING ABOVE' (U+030A)

$char_orig = 'A' . $char_combining_ring_above;
$char_norm = Normalizer::normalize( 'A' . $char_combining_ring_above, Normalizer::FORM_C );

echo ( Normalizer::isNormalized($char_orig, Normalizer::FORM_C) ) ? "normalized" : "not normalized";
echo '; ';
echo ( Normalizer::isNormalized($char_norm, Normalizer::FORM_C) ) ? "normalized" : "not normalized";
?>

   
```

El ejemplo anterior mostrará:

    not normalized; normalized

      

## Véase también

`normalizer_normalize`
