---
title: openssl_open
description: Abre datos sellados
source_url: https://www.php.net/manual/es/function.openssl-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 730fd5c3d
order: 59240
---

openssl_open

Abre datos sellados

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] openssl_open(string $data, string $output, string $encrypted_key, OpenSSLAsymmetricKey $private_key, string $cipher_algo, [string $iv]): bool
```php

La `openssl_open` abre (descifra) `data` utilizando una clave de envoltura que se descifra a partir de `encrypted_key` utilizando `private_key`. La descifrado se realiza mediante `cipher_algo` y `iv`. El IV es requerido únicamente si el método de cifrado lo exige. La función llena `output` con los datos descifrados. La clave de envoltura generalmente se genera cuando los datos son sellados utilizando una clave pública asociada a la clave privada. Consulte `openssl_seal` para más información.

## Parámetros

`data`  
Los datos sellados.

`output`  
Si la llamada tiene éxito, los datos abiertos son devueltos en este parámetro.

`encrypted_key`  
La clave simétrica cifrada que puede ser descifrada utilizando `private_key`

`private_key`  
La clave privada utilizada para descifrar `encrypted_key`.

`cipher_algo`  
El método de cifrado utilizado para el descifrado de `data`.

> [!CAUTION]
> El valor por omisión para las versiones de PHP anteriores a 8.0 es (`'RC4'`), que es considerada como no segura. Se recomienda fuertemente especificar explícitamente un método de cifrado seguro.

`iv`  
El vector de inicialización utilizado para el descifrado de `data`. Es requerido si el método de cifrado necesita un IV. Esto puede ser determinado llamando a `openssl_cipher_iv_length` con `cipher_algo`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `private_key` ahora acepta una instancia de `OpenSSLAsymmetricKey` o `OpenSSLCertificate`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key` o `OpenSSL X.509 CSR`. |
| 8.0.0 | `cipher_algo` ya no es un parámetro opcional. |

## Ejemplos

Ejemplo con `openssl_open`

```
<?php

// Se asume que $sealed, $env_key y $iv contienen los datos sellados,
// la clave de envoltura y el IV. Todos proporcionados por el remitente.

// Obtener la clave privada desde el archivo ubicado en private_key.pem
$pkey = openssl_get_privatekey("file://private_key.pem");

// Descifrado de los datos: se colocan en $open
if (openssl_open($sealed, $open, $env_key, $pkey, 'AES256', $iv)) {
    echo "Aquí están los datos descifrados: ", $open;
} else {
    echo "No se pudo descifrar los datos";
}

?>

    
```php

## Véase también

`openssl_seal`
