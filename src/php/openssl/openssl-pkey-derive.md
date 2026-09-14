---
title: openssl_pkey_derive
description: Calcula el secreto compartido para el valor público de la clave DH o
  ECDH remota y local
source_url: https://www.php.net/manual/es/function.openssl-pkey-derive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkey-derive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_revision: af71bd1bd
order: 59360
---

openssl_pkey_derive

Calcula el secreto compartido para el valor público de la clave DH o ECDH remota y local

## Descripción

```php
#[\SensitiveParameter] openssl_pkey_derive(OpenSSLAsymmetricKey $public_key, OpenSSLAsymmetricKey $private_key, [int $key_length]): string
```php

`openssl_pkey_derive` toma un conjunto de `public_key` y `private_key` y deriva un secreto compartido, para claves DH o EC.

## Parámetros

`public_key`  
`public_key` es la clave pública para la derivación. Consulte [Parámetros de clave/certificado](#openssl.certparams) para una lista de valores válidos.

`private_key`  
`private_key` es la clave privada para la derivación. Consulte [Parámetros de clave pública/privada](#openssl.certparams) para una lista de valores válidos.

`key_length`  
Si no es nulo, intentará establecer la longitud deseada del secreto derivado.

> [!CAUTION]
> Este parámetro está obsoleto y no debe utilizarse, ya que no funciona como se espera. Nunca devuelve un secreto más largo que el tamaño del primero Si la longitud deseada es menor que el tamaño del primero, trunca la longitud solo para las claves ECDH, pero falla para las claves DH.

## Valores devueltos

El secreto derivado en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                                    |
|---------|------------------------------------------------|
| 8.5.0   | El parámetro `key_length` ahora está obsoleto. |

## Ejemplos

Ejemplo de `openssl_pkey_derive`

```
<?php
// Carga la clave privada
$priv = openssl_pkey_get_private("-----BEGIN PRIVATE KEY-----
MIICJgIBADCCARcGCSqGSIb3DQEDATCCAQgCggEBAJLxRCaZ933uW+AXmabHFDDy
upojBIRlbmQLJZfigDaSA1f9YOTsIv+WwVFTX/J1mtCyx9uBcz0Nt2kmVwxWuc2f
VtCEMPsmLsVXX7xRUFLpyX1Y1IYGBVXQOoOvLWYQjpZgnx47Pkh1Ok1+smffztfC
0DCNt4KorWrbsPcmqBejXHN79KvWFjZmXOksRiNu/Bn76RiqvofC4z8Ri3kHXQG2
197JGZzzFXHadGC3xbkg8UxsNbYhVMKbm0iANfafUH7/hoS9UjAVQYtvwe7YNiW/
HnyfVCrKwcc7sadd8Iphh+3lf5P1AhaQEAMytanrzq9RDXKBxuvpSJifRYasZYsC
AQIEggEEAoIBAGwAYC2E81Y1U2Aox0U7u1+vBcbht/OO87tutMvc4NTLf6NLPHsW
cPqBixs+3rSn4fADzAIvdLBmogjtiIZoB6qyHrllF/2xwTVGEeYaZIupQH3bMK2b
6eUvnpuu4Ytksiz6VpXBBRMrIsj3frM+zUtnq8vKUr+TbjV2qyKR8l3eNDwzqz30
dlbKh9kIhZafclHfRVfyp+fVSKPfgrRAcLUgAbsVjOjPeJ90xQ4DTMZ6vjiv6tHM
hkSjJIcGhRtSBzVF/cT38GyCeTmiIA/dRz2d70lWrqDQCdp9ArijgnpjNKAAulSY
CirnMsGZTDGmLOHg4xOZ5FEAzZI2sFNLlcw=
-----END PRIVATE KEY-----
");

// Carga la clave pública
$pub = openssl_pkey_get_public("-----BEGIN PUBLIC KEY-----
MIICJDCCARcGCSqGSIb3DQEDATCCAQgCggEBAJLxRCaZ933uW+AXmabHFDDyupoj
BIRlbmQLJZfigDaSA1f9YOTsIv+WwVFTX/J1mtCyx9uBcz0Nt2kmVwxWuc2fVtCE
MPsmLsVXX7xRUFLpyX1Y1IYGBVXQOoOvLWYQjpZgnx47Pkh1Ok1+smffztfC0DCN
t4KorWrbsPcmqBejXHN79KvWFjZmXOksRiNu/Bn76RiqvofC4z8Ri3kHXQG2197J
GZzzFXHadGC3xbkg8UxsNbYhVMKbm0iANfafUH7/hoS9UjAVQYtvwe7YNiW/Hnyf
VCrKwcc7sadd8Iphh+3lf5P1AhaQEAMytanrzq9RDXKBxuvpSJifRYasZYsCAQID
ggEFAAKCAQAiCSBpxvGgsTorxAWtcAlSmzAJnJxFgSPef0g7OjhESytnc8G2QYmx
ovMt5KVergcitztWh08hZQUdAYm4rI+zMlAFDdN8LWwBT/mGKSzRkWeprd8E7mvy
ucqC1YXCMqmIwPySvLQUB/Dl8kgau7BLAnIJm8VP+MVrn8g9gghD0qRCgPgtEaDV
vocfgnOU43rhKnIgO0cHOKtw2qybSFB8QuZrYugq4j8Bwkrzh6rdMMeyMl/ej5Aj
c0wamOzuBDtXt0T9+Fx3khHaowjCc7xJZRgZCxg43SbqMWJ9lUg94I7+LTX61Gyv
dtlkbGbtoDOnxeNnN93gwQZngGYZYciu
-----END PUBLIC KEY-----
");

// Salida de la versión hexadecimal de la clave derivada
echo bin2hex(openssl_pkey_derive($pub,$priv));

    
```php
