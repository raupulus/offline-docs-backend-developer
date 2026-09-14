---
title: openssl_password_hash
description: Crea un hash de contraseña usando la implementación de Argon2 de OpenSSL
source_url: https://www.php.net/manual/es/function.openssl-password-hash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-password-hash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_revision: 29cecd7f1
order: 59250
---

openssl_password_hash

Crea un hash de contraseña usando la implementación de Argon2 de OpenSSL

## Descripción

```php
openssl_password_hash(string $algo, string $password, [array $options]): string
```php

Crea un hash de contraseña usando la implementación de Argon2 de OpenSSL. Es una alternativa a `password_hash` que utiliza OpenSSL como backend, lo que puede ofrecer aceleración por hardware en algunas plataformas.

Esta función solo está disponible cuando PHP se compila con soporte de OpenSSL que incluye Argon2 (`HAVE_OPENSSL_ARGON2`).

## Parámetros

`algo`  
El algoritmo de hash de contraseña. Valores soportados: `"argon2id"` y `"argon2i"`.

`password`  
La contraseña del usuario.

`options`  
Un `array` asociativo de opciones. Claves soportadas: `memory_cost` - Memoria máxima (en KiB) que puede utilizarse para calcular el hash, `time_cost` - Tiempo máximo que puede tomar calcular el hash, `threads` - Número de hilos a utilizar para calcular el hash

## Valores devueltos

Devuelve el hash de la contraseña como una `string`.

## Errores/Excepciones

Lanza un `ValueError` si `algo` no es uno de los valores soportados (`"argon2i"` o `"argon2id"`).

Lanza un `Error` si la operación de hashing falla por una razón desconocida.

## Historial de cambios

| Versión | Descripción               |
|---------|---------------------------|
| 8.4.0   | Se ha añadido la función. |

## Ejemplos

Ejemplo con `openssl_password_hash`

```
<?php
$hash = openssl_password_hash('argon2id', 'my-secret-password');
echo $hash;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    $argon2id$v=19$m=65536,t=4,p=1$c29tZXNhbHR2YWx1ZQ$hashvalue...

`openssl_password_hash` con opciones personalizadas

```
<?php
$hash = openssl_password_hash('argon2id', 'my-secret-password', [
    'memory_cost' => 65536,
    'time_cost'   => 4,
    'threads'     => 1,
]);
?>

   
```php

## Véase también

`openssl_password_verify`, `password_hash`
