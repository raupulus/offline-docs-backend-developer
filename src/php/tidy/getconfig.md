---
title: tidy::getConfig
description: Obtiene la configuración actual de Tidy
source_url: https://www.php.net/manual/es/tidy.getconfig.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/getconfig.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94030
---

tidy::getConfig

tidy_get_config

Obtiene la configuración actual de Tidy

## Descripción

Estilo orientado a objetos

```php
public tidy::getConfig(): array
```php

Estilo procedimental

```php
tidy_get_config(tidy $tidy): array
```

Obtiene la lista de las opciones de configuración en uso de un objeto `tidy` tidy.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve un array con las opciones de configuración.

Para una explicación de cada opción, consulte <http://api.html-tidy.org/#quick-reference>.

## Ejemplos

Ejemplo de `tidy::getConfig`

```php
<?php
$html = '<p>test</p>';
$config = array('indent' => TRUE,
                'output-xhtml' => TRUE,
                'wrap' => 200);

$tidy = tidy_parse_string($html, $config);

print_r($tidy->getConfig());
?>

    
```

El ejemplo anterior mostrará:

    Array
    (
        [indent-spaces] => 2
        [wrap] => 200
        [tab-size] => 8
        [char-encoding] => 1
        [input-encoding] => 3
        [output-encoding] => 1
        [newline] => 1
        [doctype-mode] => 1
        [doctype] =>
        [repeated-attributes] => 1
        [alt-text] =>
        [slide-style] =>
        [error-file] =>
        [output-file] =>
        [write-back] =>
        [markup] => 1
        [show-warnings] => 1
        [quiet] =>
        [indent] => 1
        [hide-endtags] =>
        [input-xml] =>
        [output-xml] => 1
        [output-xhtml] => 1
        [output-html] =>
        [add-xml-decl] =>
        [uppercase-tags] =>
        [uppercase-attributes] =>
        [bare] =>
        [clean] =>
        [logical-emphasis] =>
        [drop-proprietary-attributes] =>
        [drop-font-tags] =>
        [drop-empty-paras] => 1
        [fix-bad-comments] => 1
        [break-before-br] =>
        [split] =>
        [numeric-entities] =>
        [quote-marks] =>
        [quote-nbsp] => 1
        [quote-ampersand] => 1
        [wrap-attributes] =>
        [wrap-script-literals] =>
        [wrap-sections] => 1
        [wrap-asp] => 1
        [wrap-jste] => 1
        [wrap-php] => 1
        [fix-backslash] => 1
        [indent-attributes] =>
        [assume-xml-procins] =>
        [add-xml-space] =>
        [enclose-text] =>
        [enclose-block-text] =>
        [keep-time] =>
        [word-2000] =>
        [tidy-mark] =>
        [gnu-emacs] =>
        [gnu-emacs-file] =>
        [literal-attributes] =>
        [show-body-only] =>
        [fix-uri] => 1
        [lower-literals] => 1
        [hide-comments] =>
        [indent-cdata] =>
        [force-output] => 1
        [show-errors] => 6
        [ascii-chars] => 1
        [join-classes] =>
        [join-styles] => 1
        [escape-cdata] =>
        [language] =>
        [ncr] => 1
        [output-bom] => 2
        [replace-color] =>
        [css-prefix] =>
        [new-inline-tags] =>
        [new-blocklevel-tags] =>
        [new-empty-tags] =>
        [new-pre-tags] =>
        [accessibility-check] => 0
        [vertical-space] =>
        [punctuation-wrap] =>
        [merge-divs] => 1
    )

## Véase también

tidy_reset_config

tidy_save_config
