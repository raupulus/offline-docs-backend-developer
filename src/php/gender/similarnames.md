---
title: Gender\Gender::similarNames
description: Obtiene nombres similares
source_url: https://www.php.net/manual/es/gender-gender.similarnames.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gender/gender/similarnames.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gender
translation_status: ready
translation_reviewed: false
translation_revision: 1742a682c
order: 26060
---

Gender\Gender::similarNames

Obtiene nombres similares

## Descripción

```php
public Gender\Gender::similarNames(string $name, [int $country]): array
```php

Obtiene nombres similares para el nombre y el país proporcionados.

## Parámetros

`name`  
Nombre a verificar.

`country`  
Identificador del país, identificado por la constante de clase Gender. Si se omite, se utilizará ANY_COUNTRY.

## Valores devueltos

Devuelve un array que contiene los nombres similares encontrados.
