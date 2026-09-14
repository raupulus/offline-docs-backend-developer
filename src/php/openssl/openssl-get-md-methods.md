---
title: openssl_get_md_methods
description: Obtiene la lista de métodos digest disponibles
source_url: https://www.php.net/manual/es/function.openssl-get-md-methods.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-get-md-methods.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: b8758b060
order: 59210
---

openssl_get_md_methods

Obtiene la lista de métodos digest disponibles

## Descripción

```php
openssl_get_md_methods([bool $aliases]): array
```php

Obtiene la lista de métodos digest disponibles.

## Parámetros

`aliases`  
Pásese `true` si se desean incluir los alias de digest en el array devuelto.

## Valores devueltos

Un `array` de los métodos digest disponibles.

## Ejemplos

Ejemplo `openssl_get_md_methods`

Muestra cómo son los digests disponibles, así como los alias disponibles.

```
<?php
$digests             = openssl_get_md_methods();
$digests_and_aliases = openssl_get_md_methods(true);
$digest_aliases      = array_diff($digests_and_aliases, $digests);

print_r($digests);

print_r($digest_aliases);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => DSA
        [1] => DSA-SHA
        [2] => MD2
        [3] => MD4
        [4] => MD5
        [5] => RIPEMD160
        [6] => SHA
        [7] => SHA1
        [8] => SHA224
        [9] => SHA256
        [10] => SHA384
        [11] => SHA512
        [12] => dsaEncryption
        [13] => dsaWithSHA
        [14] => ecdsa-with-SHA1
        [15] => md2
        [16] => md4
        [17] => md5
        [18] => ripemd160
        [19] => sha
        [20] => sha1
        [21] => sha224
        [22] => sha256
        [23] => sha384
        [24] => sha512
    )
    Array
    (
        [2] => DSA-SHA1
        [3] => DSA-SHA1-old
        [4] => DSS1
        [9] => RSA-MD2
        [10] => RSA-MD4
        [11] => RSA-MD5
        [12] => RSA-RIPEMD160
        [13] => RSA-SHA
        [14] => RSA-SHA1
        [15] => RSA-SHA1-2
        [16] => RSA-SHA224
        [17] => RSA-SHA256
        [18] => RSA-SHA384
        [19] => RSA-SHA512
        [28] => dsaWithSHA1
        [29] => dss1
        [32] => md2WithRSAEncryption
        [34] => md4WithRSAEncryption
        [36] => md5WithRSAEncryption
        [37] => ripemd
        [39] => ripemd160WithRSA
        [40] => rmd160
        [43] => sha1WithRSAEncryption
        [45] => sha224WithRSAEncryption
        [47] => sha256WithRSAEncryption
        [49] => sha384WithRSAEncryption
        [51] => sha512WithRSAEncryption
        [52] => shaWithRSAEncryption
        [53] => ssl2-md5
        [54] => ssl3-md5
        [55] => ssl3-sha1
    )

## Véase también

`openssl_digest`, `openssl_get_cipher_methods`
