---
title: Imagick::queryFormats
description: Devuelve los formatos soportados por Imagick
source_url: https://www.php.net/manual/es/imagick.queryformats.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/queryformats.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 3193e2e78
order: 34790
---

Imagick::queryFormats

Devuelve los formatos soportados por Imagick

## Descripción

```php
public static Imagick::queryFormats([string $pattern]): array
```php

Devuelve los formatos soportados por Imagick.

## Parámetros

`pattern`  

## Valores devueltos

Devuelve un array que contiene los formatos soportados por Imagick.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::queryFormats`

```
<?php
    function render() {
        $output = "";
        $input = \Imagick::queryformats();
        $columns = 6;

        $output .= "<table border='2'>";

        for ($i=0; $i < count($input); $i += $columns) {
            $output .= "<tr>";
            for ($c=0; $c<$columns; $c++) {
                $output .= "<td>";
                if (($i + $c) <  count($input)) {
                    $output .= $input[$i + $c];
                }
                $output .= "</td>";
            }
            $output .= "</tr>";
        }

        $output .= "</table>";

        return $output;
    }

?>

     
```php
