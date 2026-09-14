---
title: Locale::composeLocale
description: Retorna un identificador de configuración regional correcto
source_url: https://www.php.net/manual/es/locale.composelocale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/compose-locale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41840
---

Locale::composeLocale

locale_compose

Retorna un identificador de configuración regional correcto

## Descripción

Estilo orientado a objetos

```php
public static Locale::composeLocale(array $subtags): string
```php

Estilo procedimental

```php
locale_compose(array $subtags): string
```

Retorna un identificador de configuración regional correcto, ordenado y delimitado, con las claves para identificar las particularidades regionales, y los valores asociados a estas subconfiguraciones regionales.

## Parámetros

`subtags`  
Un `array` que contiene la lista de pares clave-valor, donde las claves representan los identificadores de subconfiguraciones regionales, y sus valores asociados son los valores de los subtags.

> [!NOTE]
> Los subtags `'variant'` y `'private'` pueden tomar hasta 15 valores mientras que `'extlang'` no puede tomar más de 3 valores. Por ejemplo, las variantes están permitidas con un sufijo que va de 0 a 14. Por lo tanto, las claves del array son `variant0`, `variant1`, …, `variant14`. En el identificador de configuración regional retornado, los subtags están ordenados por sufijo, con `variant0` seguido de `variant1` seguido de `variant2` y así sucesivamente.
>
> Alternativamente, los valores de `'variant'`, `'private'` y `'extlang'` pueden ser especificados como un array bajo una clave específica (por ejemplo, `'variant'`). En este caso no se aplica ninguna limitación sobre el número de subtags reconocidos.

## Valores devueltos

El identificador de configuración regional correspondiente, o `false` cuando `subtags` está vacío.

## Ejemplos

Ejemplo con `locale_compose`, procedimental

```php
<?php
$arr = array(
    'language'=>'en',
    'script'  =>'Hans',
    'region'  =>'CN',
    'variant2'=>'rozaj',
    'variant1'=>'nedis',
    'private1'=>'prv1',
    'private2'=>'prv2'
);
echo locale_compose($arr);
?>

   
```

Ejemplo con `locale_compose`, POO

```php
<?php
$arr = array(
    'language'=>'en',
    'script'  =>'Hans',
    'region'  =>'CN',
    'variant2'=>'rozaj',
    'variant1'=>'nedis',
    'private1'=>'prv1',
    'private2'=>'prv2'
);
echo Locale::composeLocale($arr);
?>

   
```

El ejemplo anterior mostrará:

    Locale: en_Hans_CN_nedis_rozaj_x_prv1_prv2

Límites de los Subtags

Si `subtags` se proporciona como claves diferentes con un sufijo numérico, las claves no soportadas son ignoradas silenciosamente (en este caso `'extlang3'`), y ordenadas en el resultado por el sufijo numérico. No hay límites, si los subtags se proporcionan como `array`; su orden es como se indica.

```php
<?php
$arr = array(
    'language' => 'en',
    'script'   => 'Hans',
    'region'   => 'CN',
    'extlang3' => 'd',
    'extlang2' => 'c',
    'extlang1' => 'b',
    'extlang0' => 'a',
);
echo locale_compose($arr), PHP_EOL;
$arr = array(
    'language' => 'en',
    'script'   => 'Hans',
    'region'   => 'CN',
    'extlang'  => ['a', 'b', 'c', 'd'],
);
echo locale_compose($arr), PHP_EOL;
?>

   
```

El ejemplo anterior mostrará:

    en_a_b_c_Hans_CN
    en_a_b_c_d_Hans_CN

      

## Véase también

`locale_parse`
