---
title: openssl_seal
description: Sella datos
source_url: https://www.php.net/manual/es/function.openssl-seal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-seal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 110ac4325
order: 59490
---

openssl_seal

Sella datos

## Descripción

```php
#[\SensitiveParameter] openssl_seal(string $data, string $sealed_data, array $encrypted_keys, array $public_key, string $cipher_algo, [string $iv]): int
```php

La `openssl_seal` sella (cifra) `data` utilizando el `cipher_algo` especificado con una clave secreta generada aleatoriamente. La clave es posteriormente cifrada con cada una de las claves públicas en el array `public_key`, y cada clave de envoltura cifrada es devuelta en `encrypted_keys`. Esto permite enviar datos sellados a múltiples destinatarios (siempre que sus claves públicas estén disponibles). Cada destinatario debe recibir tanto los datos sellados como la clave de envoltura que ha sido cifrada con la clave pública del destinatario. El IV (vector de inicialización) es generado, y su valor es devuelto en `iv`.

## Parámetros

`data`  
Los datos a sellar

`sealed_data`  
Los datos sellados.

`encrypted_keys`  
Array de claves cifradas.

`public_key`  
Array de instancias `OpenSSLAsymmetricKey` que contienen las claves públicas.

`cipher_algo`  
El método de cifrado.

> [!CAUTION]
> El valor por omisión para versiones de PHP anteriores a 8.0 es (`'RC4'`), que se considera no segura. Se recomienda encarecidamente especificar explícitamente un método de cifrado seguro.

`iv`  
El vector de inicialización para el descifrado de `data`. Es requerido si el método de cifrado necesita un IV. Esto puede ser determinado llamando a `openssl_cipher_iv_length` con `cipher_algo`.

> [!CAUTION]
> El IV no puede ser definido explícitamente. Cualquier valor que se le asigne es sobrescrito por un valor generado aleatoriamente.

## Valores devueltos

Devuelve la longitud de los datos sellados en caso de éxito, y `false` en caso contrario. En caso de éxito, los datos sellados son colocados en el parámetro `sealed_data`, y las claves de envoltura en `encrypted_keys`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `public_key` ahora acepta un `array` de instancias de `OpenSSLAsymmetricKey`; anteriormente, se aceptaba un `array` de `resource`s de tipo `OpenSSL key`. |
| 8.0.0 | `cipher_algo` ya no es un parámetro opcional. |
| 8.0.0 | `iv` ahora es nullable. |

## Ejemplos

Ejemplo con `openssl_seal`

```
<?php

$data = "test";

// obtener las claves públicas
$pk1 = openssl_get_publickey("file://cert1.pem");
$pk2 = openssl_get_publickey("file://cert2.pem");

// sella el mensaje: solo los poseedores de $pk1 y $pk2 pueden descifrar
// el mensaje $sealed con las claves $ekeys[0] y $ekeys[1] (respectivamente).
openssl_seal($data, $sealed, $ekeys, array($pk1, $pk2));

if (openssl_seal($data, $sealed, $ekeys, array($pk1, $pk2), 'AES256', $iv) > 0) {
    // posiblemente almacenar los valores $sealed y $iv y utilizarlos más tarde en openssl_open
    echo "éxito\n";
}
?>

    
```php

## Véase también

`openssl_open`
