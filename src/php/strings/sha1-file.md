---
title: sha1_file
description: Calcula el sha1 de un fichero
source_url: https://www.php.net/manual/es/function.sha1-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/sha1-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 89040
---

sha1_file

Calcula el sha1 de un fichero

## Descripción

```php
sha1_file(string $filename, [bool $binary]): string
```php

Calcula el sha1 del fichero especificado por el argumento `filename` utilizando [`US Secure Hash Algorithm 1`](https://datatracker.ietf.org/doc/html/rfc3174), luego devuelve este sha1. El sha1 es un número hexadecimal de 40 caracteres.

## Parámetros

`filename`  
El nombre del fichero a hachear.

`binary`  
Cuando `true`, devuelve el pretratamiento en formato binario sin tratar con una longitud de 20.

## Valores devueltos

Devuelve un string en caso de éxito, `false` en caso contrario.

## Ejemplos

Ejemplo con `sha1_file`

```
<?php
foreach (glob('/examples/*.xml') as $ent)
{
    if (is_dir($ent)) {
        continue;
    }

    echo $ent . ' (SHA1: ' . sha1_file($ent) . ')', PHP_EOL;
}
?>

    
```php

## Véase también

`hash_file`, `hash_init`, `sha1`
