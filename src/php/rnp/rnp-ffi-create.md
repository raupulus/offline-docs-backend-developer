---
title: rnp_ffi_create
description: Crear un objeto de nivel superior utilizado para interactuar con la biblioteca
source_url: https://www.php.net/manual/es/function.rnp-ffi-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/functions/rnp-ffi-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72130
---

rnp_ffi_create

Crear un objeto de nivel superior utilizado para interactuar con la biblioteca

## Descripción

```php
rnp_ffi_create(string $pub_format, string $sec_format): RnpFFI
```php

## Parámetros

`pub_format`  
El formato del llavero de claves públicas, RNP_KEYSTORE_GPG o otra constante RNP_KEYSTORE\_\*.

`sec_format`  
El formato del llavero de claves secretas, RNP_KEYSTORE_GPG o otra constante RNP_KEYSTORE\_\*.

## Valores devueltos

Devuelve un objeto `RnpFFI` en caso de éxito o `false` si ocurre un error.
