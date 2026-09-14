---
title: Locale::getDefault
description: Lee el valor por defecto de una configuración local para la variable
  global 'default_locale'
source_url: https://www.php.net/manual/es/locale.getdefault.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/get-default.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41870
---

Locale::getDefault

locale_get_default

Lee el valor por defecto de una configuración local para la variable global 'default_locale'

## Descripción

Estilo orientado a objetos

```php
public static Locale::getDefault(): string
```php

Estilo procedimental

```php
locale_get_default(): string
```

Lee el valor por defecto de una configuración local para la variable global 'default_locale'. Al momento de la inicialización de PHP, este valor se extrae de la directiva 'intl.default_locale' en `php.ini`, si este valor existe, y de la función ICU uloc_getDefault() de otro modo.

## Parámetros

## Valores devueltos

La configuración local por defecto para la ejecución.

## Ejemplos

Ejemplo con `locale_get_default`, procedimental

```php
<?php
ini_set('intl.default_locale', 'de-DE');
echo locale_get_default();
echo '; ';
locale_set_default('fr');
echo locale_get_default();
?>

   
```

Ejemplo con `locale_get_default`, POO

```php
<?php
ini_set('intl.default_locale', 'de-DE');
echo Locale::getDefault();
echo '; ';
Locale::setDefault('fr');
echo Locale::getDefault();
?>

   
```

El ejemplo anterior mostrará:

    de-DE; fr

      

## Véase también

`locale_set_default`
