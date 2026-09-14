---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/cubrid.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 330a38c4d
order: 9580
---

## Instalación/Configuración

## Requisitos

Para que estas funciones estén disponibles, se debe instalar CUBRID, y compilar la Biblioteca de PHP de CUBRID con soporte para CUBRID.

## Configuración en tiempo de ejecución

No existe configuración en tiempo de ejecución.

## Tipos de recursos

En CUBRID se usan cuatro tipos de recursos. El primero es un identificador de enlace para una conexión de base de datos, el segundo es un recurso que guarda el resultado de una consulta, y los dos últimos son recursos que guardan los resultados de una consulta de tipos de datos BLOB/CLOB.

### identificador de conexión

Un identificador de conexión devuelto por `cubrid_connect`, `cubrid_connect_with_url`, `cubrid_pconnect` y `cubrid_pconnect_with_url`.

### identificador de solicitud

Un identificador de solicitud devuelto por `cubrid_prepare` y `cubrid_execute`.

### identificador LOB

Un identificador LOB devuelto por `cubrid_lob_get`.

### identificador LOB2

Un identificador LOB devuelto por `cubrid_lob2_new` u obtenido de un conjunto de resultados.
