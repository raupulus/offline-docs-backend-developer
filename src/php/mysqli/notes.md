---
title: Notas
source_url: https://www.php.net/manual/es/mysqli.notes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/notes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: cd09fab47
order: 56040
---

## Notas

Algunas notas sobre la implementación:

1.  El soporte para `MYSQL_TYPE_GEOMETRY` fue añadido a la extensión MySQLI en PHP 5.3.

2.  Cabe señalar que existen diferencias internas de implementación entre `libmysqlclient` y `mysqlnd` para gestionar las columnas de tipo `MYSQL_TYPE_GEOMETRY`. En términos generales, `mysqlnd` asigna considerablemente menos memoria. Por ejemplo, si existe una columna de tipo `POINT` en el conjunto de resultados, `libmysqlclient` asignará aproximadamente 4GB de RAM mientras que solo se requieren 50 bytes para gestionar una columna de tipo `POINT` en memoria. La asignación de memoria es aún menor que 50 bytes al utilizar `mysqlnd`.
