---
title: sodium_crypto_generichash_update
description: Añade un mensaje a un hash
source_url: https://www.php.net/manual/es/function.sodium-crypto-generichash-update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-generichash-update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76490
---

sodium_crypto_generichash_update

Añade un mensaje a un hash

## Descripción

```php
sodium_crypto_generichash_update(string $state, string $message): true
```php

Añade un mensaje al estado de hash interno.

## Parámetros

`state`  
El valor de retorno de `sodium_crypto_generichash_init`.

`message`  
Los datos a añadir al estado de hash.

## Valores devueltos

Retorna siempre `true`.

## Ejemplos

Ejemplo de `sodium_crypto_generichash_update`

```
<?php
$messages = [random_bytes(32), random_bytes(32), random_bytes(16)];
$state = sodium_crypto_generichash_init();
foreach ($messages as $message) {
    sodium_crypto_generichash_update($state, $message);
}
$final = sodium_crypto_generichash_final($state);
var_dump(sodium_bin2hex($final));

$allAtOnce = sodium_crypto_generichash(implode('', $messages));
var_dump(sodium_bin2hex($allAtOnce));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(64) "e16e28bbbbcc39d9f5b1cbc33c41f1d217808640103e57a41f24870f79831e04"
    string(64) "e16e28bbbbcc39d9f5b1cbc33c41f1d217808640103e57a41f24870f79831e04"
