---
title: NumberFormatter::getLocale
description: Lee la configuración local del formateador
source_url: https://www.php.net/manual/es/numberformatter.getlocale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/get-locale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42250
---

NumberFormatter::getLocale

numfmt_get_locale

Lee la configuración local del formateador

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::getLocale([int $type]): string
```php

Estilo procedimental

```php
numfmt_get_locale(NumberFormatter $formatter, [int $type]): string
```

Lee el nombre de la configuración local del formateador.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

`type`  
Puede seleccionarse entre un valor válido o un valor literal `Locale::VALID_LOCALE`, `Locale::ACTUAL_LOCALE`, respectivamente. El valor por omisión es el valor literal.

## Valores devueltos

El nombre de la configuración local utilizada para crear el formateador, o `false` en caso de error.

## Ejemplos

Ejemplo con `numfmt_get_error_code`, Estilo procedimental

```php
<?php
$req     = 'fr_FR_PARIS';
$fmt     = numfmt_create( $req,  NumberFormatter::DECIMAL);
$res_val = numfmt_get_locale( $fmt, Locale::VALID_LOCALE );
$res_act = numfmt_get_locale( $fmt, Locale::ACTUAL_LOCALE );
printf( "Nombre de la configuración local solicitada : %s\nNombre válido de la configuración local : %s\nValor literal de la configuración local : %s\n",
         $req, $res_val, $res_act );
?>

   
```

El ejemplo anterior mostrará:

    Nombre de la configuración local solicitada : fr_FR_PARIS
    Nombre válido de la configuración local: fr_FR
    Valor literal de la configuración local : fr

## Véase también

`numfmt_create`, `numfmt_get_error_code`
