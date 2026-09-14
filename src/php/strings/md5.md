---
title: md5
description: Calcula el md5 de un string
source_url: https://www.php.net/manual/es/function.md5.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/md5.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 71e12e2df
order: 88890
---

md5

Calcula el md5 de un string

> [!WARNING]
> No se recomienda utilizar esta función para asegurar contraseñas, debido a la naturaleza rápida de este algoritmo de hash. Ver [F.A.Q del hash de contraseñas](#faq.passwords.fasthash) para más detalles y las buenas prácticas.

## Descripción

```php
md5(string $string, [bool $binary]): string
```php

Calcula el MD5 del string `string` utilizando el algoritmo [`RSA Data Security, Inc. MD5 Message-Digest Algorithm`](https://datatracker.ietf.org/doc/html/rfc1321), y devuelve el resultado.

## Parámetros

`string`  
El string.

`binary`  
Si el argumento opcional `binary` está definido a `true`, entonces el md5 se devuelve en formato binario crudo con una longitud de 16.

## Valores devueltos

Devuelve el md5 del string, en forma de un número hexadecimal de 32 caracteres.

## Ejemplos

Ejemplo con `md5`

```
<?php
$str = 'apple';

if (md5($str) === '1f3870be274f6c49b3e31a0c6728957f') {
    echo "¿Desea una golden o una spartan?";
}
?>

    
```php

## Véase también

`hash`, `password_hash`
