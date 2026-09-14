---
title: Spoofchecker::isSuspicious
description: Verifica si un texto contiene caracteres sospechosos
source_url: https://www.php.net/manual/es/spoofchecker.issuspicious.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/spoofchecker/issuspicious.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42470
---

Spoofchecker::isSuspicious

Verifica si un texto contiene caracteres sospechosos

## Descripción

```php
public Spoofchecker::isSuspicious(string $string, [int $errorCode]): bool
```php

Verifica si el string dado contiene caracteres sospechosos como letras que son casi idénticas visualmente, pero son caracteres Unicode de diferentes conjuntos.

## Parámetros

`string`  
String a probar.

`errorCode`  
Esta variable se define por referencia a un `int` que contiene un error, si lo hubiera.

## Valores devueltos

Devuelve `true` si hay caracteres sospechosos, y `false` en caso contrario.

## Ejemplos

Ejemplo `Spoofchecker::isSuspicious`

```
<?php
$checker = new Spoofchecker();

$checker->isSuspicious('google.com'); // FALSE: solo caracteres ASCII

$checker->isSuspicious('Рaypal.com'); // TRUE
// La primera letra es Cirílico, no una "P" latina

    
```php
