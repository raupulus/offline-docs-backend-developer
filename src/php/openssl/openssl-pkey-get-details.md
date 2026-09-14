---
title: openssl_pkey_get_details
description: Devuelve un array que contiene los detalles de la clave
source_url: https://www.php.net/manual/es/function.openssl-pkey-get-details.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-pkey-get-details.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 3b06ef4bb
order: 59400
---

openssl_pkey_get_details

Devuelve un array que contiene los detalles de la clave

## Descripción

```php
openssl_pkey_get_details(OpenSSLAsymmetricKey $key): array
```php

Esta función devuelve los detalles de la clave (bits, key, type).

## Parámetros

`key`  
Recurso que contiene la clave.

## Valores devueltos

Devuelve un array con los detalles de la clave en caso de éxito, o `false` en caso de fallo. El array devuelto contiene los índices `bits` (número de bits), `key` (representación en forma de `string` de la clave pública) y `type` (tipo de clave que es uno de `OPENSSL_KEYTYPE_RSA`, `OPENSSL_KEYTYPE_DSA`, `OPENSSL_KEYTYPE_DH`, `OPENSSL_KEYTYPE_EC`, `OPENSSL_KEYTYPE_X25519`, `OPENSSL_KEYTYPE_ED25519`, `OPENSSL_KEYTYPE_X448`, `OPENSSL_KEYTYPE_ED448`, o `-1` significando desconocido).

Dependiendo del tipo de claves utilizadas, pueden devolverse detalles adicionales. Tenga en cuenta que algunos elementos pueden no estar siempre disponibles.

- `OPENSSL_KEYTYPE_RSA`, se devuelve una clave de array adicional llamada `"rsa"`, que contiene los datos de la clave.

  | Clave    | Descripción                       |
  |----------|-----------------------------------|
  | `"n"`    | módulo                            |
  | `"e"`    | exponente público                 |
  | `"d"`    | exponente privado                 |
  | `"p"`    | número primo 1                    |
  | `"q"`    | número primo 2                    |
  | `"dmp1"` | exponent1, d mod (p-1)            |
  | `"dmq1"` | exponent2, d mod (q-1)            |
  | `"iqmp"` | coeficiente, (inverso de q) mod p |

- `OPENSSL_KEYTYPE_DSA`, se devuelve una clave de array adicional llamada `"dsa"`, que contiene los datos de la clave.

  | Clave        | Descripción                                  |
  |--------------|----------------------------------------------|
  | `"p"`        | número primo (público)                       |
  | `"q"`        | 160-bit número sub-prime, q \| p-1 (público) |
  | `"g"`        | generador del subgrupo (público)             |
  | `"priv_key"` | clave privada x                              |
  | `"pub_key"`  | clave pública y = g^x                        |

- `OPENSSL_KEYTYPE_DH`, se devuelve una clave de array adicional llamada `"dh"`, que contiene los datos de la clave.

  | Clave        | Descripción                   |
  |--------------|-------------------------------|
  | `"p"`        | número primo (compartido)     |
  | `"g"`        | generador de Z_p (compartido) |
  | `"priv_key"` | valor privado DH x            |
  | `"pub_key"`  | valor público DH g^x          |

- `OPENSSL_KEYTYPE_X25519`, `OPENSSL_KEYTYPE_ED25519`, `OPENSSL_KEYTYPE_X448`, o `OPENSSL_KEYTYPE_ED448`, se devuelve una clave adicional en el array llamada `"x25519"`, `"ed25519"`, `"x448"`, o `"ed448"` respectivamente, que contiene los datos de la clave.

  | Clave        | Descripción   |
  |--------------|---------------|
  | `"priv_key"` | clave privada |
  | `"pub_key"`  | clave pública |

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se añadió el soporte para claves basadas en Curve25519 y Curve448. Más específicamente, se introdujeron los campos `x25519`, `ed25519`, `x448` y `ed448`. |
| 8.0.0 | `key` ahora acepta una instancia de `OpenSSLAsymmetricKey`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key`. |
