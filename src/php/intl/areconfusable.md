---
title: Spoofchecker::areConfusable
description: Verifica si los strings dados pueden ser confundidos
source_url: https://www.php.net/manual/es/spoofchecker.areconfusable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/spoofchecker/areconfusable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42450
---

Spoofchecker::areConfusable

Verifica si los strings dados pueden ser confundidos

## Descripción

```php
public Spoofchecker::areConfusable(string $string1, string $string2, [int $errorCode]): bool
```php

Se verifica si dos strings dados pueden ser fácilmente confundidos.

## Parámetros

`string1`  
Primer string a verificar.

`string2`  
Segundo string a verificar.

`errorCode`  
Esta variable es definida por referencia a un `int` que contiene un error, si es que hubo alguno.

## Valores devueltos

Retorna `true` si los dos strings dados pueden ser confundidos, y `false` en caso contrario.

## Ejemplos

Ejemplo `Spoofchecker::areConfusable`

```
<?php
$checker = new Spoofchecker();

$checker->areConfusable('google.com', 'goog1e.com'); // true
// La "l" minúscula puede ser confundida con el número uno

$checker->areConfusable('google.com', 'g00g1e.com'); // false
// Cero (0) no puede ser fácilmente confundido con la letra "o"

    
```php
