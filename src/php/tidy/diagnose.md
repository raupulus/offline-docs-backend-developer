---
title: tidy::diagnose
description: Ejecuta un diagnóstico sobre documento analizado y reparado
source_url: https://www.php.net/manual/es/tidy.diagnose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/diagnose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94010
---

tidy::diagnose

tidy_diagnose

Ejecuta un diagnóstico sobre documento analizado y reparado

## Descripción

Estilo orientado a objetos

```php
public tidy::diagnose(): bool
```php

Estilo procedimental

```php
tidy_diagnose(tidy $tidy): bool
```

Ejecuta un diagnóstico sobre el objeto `tidy` tidy, añadiendo alguna información adicional sobre el documento en un buffer de errores.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `tidy::diagnose`

```php
<?php

$html = <<< HTML
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<p>parrafo</p>
HTML;

$tidy = tidy_parse_string($html);
$tidy->cleanRepair();

// note the difference between the two outputs
echo $tidy->errorBuffer . "\n";

$tidy->diagnose();
echo $tidy->errorBuffer;

?>

    
```

El ejemplo anterior mostrará:

    line 4 column 1 - Warning: <p> isn't allowed in <head> elements
    line 4 column 1 - Warning: inserting missing 'title' element
    line 4 column 1 - Warning: <p> isn't allowed in <head> elements
    line 4 column 1 - Warning: inserting missing 'title' element
    Info: Doctype given is "-//W3C//DTD XHTML 1.0 Strict//EN"
    Info: Document content looks like XHTML 1.0 Strict
    2 warnings, 0 errors were found!

## Véase también

tidy::errorBuffer
