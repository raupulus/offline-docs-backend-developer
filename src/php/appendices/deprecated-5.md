---
title: Funcionalidades obsoletas
source_url: https://www.php.net/manual/es/migration73.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration73/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 47d0c1e6d
order: 610
---

## Funcionalidades obsoletas

## Núcleo PHP

### Constantes insensibles a mayúsculas y minúsculas

La declaración de constantes insensibles a las mayúsculas y minúsculas ha quedado obsoleta. Pasando `true` como el tercer argumento a `define` generará ahora una advertencia de deprecación. El uso de constantes insensibles a las mayúsculas y minúsculas con un caso que

### assert() con espacio de nombres

Declarando una función llamada `assert()` dentro de un espacio de nombres es obsoleto. La función `assert` está sujeta a un manejo especial por parte del motor, lo que puede dar lugar a un comportamiento inconsistente al definir una función con el mismo nombre.

### Buscando Strings en una aguja sin string

Pasar una aguja sin string a las funciones de búsqueda de string es obsoleto. En el futuro la aguja será interpretada como un string en lugar de un punto de código ASCII. Dependiendo del comportamiento deseado, debe lanzar la aguja explícitamente al string o realizar un llamado explícito a `chr`. Las siguientes funciones se ven afectadas:

- `strpos`

- `strrpos`

- `stripos`

- `strripos`

- `strstr`

- `strchr`

- `strrchr`

- `stristr`

### Streaming de Strip-Tags

La función `fgetss` y el [filtro stream string.strip_tags](#filters.string) son obsoletos. Esto también afecta al método SplFileObject::fgetss y la función `gzgetss`.

## Filtrado de datos

El uso explícito de las constantes `FILTER_FLAG_SCHEME_REQUIRED` y `FILTER_FLAG_HOST_REQUIRED` es ahora obsoleto; ambos están implícitos para `FILTER_VALIDATE_URL` de todos modos.

## Procesamiento de imágenes y GD

`image2wbmp` ha quedado obsoleta.

## Funciones de internacionalización

El uso de la forma `Normalizer::NONE` lanza una advertencia de obsoleto, si PHP es enlazado con ICU ≥ 56.

## Cadenas Multibyte

El siguiente alias indocumentado `mbereg_*()` ha sido desaprobado. Use las correspondientes variantes `mb_ereg_*()` en su lugar.

- `mbregex_encoding`

- `mbereg`

- `mberegi`

- `mbereg_replace`

- `mberegi_replace`

- `mbsplit`

- `mbereg_match`

- `mbereg_search`

- `mbereg_search_pos`

- `mbereg_search_regs`

- `mbereg_search_init`

- `mbereg_search_getregs`

- `mbereg_search_getpos`

- `mbereg_search_setpos`

## Funciones ODBC y DB2 (PDO_ODBC)

La configuración ini [pdo_odbc.db2_instance_name](#ini.pdo-odbc.db2-instance-name) ha sido formalmente desaprobada. Está obsoleto en la documentación a partir de PHP 5.1.1.
