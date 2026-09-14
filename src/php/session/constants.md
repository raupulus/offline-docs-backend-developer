---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/session.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: 7c4e8d821
order: 73690
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`SID` (`string`)  
Constante que contiene el nombre de la sesión y el identificador en curso, en el formato `"name=ID"` o una cadena vacía si el identificador de sesión ha sido definido en una cookie de sesión. Es el mismo valor que el devuelto por la función `session_id`.

> [!WARNING]
> Esta constante ha quedado obsoleta a partir de PHP 8.4.0.

`PHP_SESSION_DISABLED` (`int`)  
Valor devuelto por `session_status` si la sesión está desactivada.

`PHP_SESSION_NONE` (`int`)  
Valor devuelto por `session_status` si la sesión está activada, pero no existe.

`PHP_SESSION_ACTIVE` (`int`)  
Valor devuelto por `session_status` si la sesión está activada, y existe.
