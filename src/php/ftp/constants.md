---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/ftp.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 5bc8ebe3c
order: 24320
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`FTP_ASCII` (`int`)  

`FTP_AUTOSEEK` (`int`)  
Ver `ftp_set_option` para más información.

`FTP_AUTORESUME` (`int`)  
Determinar automáticamente la posición de reanudación y la posición de inicio para las peticiones GET y PUT (solo funciona si FTP_AUTOSEEK está activado)

`FTP_FAILED` (`int`)  
La transferencia asíncrona ha fallado

`FTP_FINISHED` (`int`)  
La transferencia asíncrona ha finalizado

`FTP_MOREDATA` (`int`)  
La transferencia asíncrona sigue activa

`FTP_TEXT` (`int`)  
Alias de `FTP_ASCII`.

`FTP_BINARY` (`int`)  

`FTP_IMAGE` (`int`)  
Alias de `FTP_BINARY`.

`FTP_TIMEOUT_SEC` (`int`)  
Ver `ftp_set_option` para más información.

`FTP_USEPASVADDRESS` (`int`)  
Ver `ftp_set_option` para más información.
