---
title: htmlentities
description: Convierte todos los caracteres elegibles en entidades HTML
source_url: https://www.php.net/manual/es/function.htmlentities.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/htmlentities.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 06394ea77
order: 88790
---

htmlentities

Convierte todos los caracteres elegibles en entidades HTML

## Descripción

```php
htmlentities(string $string, [int $flags], [string $encoding], [bool $double_encode]): string
```php

`htmlentities` es idéntica a la función `htmlspecialchars`, salvo que todos los caracteres que tienen equivalentes en entidades HTML son efectivamente traducidos. La función `get_html_translation_table` puede ser utilizada para retornar la tabla de traducción utilizada en función de las constantes `flags` proporcionadas.

Si se desea realizar la operación inversa, se debe utilizar la función `html_entity_decode`.

## Parámetros

`string`  
El string de entrada.

`flags`  
Una máscara de uno o varios flags siguientes, que determinan la forma en que las comillas serán gestionadas, cómo las secuencias de código inválido serán gestionadas así como el tipo de documento utilizado. Por omisión, es `ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML401`.

| Constante | Descripción |
|----|----|
| `ENT_COMPAT` | Convierte las comillas dobles e ignora las comillas simples. |
| `ENT_QUOTES` | Convierte las comillas dobles y las comillas simples. |
| `ENT_NOQUOTES` | Ignora las comillas dobles y las comillas simples. |
| `ENT_IGNORE` | Ignora las secuencias de caracteres inválidas en lugar de retornar un string vacío. El uso de este flag es fuertemente desaconsejado por [razones de seguridad](http://unicode.org/reports/tr36/#Deletion_of_Noncharacters). |
| `ENT_SUBSTITUTE` | Reemplaza las secuencias de código inválido con un carácter de reemplazo Unicode U+FFFD (UTF-8) o &#FFFD; (de lo contrario) en lugar de retornar un string vacío. |
| `ENT_DISALLOWED` | Reemplaza los puntos de código inválidos del documento proporcionado con un carácter de reemplazo Unicode U+FFFD (UTF-8) o &#FFFD; (de lo contrario) en lugar de dejarlo tal cual. Esto puede ser útil para, por ejemplo, asegurar el correcto formato de documentos XML que contienen contenido externo. |
| `ENT_HTML401` | Gestiona el código como HTML 4.01. |
| `ENT_XML1` | Gestiona el código como XML 1. |
| `ENT_XHTML` | Gestiona el código como XHTML. |
| `ENT_HTML5` | Gestiona el código como HTML 5. |

Constantes disponibles para `flags`

`encoding`  
Un argumento opcional que define el codificado utilizado durante la conversión de caracteres.

Si se omite, el valor predeterminado del parámetro `encoding` es el valor de la opción de configuración [default_charset](#ini.default-charset) .

Aunque este argumento es técnicamente opcional, se recomienda encarecidamente especificar el valor correcto para su código si la opción de configuración [default_charset](#ini.default-charset) ha sido definida incorrectamente para la entrada proporcionada.

`double_encode`  
Cuando `double_encode` está desactivado, PHP no codificará las entidades html existentes. Por omisión, todo es convertido.

## Valores devueltos

Retorna el string codificado.

Si la entrada `string` contiene una secuencia de código inválido en el encoding `encoding` proporcionado, un string vacío será retornado, a menos que el flag `ENT_IGNORE` o el flag `ENT_SUBSTITUTE` esté definido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | `flags` cambió de `ENT_COMPAT` a `ENT_QUOTES` \| `ENT_SUBSTITUTE` \| `ENT_HTML401`. |
| 8.0.0 | `encoding` ahora es nullable. |

## Ejemplos

Ejemplo con `htmlentities`

```
<?php
$str = 'Un \'apostrophe\' en <strong>gras</strong>';

echo htmlentities($str);
echo "\n\n";
echo htmlentities($str, ENT_COMPAT);
?>

    
```php

El ejemplo anterior mostrará:

    Un &#039;apostrophee&#039; est &lt;b&gt;gras&lt;/b&gt;

    Un 'apostrophe' est &lt;b&gt;gras&lt;/b&gt

Utilización de `ENT_IGNORE`

```
<?php
$str = "\x8F!!!";

// Muestra un string vacío
echo htmlentities($str, ENT_QUOTES, "UTF-8");

// Muestra "!!!"
echo htmlentities($str, ENT_QUOTES | ENT_IGNORE, "UTF-8");
?>

    
```php

## Véase también

`html_entity_decode`, `get_html_translation_table`, `htmlspecialchars`, `nl2br`, `urlencode`
