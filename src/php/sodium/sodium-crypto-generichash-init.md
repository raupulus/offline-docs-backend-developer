---
title: sodium_crypto_generichash_init
description: Inicializa un hash para el streaming
source_url: https://www.php.net/manual/es/function.sodium-crypto-generichash-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-generichash-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76470
---

sodium_crypto_generichash_init

Inicializa un hash para el streaming

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_generichash_init([string $key], [int $length]): string
```php

El método de inicialización para la API de hash genérico en streaming.

## Parámetros

`key`  
La clave de hash genérico.

`length`  
El tamaño de la salida esperada de la función de hash.

## Valores devueltos

Devuelve un estado de hash, serializado en forma de una string binaria bruta.

## Ejemplos

Ejemplo de `sodium_crypto_generichash_init`

```
<?php
$messages = [random_bytes(32), random_bytes(32), random_bytes(16)];
$state = sodium_crypto_generichash_init('', 32);
foreach ($messages as $message) {
    sodium_crypto_generichash_update($state, $message);
}
$final = sodium_crypto_generichash_final($state, 32);
var_dump(sodium_bin2hex($final));
$allAtOnce = sodium_crypto_generichash(implode('', $messages));
var_dump(sodium_bin2hex($allAtOnce));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(64) "a2939a9163cb7c796ec28e01028489e72475c136b2697ea59e3e760ab4a8ab20"
    string(64) "a2939a9163cb7c796ec28e01028489e72475c136b2697ea59e3e760ab4a8ab20"
