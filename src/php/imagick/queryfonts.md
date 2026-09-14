---
title: Imagick::queryFonts
description: Devuelve la lista de fuentes configuradas
source_url: https://www.php.net/manual/es/imagick.queryfonts.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/queryfonts.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 3193e2e78
order: 34780
---

Imagick::queryFonts

Devuelve la lista de fuentes configuradas

## Descripción

```php
public static Imagick::queryFonts([string $pattern]): array
```php

Devuelve la lista de fuentes configuradas para Imagick.

## Parámetros

`pattern`  
El patrón de búsqueda

## Valores devueltos

Devuelve un array que contiene las fuentes configuradas.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Ejemplo con `Imagick::queryFonts`

```
      
<?php
        $output = '';
        $output .= "Las fuentes que coinciden con 'Helvetica*' son:<br/>";

        $fontList = \Imagick::queryFonts("Helvetica*");

        foreach ($fontList as $fontName) {
            $output .= '<li>'. $fontName."</li>";
        }

        return $output;

?>

      
```php
