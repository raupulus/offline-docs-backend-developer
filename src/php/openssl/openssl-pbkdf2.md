---
title: openssl_pbkdf2
description: Genera una cadena PKCS5 v2 PBKDF2
source_url: https://www.php.net/manual/es/function.openssl-pbkdf2.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pbkdf2.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 59270
---

openssl_pbkdf2

Genera una cadena PKCS5 v2 PBKDF2

## Descripción

```php
#[\SensitiveParameter] openssl_pbkdf2(string $password, string $salt, int $key_length, int $iterations, [string $digest_algo]): string
```php

`openssl_pbkdf2` calcula PBKDF2 (Password-Based Key Derivation Function 2), una función de derivación de clave definida en PKCS5 v2.

## Parámetros

`password`  
Contraseña desde la cual se genera la clave derivada.

`salt`  
PBKDF2 recomienda un sal criptográfico de al menos 128 bits (16 octetos).

`key_length`  
Longitud deseada de la clave de salida.

`iterations`  
El número de iteraciones deseado. [El NIST recomienda al menos 1 000](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf). A partir de 2023, el OWASP recomienda 600 000 iteraciones para PBKDF2-HMAC-SHA256 y 210 000 para PBKDF2-HMAC-SHA512.

`digest_algo`  
Algoritmo de hash o digest opcional a partir de `openssl_get_md_methods`. Por omisión SHA-1. Se recomienda definirlo en SHA-256 o SHA-512.

## Valores devueltos

Devuelve una cadena binaria sin tratar o `false` si ocurre un error.

## Ejemplos

Ejemplo con openssl_pbkdf2()

```
<?php
$password = 'password';
$salt = openssl_random_pseudo_bytes(16);
$keyLength = 20;
$iterations = 600000;
$generated_key = openssl_pbkdf2($password, $salt, $keyLength, $iterations, 'sha256');
echo bin2hex($generated_key)."\n";
echo base64_encode($generated_key)."\n";
?>

    
```php

## Véase también

`hash_pbkdf2`, `openssl_get_md_methods`
