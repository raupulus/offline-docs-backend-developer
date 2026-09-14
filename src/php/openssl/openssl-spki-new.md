---
title: openssl_spki_new
description: Genera una clave pública firmada y realiza un desafío
source_url: https://www.php.net/manual/es/function.openssl-spki-new.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-spki-new.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 5bc68add3
order: 59530
---

openssl_spki_new

Genera una clave pública firmada y realiza un desafío

## Descripción

```php
#[\SensitiveParameter] openssl_spki_new(OpenSSLAsymmetricKey $private_key, string $challenge, [int $digest_algo]): string
```php

Genera una clave pública firmada utilizando un algoritmo de hash especificado.

## Parámetros

`private_key`  
`private_key` debe ser una clave privada que haya sido previamente generada por la función `openssl_pkey_new` (o de lo contrario, obtenida desde una función de la familia openssl_pkey). La porción pública de la clave será utilizada para firmar el CSR.

`challenge`  
El desafío asociado al SPKAC

`digest_algo`  
El algoritmo digest. Ver openssl_get_md_method().

## Valores devueltos

Devuelve una clave pública firmada en forma de string o `false` en caso de fallo.

## Errores/Excepciones

Emite una alerta de nivel `E_WARNING` si un algoritmo con una firma desconocida es pasado mediante el parámetro `digest_algo`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `private_key` ahora acepta una instancia de `OpenSSLAsymmetricKey`; anteriormente, se aceptaba un `resource` de tipo `OpenSSL key`. |

## Ejemplos

Ejemplo con `openssl_spki_new`

Genera un nuevo SPKAC con el digest por defecto (MD5)

```
<?php
$pkey = openssl_pkey_new('secret password');
$spkac = openssl_spki_new($pkey, 'testing');

if ($spkac !== NULL) {
    echo $spkac;
} else {
    echo "La generación de SPKAC ha fallado";
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    MIICRzCCAS8wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDM3V3sS4o4
    mB9dczziRnjGAmSp+JwPrHoYMAFGvDNmZGyiWfU586X4BKs++BAj7e/FsAfno0Hd
    hN9FwpCNFSox30L03nQvLYJE7f/WqigwBeMRT7Op/xvFks4sT70xP2HRYv4KqP9a
    WRcKU6cFH8VxhFhqM2txEIxZKdFLaL28yT7bEDmcglf4JLDdgNMb9rET1dkgtKE6
    dOaJHPGjf1uvnOH4YwkQr7n4sLUR3Kdbh0ZJAFuQVDZulo+LLzxBBkqJJcB6FhF+
    oXCdHTKZnqAhpWDz+NXYytAmevab6IYm5TWPWsJUv1YKJA5lg2mXbbloIZlN9Mgc
    i9fi03bdw+crAgMBAAEWB3Rlc3RpbmcwDQYJKoZIhvcNAQEEBQADggEBALyUvP/o
    pPSoWBlorFyZ2RnGwKf9qMpE0q2IJP7G3oDR4LyK/m933DUiZ+YnqThrH/CWb4Ek
    y5I3OCyl3S4wCuU1ibZZwDVwYShr5ELp0J9PEf7qMQZOhNsizoC7k+Czb2xB6hYW
    sKfsfTKm3cXBtH3fdgc/Z1Z7VSWnAzYo38snqm72NTf5yFRnrQdphNNXi+kn1zHA
    lxXRyFDXHOcYsOnwAWfyXFA4QDHQ0ezz0UoCY8gJXovcZb4GRYqOLUAsF2HcNboy
    29WN8VqE29sL9QxVZFlwMcqyoLcNnyw38GvNvAGqSvzzbnEFP2MAQXJVe0H0hdp/
    MML5G2iNVgNozAo=

## Véase también

`openssl_spki_verify`, `openssl_spki_export_challenge`, `openssl_spki_export`, `openssl_get_md_methods`, `openssl_csr_new`, `openssl_csr_sign`
