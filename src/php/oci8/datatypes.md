---
title: Tipos de datos admitidos
source_url: https://www.php.net/manual/es/oci8.datatypes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/datatypes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: 44e38e287
order: 57140
---

## Tipos de datos admitidos

| Tipo | Referencia |
|----|----|
| `SQLT_NTY` | Hace referencia a un tipo de colección nativo desde un objeto colección de PHP, tales como aquellos creados por `oci_new_collection`. |
| `SQLT_BFILEE` | Hace referencia a un descriptor nativo, tales como a aquellos creados por `oci_new_descriptor`. |
| `SQLT_CFILEE` | Hace referencia a un descriptor nativo, tales como a aquellos creados por `oci_new_descriptor`. |
| `SQLT_CLOB` | Hace referencia a un descriptor nativo, tales como a aquellos creados por `oci_new_descriptor`. |
| `SQLT_BLOB` | Hace referencia a un descriptor nativo, tales como a aquellos creados por `oci_new_descriptor`. |
| `SQLT_RDD` | Hace referencia a un descriptor nativo, tales como a aquellos creados por `oci_new_descriptor`. |
| `SQLT_NUM` | Convierte el parámetro de PHP al tipo long de 'C', y lo vincula a ese valor. |
| `SQLT_RSET` | Hace referencia a un gestor de sentencias nativo, tales como a aquellos creados por `oci_parse` o aquellos recuperados desde otras consultas de OCI. |
| `SQLT_BOL` | Vincular el parámetro de PHP a un BOOLEAN de PL/SQL |
| `SQLT_CHR` y cualquier otro tipo | Convierte el parámetro de PHP al tipo string y lo vincula como string. |

El controlador admite los siguientes tipos cuando se vinculan parámetros usando la función `oci_bind_by_name`:

| Tipo | Referencia |
|----|----|
| `SQLT_RSET` | Crea un recurso de sentencia de OCI para representar al cursor. |
| `SQLT_RDD` | Crea un objeto ROWID. |
| `SQLT_BLOB` | Crea un objeto LOB. |
| `SQLT_CLOB` | Crea un objeto LOB. |
| `SQLT_BFILE` | Crea un objeto LOB. |
| `SQLT_LNG` | Vinculado como SQLT_CHR, devuelto como string |
| `SQLT_LBI` | Vinculado como `SQLT_BIN`, devuelto como string |
| Cualquier otro tipo | Vinculado como `SQLT_CHR`, devuelto como string |

Los siguientes tipos son admitidos cuando se recuperan columnas desde un conjunto de resultados:
