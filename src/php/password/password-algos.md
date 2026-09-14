---
title: password_algos
description: Obtiene todos los identificadores de los algoritmos de hash de contraseñas
  disponibles
source_url: https://www.php.net/manual/es/function.password-algos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/password/functions/password-algos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: password
translation_status: ready
translation_reviewed: false
translation_revision: d4e842ad1
order: 61090
---

password_algos

Obtiene todos los identificadores de los algoritmos de hash de contraseñas disponibles

## Descripción

```php
password_algos(): array
```php

Devuelve una lista completa de todos los identificadores de los algoritmos de hash de contraseñas registrados, en forma de un `array` de `string`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve todos los identificadores de los algoritmos de hash de contraseñas disponibles.

## Ejemplos

Uso básico de la función `password_algos`

```
<?php
print_r(password_algos());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => 2y
        [1] => argon2i
        [2] => argon2id
    )
