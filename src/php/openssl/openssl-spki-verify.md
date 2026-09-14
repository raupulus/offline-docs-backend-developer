---
title: openssl_spki_verify
description: Verifica una clave pública firmada y realiza un desafío
source_url: https://www.php.net/manual/es/function.openssl-spki-verify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-spki-verify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 7f99d5e48
order: 59540
---

openssl_spki_verify

Verifica una clave pública firmada y realiza un desafío

## Descripción

```php
openssl_spki_verify(string $spki): bool
```php

Verifica una clave pública firmada y realiza un desafío.

## Parámetros

`spki`  
Una clave pública firmada válida

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite una alerta de nivel `E_WARNING` si un argumento inválido es pasado al parámetro `spkac`.

## Ejemplos

Ejemplo con `openssl_spki_verify`

Valida una clave pública firmada existente y realiza un desafío

```
<?php
$pkey = openssl_pkey_new('secret password');
$spkac = openssl_spki_new($pkey, 'challenge string');

if (openssl_spki_verify(preg_replace('/SPKAC=/', '', $spkac))) {
    echo $spkac;
} else {
    echo "La validación SPKAC ha fallado";
}
?>

   
```php

Ejemplo con `openssl_spki_verify` desde \<keygen\>

Valida una clave pública firmada existente procedente de un elemento \<keygen\>

```
<?php
if (openssl_spki_verify(preg_replace('/SPKAC=/', '', $_POST['spkac']))) {
    echo $spkac;
} else {
    echo "La validación SPKAC ha fallado";
}
?>
<keygen name="spkac" challenge="challenge string" keytype="RSA">

   
```php

## Véase también

`openssl_spki_new`, `openssl_spki_export_challenge`, `openssl_spki_export`, `openssl_get_md_methods`, `openssl_csr_new`, `openssl_csr_sign`
