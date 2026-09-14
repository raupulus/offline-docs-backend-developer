---
title: Normalizer::normalize
description: Normaliza una cadena en entrada
source_url: https://www.php.net/manual/es/normalizer.normalize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/normalizer/normalize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 42160
---

Normalizer::normalize

normalizer_normalize

Normaliza una cadena en entrada

## Descripción

Estilo orientado a objetos

```php
public static Normalizer::normalize(string $string, [int $form]): string
```php

Estilo procedimental

```php
normalizer_normalize(string $string, [int $form]): string
```

Normaliza la cadena en entrada y devuelve una cadena normalizada.

## Parámetros

`string`  
La cadena a normalizar

`form`  
Una de las formas de normalización.

## Valores devueltos

La cadena normalizada, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `normalizer_normalize`, procedimental

```php
    
<?php
$char_A_ring = "\xC3\x85"; // 'LATIN CAPITAL LETTER A WITH RING ABOVE' (U+00C5)
$char_combining_ring_above = "\xCC\x8A";  // 'COMBINING RING ABOVE' (U+030A)

$char_1 = normalizer_normalize( $char_A_ring, Normalizer::FORM_C );
$char_2 = normalizer_normalize( 'A' . $char_combining_ring_above, Normalizer::FORM_C );

echo urlencode($char_1);
echo ' ';
echo urlencode($char_2);
?>

   
```

Ejemplo con `normalizer_normalize`, POO

```php
    
<?php
$char_A_ring = "\xC3\x85"; // 'LATIN CAPITAL LETTER A WITH RING ABOVE' (U+00C5)
$char_combining_ring_above = "\xCC\x8A";  // 'COMBINING RING ABOVE' (U+030A)

$char_1 = Normalizer::normalize( $char_A_ring, Normalizer::FORM_C );
$char_2 = Normalizer::normalize( 'A' . $char_combining_ring_above, Normalizer::FORM_C );

echo urlencode($char_1);
echo ' ';
echo urlencode($char_2);
?>

   
```

El ejemplo anterior mostrará:

       
    %C3%85 %C3%85

      

## Véase también

`normalizer_is_normalized`
