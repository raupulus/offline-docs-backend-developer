---
title: get_html_translation_table
description: Devuelve la tabla de traducción de entidades utilizada por htmlspecialchars
  y htmlentities
source_url: https://www.php.net/manual/es/function.get-html-translation-table.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/get-html-translation-table.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: eabde0419
order: 88740
---

get_html_translation_table

Devuelve la tabla de traducción de entidades utilizada por

htmlspecialchars

y

htmlentities

## Descripción

```php
get_html_translation_table([int $table], [int $flags], [string $encoding]): array
```php

`get_html_translation_table` devuelve la tabla de traducción de entidades utilizada internamente por las funciones `htmlspecialchars` y `htmlentities`.

> [!NOTE]
> Los caracteres especiales pueden ser codificados de diferentes maneras. Por ejemplo, `"` puede ser codificado como `&quot;`, `&#34;` o `&#x22`. `get_html_translation_table` devuelve únicamente la forma utilizada por `htmlspecialchars` y `htmlentities`.

## Parámetros

`table`  
La tabla a devolver. Puede ser `HTML_ENTITIES` o `HTML_SPECIALCHARS`.

`flags`  
Una máscara de uno o varios flag siguientes, que especifican qué comillas contendrá la tabla, así como el tipo de documento previsto para la tabla. El valor por omisión es `ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML401`.

| Nombre de la constante | Descripción |
|----|----|
| `ENT_COMPAT` | La tabla contiene entidades para las comillas dobles, pero no para las comillas simples. |
| `ENT_QUOTES` | La tabla contiene entidades para las comillas dobles y simples. |
| `ENT_NOQUOTES` | La tabla no contiene entidades para las comillas dobles ni simples. |
| `ENT_SUBSTITUTE` | Reemplaza las secuencias de código no válidas con un carácter de reemplazo Unicode U+FFFD (UTF-8) o &#FFFD; (en otro caso) en lugar de devolver una string vacía. |
| `ENT_HTML401` | Tabla para HTML 4.01. |
| `ENT_XML1` | Tabla para XML 1. |
| `ENT_XHTML` | Tabla para XHTML. |
| `ENT_HTML5` | Tabla para HTML 5. |

Constantes disponibles para el flag `flags`

`encoding`  
Codificación a utilizar. Si se omite, el valor por omisión es UTF-8.

## Valores devueltos

Devuelve la tabla de traducción, en forma de array, con las claves como caracteres originales y los valores como las entidades correspondientes.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | `flags` cambió de `ENT_COMPAT` a `ENT_QUOTES` \| `ENT_SUBSTITUTE` \| `ENT_HTML401`. |

## Ejemplos

Ejemplo con la tabla de traducción de caracteres a entidades HTML

```
<?php
var_dump(get_html_translation_table(HTML_ENTITIES, ENT_QUOTES | ENT_HTML5));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(1510) {
      ["
    "]=>
      string(9) "&NewLine;"
      ["!"]=>
      string(6) "&excl;"
      ["""]=>
      string(6) "&quot;"
      ["#"]=>
      string(5) "&num;"
      ["$"]=>
      string(8) "&dollar;"
      ["%"]=>
      string(8) "&percnt;"
      ["&"]=>
      string(5) "&amp;"
      ["'"]=>
      string(6) "&apos;"
      // ...
    }

## Véase también

`htmlspecialchars`, `htmlentities`, `html_entity_decode`
