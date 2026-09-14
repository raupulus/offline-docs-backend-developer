---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/ibm-db2.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 30610
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`DB2_BINARY` (`int`)  
Especifica que los datos binarios serán devueltos tal cual. Este es el modo por defecto.

`DB2_CONVERT` (`int`)  
Especifica que los datos binarios serán convertidos a hexadecimal y devueltos como una cadena ASCII.

`DB2_PASSTHRU` (`int`)  
Especifica que los datos binarios serán convertidos a valor `null`.

`DB2_SCROLLABLE` (`int`)  
Especifica el cursor flotante para una declaración de recurso. Este modo permite un acceso aleatorio a las filas del juego de resultados, pero actualmente, solo es soportado por IBM DB2 Universal Database.

`DB2_FORWARD_ONLY` (`int`)  
Especifica un cursor de avance único para una declaración de recurso. Este es el valor por defecto de este tipo de cursor, y es soportado por todos los servidores de base de datos.

`DB2_PARAM_IN` (`int`)  
Especifica que la variable PHP debe ser vinculada como un parámetro ENTRADA para un procedimiento de registro.

`DB2_PARAM_OUT` (`int`)  
Especifica que la variable PHP debe ser vinculada como un parámetro SALIDA para un procedimiento de registro.

`DB2_PARAM_INOUT` (`int`)  
Especifica que la variable PHP debe ser vinculada como un parámetro ENTRADA/SALIDA para un procedimiento de registro.

`DB2_PARAM_FILE` (`int`)  
Especifica que la columna debe ser vinculada directamente a un fichero para entrada.

`DB2_AUTOCOMMIT_ON` (`int`)  
Especifica que autocommit debe ser activado.

`DB2_AUTOCOMMIT_OFF` (`int`)  
Especifica que autocommit debe ser desactivado.

`DB2_DOUBLE` (`int`)  
Especifica que la variable debe ser vinculada a un tipo DOUBLE, FLOAT o REAL.

`DB2_LONG` (`int`)  
Especifica que la variable debe ser vinculada a un tipo SMALLINT, INTEGER o BIGINT.

`DB2_CHAR` (`int`)  
Especifica que la variable debe ser vinculada a un tipo CHAR o VARCHAR

`DB2_CASE_NATURAL` (`int`)  
Especifica que los nombres de columnas deben ser devueltos en sus casos naturales.

`DB2_CASE_LOWER` (`int`)  
Especifica que los nombres de columnas deben ser devueltos en minúsculas.

`DB2_CASE_UPPER` (`int`)  
Especifica que los nombres de columnas deben ser devueltos en mayúsculas.

`DB2_DEFERRED_PREPARE_ON` (`int`)  
Especifica que la preparación diferida debe ser activada para el recurso de consulta especificado.

`DB2_DEFERRED_PREPARE_OFF` (`int`)  
Especifica que la preparación diferida debe ser desactivada para el recurso de consulta especificado.
