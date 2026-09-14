---
title: Locale::setDefault
description: Configura la configuración local por defecto
source_url: https://www.php.net/manual/es/locale.setdefault.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/set-default.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 679cf93fa
order: 42000
---

Locale::setDefault

locale_set_default

Configura la configuración local por defecto

## Descripción

Estilo orientado a objetos

```php
public static Locale::setDefault(string $locale): true
```php

Estilo procedimental

```php
locale_set_default(string $locale): true
```

Configura la configuración local por defecto a `locale`. Esto cambia el valor de la global INTL 'default_locale'. Las extensiones UAX \#35 son también admitidas.

## Parámetros

`locale`  
Un idioma en formato BCP 47.

## Valores devueltos

Retorna `true`.

## Ejemplos

Ejemplo con `locale_set_default`, procedimental

```php
<?php
locale_set_default('de-DE');
echo locale_get_default();
?>

   
```

Ejemplo con `locale_set_default`, POO

```php
<?php
Locale::setDefault('de-DE');
echo Locale::getDefault();
?>

   
```

El ejemplo anterior mostrará:

    de-DE

      

## Véase también

`locale_get_default`
