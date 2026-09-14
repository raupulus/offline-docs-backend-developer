---
title: tidy_config_count
description: Devuelve el número de errores de configuración Tidy encontrados en un
  documento dado
source_url: https://www.php.net/manual/es/function.tidy-config-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/functions/tidy-config-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 04f10f9f8
order: 93920
---

tidy_config_count

Devuelve el número de errores de configuración Tidy encontrados en un documento dado

## Descripción

```php
tidy_config_count(tidy $tidy): int
```php

Devuelve el número de errores encontrados en la configuración del objeto `tidy` tidy especificado.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve el número de errores.

## Ejemplos

Ejemplo de la función `tidy_config_count`

```
<?php
$html = '<p>test</I>';

$config = array('doctype' => 'bogus');

$tidy = tidy_parse_string($html, $config);

/* Saldrá 1, porque 'bogus' no es un doctype válido */
echo tidy_config_count($tidy);
?>

    
```php
