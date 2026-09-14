---
title: Gender\Gender::country
description: Obtiene la representación textual de un país
source_url: https://www.php.net/manual/es/gender-gender.country.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gender/gender/country.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gender
translation_status: ready
translation_reviewed: false
translation_revision: 1742a682c
order: 26030
---

Gender\Gender::country

Obtiene la representación textual de un país

## Descripción

```php
public Gender\Gender::country(int $country): array
```php

Obtiene la representación textual de un país desde la constante de la clase Gender.

## Parámetros

`country`  
Identificador del país (corresponde a una constante de la clase `Gender\Gender`).

## Valores devueltos

Devuelve un array que contiene los nombres cortos y largos del país en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con Gender\Gender::country

```
$gender = new Gender\Gender;
var_dump($gender->country(Gender\Gender::BRITAIN));

   
```php

El ejemplo anterior mostrará:

    array(2) {
      'country_short' =>
      string(2) "UK"
      'country' =>
      string(13) "Great Britain"
    }
