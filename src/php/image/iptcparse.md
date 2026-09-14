---
title: iptcparse
description: Analiza un bloque binario IPTC y busca las etiquetas simples
source_url: https://www.php.net/manual/es/function.iptcparse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/iptcparse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 32510
---

iptcparse

Analiza un bloque binario IPTC y busca las etiquetas simples

## Descripción

```php
iptcparse(string $iptc_block): array
```php

Analiza un bloque binario [IPTC](http://www.iptc.org/) y busca las etiquetas simples.

## Parámetros

`iptc_block`  
Un bloque binario IPTC.

## Valores devueltos

Retorna un array con las etiquetas como índices y los valores de estas etiquetas IPTC en los valores del array correspondientes. En caso de error, o si ninguna etiqueta IPTC ha sido encontrada, esta función retorna `false`.

## Ejemplos

Ejemplo con iptcparse() y `getimagesize`

```
<?php
$size = getimagesize('./test.jpg', $info);
if(isset($info['APP13']))
{
    $iptc = iptcparse($info['APP13']);
    var_dump($iptc);
}
?>

    
```php

## Notas

> [!NOTE]
> Esta función no requiere la biblioteca GD.
