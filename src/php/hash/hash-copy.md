---
title: hash_copy
description: Copia un contexto de hachado
source_url: https://www.php.net/manual/es/function.hash-copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: false
translation_revision: 584a9fb97
order: 29240
---

hash_copy

Copia un contexto de hachado

## Descripción

```php
hash_copy(HashContext $context): HashContext
```php

## Parámetros

`context`  
Contexto de hachado, retornado por la función `hash_init`.

## Valores devueltos

Retorna una copia del contexto de hash.

## Historial de cambios

| Versión | Descripción                                                      |
|---------|------------------------------------------------------------------|
| 7.2.0   | Acepta y retorna una clase `HashContext` en lugar de un recurso. |

## Ejemplos

Ejemplo con `hash_copy`

```
<?php
$context = hash_init("sha256");
hash_update($context, "The quick brown fox ");

/* copia el contexto para poder continuar utilizándolo */
$copy_context = hash_copy($context);

echo hash_final($context), "\n";

hash_update($copy_context, "jumped over the lazy dog.");
echo hash_final($copy_context), "\n";
?>

    
```php

El ejemplo anterior mostrará:

    b29d66e56ed90cce9b0165c43fedec612b60a071974d8be4513e18580d55b5bd
    68b1282b91de2c054c36629cb8dd447f12f096d3e3c587978dc2248444633483
