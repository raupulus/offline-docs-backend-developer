---
title: octdec
description: Conversión de octal a decimal
source_url: https://www.php.net/manual/es/function.octdec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/octdec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 44810
---

octdec

Conversión de octal a decimal

## Descripción

```php
octdec(string $octal_string): int
```php

Devuelve un string que contiene la representación decimal del número `octal_string`.

## Parámetros

`octal_string`  
El string octal a convertir. Cualquier carácter inválido en `octal_string` es ignorado silenciosamente. A partir de PHP 7.4.0, proporcionar caracteres inválidos está deprecado. El número a convertir.

## Valores devueltos

La representación decimal de `octal_string`

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | Proporcionar caracteres inválidos generará ahora una advertencia deprecada. El resultado siempre será calculado como si los caracteres inválidos no existieran. |

## Ejemplos

Ejemplo con `octdec`

```
<?php
echo octdec('77') . "\n";
echo octdec(decoct(45));
?>

    
```php

El ejemplo anterior mostrará:

    63
    45

## Notas

> [!NOTE]
> La función puede convertir números que son demasiado grandes para caber en un tipo `int`, en cuyo caso, estos valores son devueltos como `float`.

## Véase también

`decoct`, `bindec`, `hexdec`, `base_convert`
