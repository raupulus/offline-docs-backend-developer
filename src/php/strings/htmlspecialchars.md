---
title: htmlspecialchars
description: Convierte caracteres especiales en entidades HTML
source_url: https://www.php.net/manual/es/function.htmlspecialchars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/htmlspecialchars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: eabde0419
order: 88810
---

htmlspecialchars

Convierte caracteres especiales en entidades HTML

## Descripción

```php
htmlspecialchars(string $string, [int $flags], [string $encoding], [bool $double_encode]): string
```php

Algunos caracteres tienen significados especiales en HTML, y deben ser reemplazados por entidades HTML para conservar sus significados. Esta función retorna un string con estas modificaciones. Si se necesita que todas las subcadenas de entrada que están asociadas a entidades nombradas sean transformadas, se debe utilizar la función `htmlentities`.

Si el string de entrada pasado a esta función y el documento final comparten el mismo juego de caracteres, esta función es suficiente para preparar la entrada para una inclusión en la mayoría de los contextos de un documento HTML. Sin embargo, si la entrada puede presentar caracteres que no están codificados en el juego de caracteres del documento final, y se desea preservar estos caracteres (como numéricos o entidades nombradas), esta función y la función `htmlentities` (que solo codifica las subcadenas que tienen entidades nombradas equivalentes) no son suficientes. Se debe utilizar la función `mb_encode_numericentity` en su lugar.

| Carácter | Reemplazo |
|----|----|
| `&` (ampersand) | `&amp;` |
| `"` (comillas dobles) | `&quot;` excepto si `ENT_NOQUOTES` |
| `'` (comilla simple) | `&#039;` (para `ENT_HTML401`) o `&apos;` (para `ENT_XML1`, `ENT_XHTML` o `ENT_HTML5`), pero solo cuando `ENT_QUOTES` está definido |
| `<` (menor que) | `&lt;` |
| `>` (mayor que) | `&gt;` |

Reemplazos realizados

## Parámetros

`string`  
El string a convertir.

`flags`  
Una máscara de bits de uno o más flags siguientes, que determinan la forma en que las comillas serán gestionadas, cómo se manejarán las secuencias de código inválido, así como el tipo de documento utilizado. Por omisión, es `ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML401`.

| Constante | Descripción |
|----|----|
| `ENT_COMPAT` | Convierte las comillas dobles e ignora las comillas simples. |
| `ENT_QUOTES` | Convierte las comillas dobles y las comillas simples. |
| `ENT_NOQUOTES` | Ignora las comillas dobles y las comillas simples. |
| `ENT_IGNORE` | Ignora las secuencias de caracteres inválidas en lugar de retornar un string vacío. El uso de este flag está fuertemente desaconsejado por [razones de seguridad](http://unicode.org/reports/tr36/#Deletion_of_Noncharacters). |
| `ENT_SUBSTITUTE` | Reemplaza las secuencias de código inválido con un carácter de reemplazo Unicode U+FFFD (UTF-8) o \&#xFFFD; (de lo contrario) en lugar de retornar un string vacío. |
| `ENT_DISALLOWED` | Reemplaza los puntos de código inválidos del documento proporcionado con un carácter de reemplazo Unicode U+FFFD (UTF-8) o \&#xFFFD; (de lo contrario) en lugar de dejarlo tal cual. Esto puede ser útil para, por ejemplo, asegurar el correcto formato de documentos XML que contienen contenido externo. |
| `ENT_HTML401` | Maneja el código como HTML 4.01. |
| `ENT_XML1` | Maneja el código como XML 1. |
| `ENT_XHTML` | Maneja el código como XHTML. |
| `ENT_HTML5` | Maneja el código como HTML 5. |

Constantes disponibles para `flags`

`encoding`  
Un argumento opcional que define el codificado utilizado durante la conversión de caracteres.

Si se omite, el valor predeterminado del parámetro `encoding` es el valor de la opción de configuración [default_charset](#ini.default-charset) .

Aunque este argumento es técnicamente opcional, se recomienda encarecidamente especificar el valor correcto para su código si la opción de configuración [default_charset](#ini.default-charset) ha sido definida incorrectamente para la entrada proporcionada.

Para esta función, los encodings `ISO-8859-1`, `ISO-8859-15`, `UTF-8`, `cp866`, `cp1251`, `cp1252`, y `KOI8-R` son equivalentes, siempre que el parámetro `string` sea válido para el encoding, en el sentido de que los caracteres afectados por la función `htmlspecialchars` ocupen la misma posición en todos estos encodings.

`double_encode`  
Cuando el parámetro `double_encode` está desactivado, PHP no codificará las entidades html existentes; por omisión, todo es convertido.

## Valores devueltos

El string convertido.

Si el string de entrada `string` contiene una secuencia de código inválida en el parámetro `encoding` proporcionado, se retornará un string vacío a menos que el flag `ENT_IGNORE` o `ENT_SUBSTITUTE` esté definido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | `flags` cambió de `ENT_COMPAT` a `ENT_QUOTES` \| `ENT_SUBSTITUTE` \| `ENT_HTML401`. |

## Ejemplos

Ejemplo con `htmlspecialchars`

```
<?php
$new = htmlspecialchars("<a href='test'>Test</a>", ENT_QUOTES);
echo $new; // &lt;a href=&#039;test&#039;&gt;Test&lt;/a&gt;
?>

    
```php

## Notas

> [!NOTE]
> Tenga en cuenta que esta función no realiza ningún otro reemplazo que los que están listados anteriormente. Para realizar un reemplazo completo, consulte `htmlentities`.

> [!NOTE]
> En el caso de un valor ambiguo para `flags`, se aplican las siguientes reglas:
>
> - Cuando ninguno de `ENT_COMPAT`, `ENT_QUOTES`, `ENT_NOQUOTES` está presente, el valor por omisión es `ENT_NOQUOTES`.
>
> - Cuando más de uno de `ENT_COMPAT`, `ENT_QUOTES`, `ENT_NOQUOTES` están presentes, `ENT_QUOTES` tiene la mayor prioridad, seguido de `ENT_COMPAT`.
>
> - Cuando ninguno de `ENT_HTML401`, `ENT_HTML5`, `ENT_XHTML`, `ENT_XML1` está presente, el valor por omisión es `ENT_HTML401`.
>
> - Cuando más de uno de `ENT_HTML401`, `ENT_HTML5`, `ENT_XHTML`, `ENT_XML1` están presentes, `ENT_HTML5` tiene la mayor prioridad, seguido de `ENT_XHTML`, `ENT_XML1` y `ENT_HTML401`.
>
> - Cuando más de uno de `ENT_DISALLOWED`, `ENT_IGNORE`, `ENT_SUBSTITUTE` están presentes, `ENT_IGNORE` tiene la mayor prioridad, seguido de `ENT_SUBSTITUTE`.

## Véase también

`get_html_translation_table`, `htmlspecialchars_decode`, `strip_tags`, `htmlentities`, `nl2br`
