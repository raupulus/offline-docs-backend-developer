---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/pdo-cubrid.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_cubrid/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 62260
---

## Constantes predefinidas

Las constantes a continuación son definidas por este controlador y solo estarán disponibles cuando la extensión haya sido compilada en PHP o cargada dinámicamente del motor de ejecución. Además, estas constantes específicas del controlador deberían ser usadas solo si se usa este controlador. Usar atributos específicos de un controlador con otro controlador podría causar un comportamiento inesperado. `PDO::getAttribute` podría ser usado para obtener el atributo `PDO::ATTR_DRIVER_NAME` para verificar el controlador, si su código puede funcionar en múltiples controladores.

Las constantes siguientes pueden ser utilizadas para configurar los atributos de la base de datos. Pueden ser pasadas al método `PDO::getAttribute` o al método `PDO::setAttribute`.

| Constante | Descripción |
|----|----|
| `PDO::CUBRID_ATTR_ISOLATION_LEVEL` | El nivel de aislamiento de la transacción para la conexión a la base de datos. |
| `PDO::CUBRID_ATTR_LOCK_TIMEOUT` | Tiempo de expiración de la transacción en segundos. |
| `PDO::CUBRID_ATTR_MAX_STRING_LENGTH` | Solo lectura. La longitud máxima del string para los tipos de datos bit, varbit, char, varchar, nchar, nvarchar al utilizar la API CUBRID PDO. |

Banderas para los atributos PDO::CUBRID

Las constantes siguientes pueden ser utilizadas al configurar el nivel de aislamiento de la transacción. Pueden ser pasadas al método `PDO::getAttribute` o al método `PDO::setAttribute`.

| Constante | Descripción |
|----|----|
| `PDO::TRAN_COMMIT_CLASS_UNCOMMIT_INSTANCE` | El nivel de aislamiento más bajo (1). Una lectura no fiable, no reproducible o fantasma puede ocurrir sobre el tuple, pero también una lectura no reproducible puede ocurrir para la tabla. |
| `PDO::TRAN_COMMIT_CLASS_COMMIT_INSTANCE` | Un nivel de aislamiento relativamente bajo (2). Una lectura no fiable no puede ocurrir, pero una lectura no reproducible o fantasma puede ocurrir. |
| `PDO::TRAN_REP_CLASS_UNCOMMIT_INSTANCE` | El nivel de aislamiento por defecto para CUBRID (3). Una lectura no fiable o fantasma puede ocurrir sobre el tuple, pero la reproducibilidad de la lectura está asegurada sobre la tabla. |
| `PDO::TRAN_REP_CLASS_COMMIT_INSTANCE` | Un nivel de aislamiento relativamente bajo (4). Una lectura no fiable no puede ocurrir, pero las lecturas no reproducibles o fantasma pueden ocurrir. |
| `PDO::TRAN_REP_CLASS_REP_INSTANCE` | Un nivel de aislamiento relativamente alto (5). Las lecturas no fiables o no reproducibles no pueden ocurrir, pero una lectura fantasma es posible. |
| `PDO::TRAN_SERIALIZABLE` | El nivel de aislamiento más alto (6). Los problemas relacionados con la concurrencia (i.e. lectura no fiable, lectura no reproducible, lectura fantasma, etc...) no pueden ocurrir. |

Banderas para el nivel de aislamiento PDO::CUBRID

Las constantes siguientes pueden ser utilizadas para recuperar la información sobre el esquema. Pueden ser pasadas a la función `PDO::cubrid_schema`.

| Constante | Descripción |
|----|----|
| `PDO::CUBRID_SCH_TABLE` | Recupera el nombre y el tipo de tabla CUBRID. |
| `PDO::CUBRID_SCH_VIEW` | Recupera el nombre y el tipo de vista en CUBRID. |
| `PDO::CUBRID_SCH_QUERY_SPEC` | Recupera la definición de la consulta de la vista. |
| `PDO::CUBRID_SCH_ATTRIBUTE` | Recupera los atributos de la columna de la tabla. |
| `PDO::CUBRID_SCH_TABLE_ATTRIBUTE` | Recupera los atributos de la tabla. |
| `PDO::CUBRID_SCH_METHOD` | Recupera el método de la instancia. Es un método llamado por la instancia de la clase. Se utiliza más a menudo que el método de la clase ya que la mayoría de las operaciones se ejecutan en la instancia. |
| `PDO::CUBRID_SCH_TABLE_METHOD` | Recupera el método de la clase. Es un método llamado por un objeto de la clase. Se utiliza habitualmente para crear una nueva instancia de la clase o para inicializarla. También se utiliza para acceder o actualizar los atributos de la clase. |
| `PDO::CUBRID_SCH_METHOD_FILE` | Recupera la información sobre el archivo donde el método de la tabla está definido. |
| `PDO::CUBRID_SCH_SUPER_TABLE` | Recupera el nombre y el tipo de la tabla de la que los atributos heredan. |
| `PDO::CUBRID_SCH_SUB_TABLE` | Recupera el nombre y el tipo de la tabla de la que los atributos heredan. |
| `PDO::CUBRID_SCH_CONSTRAINT` | Recupera las restricciones de la tabla. |
| `PDO::CUBRID_SCH_TRIGGER` | Recupera los triggers de la tabla. |
| `PDO::CUBRID_SCH_TABLE_PRIVILEGE` | Recupera la información sobre los privilegios de la tabla. |
| `PDO::CUBRID_SCH_COL_PRIVILEGE` | Recupera la información sobre los privilegios de una columna. |
| `PDO::CUBRID_SCH_DIRECT_SUPER_TABLE` | Recupera la tabla directamente superior a la tabla. |
| `PDO::CUBRID_SCH_PRIMARY_KEY` | Recupera la clave primaria de la tabla. |
| `PDO::CUBRID_SCH_IMPORTED_KEYS` | Recupera las claves importadas de una tabla. |
| `PDO::CUBRID_SCH_EXPORTED_KEYS` | Recupera las claves exportadas de una tabla. |
| `PDO::CUBRID_SCH_CROSS_REFERENCE` | Recupera las relaciones de referencia entre 2 tablas. |

Banderas para el esquema CUBRID
