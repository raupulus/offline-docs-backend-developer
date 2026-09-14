---
title: tidy::getOpt
description: Devuelve el valor de la opción de configuración especificada para el
  documento tidy
source_url: https://www.php.net/manual/es/tidy.getopt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/getopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94050
---

tidy::getOpt

tidy_getopt

Devuelve el valor de la opción de configuración especificada para el documento tidy

## Descripción

Estilo orientado a objetos

```php
public tidy::getOpt(string $option): string
```php

Estilo procedimental

```php
tidy_getopt(tidy $tidy, string $option): string
```

Devuelve el valor de la opción `option` de configuración del objeto `tidy` tidy especificado.

## Parámetros

`tidy`  
El objeto `Tidy`

`option`  
Encontrará una lista con cada opción de configuración y sus tipos en: <http://api.html-tidy.org/#quick-reference>.

## Valores devueltos

Devuelve el valor de la opción `option` especificada. El tipo de valor depende de la opción.

## Ejemplos

Ejemplo de `tidy_getopt`

```php
<?php

$html ='<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">
<html><head><title>Title</title></head>
<body>

<p><img src="img.png"></p>

</body></html>';

$config = array('accessibility-check' => 3,
                'alt-text' => 'some text');

$tidy = new tidy();
$tidy->parseString($html, $config);

var_dump($tidy->getOpt('accessibility-check')); //integer
var_dump($tidy->getOpt('lower-literals')); //boolean
var_dump($tidy->getOpt('alt-text')); //string

?>

    
```

El ejemplo anterior mostrará:

    int(3)
    bool(true)
    string(9) "some text"
