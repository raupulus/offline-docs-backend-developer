---
title: cubrid_schema
description: Recupera información sobre un esquema
source_url: https://www.php.net/manual/es/function.cubrid-schema.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-schema.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9440
---

cubrid_schema

Recupera información sobre un esquema

## Descripción

```php
cubrid_schema(resource $conn_identifier, int $schema_type, [string $class_name], [string $attr_name]): array
```php

La función `cubrid_schema` se utiliza para recuperar información de un esquema desde la base de datos. Para recuperar la información de una clase particular, debe definirse `class_name`, para recuperar la información sobre un atributo particular (solo utilizable con `CUBRID_SCH_ATTR_PRIVILEGE`), debe definirse `attr_name`.

El resultado de la función `cubrid_schema` se devuelve en forma de un array de 2 dimensiones (columna (array asociativo) \* filas (array numérico)). Las tablas siguientes muestran los tipos de un esquema así como la estructura de una columna del array resultante, según el tipo de esquema solicitado.

| Esquema | Número de columna | Nombre de la columna | Valor |
|----|----|----|----|
| CUBRID_SCH_CLASS | 1 | NAME |  |
|  | 2 | TYPE | 0:system class 1:vclass 2:class |
| CUBRID_SCH_VCLASS | 1 | NAME |  |
|  | 2 | TYPE | 1:vclass |
| CUBRID_SCH_QUERY_SPEC | 1 | QUERY_SPEC |  |
| CUBRID_SCH_ATTRIBUTE / CUBRID_SCH_CLASS_ATTRIBUTE | 1 | ATTR_NAME |  |
|  | 2 | DOMAIN |  |
|  | 3 | SCALE |  |
|  | 4 | PRECISION |  |
|  | 5 | INDEXED | 1:indexed |
|  | 6 | NOT NULL | 1:not null |
|  | 7 | SHARED | 1:shared |
|  | 8 | UNIQUE | 1:unique |
|  | 9 | DEFAULT |  |
|  | 10 | ATTR_ORDER | base:1 |
|  | 11 | CLASS_NAME |  |
|  | 12 | SOURCE_CLASS |  |
|  | 13 | IS_KEY | 1:key |
| CUBRID_SCH_METHOD / CUBRID_SCH_CLASS_METHOD | 1 | NAME |  |
|  | 2 | RET_DOMAIN |  |
|  | 3 | ARG_DOMAIN |  |
| CUBRID_SCH_METHOD_FILE | 1 | METHOD_FILE |  |
| CUBRID_SCH_SUPERCLASS / CUBRID_SCH_DIRECT_SUPER_CLASS / CUBRID_SCH_SUBCLASS | 1 | CLASS_NAME |  |
|  | 2 | TYPE | 0:system class 1:vclass 2:class |
| CUBRID_SCH_CONSTRAINT | 1 | TYPE | 0:unique 1:index 2:reverse unique 3:reverse index |
|  | 2 | NAME |  |
|  | 3 | ATTR_NAME |  |
|  | 4 | NUM_PAGES |  |
|  | 5 | NUM_KEYS |  |
|  | 6 | PRIMARY_KEY | 1:primary key |
|  | 7 | KEY_ORDER | base:1 |
| CUBRID_SCH_TRIGGER | 1 | NAME |  |
|  | 2 | STATUS |  |
|  | 3 | EVENT |  |
|  | 4 | TARGET_CLASS |  |
|  | 5 | TARGET_ATTR |  |
|  | 6 | ACTION_TIME |  |
|  | 7 | ACTION |  |
|  | 8 | PRIORITY |  |
|  | 9 | CONDITION_TIME |  |
|  | 10 | CONDITION |  |
| CUBRID_SCH_CLASS_PRIVILEGE / CUBRID_SCH_ATTR_PRIVILEGE | 1 | CLASS_NAME / ATTR_NAME |  |
|  | 2 | PRIVILEGE |  |
|  | 3 | GRANTABLE |  |
| CUBRID_SCH_PRIMARY_KEY | 1 | CLASS_NAME |  |
|  | 2 | ATTR_NAME |  |
|  | 3 | KEY_SEQ | base:1 |
|  | 4 | KEY_NAME |  |
| CUBRID_SCH_IMPORTED_KEYS / CUBRID_SCH_EXPORTED_KEYS / CUBRID_SCH_CROSS_REFERENCE | 1 | PKTABLE_NAME |  |
|  | 2 | PKCOLUMN_NAME |  |
|  | 3 | FKTABLE_NAME | base:1 |
|  | 4 | FKCOLUMN_NAME |  |
|  | 5 | KEY_SEQ | base:1 |
|  | 6 | UPDATE_ACTION | 0:cascade 1:restrict 2:no action 3:set null |
|  | 7 | DELETE_ACTION | 0:cascade 1:restrict 2:no action 3:set null |
|  | 8 | FK_NAME |  |
|  | 9 | PK_NAME |  |

Composición del resultado para cada tipo

## Parámetros

`conn_identifier`  
Identificador de conexión.

`schema_type`  
Datos del esquema a recuperar.

`class_name`  
Clase para la cual se desea conocer el esquema.

`attr_name`  
Atributo para el cual se desea conocer el esquema.

## Valores devueltos

Un array que contiene la información sobre el esquema en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.1 | Modificación del valor devuelto: cuando la función falla, el valor devuelto es ahora `false` en lugar de -1. |

## Ejemplos

Ejemplo con `cubrid_schema`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb", "dba");

printf("\n--- Primary Key ---\n");
$pk = cubrid_schema($conn, CUBRID_SCH_PRIMARY_KEY, "game");
var_dump($pk);

printf("\n--- Foreign Keys ---\n");
$fk = cubrid_schema($conn, CUBRID_SCH_IMPORTED_KEYS, "game");
var_dump($fk);

printf("\n--- Column Attribute ---\n");
$attr = cubrid_schema($conn, CUBRID_SCH_ATTRIBUTE, "stadium", "area");
var_dump($attr);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    --- Primary Key ---
    array(3) {
      [0]=>
      array(4) {
        ["CLASS_NAME"]=>
        string(4) "game"
        ["ATTR_NAME"]=>
        string(12) "athlete_code"
        ["KEY_SEQ"]=>
        string(1) "3"
        ["KEY_NAME"]=>
        string(41) "pk_game_host_year_event_code_athlete_code"
      }
      [1]=>
      array(4) {
        ["CLASS_NAME"]=>
        string(4) "game"
        ["ATTR_NAME"]=>
        string(10) "event_code"
        ["KEY_SEQ"]=>
        string(1) "2"
        ["KEY_NAME"]=>
        string(41) "pk_game_host_year_event_code_athlete_code"
      }
      [2]=>
      array(4) {
        ["CLASS_NAME"]=>
        string(4) "game"
        ["ATTR_NAME"]=>
        string(9) "host_year"
        ["KEY_SEQ"]=>
        string(1) "1"
        ["KEY_NAME"]=>
        string(41) "pk_game_host_year_event_code_athlete_code"
      }
    }

    --- Foreign Keys ---
    array(2) {
      [0]=>
      array(9) {
        ["PKTABLE_NAME"]=>
        string(7) "athlete"
        ["PKCOLUMN_NAME"]=>
        string(4) "code"
        ["FKTABLE_NAME"]=>
        string(4) "game"
        ["FKCOLUMN_NAME"]=>
        string(12) "athlete_code"
        ["KEY_SEQ"]=>
        string(1) "1"
        ["UPDATE_RULE"]=>
        string(1) "1"
        ["DELETE_RULE"]=>
        string(1) "1"
        ["FK_NAME"]=>
        string(20) "fk_game_athlete_code"
        ["PK_NAME"]=>
        string(15) "pk_athlete_code"
      }
      [1]=>
      array(9) {
        ["PKTABLE_NAME"]=>
        string(5) "event"
        ["PKCOLUMN_NAME"]=>
        string(4) "code"
        ["FKTABLE_NAME"]=>
        string(4) "game"
        ["FKCOLUMN_NAME"]=>
        string(10) "event_code"
        ["KEY_SEQ"]=>
        string(1) "1"
        ["UPDATE_RULE"]=>
        string(1) "1"
        ["DELETE_RULE"]=>
        string(1) "1"
        ["FK_NAME"]=>
        string(18) "fk_game_event_code"
        ["PK_NAME"]=>
        string(13) "pk_event_code"
      }
    }

    --- Column Attribute ---
    array(1) {
      [0]=>
      array(13) {
        ["ATTR_NAME"]=>
        string(4) "area"
        ["DOMAIN"]=>
        string(1) "7"
        ["SCALE"]=>
        string(1) "2"
        ["PRECISION"]=>
        string(2) "10"
        ["INDEXED"]=>
        string(1) "0"
        ["NON_NULL"]=>
        string(1) "0"
        ["SHARED"]=>
        string(1) "0"
        ["UNIQUE"]=>
        string(1) "0"
        ["DEFAULT"]=>
        NULL
        ["ATTR_ORDER"]=>
        string(1) "4"
        ["CLASS_NAME"]=>
        string(7) "stadium"
        ["SOURCE_CLASS"]=>
        string(7) "stadium"
        ["IS_KEY"]=>
        string(1) "0"
      }
    }
