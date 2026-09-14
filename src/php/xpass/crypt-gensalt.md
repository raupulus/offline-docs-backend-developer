---
title: crypt_gensalt
description: Compila una cadena para usar como argumento de sal para crypt
source_url: https://www.php.net/manual/es/function.crypt-gensalt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xpass/functions/crypt-gensalt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xpass
translation_status: ready
translation_reviewed: true
translation_revision: 7b9d57fa4
order: 104030
---

crypt_gensalt

Compila una cadena para usar como argumento de sal para crypt

## Descripción

```php
crypt_gensalt([string $prefix], [int $count]): string
```php

Compila una cadena para usar como argumento de sal para `crypt`.

## Parámetros

`prefix`  
El método de hash a usar. Una de las constantes `CRYPT_PREFIX_*`. Si es `null`, se seleccionará el mejor método de hash disponible.

`count`  
Controla el costo de procesamiento del hash; el rango válido y el significado exacto de count dependen del método de hash, pero números más grandes corresponden a hashes más costosos en términos de tiempo de CPU y posiblemente de uso de memoria. Si count es `0`, se seleccionará un costo bajo por defecto.

## Valores devueltos

Devuelve una cadena con el parámetro, o `null` en caso de error.

## Ejemplos

Un ejemplo de `crypt_gensalt`

```
<?php
// Genera la sal
$salt = crypt_gensalt(CRYPT_PREFIX_BLOWFISH);
// Hashea la contraseña
$hash = crypt("secret", $salt);
// Verifica el hash
$test = hash_equals(crypt("secret", $hash), $hash);
var_dump($salt, $hash, $test);
?>

   
```php

El ejemplo anterior mostrará:

    string(29) "$2y$05$GcPykP.Am8C1.dGamdpwW."
    string(60) "$2y$05$GcPykP.Am8C1.dGamdpwW.1RR.7uicWvJPZfJfCEizZHqVWwuaJLm"
    bool(true)

## Véase también

crypt_preferred_method

crypt

hash_equals
