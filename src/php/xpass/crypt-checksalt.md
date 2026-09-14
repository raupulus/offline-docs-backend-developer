---
title: crypt_checksalt
description: Valida un parámetro de hash de contraseña
source_url: https://www.php.net/manual/es/function.crypt-checksalt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xpass/functions/crypt-checksalt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xpass
translation_status: ready
translation_reviewed: true
translation_revision: 7b9d57fa4
order: 104020
---

crypt_checksalt

Valida un parámetro de hash de contraseña

## Descripción

```php
crypt_checksalt(string $salt): string
```php

Verifica si la cadena de sal cumple con la configuración del sistema y señala si el método de hash y los parámetros que especifica son aceptables. Está destinado a ser utilizado para determinar si la contraseña del usuario debe ser rehasheada utilizando el método de hash actualmente preferido.

## Parámetros

`salt`  
La cadena de sal a verificar.

## Valores devueltos

Devuelve una de las constantes `CRYPT_SALT_*` como `int`.

## Ejemplos

Un ejemplo de `crypt_checksalt`

```
<?php
// Genera una sal para un método obsoleto
$salt = crypt_gensalt(CRYPT_PREFIX_STD_DES);
// Verifica la sal
$test = crypt_checksalt($salt);
var_dump($test === CRYPT_SALT_METHOD_LEGACY);

// Genera una sal para un método por defecto
$salt = crypt_gensalt();
// Verifica la sal
$test = crypt_checksalt($salt);
var_dump($test === CRYPT_SALT_OK);
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(true)

## Véase también

crypt_gensalt
