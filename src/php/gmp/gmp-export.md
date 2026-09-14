---
title: gmp_export
description: Exportación hacia un string binario
source_url: https://www.php.net/manual/es/function.gmp-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: false
translation_revision: '548548299'
order: 28470
---

gmp_export

Exportación hacia un string binario

## Descripción

```php
gmp_export(GMP $num, [int $word_size], [int $flags]): string
```php

Exporta un número GMP hacia un string binario.

## Parámetros

`num`  
El número GMP a exportar.

`word_size`  
El valor por omisión es 1. El número de bytes en cada parte de datos binarios. Principalmente utilizado con el argumento options.

`flags`  
El valor por omisión es `GMP_MSW_FIRST` \| `GMP_NATIVE_ENDIAN`.

## Valores devueltos

Retorna un string.

## Historial de cambios

| Versión | Descripción                                          |
|---------|------------------------------------------------------|
| 8.0.0   | Esta función ya no retorna `false` en caso de error. |

## Ejemplos

Ejemplo con `gmp_export`

```
<?php
$number = gmp_init(16705);
echo gmp_export($number) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    AA

## Véase también

`gmp_import`
