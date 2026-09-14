---
title: openssl_spki_export
description: Exporta un PEM válido formateado como una clave pública firmada
source_url: https://www.php.net/manual/es/function.openssl-spki-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-spki-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 497c40ac1
order: 59520
---

openssl_spki_export

Exporta un

PEM

válido formateado como una clave pública firmada

## Descripción

```php
openssl_spki_export(string $spki): string
```php

Exporta un PEM válido formateado como una clave pública firmada.

## Parámetros

`spki`  
Una clave pública firmada válida

## Valores devueltos

Devuelve el PEM asociado formateado como clave pública, o `false` si se produce un error.

## Errores/Excepciones

Emite una alerta de nivel `E_WARNING` si un argumento no válido es pasado mediante el parámetro `spki`.

## Ejemplos

Ejemplo con `openssl_spki_export`

Extrae el PEM asociado formateado como clave pública, o `null` en caso de fallo.

```
<?php
$pkey = openssl_pkey_new('secret password');
$spkac = openssl_spki_new($pkey, 'challenge string');
$pubKey = openssl_spki_export(preg_replace('/SPKAC=/', '', $spkac));

if ($pubKey) {
    echo $pubKey;
}
?>

   
```php

Ejemplo con `openssl_spki_export` desde \<keygen\>

Extrae el PEM asociado formateado como clave pública, procedente de un elemento \<keygen\>

```
<?php
$spkac = openssl_spki_export(preg_replace('/SPKAC=/', '', $_POST['spkac']));
if ($spkac != NULL) {
    echo $spkac;
} else {
    echo "La extracción de la clave pública ha fallado";
}
?>
<keygen name="spkac" challenge="challenge string" keytype="RSA">

   
```php

## Véase también

`openssl_spki_new`, `openssl_spki_verify`, `openssl_spki_export_challenge`, `openssl_get_md_methods`, `openssl_csr_new`, `openssl_csr_sign`
