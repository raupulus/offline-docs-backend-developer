---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/oci8.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: aca4a6319
order: 57130
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

| Constante | Descripción |
|----|----|
| `OCI_ASSOC` | Utilizado con `oci_fetch_all` y `oci_fetch_array` para recuperar los resultados en un array asociativo. |
| `OCI_BOTH` | Utilizado con `oci_fetch_all` y `oci_fetch_array` para recuperar los resultados en un array asociativo e indexado numéricamente. |
| `OCI_COMMIT_ON_SUCCESS` | Modo de ejecución de comandos para `oci_execute`. El comando se valida automáticamente tras el éxito de la consulta. |
| `OCI_CRED_EXT` | Utilizado con `oci_connect` para la identificación en un servidor Oracle externo o en el sistema operativo. |
| `OCI_DEFAULT` | Ver la constante `OCI_NO_AUTO_COMMIT`. |
| `OCI_DESCRIBE_ONLY` | Modo de ejecución de comandos para `oci_execute`. Utilícelo si no desea ejecutar el comando, pero obtener descripciones. |
| `OCI_EXACT_FETCH` | Obsoleto. Modo de lectura de resultados. Utilizado cuando las aplicaciones conocen de antemano el número de líneas que se necesitarán leer. Este modo desactiva la lectura anticipada de Oracle versión 8 y posteriores. El cursor se anula una vez que se alcanza el número de líneas a leer, lo que reduce los recursos consumidos en el servidor. |
| `OCI_FETCHSTATEMENT_BY_COLUMN` | Modo por defecto de `oci_fetch_all`. |
| `OCI_FETCHSTATEMENT_BY_ROW` | Modo alternativo para `oci_fetch_all`. |
| `OCI_LOB_BUFFER_FREE` | Utilizado con [???](#ocilob.flush) para liberar los buffers utilizados. |
| `OCI_NO_AUTO_COMMIT` | Modo de ejecución de la consulta para `oci_execute`. La transacción no se valida automáticamente al utilizar este modo. Para mayor claridad en su código, utilice este valor en lugar del antiguo valor `OCI_DEFAULT`. |
| `OCI_NUM` | Utilizado con `oci_fetch_all` y `oci_fetch_array` para leer un array enumerado. |
| `OCI_RETURN_LOBS` | Utilizado con `oci_fetch_array` para obtener la valor del LOB en lugar del puntero. |
| `OCI_RETURN_NULLS` | Utilizado con `oci_fetch_array` para obtener elementos vacíos, si el valor del campo es `null`. |
| `OCI_SEEK_CUR` | Utilizado con [???](#ocilob.seek) para definir la posición. |
| `OCI_SEEK_END` | Utilizado con [???](#ocilob.seek) para definir la posición. |
| `OCI_SEEK_SET` | Utilizado con [???](#ocilob.seek) para definir la posición. |
| `OCI_SYSDATE` | Obsoleto. |
| `OCI_SYSDBA` | Utilizado con `oci_connect` para conectarse como SYSDBA utilizando credenciales externas ([oci8.privileged_connect](#ini.oci8.privileged-connect) debe estar activado para utilizar esta constante). |
| `OCI_SYSOPER` | Utilizado con `oci_connect` para conectarse como SYSOPER utilizando credenciales externas ([oci8.privileged_connect](#ini.oci8.privileged-connect) debe estar activado para utilizar esta constante). |
| `OCI_TEMP_BLOB` | Utilizado con [???](#ocilob.writetemporary) para indicar explícitamente que debe crearse un BLOB temporal. |
| `OCI_TEMP_CLOB` | Utilizado con [???](#ocilob.writetemporary) para indicar explícitamente que debe crearse un CLOB temporal. |

Métodos y funciones OCI8

| Constante | Descripción |
|----|----|
| `OCI_B_BFILE` | Utilizado con `oci_bind_by_name` para vincular BFILEs. |
| `OCI_B_BIN` | Utilizado con `oci_bind_by_name` para vincular valores brutos (RAW). |
| `OCI_B_BLOB` | Utilizado con `oci_bind_by_name` para vincular BLOB. |
| `OCI_B_BOL` | Utilizado con `oci_bind_by_name` para vincular una variable booleana PL/SQL. |
| `OCI_B_CFILEE` | Utilizado con `oci_bind_by_name` para vincular CFILEs. |
| `OCI_B_CLOB` | Utilizado con `oci_bind_by_name` para vincular CLOB. |
| `OCI_B_CURSOR` | Utilizado con `oci_bind_by_name` para vincular cursores, previamente asignados con `oci_new_descriptor`. |
| `OCI_B_INT` | Utilizado con `oci_bind_array_by_name` para vincular arrays de enteros. |
| `OCI_B_NTY` | Utilizado con `oci_bind_by_name` para vincular nombres de tipos de datos. |
| `OCI_B_NUM` | Utilizado con `oci_bind_array_by_name` para vincular arrays de números. |
| `OCI_B_ROWID` | Utilizado con `oci_bind_by_name` para vincular ROWID. |
| `SQLT_AFC` | Utilizado con `oci_bind_array_by_name` para vincular arrays de CHAR. |
| `SQLT_AVC` | Utilizado con `oci_bind_array_by_name` para vincular arrays de VARCHAR2. |
| `SQLT_BDOUBLE` | No soportado. |
| `SQLT_BFILEE` | Idéntico a `OCI_B_BFILE`. |
| `SQLT_BFLOAT` | No soportado. |
| `SQLT_BIN` | Idéntico a `OCI_B_BIN`. |
| `SQLT_BLOB` | Idéntico a `OCI_B_BLOB`. |
| `SQLT_BOL` | Idéntico a `OCI_B_BOL`. |
| `SQLT_CFILEE` | Idéntico a `OCI_B_CFILEE`. |
| `SQLT_CHR` | Utilizado con `oci_bind_array_by_name` para vincular arrays de VARCHAR2. También utilizado con `oci_bind_by_name`. |
| `SQLT_CLOB` | Idéntico a `OCI_B_CLOB`. |
| `SQLT_FLT` | Utilizado con `oci_bind_array_by_name` para vincular arrays de FLOAT. |
| `SQLT_INT` | Idéntico a `OCI_B_INT`. |
| `SQLT_LBI` | Utilizado con `oci_bind_by_name` para vincular valores LONG RAW. |
| `SQLT_LNG` | Utilizado con `oci_bind_by_name` para vincular valores LONG. |
| `SQLT_LVC` | Utilizado con `oci_bind_array_by_name` para vincular arrays de LONG VARCHAR. |
| `SQLT_NTY` | Idéntico a `OCI_B_NTY`. |
| `SQLT_NUM` | Idéntico a `OCI_B_NUM`. |
| `SQLT_ODT` | Utilizado con `oci_bind_array_by_name` para vincular arrays de LONG. |
| `SQLT_RDD` | Idéntico a `OCI_B_ROWID`. |
| `SQLT_RSET` | Idéntico a `OCI_B_CURSOR`. |
| `SQLT_STR` | Utilizado con `oci_bind_array_by_name` para vincular arrays de string. |
| `SQLT_UIN` | No soportado. |
| `SQLT_VCS` | Utilizado con `oci_bind_array_by_name` para vincular arrays de VARCHAR. |

Tipos definidos y vinculados OCI8

| Constante | Descripción |
|----|----|
| `OCI_DTYPE_FILE` | Esta opción indica a `oci_new_descriptor` que inicialice un nuevo puntero FILE. |
| `OCI_DTYPE_LOB` | Esta opción indica a `oci_new_descriptor` que inicialice un nuevo descriptor LOB. |
| `OCI_DTYPE_ROWID` | Esta opción indica a `oci_new_descriptor` que inicialice un nuevo puntero LOB. |
| `OCI_D_FILE` | Idéntico a `OCI_DTYPE_FILE`. |
| `OCI_D_LOB` | Idéntico a `OCI_DTYPE_LOB`. |
| `OCI_D_ROWID` | Idéntico a `OCI_DTYPE_ROWID`. |

Tipos de descriptores OCI8

`OCI_FO_ABORT` (`int`)  
El failover ha fallado y no hay posibilidad de reintentar.

`OCI_FO_BEGIN` (`int`)  
El failover ha detectado una conexión perdida y comienza el failover.

`OCI_FO_END` (`int`)  
El failover ha finalizado con éxito.

`OCI_FO_ERROR` (`int`)  
El failover ha fallado pero permite a la aplicación gestionar el error y devolver `OCI_FO_RETRY` para reintentar el failover.

`OCI_FO_NONE` (`int`)  
El usuario no ha solicitado ningún tipo de failover.

`OCI_FO_REAUTH` (`int`)  
Un usuario de Oracle ha sido reautenticado.

`OCI_FO_RETRY` (`int`)  
El failover debe ser reintentado por Oracle. En caso de error durante el failover a una nueva conexión, TAF puede reintentar el failover. Típicamente, el código de la aplicación debe dormir durante un tiempo antes de devolver `OCI_FO_RETRY`.

`OCI_FO_SELECT` (`int`)  
El usuario también ha solicitado el failover SELECT. Permite a los usuarios con cursores abiertos continuar utilizándolos tras una caída.

`OCI_FO_SESSION` (`int`)  
El usuario ha solicitado únicamente el failover de sesión. Por ejemplo, si la conexión de un usuario se pierde, entonces se crea automáticamente una nueva sesión para el usuario en la copia de seguridad. Este tipo de failover no intenta recuperar los SELECT.

`OCI_FO_TXNAL` (`int`)  
El usuario ha solicitado un failover de transacción.
