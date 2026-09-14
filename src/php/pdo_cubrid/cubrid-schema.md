---
title: PDO::cubrid_schema
description: Recupera el esquema de información solicitado
source_url: https://www.php.net/manual/es/pdo.cubrid-schema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_cubrid/pdo_overloaded/cubrid-schema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 59ce48edd
order: 62270
---

PDO::cubrid_schema

Recupera el esquema de información solicitado

## Descripción

```php
public PDO::cubrid_schema(int $schema_type, [string $table_name], [string $col_name]): array
```php

Esta función se utiliza para recuperar el esquema de información solicitado desde la base de datos. Debe designarse el argumento `table_name`, si se desea recuperar las informaciones de una cierta tabla, el argumento `col_name`, si se desea recuperar las informaciones de una cierta columna (solo puede ser utilizado con PDO::CUBRID_SCH_COL_PRIVILEGE).

El resultado de esta función es devuelto en forma de un array de 2 dimensiones (columna(array asociativo) \* fila (array numérico)). Las tablas siguientes muestran los tipos de esquema y la estructura de la columna del array resultante.

| Esquema | Número de la columna | Nombre de la columna | Valor |
|----|----|----|----|
| PDO::CUBRID_SCH_TABLE | 1 | NAME |  |
|  | 2 | TYPE | 0:tabla del sistema 1:vista 2:tabla |
| PDO::CUBRID_SCH_VIEW | 1 | NAME |  |
|  | 2 | TYPE | 1:vista |
| PDO::CUBRID_SCH_QUERY_SPEC | 1 | QUERY_SPEC |  |
| PDO::CUBRID_SCH_ATTRIBUTE / PDO::CUBRID_SCH_TABLE_ATTRIBUTE | 1 | ATTR_NAME |  |
|  | 2 | DOMAIN |  |
|  | 3 | SCALE |  |
|  | 4 | PRECISION |  |
|  | 5 | INDEXED | 1:indexado |
|  | 6 | NOT NULL | 1:no nulo |
|  | 7 | SHARED | 1:compartido |
|  | 8 | UNIQUE | 1:único |
|  | 9 | DEFAULT |  |
|  | 10 | ATTR_ORDER | base:1 |
|  | 11 | CLASS_NAME |  |
|  | 12 | SOURCE_CLASS |  |
|  | 13 | IS_KEY | 1:clave |
| PDO::CUBRID_SCH_METHOD / PDO::CUBRID_SCH_TABLE_METHOD | 1 | NAME |  |
|  | 2 | RET_DOMAIN |  |
|  | 3 | ARG_DOMAIN |  |
| PDO::CUBRID_SCH_METHOD_FILE | 1 | METHOD_FILE |  |
| PDO::CUBRID_SCH_SUPER_TABLE / PDO::CUBRID_SCH_DIRECT_SUPER_TABLE / PDO::CUBRID_SCH_SUB_TABLE | 1 | CLASS_NAME |  |
|  | 2 | TYPE | 0:tabla del sistema 1:vista 2:tabla |
| PDO::CUBRID_SCH_CONSTRAINT | 1 | TYPE | 0:único 1:índice 2:único inverso 3:índice inverso |
|  | 2 | NAME |  |
|  | 3 | ATTR_NAME |  |
|  | 4 | NUM_PAGES |  |
|  | 5 | NUM_KEYS |  |
|  | 6 | PRIMARY_KEY | 1:clave primaria |
|  | 7 | KEY_ORDER | base:1 |
| PDO::CUBRID_SCH_TRIGGER | 1 | NAME |  |
|  | 2 | STATUS |  |
|  | 3 | EVENT |  |
|  | 4 | TARGET_CLASS |  |
|  | 5 | TARGET_ATTR |  |
|  | 6 | ACTION_TIME |  |
|  | 7 | ACTION |  |
|  | 8 | PRIORITY |  |
|  | 9 | CONDITION_TIME |  |
|  | 10 | CONDITION |  |
| PDO::CUBRID_SCH_TABLE_PRIVILEGE / PDO::CUBRID_SCH_COL_PRIVILEGE | 1 | CLASS_NAME / ATTR_NAME |  |
|  | 2 | PRIVILEGE |  |
|  | 3 | GRANTABLE |  |
| PDO::CUBRID_SCH_PRIMARY_KEY | 1 | CLASS_NAME |  |
|  | 2 | ATTR_NAME |  |
|  | 3 | KEY_SEQ | base:1 |
|  | 4 | KEY_NAME |  |
| PDO::CUBRID_SCH_IMPORTED_KEYS / PDO::CUBRID_SCH_EXPORTED_KEYS / PDO::CUBRID_SCH_CROSS_REFERENCE | 1 | PKTABLE_NAME |  |
|  | 2 | PKCOLUMN_NAME |  |
|  | 3 | FKTABLE_NAME | base:1 |
|  | 4 | FKCOLUMN_NAME |  |
|  | 5 | KEY_SEQ | base:1 |
|  | 6 | UPDATE_ACTION | 0:cascada 1:restringir 2:sin acción 3:establecer nulo |
|  | 7 | DELETE_ACTION | 0:cascada 1:restringir 2:sin acción 3:establecer nulo |
|  | 8 | FK_NAME |  |
|  | 9 | PK_NAME |  |

Composición del resultado para cada tipo

## Parámetros

`schema_type`  
El tipo de esquema que se desea recuperar.

`table_name`  
La tabla de la cual se desea recuperar el esquema.

`col_name`  
La columna de la cual se desea recuperar el esquema.

## Valores devueltos

Un array que contiene las informaciones relativas al esquema, cuando el proceso se ha ejecutado con éxito.

FALSE será devuelto si ocurre un error.

## Ejemplos

Ejemplo con `PDO::cubrid_schema`

Este ejemplo muestra cómo recuperar las claves primarias y extranjeras de la tabla "game".

```
<?php
$pk_list = $dbh->cubrid_schema(PDO::CUBRID_SCH_PRIMARY_KEY, "game");
print_r($pk_list);

$fk_list = $dbh->cubrid_schema(PDO::CUBRID_SCH_IMPORTED_KEYS, "game");
print_r($fk_list);
?>

   
```php

El ejemplo anterior mostrará:

    Resultado:
    Array
    (
        [0] => Array
            (
                [CLASS_NAME] => game
                [ATTR_NAME] => athlete_code
                [KEY_SEQ] => 3
                [KEY_NAME] => pk_game_host_year_event_code_athlete_code
            )

        [1] => Array
            (
                [CLASS_NAME] => game
                [ATTR_NAME] => event_code
                [KEY_SEQ] => 2
                [KEY_NAME] => pk_game_host_year_event_code_athlete_code
            )

        [2] => Array
            (
                [CLASS_NAME] => game
                [ATTR_NAME] => host_year
                [KEY_SEQ] => 1
                [KEY_NAME] => pk_game_host_year_event_code_athlete_code
            )

    )
    Array
    (
        [0] => Array
            (
                [PKTABLE_NAME] => athlete
                [PKCOLUMN_NAME] => code
                [FKTABLE_NAME] => game
                [FKCOLUMN_NAME] => athlete_code
                [KEY_SEQ] => 1
                [UPDATE_RULE] => 1
                [DELETE_RULE] => 1
                [FK_NAME] => fk_game_athlete_code
                [PK_NAME] => pk_athlete_code
            )

        [1] => Array
            (
                [PKTABLE_NAME] => event
                [PKCOLUMN_NAME] => code
                [FKTABLE_NAME] => game
                [FKCOLUMN_NAME] => event_code
                [KEY_SEQ] => 1
                [UPDATE_RULE] => 1
                [DELETE_RULE] => 1
                [FK_NAME] => fk_game_event_code
                [PK_NAME] => pk_event_code
            )

    )
