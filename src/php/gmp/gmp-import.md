---
title: gmp_import
description: Importación desde una cadena binaria
source_url: https://www.php.net/manual/es/function.gmp-import.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-import.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: false
translation_revision: '548548299'
order: 28520
---

gmp_import

Importación desde una cadena binaria

## Descripción

```php
gmp_import(string $data, [int $word_size], [int $flags]): GMP
```php

Importa un número GMP desde una cadena binaria.

## Parámetros

`data`  
La cadena binaria a importar.

`word_size`  
El valor por omisión es 1. El número de bytes en cada parte de datos binarios. Principalmente utilizado con el argumento options.

`flags`  
El valor por omisión es `GMP_MSW_FIRST` \| `GMP_NATIVE_ENDIAN`.

## Valores devueltos

Devuelve un número GMP.

## Historial de cambios

| Versión | Descripción                                           |
|---------|-------------------------------------------------------|
| 8.0.0   | Esta función ya no devuelve `false` en caso de error. |

## Ejemplos

Ejemplo con `gmp_import`

```
<?php
$number = gmp_import("\0");
echo gmp_strval($number) . "\n";

$number = gmp_import("\0\1\2");
echo gmp_strval($number) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    0
    258

## Véase también

`gmp_export`
