---
title: htmlspecialchars_decode
description: Convierte las entidades HTML especiales en caracteres
source_url: https://www.php.net/manual/es/function.htmlspecialchars-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/htmlspecialchars-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: eabde0419
order: 88800
---

htmlspecialchars_decode

Convierte las entidades HTML especiales en caracteres

## Descripción

```php
htmlspecialchars_decode(string $string, [int $flags]): string
```php

Esta función es la opuesta a `htmlspecialchars`. Convierte las entidades HTML especiales en caracteres.

Las entidades convertidas son: `&amp;`, `&quot;` (cuando `ENT_NOQUOTES` no está activado), `&#039;` (cuando `ENT_QUOTES` está activado), `&lt;` y `&gt;`.

## Parámetros

`string`  
La `string` a decodificar

`flags`  
Una máscara de uno o varios flags siguientes, que especifican cómo deben ser gestionadas las comillas y qué tipo de documento utilizar. Por omisión, es `ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML401`.

| Nombre de la constante | Descripción |
|----|----|
| `ENT_COMPAT` | Convertirá las comillas y dejará las apóstrofes. |
| `ENT_QUOTES` | Convertirá las comillas y los apóstrofes. |
| `ENT_NOQUOTES` | Dejará las comillas y los apóstrofes sin convertir. |
| `ENT_SUBSTITUTE` | Reemplaza las secuencias de código no válidas con un carácter de reemplazo Unicode U+FFFD (UTF-8) o &#FFFD; (en otro caso) en lugar de devolver una cadena vacía. |
| `ENT_HTML401` | Gestiona el código como HTML 4.01. |
| `ENT_XML1` | Gestiona el código como XML 1. |
| `ENT_XHTML` | Gestiona el código como XHTML. |
| `ENT_HTML5` | Gestiona el código como HTML 5. |

Constantes disponibles para el parámetro `flags`

## Valores devueltos

Devuelve la cadena de caracteres decodificada.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | `flags` cambió de `ENT_COMPAT` a `ENT_QUOTES` \| `ENT_SUBSTITUTE` \| `ENT_HTML401`. |

## Ejemplos

Ejemplo con `htmlspecialchars_decode`

```
<?php
$str = "<p>this -&gt; &quot;</p>\n";

echo htmlspecialchars_decode($str);

// note aquí que las comillas no están convertidas
echo htmlspecialchars_decode($str, ENT_NOQUOTES);
?>

    
```php

El ejemplo anterior mostrará:

    <p>this -> "</p>
    <p>this -> &quot;</p>

## Véase también

`htmlspecialchars`, `html_entity_decode`, `get_html_translation_table`
