---
title: pcntl_unshare
description: Disocia partes del contexto de ejecución del proceso
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-unshare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: d7c1097cc
order: 61410
---

pcntl_unshare

Disocia partes del contexto de ejecución del proceso

## Descripción

```php
pcntl_unshare(int $flags): bool
```php

`pcntl_unshare` permite a un proceso disociar partes de su contexto de ejecución que actualmente están compartidas con otros procesos. El uso principal de `pcntl_unshare` es permitir a un proceso controlar su contexto de ejecución compartido sin crear un nuevo proceso.

## Parámetros

`flags`  
El parámetro `flags` es una máscara de bits que especifica qué partes del contexto de ejecución deben ser disociadas. Este parámetro se especifica combinando por OR una o más de las constantes `CLONE_*` siguientes: `CLONE_NEWNS`, `CLONE_NEWIPC`, `CLONE_NEWUTS`, `CLONE_NEWNET`, `CLONE_NEWPID`, `CLONE_NEWUSER`, `CLONE_NEWCGROUP`

## Valores devueltos

Devuelve `0` en caso de éxito, `-1` en caso contrario. En caso de fallo, define un código de error, que puede ser recuperado con `pcntl_get_last_error`.

## Véase también

[Constante PCNTL](#pcntl.constants.clone), `pcntl_get_last_error`
