---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/hash.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: false
translation_revision: e32577662
order: 29430
---

## Instalación/Configuración

## Instalación

La extensión Hash es una extensión principal de PHP, por lo que siempre está habilitada.

Antes de PHP 7.4.0, la extensión Hash se incluía y compilaba con PHP por defecto, pero podía deshabilitarse explícitamente usando `--disable-hash`.

Antes de 5.1.2, la extensión Hash se instalaba como un [módulo PECL](https://pecl.php.net/package/hash).

## Tipos de recursos

Esta extensión define un recurso de Contexto de Hashing devuelto por `hash_init`.
