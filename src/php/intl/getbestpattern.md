---
title: IntlDatePatternGenerator::getBestPattern
description: Determina el formato de fecha/hora más adecuado
source_url: https://www.php.net/manual/es/intldatepatterngenerator.getbestpattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intldatepatterngenerator/getbestpattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 5b6663923
order: 41310
---

IntlDatePatternGenerator::getBestPattern

Determina el formato de fecha/hora más adecuado

## Descripción

```php
public IntlDatePatternGenerator::getBestPattern(string $skeleton): string
```php

Determina qué formato de fecha/hora es el más adecuado para una configuración local dada.

## Parámetros

`skeleton`  
El esqueleto.

## Valores devueltos

Devuelve un patrón de fecha/hora ICU aceptado por `IntlDateFormatter` en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de IntlDatePatternGenerator::getBestPattern

```
<?php

$skeleton = 'YYYYMMdd';
$today = \DateTimeImmutable::createFromFormat('Y-m-d', '2021-04-24');

$patternGenerator = new \IntlDatePatternGenerator('de_DE');
$pattern = $patternGenerator->getBestPattern($skeleton);
echo 'de: ', \IntlDateFormatter::formatObject($today, $pattern, 'de_DE'), "\n";

$patternGenerator = new \IntlDatePatternGenerator('en_US');
$pattern = $patternGenerator->getBestPattern($skeleton);
echo 'en: ', \IntlDateFormatter::formatObject($today, $pattern, 'en_US');
?>

    
```php

El ejemplo anterior mostrará:

    de: 24.04.2021
    en: 04/24/2021
