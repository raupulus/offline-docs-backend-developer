---
title: html_entity_decode
description: Convierte las entidades HTML a sus caracteres correspondientes
source_url: https://www.php.net/manual/es/function.html-entity-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/html-entity-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 45042fef6
order: 88780
---

html_entity_decode

Convierte las entidades HTML a sus caracteres correspondientes

## Descripción

```php
html_entity_decode(string $string, [int $flags], [string $encoding]): string
```php

`html_entity_decode` es la función contraria de `htmlentities`: convierte las entidades HTML de la cadena `string` a sus caracteres correspondientes.

De manera más explícita, esta función decodifica todas las entidades (incluyendo las entidades numéricas) que 1) son necesariamente válidas para el tipo de documento seleccionado - es decir, para XML, esta función no decodifica las entidades nombradas que pueden estar definidas en una DTD - y 2) cuyo carácter o caracteres están en el juego de caracteres codificado con la codificación elegida y están permitidos en el tipo de documento seleccionado. Todas las demás entidades se dejan tal cual.

## Parámetros

`string`  
La cadena de entrada.

`flags`  
Una máscara de uno o varios flag siguientes, que especifican la forma en que deben ser gestionadas las comillas y qué tipo de documento debe ser utilizado. Por omisión, es `ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML401`.

| Constante | Descripción |
|----|----|
| `ENT_COMPAT` | Convierte las comillas dobles e ignora las comillas simples. |
| `ENT_QUOTES` | Convierte las comillas dobles y las comillas simples. |
| `ENT_NOQUOTES` | No convierte ninguna comilla. |
| `ENT_SUBSTITUTE` | Reemplaza las secuencias de código no válidas con un carácter de reemplazo Unicode U+FFFD (UTF-8) o &#FFFD; (de lo contrario) en lugar de devolver una cadena vacía. |
| `ENT_HTML401` | Gestiona el código como HTML 4.01. |
| `ENT_XML1` | Gestiona el código como XML 1. |
| `ENT_XHTML` | Gestiona el código como XHTML. |
| `ENT_HTML5` | Gestiona el código como HTML 5. |

Constantes disponibles para `flags`

`encoding`  
Un argumento opcional que define el codificado utilizado durante la conversión de caracteres.

Si se omite, el valor predeterminado del parámetro `encoding` es el valor de la opción de configuración [default_charset](#ini.default-charset) .

Aunque este argumento es técnicamente opcional, se recomienda encarecidamente especificar el valor correcto para su código si la opción de configuración [default_charset](#ini.default-charset) ha sido definida incorrectamente para la entrada proporcionada.

## Valores devueltos

Devuelve la cadena decodificada.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | `flags` cambió de `ENT_COMPAT` a `ENT_QUOTES` \| `ENT_SUBSTITUTE` \| `ENT_HTML401`. |
| 8.0.0 | `encoding` ahora puede ser nullable. |

## Ejemplos

Decodificar entidades HTML

```
<?php
$orig = 'J\'ai "sorti" le <strong>chien</strong> tout à l\'heure';
$a = htmlentities($orig);
$b = html_entity_decode($a);

echo $a, PHP_EOL; // J'ai &quot;sorti&quot; le &lt;strong&gt;chien&lt;/strong&gt; tout &amp;agrave; l'heure
echo $b, PHP_EOL; // J'ai "sorti" le <strong>chien</strong> tout à l'heure

?>

    
```php

## Notas

> [!NOTE]
> Podría preguntarse por qué `trim(html_entity_decode('&nbsp;'));` no reduce la cadena a la cadena vacía. Esto se debe a que la entidad `&nbsp;` no es un código ASCII 32 (que sería eliminado por `trim`), sino un código ASCII 160 (`0xa0`) en la codificación por omisión `ISO 8859-1`.

## Véase también

`htmlentities`, `htmlspecialchars`, `get_html_translation_table`, `urldecode`
