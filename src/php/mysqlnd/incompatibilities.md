---
title: Incompatibilidades
source_url: https://www.php.net/manual/es/mysqlnd.incompatibilities.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqlnd/incompatibilities.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqlnd
translation_status: ready
translation_reviewed: false
translation_revision: 9598935f2
order: 56130
---

## Incompatibilidades

El Driver MySQL Native es compatible en muchos casos con la librería MySQL Client (`libmysql`). Esta sección documenta las incompatibilidades entre estas librerías.

- Los valores de tipo `bit` son devueltos como strings binarios (p.e. "\0" o "\x1F") con `libmysql` y como strings decimales (p.e. "0" o "31") con `mysqlnd`. Si se desea que el código sea compatible con ambas librerías entonces siempre se deberá devolver campos de tipo bit como números desde MySQL con una consulta como la siguiente: `SELECT bit + 0 FROM table`.
