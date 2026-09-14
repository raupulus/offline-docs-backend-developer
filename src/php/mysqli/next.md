---
title: mysqli_warning::next
description: Obtiene el siguiente aviso
source_url: https://www.php.net/manual/es/mysqli-warning.next.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_warning/next.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 035c126c0
order: 56020
---

mysqli_warning::next

Obtiene el siguiente aviso

## Descripción

```php
public mysqli_warning::next(): bool
```php

Modifica la información del aviso al siguiente aviso si es posible.

Una vez que el aviso se ha establecido en el siguiente aviso, nuevos valores para las propiedades `message`, `sqlstate` y `errno` de `mysqli_warning` están disponibles.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna `true` si el siguiente aviso se ha recuperado con éxito. Si no hay más avisos, retornará `false`.
