---
title: Transliterator::listIDs
description: Obtiene los identificadores de este transliterador
source_url: https://www.php.net/manual/es/transliterator.listids.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/transliterator/listids.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42590
---

Transliterator::listIDs

transliterator_list_ids

Obtiene los identificadores de este transliterador

## Descripción

Estilo orientado a objetos

```php
public static Transliterator::listIDs(): array
```php

Estilo procedimental

```php
transliterator_list_ids(): array
```

Devuelve un array que contiene todos los identificadores registrados para este transliterador.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` que contiene todos los identificadores registrados para este transliterador en caso de éxito o `false` si ocurre un error.

## Ejemplos

Obtención de los identificadores transliterador registrados

```php
<?php
print_r(Transliterator::listIDs());
?>

   
```

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => ASCII-Latin
        [1] => Accents-Any
        [2] => Amharic-Latin/BGN
        [3] => Any-Accents
        [4] => Any-Publishing
    ...
        [650] => Any-ps_Latn/BGN
        [651] => Any-tk/BGN
        [652] => Any-ch_FONIPA
        [653] => Any-cs_FONIPA
        [654] => Any-cy_FONIPA
    )

## Véase también

Transliterator::getErrorMessage, Transliterator::transliterate
