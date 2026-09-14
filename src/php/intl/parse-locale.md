---
title: Locale::parseLocale
description: Devuelve los subelementos de la configuración regional
source_url: https://www.php.net/manual/es/locale.parselocale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/parse-locale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41990
---

Locale::parseLocale

locale_parse

Devuelve los subelementos de la configuración regional

## Descripción

Estilo orientado a objetos

```php
public static Locale::parseLocale(string $locale): array
```php

Estilo procedimental

```php
locale_parse(string $locale): array
```

Devuelve un array de pares clave-valor para los elementos del subtag de la configuración regional.

## Parámetros

`locale`  
La configuración regional de la cual extraer el array. Tenga en cuenta que 'variant' y 'private' pueden tomar hasta 15 valores como máximo, mientras que 'extlang' puede tomar hasta 3 valores.

## Valores devueltos

Devuelve un array que contiene la lista de pares clave-valor, donde las claves son los nombres de los elementos, y los valores son su valor asociado. El array está ordenado de la misma manera que los elementos en la configuración regional, por ejemplo, si las variantes son '-varX-varY-varZ' entonces el array devuelto contendrá variant0=\>varX, variant1=\>varY, variant2=\>varZ, etc.

Devuelve `null` cuando el tamaño de `locale` excede `INTL_MAX_LOCALE_LEN`.

## Ejemplos

Ejemplo con `locale_parse`, procedimental

```php
<?php
$arr = locale_parse('sl-Latn-IT-nedis');
if ($arr) {
    foreach ($arr as $key => $value) {
        echo "$key : $value , ";
    }
}
?>

   
```

Ejemplo con `locale_parse`, POO

```php
<?php
$arr = Locale::parseLocale('sl-Latn-IT-nedis');
if ($arr) {
    foreach ($arr as $key => $value) {
        echo "$key : $value , ";
    }
}
?>

   
```

El ejemplo anterior mostrará:

    language : sl , script : Latn , region : IT , variant0 : NEDIS ,

      

## Véase también

`locale_compose`
