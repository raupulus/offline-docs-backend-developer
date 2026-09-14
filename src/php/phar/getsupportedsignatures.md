---
title: Phar::getSupportedSignatures
description: Devuelve un array de los tipos de firma soportados
source_url: https://www.php.net/manual/es/phar.getsupportedsignatures.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/getSupportedSignatures.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64160
---

Phar::getSupportedSignatures

Devuelve un array de los tipos de firma soportados

## Descripción

```php
final public static Phar::getSupportedSignatures(): array
```php

Devuelve un array de los tipos de firma soportados

## Parámetros

No se admiten argumentos.

## Valores devueltos

Devuelve un array que contiene uno o más de los tipos `MD5`, `SHA-1`, `SHA-256`, `SHA-512`.

## Véase también

`Phar::getSignature`, `Phar::setSignatureAlgorithm`
