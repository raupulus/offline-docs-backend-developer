---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/dba.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 11670
---

## Instalación/Configuración

## Requisitos

El comportamiento de ciertos aspectos depende de la implementación de la base de datos subyacente. Las funciones como `dba_optimize` y `dba_sync` funcionan como se espera para una base de datos, mientras que pueden no hacer nada en otras. Deben descargarse e instalarse los gestores DBA soportados.

| Gestor | Notas |
|----|----|
| `dbm` | DBM es la más antigua (la original) de las bases de datos de estilo Berkeley DB. Debería evitarse su uso si es posible. No se proporciona soporte para la compatibilidad de las funciones internas a DB2 y gdbm, ya que solo son compatibles a nivel de código fuente, pero no pueden manejar el formato original DBM. |
| `ndbm` | Ndbm es un nuevo tipo y más flexible que dbm. Sin embargo, presenta limitaciones arbitrarias de dbm (y por lo tanto, está obsoleto). |
| `gdbm` | Gdbm es un [gestor de bases de datos GNU](https://ftp.gnu.org/pub/gnu/gdbm/). |
| `db2` | [Oracle Berkeley DB 2](http://www.sleepycat.com/). Se describe como "un toolkit que proporciona soporte de alto rendimiento para bases de datos, tanto del lado cliente como del lado servidor." |
| `db3` | [Oracle Berkeley DB 3](http://www.sleepycat.com/). |
| `db4` | [Oracle Berkeley DB 4 o 5](http://www.sleepycat.com/). Esta opción puede utilizarse con BDB 5 a partir de PHP 5.3.3. |
| `cdb` | Cdb es un paquete rápido, ligero y fiable para crear y leer bases de datos constantes. Fue creado por el autor de qmail y puede encontrarse en <http://cr.yp.to/cdb.html>. Dado que es "constante", solo se soportarán las operaciones de lectura. También se soporta la escritura (y no la actualización) mediante la biblioteca interna cdb. |
| `cdb_make` | Se soporta la escritura (y no la actualización) de archivos cdb cuando se utiliza la biblioteca cdb. |
| `flatfile` | Esto está disponible por razones de compatibilidad con la extensión obsoleta `dbm`. Sin embargo, puede utilizarse cuando los archivos han sido creados en este formato. Ocurre cuando la configuración no ha logrado encontrar una biblioteca externa. |
| `inifile` | Esto está disponible para permitir la modificación de los archivos php.ini desde scripts PHP. Al utilizar archivos ini, pueden pasarse arrays de la forma (0=\>grupo,1=\>nombre_valor) o strings de la forma "\[grupo\]nombre_valor" donde el grupo es opcional. Dado que las funciones `dba_firstkey` y `dba_nextkey` devuelven un string representando la clave, existe una nueva función, `dba_key_split`, que permite convertir las claves en arrays sin pérdida. |
| `qdbm` | La biblioteca qdbm puede descargarse desde <http://fallabs.com/qdbm/index.html>. |
| `tcadb` | La biblioteca Tokyo Cabinet puede ser descargada desde <http://fallabs.com/tokyocabinet/>. |
| `lmdb` | Disponible a partir de PHP 7.2.0. La biblioteca Lightning Memory-Mapped Database puede ser descargada desde <https://symas.com/lmdb/>. |

Lista de gestores DBA

Al llamar a la función `dba_open` o la función `dba_popen`, debe proporcionarse uno de los nombres de gestor como argumento. La lista de gestores disponibles puede mostrarse utilizando la función `phpinfo` o la función `dba_handlers`.

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [dba.default_handler](#ini.dba.default_handler) | DBA_DEFAULT | `INI_ALL` |  |

Opciones de configuración DBA

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`dba.default_handler` `string`  
El nombre del gestor por defecto

## Tipos de recursos

A partir de PHP 8.4.0, la mayoría de las funciones DBA operan sobre o devuelven recursos (por ejemplo, `dba_open` devuelve un identificador de enlace DBA positivo requerido por la mayoría de las funciones DBA).
