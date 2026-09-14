---
title: Phar::getSignature
description: Devuelve la firma MD5/SHA1/SHA256/SHA512 de un archivo Phar
source_url: https://www.php.net/manual/es/phar.getsignature.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/getSignature.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64130
---

Phar::getSignature

Devuelve la firma MD5/SHA1/SHA256/SHA512 de un archivo Phar

## Descripción

```php
public Phar::getSignature(): array
```php

Devuelve la firma de verificación de un archivo phar en forma de un string hexadecimal.

## Parámetros

## Valores devueltos

Un array con la firma del archivo abierto con el `hash` como clave y "`MD5`", "`SHA-1`", "`SHA-256`" o "`SHA-512`" como `hash_type`. Esta firma es un hash calculado a partir del contenido completo del archivo; puede ser utilizada para verificar la integridad del archivo. Una firma válida es absolutamente requerida para todos los archivos phar ejecutables si la variable INI [phar.require_hash](#ini.phar.require-hash) vale `true`. Si no hay firma, la función devuelve `false`
