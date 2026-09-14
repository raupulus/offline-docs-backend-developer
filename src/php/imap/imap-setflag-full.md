---
title: imap_setflag_full
description: Establece un flag en un mensaje
source_url: https://www.php.net/manual/es/function.imap-setflag-full.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-setflag-full.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 673d373ed
order: 38550
---

imap_setflag_full

Establece un flag en un mensaje

## Descripción

```php
imap_setflag_full(IMAP\Connection $imap, string $sequence, string $flag, [int $options]): true
```php

`imap_setflag_full` asigna el `flag` especificado a los mensajes de la `sequence` dada.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`sequence`  
Una secuencia de números de mensajes. Los mensajes deseados pueden ser enumerados con la sintaxis `X,Y`, o recuperar todos los mensajes de un intervalo con la sintaxis `X:Y`

`flag`  
Los flags que pueden ser modificados son `\Seen`, `\Answered`, `\Flagged`, `\Deleted`, y `\Draft` (como se define en la [RFC2060](https://datatracker.ietf.org/doc/html/rfc2060)).

`options`  
`options` es una máscara de bits, que acepta únicamente el siguiente valor:

- `ST_UID` - la secuencia contiene UID en lugar de números de secuencia.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Lanza una excepción `ValueError` si el argumento `options` es inválido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |
| 8.0.0 | Una excepción `ValueError` es ahora lanzada para valores de argumento `options` inválidos. Anteriormente, se emitía una advertencia y la función devolvía `false`. |

## Ejemplos

Ejemplo con `imap_setflag_full`

```
<?php
$mbox = imap_open("{imap.example.org:143}", "username", "password")
     or die("Conexión imposible: " . imap_last_error());

$status = imap_setflag_full($mbox, "2,5", "\\Seen \\Flagged");

echo gettype($status) . "\n";
echo $status . "\n";

imap_close($mbox);
?>

    
```php

## Véase también

`imap_clearflag_full`
