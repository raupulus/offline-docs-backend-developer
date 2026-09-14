---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/sqlite3.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 85580
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`SQLITE3_ASSOC` (`int`)  
Especifica que el método Sqlite3Result::fetchArray debe devolver un array indexado por el nombre de la columna en el conjunto de resultados correspondiente.

`SQLITE3_NUM` (`int`)  
Especifica que el método Sqlite3Result::fetchArray debe devolver un array indexado por el número de la columna en el conjunto de resultados correspondiente, comenzando por la columna 0.

`SQLITE3_BOTH` (`int`)  
Especifica que el método Sqlite3Result::fetchArray debe devolver un array indexado por el nombre y el número de la columna en el conjunto de resultados correspondiente, comenzando por la columna 0.

`SQLITE3_INTEGER` (`int`)  
Representa la clase de almacenamiento INTEGER de SQLite3.

`SQLITE3_FLOAT` (`int`)  
Representa la clase de almacenamiento REAL (FLOAT) de SQLite3.

`SQLITE3_TEXT` (`int`)  
Representa la clase de almacenamiento TEXT de SQLite3.

`SQLITE3_BLOB` (`int`)  
Representa la clase de almacenamiento BLOB de SQLite3.

`SQLITE3_NULL` (`int`)  
Representa la clase de almacenamiento NULL de SQLite3.

`SQLITE3_OPEN_READONLY` (`int`)  
Especifica que la base de datos SQLite3 debe ser abierta en modo de solo lectura.

`SQLITE3_OPEN_READWRITE` (`int`)  
Especifica que la base de datos SQLite3 debe ser abierta en modo de lectura y escritura.

`SQLITE3_OPEN_CREATE` (`int`)  
Especifica que la base de datos SQLite3 debe ser creada si no existe previamente.

`SQLITE3_DETERMINISTIC` (`int`)  
Especifica que una función creada con `SQLite3::createFunction` es determinista, es decir, que siempre devuelve el mismo resultado dado los mismos argumentos en una sola instrucción SQL. (disponible a partir de PHP 7.1.4)
