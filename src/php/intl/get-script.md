---
title: Locale::getScript
description: Devuelve un código para el script de la configuración local
source_url: https://www.php.net/manual/es/locale.getscript.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/get-script.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41960
---

Locale::getScript

locale_get_script

Devuelve un código para el script de la configuración local

## Descripción

Estilo orientado a objetos

```php
public static Locale::getScript(string $locale): string
```php

Estilo procedimental

```php
locale_get_script(string $locale): string
```

Devuelve un código para el script de la configuración local

## Parámetros

`locale`  
La configuración local de la cual extraer el código del script.

## Valores devueltos

El código de script para la configuración local o `null` si está ausente.

## Ejemplos

Ejemplo con `locale_get_script`, procedimental

```php
<?php
echo locale_get_script('sr-Cyrl');
?>

   
```

Ejemplo con `locale_get_script`, POO

```php
<?php
echo Locale::getScript('sr-Cyrl');
?>

   
```

El ejemplo anterior mostrará:

    Cyrl

      

## Véase también

`locale_get_primary_language`, `locale_get_region`, `locale_get_all_variants`
