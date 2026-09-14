---
title: imap_search
description: Devuelve un array de mensajes después de la búsqueda
source_url: https://www.php.net/manual/es/function.imap-search.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-search.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38520
---

imap_search

Devuelve un array de mensajes después de la búsqueda

## Descripción

```php
imap_search(IMAP\Connection $imap, string $criteria, [int $flags], [string $charset]): array
```php

Realiza una búsqueda en el buzón de correo actual, en el flujo IMAP actual.

Por ejemplo, para buscar los mensajes no respondidos, enviados por mamá, se puede utilizar: "UNANSWERED FROM mamá". Las búsquedas parecen no distinguir entre mayúsculas y minúsculas. Esta lista de criterios proviene del código de un cliente C UW y puede ser incompleta o imprecisa. (ver también la [RFC1176](https://datatracker.ietf.org/doc/html/rfc1176), y en particular, la sección "tag SEARCH search_criteria").

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`criteria`  
Un `string`, delimitado por espacios, en el que se aceptan los siguientes palabras clave. Todos los argumentos de varias palabras (e.g. `FROM "joey smith"`) deben colocarse entre comillas. Los resultados deben coincidir con todas las entradas `criteria`.

- ALL - devuelve todos los mensajes que cumplen con el resto del criterio.

- ANSWERED - todos los mensajes con el flag \\ANSWERED

- BCC "string" - todos los mensajes con la cadena "string" en el campo Bcc

- BEFORE "date" - todos los mensajes con Date: antes de "date"

- BODY "string" - todos los mensajes con "string" en el cuerpo

- CC "string" - todos los mensajes con "string" en el campo Cc

- DELETED - todos los mensajes borrados

- FLAGGED - todos los mensajes con el flag \\FLAGGED (a veces interpretado como Importante o Urgente)

- FROM "string" - todos los mensajes con la cadena "string" en el campo From

- KEYWORD "string" - todos los mensajes con la cadena "string" como palabra clave

- NEW - todos los mensajes nuevos

- OLD - todos los mensajes antiguos

- ON "date" - todos los mensajes con la fecha "date" como campo Date

- RECENT - todos los mensajes con el flag \\RECENT

- SEEN - todos los mensajes leídos (con el flag\\SEEN flag)

- SINCE "date" - todos los mensajes con la fecha Date: después de "date"

- SUBJECT "string" - todos los mensajes con la cadena "string" en el campo Subject

- TEXT "string" - todos los mensajes con el texto "string"

- TO "string" - todos los mensajes con la cadena "string" en el campo To

- UNANSWERED - todos los mensajes no respondidos

- UNDELETED - todos los mensajes no borrados

- UNFLAGGED - todos los mensajes no marcados

- UNKEYWORD "string" - todos los mensajes que no contienen la palabra clave "string"

- UNSEEN - todos los mensajes no leídos

`flags`  
Los valores para `flags` son `SE_UID`, que hace que el array de respuesta contenga los UID en lugar de los números de secuencia.

`charset`  
Conjunto de caracteres MIME a utilizar durante la búsqueda de `string`.

## Valores devueltos

Devuelve un array de números de mensajes o de UID.

Devuelve `false` si la búsqueda no es comprendida, o bien si ningún mensaje ha sido encontrado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_search`

```
<?php
$imap   = imap_open('{imap.example.com:993/imap/ssl}INBOX', 'foo@example.com', 'pass123', OP_READONLY);

$some   = imap_search($imap, 'SUBJECT "HOWTO be Awesome" SINCE "8 August 2008"', SE_UID);
$msgnos = imap_search($imap, 'ALL');
$uids   = imap_search($imap, 'ALL', SE_UID);

print_r($some);
print_r($msgnos);
print_r($uids);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => 4
        [1] => 6
        [2] => 11
    )
    Array
    (
        [0] => 1
        [1] => 2
        [2] => 3
        [3] => 4
        [4] => 5
        [5] => 6
    )
    Array
    (
        [0] => 1
        [1] => 4
        [2] => 6
        [3] => 8
        [4] => 11
        [5] => 12
    )

## Véase también

`imap_listscan`
