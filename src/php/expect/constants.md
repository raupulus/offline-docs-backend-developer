---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/expect.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/expect/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: expect
translation_status: ready
translation_reviewed: false
translation_revision: aa1da6d20
order: 20750
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`EXP_GLOB` (`int`)  
Indica que el patrón es del tipo glob (tipo Unix).

`EXP_EXACT` (`int`)  
Indica que el patrón es una cadena exacta.

`EXP_REGEXP` (`int`)  
Indica que el patrón es un texto de tipo expresión regular.

`EXP_EOF` (`int`)  
Valor, devuelto por `expect_expectl`, cada vez que se alcanza EOF (fin del fichero).

`EXP_TIMEOUT` (`int`)  
Valor, devuelto por `expect_expectl` pasados unos determinados segundos, con el valor especificado en [expect.timeout](#ini.expect.timeout)

`EXP_FULLBUFFER` (`int`)  
Valor, devuelto por `expect_expectl` si no coincidiera ningún patrón.
