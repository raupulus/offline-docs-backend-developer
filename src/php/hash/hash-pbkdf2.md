---
title: hash_pbkdf2
description: Genera una clave PBKDF2 derivada de la contraseña proporcionada
source_url: https://www.php.net/manual/es/function.hash-pbkdf2.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-pbkdf2.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: false
translation_revision: 539a9823a
order: 29330
---

hash_pbkdf2

Genera una clave PBKDF2 derivada de la contraseña proporcionada

## Descripción

```php
#[\SensitiveParameter] hash_pbkdf2(string $algo, string $password, string $salt, int $iterations, [int $length], [bool $binary], [array $options]): string
```php

## Parámetros

`algo`  
Nombre del algoritmo de hash seleccionado (por ejemplo: `"sha256"`). Para una lista de los algoritmos soportados ver `hash_hmac_algos`.

> [!NOTE]
> Las funciones de hash no criptográficas no están permitidas.

`password`  
La contraseña a utilizar para la derivación.

`salt`  
El salt a utilizar para la derivación. Este valor debe ser generado aleatoriamente.

`iterations`  
El número de iteraciones internas para efectuar la derivación.

`length`  
La longitud de la cadena de salida. Si el parámetro `binary` vale `true`, este parámetro corresponderá a la longitud, en bytes, de la clave derivada; si el parámetro `binary` vale `false`, corresponderá al doble de la longitud, en bytes, de la clave derivada (ya que cada byte de la clave es devuelto sobre dos hexits).

Si `0` es pasado, la salida completa del algoritmo elegido será utilizada.

`binary`  
Cuando está definido a `true`, la función mostrará los datos binarios brutos. Si vale `false`, la visualización se hará en minúsculas.

`options`  
Un array de opciones para los diferentes algoritmos de hash. Actualmente, solo la clave `"seed"` es soportada por las variantes MurmurHash.

## Valores devueltos

Devuelve una cadena que contiene la clave derivada en minúsculas, a menos que el parámetro `binary` esté posicionado a `true` en cuyo caso, la representación binaria bruta de la clave derivada será devuelta.

## Errores/Excepciones

Una excepción `ValueError` si el algoritmo no es conocido, si el parámetro `iterations` es inferior o igual a `0`, si la longitud `length` es inferior o igual a `0` o si el `salt` es demasiado largo (mayor que `INT_MAX``- 4`).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | El uso de funciones de hash no criptográficas (adler32, crc32, crc32b, fnv132, fnv1a32, fnv164, fnv1a64, joaat) ha sido desactivado. |
| 8.0.0 | Levanta una excepción `ValueError` ahora en caso de error. Anteriormente, `false` era devuelto y un mensaje `E_WARNING` era emitido. |

## Ejemplos

Ejemplo con `hash_pbkdf2`

```
<?php
$password = "password";
$iterations = 600000;

// Genera un salt criptográficamente seguro aleatorio usando la función random_bytes(),
$salt = random_bytes(16);

$hash = hash_pbkdf2("sha256", $password, $salt, $iterations, 20);
var_dump($hash);

// Para binario bruto, $length debe ser dividido por dos para resultados equivalentes
$hash = hash_pbkdf2("sha256", $password, $salt, $iterations, 10, true);
var_dump(bin2hex($hash));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(20) "120fb6cffcf8b32c43e7"
    string(20) "120fb6cffcf8b32c43e7"

## Notas

> [!CAUTION]
> El método PBKDF2 puede ser utilizado para hashear contraseñas para el almacenamiento. Sin embargo, debe tenerse en cuenta que la función `password_hash` o la función `crypt` con la constante `CRYPT_BLOWFISH` es mejor para este uso.

## Véase también

`password_hash`, `hash_hkdf`, `sodium_crypto_pwhash`
