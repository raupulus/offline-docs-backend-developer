---
title: openssl_spki_export_challenge
description: Exporta el challenge asociado con la clave pública firmada
source_url: https://www.php.net/manual/es/function.openssl-spki-export-challenge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-spki-export-challenge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 7f99d5e48
order: 59510
---

openssl_spki_export_challenge

Exporta el challenge asociado con la clave pública firmada

## Descripción

```php
openssl_spki_export_challenge(string $spki): string
```php

Exporta el challenge asociado con la clave pública firmada.

## Parámetros

`spki`  
Una clave pública firmada válida

## Valores devueltos

Devuelve el challenge asociado en forma de string o `false` en caso de error.

## Errores/Excepciones

Emite una advertencia de nivel `E_WARNING` si se pasa un argumento inválido a través del parámetro `spki`.

## Ejemplos

Ejemplo con `openssl_spki_export_challenge`

Extrae el challenge asociado en forma de string o `null` en caso de error.

```
<?php
$pkey = openssl_pkey_new('secret password');
$spkac = openssl_spki_new($pkey, 'challenge string');
$challenge = openssl_spki_export_challenge(preg_replace('/SPKAC=/', '', $spkac));
?>

   
```php

Ejemplo con `openssl_spki_export_challenge` desde \<keygen\>

Extrae el challenge asociado de un elemento \<keygen\>

```
<?php
$challenge = openssl_spki_export_challenge(preg_replace('/SPKAC=/', '', $_POST['spkac']));
?>
<keygen name="spkac" challenge="challenge string" keytype="RSA">

   
```php

## Véase también

`openssl_spki_new`, `openssl_spki_verify`, `openssl_spki_export`, `openssl_get_md_methods`, `openssl_csr_new`, `openssl_csr_sign`
