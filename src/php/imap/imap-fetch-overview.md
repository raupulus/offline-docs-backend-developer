---
title: imap_fetch_overview
description: Lee el resumen de los encabezados de los mensajes
source_url: https://www.php.net/manual/es/function.imap-fetch-overview.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-fetch-overview.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38080
---

imap_fetch_overview

Lee el resumen de los encabezados de los mensajes

## Descripción

```php
imap_fetch_overview(IMAP\Connection $imap, string $sequence, [int $flags]): array
```php

Lee los encabezados de los correos electrónicos de la secuencia `sequence` y devuelve un resumen de su contenido.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`sequence`  
Una descripción de la secuencia del mensaje. Se pueden enumerar los mensajes deseados con la sintaxis `X,Y`, o recuperar todos los mensajes de un intervalo, con la sintaxis `X:Y`

`flags`  
`sequence` contendrá una secuencia de índice de mensaje o de UID, si `flags` contiene `FT_UID`.

## Valores devueltos

Devuelve un array de objetos que describen el encabezado de cada mensaje. El objeto solo definirá una propiedad si existe. Las propiedades posibles son:

- `subject` : el asunto del mensaje

- `from` : el remitente

- `to` : el destinatario

- `date` : la fecha de envío

- `message_id` : la identificación del mensaje

- `references` : la referencia sobre el id de este mensaje

- `in_reply_to` : la respuesta a este identificador de mensaje

- `size` : el tamaño en bytes

- `uid` : UID del mensaje en el buzón

- `msgno` : el número de secuencia del mensaje en el buzón

- `recent` : este mensaje es reciente

- `flagged` : este mensaje está marcado

- `answered` : este mensaje ha dado lugar a una respuesta

- `deleted` : este mensaje está marcado para el borrado

- `seen` : este mensaje ya ha sido leído

- `draft` : este mensaje es un borrador

- `udate` : el horario UNIX de la hora de llegada

La función devuelve `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_fetch_overview`

```
<?php
$mbox = imap_open("{imap.example.org:143}INBOX", "username", "password")
     or die("Conexión imposible: " . imap_last_error());

$MC = imap_check($mbox);

// Recupera el resumen para todos los mensajes contenidos en INBOX
$result = imap_fetch_overview($mbox,"1:{$MC->Nmsgs}",0);
foreach ($result as $overview) {
    echo "#{$overview->msgno} ({$overview->date}) - From: {$overview->from}
    {$overview->subject}\n";
}
imap_close($mbox);
?>

    
```php

## Véase también

`imap_fetchheader`
