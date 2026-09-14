---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/ssh2.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: b3c45f073
order: 86400
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`SSH2_FINGERPRINT_MD5` (`int`)  
Flag que permite a la función `ssh2_fingerprint` solicitar la huella de la clave del host como hash MD5.

`SSH2_FINGERPRINT_SHA1` (`int`)  
Flag que permite a la función `ssh2_fingerprint` solicitar la huella de la clave del host como hash SHA1.

`SSH2_FINGERPRINT_HEX` (`int`)  
Flag que permite a la función `ssh2_fingerprint` solicitar la huella de la clave del host como string hexits.

`SSH2_FINGERPRINT_RAW` (`int`)  
Flag que permite a la función `ssh2_fingerprint` solicitar la huella de la clave del host como string de caracteres 8-bit.

`SSH2_TERM_UNIT_CHARS` (`int`)  
Flag que especifica a la función `ssh2_shell` que los parámetros `width` y `height` se proporcionan en forma de tamaño de caracteres.

`SSH2_TERM_UNIT_PIXELS` (`int`)  
Flag que especifica a la función `ssh2_shell` que los parámetros `width` y `height` se proporcionan en forma de píxeles.

`SSH2_DEFAULT_TERM_WIDTH` (`int`)  
Ancho por defecto del terminal solicitado por la función `ssh2_shell`.

`SSH2_DEFAULT_TERM_HEIGHT` (`int`)  
Altura por defecto del terminal solicitado por la función `ssh2_shell`.

`SSH2_DEFAULT_TERM_UNIT` (`int`)  
Unidad por defecto del terminal solicitado por la función `ssh2_shell`.

`SSH2_STREAM_STDIO` (`int`)  
Flag para que la función `ssh2_fetch_stream` solicite un subcanal STDIO.

`SSH2_STREAM_STDERR` (`int`)  
Flag para que la función `ssh2_fetch_stream` solicite un subcanal STDERR.

`SSH2_DEFAULT_TERMINAL` (`string`)  
Tipo por defecto del terminal (e.g. `"vt102"`, `"ansi"`, `"xterm"`, `"vanilla"`) solicitado por la función `ssh2_shell`.

`SSH2_POLLIN` (`int`)  

`SSH2_POLLEXT` (`int`)  

`SSH2_POLLOUT` (`int`)  

`SSH2_POLLERR` (`int`)  

`SSH2_POLLHUP` (`int`)  

`SSH2_POLLNVAL` (`int`)  

`SSH2_POLL_SESSION_CLOSED` (`int`)  

`SSH2_POLL_CHANNEL_CLOSED` (`int`)  

`SSH2_POLL_LISTENER_CLOSED` (`int`)
