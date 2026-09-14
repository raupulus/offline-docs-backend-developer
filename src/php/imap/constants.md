---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/imap.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 5e9500dda
order: 37910
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`NIL` (`int`)  
Obsoleto a partir de PHP 8.1.0.

`OP_DEBUG` (`int`)  

`OP_READONLY` (`int`)  
Abre un buzón de correo en modo de solo lectura.

`OP_ANONYMOUS` (`int`)  
No utilizar, o modificar el fichero `.newsrc` para las noticias, (NNTP únicamente).

`OP_SHORTCACHE` (`int`)  

`OP_SILENT` (`int`)  

`OP_PROTOTYPE` (`int`)  

`OP_HALFOPEN` (`int`)  
Para los nombres IMAP y NNTP, abre una conexión pero no abre un buzón de correo.

`OP_EXPUNGE` (`int`)  

`OP_SECURE` (`int`)  

`CL_EXPUNGE` (`int`)  
purgar automáticamente el buzón de correo al llamar a `imap_close`

`FT_UID` (`int`)  
El argumento es un UID.

`FT_PEEK` (`int`)  
No levantar el flag \Seen (Mensaje leído) si no está ya levantado.

`FT_NOT` (`int`)  

`FT_INTERNAL` (`int`)  
La cadena devuelta está en formato interno, y no va a canonizar los CRLF.

`FT_PREFETCHTEXT` (`int`)  

`ST_UID` (`int`)  
la secuencia contiene UID en lugar de números de secuencia

`ST_SILENT` (`int`)  

`ST_SET` (`int`)  

`CP_UID` (`int`)  
La secuencia de números contiene UID

`CP_MOVE` (`int`)  
Borra los mensajes después de copiar con `imap_mail_copy`

`SE_UID` (`int`)  
Devuelve UID en lugar de números

`SE_FREE` (`int`)  

`SE_NOPREFETCH` (`int`)  
No pretelecargar los mensajes encontrados

`SO_FREE` (`int`)  

`SO_NOSERVER` (`int`)  

`SA_MESSAGES` (`int`)  

`SA_RECENT` (`int`)  

`SA_UNSEEN` (`int`)  

`SA_UIDNEXT` (`int`)  

`SA_UIDVALIDITY` (`int`)  

`SA_ALL` (`int`)  

`LATT_NOINFERIORS` (`int`)  
Este buzón de correo no tiene "hijos" (no hay más buzones de correo debajo de este).

`LATT_NOSELECT` (`int`)  
Esto es solo un contenedor, no un buzón de correo (no se puede abrir).

`LATT_MARKED` (`int`)  
Este buzón de correo está marcado. Utilizado únicamente con UW-IMAPD.

`LATT_UNMARKED` (`int`)  
Este buzón de correo no está marcado. Utilizado únicamente con UW-IMAPD.

`LATT_REFERRAL` (`int`)  
Este contenedor tiene una referencia a un buzón de correo remoto.

`LATT_HASCHILDREN` (`int`)  
Este buzón de correo tiene inferiores seleccionables.

`LATT_HASNOCHILDREN` (`int`)  
Este buzón de correo no tiene inferiores seleccionables.

`SORTDATE` (`int`)  
Criterio de ordenación para `imap_sort` : Fecha del mensaje

`SORTARRIVAL` (`int`)  
Criterio de ordenación para `imap_sort` : Fecha de llegada

`SORTFROM` (`int`)  
Criterio de ordenación para `imap_sort` : Nombre de la primera caja de correo de la dirección de origen (From address)

`SORTSUBJECT` (`int`)  
Criterio de ordenación para `imap_sort` : Asunto del mensaje

`SORTTO` (`int`)  
Criterio de ordenación para `imap_sort` : Nombre de la primera caja de correo de destino (To address)

`SORTCC` (`int`)  
Criterio de ordenación para `imap_sort` : Nombre de la caja de correo de copia oculta (cc address)

`SORTSIZE` (`int`)  
Criterio de ordenación para `imap_sort` : Tamaño del mensaje en bytes

`TYPETEXT` (`int`)  
Tipo de cuerpo primario : texto no formateado

`TYPEMULTIPART` (`int`)  
Tipo de cuerpo primario : varias partes

`TYPEMESSAGE` (`int`)  
Tipo de cuerpo primario : mensaje encapsulado

`TYPEAPPLICATION` (`int`)  
Tipo de cuerpo primario : datos de aplicación

`TYPEAUDIO` (`int`)  
Tipo de cuerpo primario : audio

`TYPEIMAGE` (`int`)  
Tipo de cuerpo primario : imagen estática

`TYPEVIDEO` (`int`)  
Tipo de cuerpo primario : video

`TYPEMODEL` (`int`)  
Tipo de cuerpo primario : modelo

`TYPEOTHER` (`int`)  
Tipo de cuerpo primario : desconocido

`ENC7BIT` (`int`)  
Codificación del cuerpo : datos semánticos SMTP 7 bit

`ENC8BIT` (`int`)  
Codificación del cuerpo : datos semánticos SMTP 8 bit

`ENCBINARY` (`int`)  
Codificación del cuerpo : datos binarios 8 bit

`ENCBASE64` (`int`)  
Codificación del cuerpo : datos codificados en base-64

`ENCQUOTEDPRINTABLE` (`int`)  
Codificación del cuerpo : datos 8-7-bit legibles por el ser humano

`ENCOTHER` (`int`)  
Codificación del cuerpo : desconocido

`IMAP_OPENTIMEOUT` (`int`)  

`IMAP_READTIMEOUT` (`int`)  

`IMAP_WRITETIMEOUT` (`int`)  

`IMAP_CLOSETIMEOUT` (`int`)  

`IMAP_GC_ELT` (`int`)  
Recolección de la memoria, eliminación de las cachés de elementos de mensaje.

`IMAP_GC_ENV` (`int`)  
Recolección de la memoria, eliminación de las envolturas y cuerpos.

`IMAP_GC_TEXTS` (`int`)  
Recolección de la memoria, eliminación de los textos.
