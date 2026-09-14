---
title: sodium_crypto_pwhash_str
description: Devuelve un hash codificado en ASCII
source_url: https://www.php.net/manual/es/function.sodium-crypto-pwhash-str.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-pwhash-str.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76640
---

sodium_crypto_pwhash_str

Devuelve un hash codificado en ASCII

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_pwhash_str(string $password, int $opslimit, int $memlimit): string
```php

Utiliza un algoritmo de hash intensivo en CPU y memoria con una sal generada aleatoriamente, y límites de memoria y CPU para generar un hash codificado en ASCII adecuado para el almacenamiento de contraseñas.

## Parámetros

`password`  
`string`; La contraseña para la cual se generará un hash.

`opslimit`  
Representa una cantidad máxima de cálculos a realizar. Aumentar este número hará que la función requiera más ciclos de CPU para calcular una clave. Existen constantes disponibles para definir el límite de operaciones a valores apropiados según el uso previsto, en orden de fuerza: `SODIUM_CRYPTO_PWHASH_OPSLIMIT_INTERACTIVE`, `SODIUM_CRYPTO_PWHASH_OPSLIMIT_MODERATE` y `SODIUM_CRYPTO_PWHASH_OPSLIMIT_SENSITIVE`.

`memlimit`  
La cantidad máxima de RAM que la función utilizará, en bytes. Existen constantes para ayudar a elegir un valor apropiado, en orden de tamaño: `SODIUM_CRYPTO_PWHASH_MEMLIMIT_INTERACTIVE`, `SODIUM_CRYPTO_PWHASH_MEMLIMIT_MODERATE` y `SODIUM_CRYPTO_PWHASH_MEMLIMIT_SENSITIVE`. Típicamente, estos valores deberían asociarse con los valores opslimit correspondientes.

## Valores devueltos

Devuelve el hash de la contraseña.

Para producir el mismo hash de contraseña a partir de la misma contraseña, los mismos valores para `opslimit` y `memlimit` deben ser utilizados. Estos valores están integrados en el hash generado, por lo que todo lo necesario para verificar el hash está incluido. Esto permite a la función `sodium_crypto_pwhash_str_verify` verificar el hash sin necesidad de almacenamiento separado para los otros parámetros.

## Ejemplos

Ejemplo de `sodium_crypto_pwhash_str`

```
<?php
$password = 'password';
echo sodium_crypto_pwhash_str(
    $password,
    SODIUM_CRYPTO_PWHASH_OPSLIMIT_INTERACTIVE,
    SODIUM_CRYPTO_PWHASH_MEMLIMIT_INTERACTIVE
);

   
```php

Resultado del ejemplo anterior es similar a:

    $argon2id$v=19$m=65536,t=2,p=1$oWIfdaXwWwhVmovOBc2NAQ$EbsZ+JnZyyavkafS0hoc4HdaOB0ILWZESAZ7kVGa+Iw

## Notas

> [!NOTE]
> Los hashes son calculados utilizando el algoritmo Argon2ID, proporcionando resistencia tanto a ataques GPU como a ataques por canales laterales. A diferencia de la función `password_hash`, no hay parámetro de sal (una sal es generada automáticamente), y los parámetros `opslimit` y `memlimit` no son opcionales.

## Véase también

sodium_crypto_pwhash_str_verify

sodium_crypto_pwhash

password_hash

password_verify

Libsodium Argon2 docs
