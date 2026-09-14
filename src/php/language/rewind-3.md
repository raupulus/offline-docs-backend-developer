---
title: Iterator::rewind
description: Rebobine la Iterator al primer elemento
source_url: https://www.php.net/manual/es/iterator.rewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/iterator/rewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 7fbb16f53
order: 3760
---

Iterator::rewind

Rebobine la Iterator al primer elemento

## Descripción

```php
public Iterator::rewind(): void
```php

Rebobina de nuevo al primer elemento de la Iterator.

> [!NOTE]
> Este es el *primer* método llamado cuando se inicia un [`foreach`](#control-structures.foreach) bucle. *No* va a ser ejecutado *despues* [`foreach`](#control-structures.foreach) bucle.
>
> Como [`foreach`](#control-structures.foreach) siempre llama a rewind antes de iniciar la iteración, avanzar manualmente la posición del iterador (por ejemplo mediante SplFileObject::seek) será reiniciado.
>
> Para iterar sin rebobinar el iterador, envuélvalo en un `NoRewindIterator`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Cualquier valor devuelto se pasa por alto.
