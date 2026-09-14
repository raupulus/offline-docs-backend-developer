---
title: sha1
description: Calcula el sha1 de un string
source_url: https://www.php.net/manual/es/function.sha1.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/sha1.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 71e12e2df
order: 89050
---

sha1

Calcula el sha1 de un string

> [!WARNING]
> No se recomienda utilizar esta función para asegurar contraseñas, debido a la naturaleza rápida de este algoritmo de hash. Ver [F.A.Q del hash de contraseñas](#faq.passwords.fasthash) para más detalles y las buenas prácticas.

## Descripción

```php
sha1(string $string, [bool $binary]): string
```php

Calcula el sha1 del string `string` utilizando [`US Secure Hash Algorithm 1`](https://datatracker.ietf.org/doc/html/rfc3174).

## Parámetros

`string`  
El string de entrada.

`binary`  
Si el argumento opcional `binary` se establece a `true`, el sha1 se devuelve en formato binario crudo con un tamaño de 20 caracteres, de lo contrario, se devuelve como un número hexadecimal con un tamaño de 40 caracteres.

## Valores devueltos

Devuelve el sha1, en forma de un string.

## Ejemplos

Ejemplo con `sha1`

```
<?php
$str = 'pomme';

if (sha1($str) === '752c14ea195c460bac3c3b7896975ee9fd15eeb7') {
    echo "¿Desea una golden o una spartan?";
}
?>

    
```php

## Véase también

`hash`
