---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/cubrid.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 8580
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

Las constantes siguientes pueden ser utilizadas durante la ejecución de consultas SQL. Pueden ser pasadas a las funciones `cubrid_prepare` y `cubrid_execute`.

| Constante | Descripción |
|----|----|
| `CUBRID_INCLUDE_OID` | Determina si se debe recuperar el OID durante la ejecución de la consulta. |
| `CUBRID_ASYNC` | Ejecuta la consulta en modo asíncrono. |
| `CUBRID_EXEC_QUERY_ALL` | Ejecuta la consulta en modo síncrono. Este flag debe ser definido durante la ejecución de consultas SQL múltiples. |

Flags de ejecución SQL CUBRID

Las constantes siguientes pueden ser utilizadas durante la recuperación de los resultados para especificar su comportamiento. Pueden ser pasadas a las funciones `cubrid_fetch` y `cubrid_fetch_array`.

| Constante | Descripción |
|----|----|
| `CUBRID_NUM` | Recupera el resultado de la consulta en forma de array numérico (con índices comenzando en 0). |
| `CUBRID_ASSOC` | Recupera el resultado de la consulta en forma de array asociativo. |
| `CUBRID_BOTH` | Recupera el resultado de la consulta tanto en forma de array numérico como de array asociativo (valor por defecto). |
| `CUBRID_OBJECT` | Recupera el resultado de la consulta en forma de objeto. |
| `CUBRID_LOB` | La constante CUBRID_LOB puede ser utilizada cuando se desea utilizar un objeto LOB. Puede ser pasada a las funciones `cubrid_fetch`, `cubrid_fetch_row`, `cubrid_fetch_array`, `cubrid_fetch_assoc` y `cubrid_fetch_object`. |

Flags de recuperación CUBRID

Las constantes siguientes pueden ser utilizadas durante el posicionamiento del cursor en los resultados de la consulta. Pueden ser pasadas a o retornadas por la función `cubrid_move_cursor`.

| Constante | Descripción |
|----|----|
| `CUBRID_CURSOR_FIRST` | Mueve el cursor actual a la primera posición del resultado. |
| `CUBRID_CURSOR_CURRENT` | Mueve el cursor actual a un valor por defecto si el origen no está especificado. |
| `CUBRID_CURSOR_LAST` | Mueve el cursor actual a la última posición del resultado. |
| `CUBRID_CURSOR_SUCCESS` | El valor retornado por la función `cubrid_move_cursor` en caso de éxito. Este flag fue eliminado desde la versión 8.4.1. |
| `CUBRID_NO_MORE_DATA` | El valor retornado por la función `cubrid_move_cursor` si ocurre un error. Este flag fue eliminado desde la versión 8.4.1. |
| `CUBRID_CURSOR_ERROR` | El valor retornado por la función `cubrid_move_cursor` si ocurre un error. Este flag fue eliminado desde la versión 8.4.1. |

Flags de posicionamiento del cursor CUBRID

Las constantes siguientes pueden ser utilizadas durante la definición del modo auto-commit para la conexión a la base de datos. Pueden ser pasadas a la función `cubrid_set_autocommit` o retornadas por la función `cubrid_get_autocommit`.

| Constante                 | Descripción                    |
|---------------------------|--------------------------------|
| `CUBRID_AUTOCOMMIT_TRUE`  | Activa el modo auto-commit.    |
| `CUBRID_AUTOCOMMIT_FALSE` | Desactiva el modo auto-commit. |

Flags CUBRID para el modo auto-commit

Las constantes siguientes pueden ser utilizadas durante la definición de parámetros a la base de datos. Pueden ser pasadas a la función `cubrid_set_db_parameter`.

| Constante | Descripción |
|----|----|
| `CUBRID_PARAM_ISOLATION_LEVEL` | Nivel de aislamiento de la transacción para la conexión a la base de datos. |
| `CUBRID_PARAM_LOCK_TIMEOUT` | Tiempo de expiración de la transacción en segundos. |

Flags de parámetros CUBRID

Las constantes siguientes pueden ser utilizadas para definir el nivel de aislamiento de la transacción. Pueden ser pasadas a la función `cubrid_set_db_parameter` o retornadas por la función `cubrid_get_db_parameter`.

| Constante | Descripción |
|----|----|
| `TRAN_COMMIT_CLASS_UNCOMMIT_INSTANCE` | El nivel de aislamiento más bajo (1). Una lectura de datos modificados, no repetibles, o fantasmas puede ocurrir en el tuple y, además, una lectura no repetible puede ocurrir en la tabla. |
| `TRAN_COMMIT_CLASS_COMMIT_INSTANCE` | Un nivel de aislamiento relativamente bajo (2). Una lectura de datos modificados no puede ocurrir, pero una lectura de datos no repetibles o fantasmas puede ocurrir. |
| `TRAN_REP_CLASS_UNCOMMIT_INSTANCE` | El nivel de aislamiento por defecto para CUBRID (3). Una lectura de datos modificados, no repetibles o fantasmas puede ocurrir en el tuple, pero la lectura de datos repetibles está asegurada para la tabla. |
| `TRAN_REP_CLASS_COMMIT_INSTANCE` | Un nivel de aislamiento relativamente bajo (4). Una lectura de datos modificados no puede ocurrir, pero una lectura de datos no repetibles o fantasmas puede ocurrir. |
| `TRAN_REP_CLASS_REP_INSTANCE` | Un nivel de aislamiento relativamente alto (5). Una lectura de datos modificados o no repetibles no puede ocurrir, pero una lectura de datos fantasmas puede ocurrir. |
| `TRAN_SERIALIZABLE` | El nivel de aislamiento más alto (6). Los problemas relacionados con la concurrencia (i.e. lectura de datos modificados, no repetibles, fantasmas, etc...) no puede ocurrir. |

Flags CUBRID para el nivel de aislamiento

Las constantes siguientes pueden ser utilizadas para recuperar las informaciones de esquema. Pueden ser pasadas a la función `cubrid_schema`.

| Constante | Descripción |
|----|----|
| `CUBRID_SCH_CLASS` | Recupera el nombre y el tipo de la tabla en CUBRID. |
| `CUBRID_SCH_VCLASS` | Recupera el nombre y el tipo de la vista en CUBRID. |
| `CUBRID_SCH_QUERY_SPEC` | Recupera la definición de la consulta para una vista. |
| `CUBRID_SCH_ATTRIBUTE` | Recupera los atributos de una columna de una tabla. |
| `CUBRID_SCH_CLASS_ATTRIBUTE` | Recupera los atributos de una tabla. |
| `CUBRID_SCH_METHOD` | Recupera el método de la instancia. El método de la instancia es el método llamado por una instancia de clase. Es más frecuentemente utilizado que un método de clase ya que la mayoría de las operaciones son ejecutadas en la instancia. |
| `CUBRID_SCH_CLASS_METHOD` | Recupera el método de clase. El método de clase es el método llamado por un objeto de la clase. Es habitualmente utilizado para crear una nueva instancia de la clase o para inicializarla. También es utilizado para acceder o actualizar los atributos de la clase. |
| `CUBRID_SCH_METHOD_FILE` | Recupera las informaciones del archivo que define el método de la tabla. |
| `CUBRID_SCH_SUPERCLASS` | Recupera el nombre y el tipo de la tabla de la cual la tabla hereda sus atributos. |
| `CUBRID_SCH_SUBCLASS` | Recupera el nombre y el tipo de la tabla que hereda los atributos. |
| `CUBRID_SCH_CONSTRAINT` | Recupera las restricciones de la tabla. |
| `CUBRID_SCH_TRIGGER` | Recupera los triggers de la tabla. |
| `CUBRID_SCH_CLASS_PRIVILEGE` | Recupera las informaciones sobre los privilegios de la tabla. |
| `CUBRID_SCH_ATTR_PRIVILEGE` | Recupera las informaciones de privilegios de una columna. |
| `CUBRID_SCH_DIRECT_SUPER_CLASS` | Recupera la tabla super directa de la tabla. |
| `CUBRID_SCH_PRIMARY_KEY` | Recupera la clave primaria de la tabla. |
| `CUBRID_SCH_IMPORTED_KEYS` | Recupera las claves importadas de la tabla. |
| `CUBRID_SCH_EXPORTED_KEYS` | Recupera las claves exportadas de la tabla. |
| `CUBRID_SCH_CROSS_REFERENCE` | Recupera las referencias de los enlaces de 2 tablas. |

Flags para los esquemas CUBRID

Las constantes siguientes pueden ser utilizadas durante el reporte de errores. Pueden ser retornadas por la función `cubrid_error_code_facility`.

| Constante                | Descripción                                  |
|--------------------------|----------------------------------------------|
| `CUBRID_FACILITY_DBMS`   | El error ocurrió en la base de datos CUBRID. |
| `CUBRID_FACILITY_CAS`    | El error ocurrió en el broker CUBRID.        |
| `CUBRID_FACILITY_CCI`    | El error ocurrió en el cci CUBRID.           |
| `CUBRID_FACILITY_CLIENT` | El error ocurrió en el cliente PHP CUBRID.   |

Código de facilidad de errores CUBRID
