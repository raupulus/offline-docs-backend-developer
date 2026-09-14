---
title: openssl_digest
description: Calcula un digest
source_url: https://www.php.net/manual/es/function.openssl-digest.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-digest.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: d1e3ea622
order: 59140
---

openssl_digest

Calcula un digest

## Descripción

```php
openssl_digest(string $data, string $digest_algo, [bool $binary]): string
```php

Calcula un hash digest para los datos de entrada utilizando el método proporcionado. Devuelve un string bruto o hexadecimal.

## Parámetros

`data`  
Los datos.

`digest_algo`  
El método digest a utilizar, por ejemplo "SHA256". Consulte `openssl_get_md_methods` para obtener la lista de métodos de digest disponibles.

`binary`  
Pase a `true` y se devolverá un dato bruto, de lo contrario el valor devuelto será hexadecimal.

## Valores devueltos

Devuelve el valor en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si se pasa un algoritmo desconocido al argumento `digest_algo`.

## Véase también

`openssl_get_md_methods`
