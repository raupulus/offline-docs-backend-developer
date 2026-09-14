---
title: tidy::cleanRepair
description: Ejecuta una operación de limpieza y reparación de las etiquetas HTML
source_url: https://www.php.net/manual/es/tidy.cleanrepair.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/cleanrepair.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 93990
---

tidy::cleanRepair

tidy_clean_repair

Ejecuta una operación de limpieza y reparación de las etiquetas HTML

## Descripción

Estilo orientado a objetos

```php
public tidy::cleanRepair(): bool
```php

Estilo procedimental

```php
tidy_clean_repair(tidy $tidy): bool
```

Esta función limpia y repara el objeto `object` pasado como argumento.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `tidy::cleanrepair`

```php
<?php
$html = '<p>test</I>';

$tidy = tidy_parse_string($html);
$tidy->cleanRepair();

echo $tidy;
?>

    
```

El ejemplo anterior mostrará:

    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">
    <html>
    <head>
    <title></title>
    </head>
    <body>
    <p>test</p>
    </body>
    </html>

## Véase también

tidy::repairFile

tidy::repairString
