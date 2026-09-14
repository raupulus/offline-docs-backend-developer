---
title: xdiff_string_diff
description: Hacer un diff unificado de dos strings
source_url: https://www.php.net/manual/es/function.xdiff-string-diff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-string-diff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_revision: '475439775'
order: 102220
---

xdiff_string_diff

Hacer un diff unificado de dos strings

## Descripción

```php
xdiff_string_diff(string $old_data, string $new_data, [int $context], [bool $minimal]): string
```php

Hace un diff unificado que contiene diferencias entre el string `old_data` y el string `new_data` y devuelve este. El diff resultante es legible. Un parámetro opcional `context` especifica el número de líneas de contexto que hay que añadir alrededor de cada cambio. Establecer el parámetro `minimal` a true dará como resultado de salida el archivo parche más corto posible (puede tomar algo de tiempo).

## Parámetros

`old_data`  
Primera cadena con información. Esta actúa como "vieja" información.

`new_data`  
Segundo string con información. Esta actúa como "nueva" información.

`context`  
Indica el número de líneas de contexto que desea incluir en el diff resultado.

`minimal`  
Establezca este parámetro a `true` si desea reducir el tamaño del resultado (puede tomar algo de tiempo).

## Valores devueltos

Devuelve un string con el resultado diff o `false` si ocurriera un error interno.

## Ejemplos

Ejemplo de `xdiff_string_diff`

El siguiente código hace un diff unificado de dos artículos.

```
<?php
$old_article = file_get_contents('./old_article.txt');
$new_article = $_REQUEST['article']; /* Supongamos que alguien pega un nuevo artículo en formato html */

$diff = xdiff_string_diff($old_article, $new_article, 1);
if (is_string($diff)) {
    echo "Diferencias entre los dos artículos:\n";
    echo $diff;
}

?>

    
```php

## Notas

> [!NOTE]
> Esta función no funciona bien con string binarios. Para hacer un diff de string binario utilice `xdiff_string_bdiff`/`xdiff_string_rabdiff`.

## Véase también

`xdiff_string_patch`
