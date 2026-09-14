---
title: Random\Engine\Secure::generate
description: Genera datos aleatorios de manera criptográficamente segura
source_url: https://www.php.net/manual/es/random-engine-secure.generate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/engine/secure/generate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: true
translation_revision: 02580ba1b
order: 68060
---

Random\Engine\Secure::generate

Genera datos aleatorios de manera criptográficamente segura

## Descripción

```php
public Random\Engine\Secure::generate(): string
```php

Devuelve datos aleatorios de manera criptográficamente segura.

Las fuentes de aleatoriedad por orden de prioridad son las siguientes:

- Linux: [getrandom()](http://man7.org/linux/man-pages/man2/getrandom.2.html), `/dev/urandom`

- FreeBSD \>= 12 (PHP \>= 7.3): [getrandom()](http://man7.org/linux/man-pages/man2/getrandom.2.html), `/dev/urandom`

- Windows (PHP \>= 7.2): [CNG-API](https://docs.microsoft.com/en-us/windows/desktop/SecCNG/cng-portal)

  Windows: [CryptGenRandom](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379942(v=vs.85).aspx)

- macOS (PHP \>= 8.2; \>= 8.1.9; \>= 8.0.22 si CCRandomGenerateBytes está disponible en el momento de la compilación): CCRandomGenerateBytes()

  macOS (PHP \>= 8.1; \>= 8.0.2): arc4random_buf(), `/dev/urandom`

- NetBSD \>= 7 (PHP \>= 7.1; \>= 7.0.1): arc4random_buf(), `/dev/urandom`

- OpenBSD \>= 5.5 (PHP \>= 7.1; \>= 7.0.1): arc4random_buf(), `/dev/urandom`

- DragonflyBSD (PHP \>= 8.1): [getrandom()](http://man7.org/linux/man-pages/man2/getrandom.2.html), `/dev/urandom`

- Solaris (PHP \>= 8.1): [getrandom()](http://man7.org/linux/man-pages/man2/getrandom.2.html), `/dev/urandom`

- Cualquier combinación de un sistema operativo y una versión de PHP no mencionada anteriormente: `/dev/urandom`.

- Si ninguna de las fuentes de aleatoriedad está disponible o todas fallan al generar aleatoriedad, se lanzará una excepción de tipo `Random\RandomException` .

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una string que contiene `PHP_INT_SIZE` bytes de aleatoriedad criptográficamente segura.

## Errores/Excepciones

- Si no se encuentra ninguna fuente de datos aleatorios, se lanzará una `Random\RandomException`.
