---
title: Instalación
source_url: https://www.php.net/manual/es/odbc.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: eec6a4a36
order: 98610
---

## Instalación

`--with-adabas[=DIR]`  
Incluye el soporte para Adabas D. DIR es el directorio de instalación de Adabas D. Por omisión, es `/usr/local`.

`--with-sapdb[=DIR]`  
Incluye el soporte para SAP DB. DIR es el directorio de instalación de SAP DB. Por omisión, es `/usr/local`.

`--with-solid[=DIR]`  
Incluye el soporte para Solid. DIR es el directorio de instalación de Solid. Por omisión, es `/usr/local/solid`.

`--with-ibm-db2[=DIR]`  
Incluye el soporte para IBM DB2. DIR es el directorio de instalación de DB2. Por omisión, es `/home/db2inst1/sqllib`.

`--with-empress[=DIR]`  
Incluye el soporte para Empress. DIR es el directorio de instalación de Empress. Por omisión, es `$EMPRESSPATH`. Esta opción solo soporta Empress versión 8.60 y posteriores.

`--with-empress-bcs[=DIR]`  
Incluye el soporte para `"Empress Local Access"`. DIR es el directorio de instalación de Empress. Por omisión, es `$EMPRESSPATH`. Esta opción solo soporta Empress versión 8.60 y posteriores.

`--with-birdstep[=DIR]`  
Incluye el soporte para Birdstep. DIR es el directorio de instalación de Birdstep. Por omisión, es `/usr/local/birdstep`.

`--with-custom-odbc[=DIR]`  
Incluye el soporte para un ODBC definido por el usuario. DIR es el directorio de instalación de ODBC. Por omisión, es `/usr/local`. Asegúrese de que la variable CUSTOM_ODBC_LIBS esté definida y de que el fichero `odbc.h` esté en la ruta de inclusión, es decir, que se deban definir las siguientes líneas para `Sybase SQL Anywhere 5.5.00` bajo QNX, antes de utilizar el script de configuración: CPPFLAGS="-DODBC_QNX -DSQLANY_BUG" LDFLAGS=-lunix CUSTOM_ODBC_LIBS="-ldblib -lodbc".

`--with-iodbc[=DIR]`  
Incluye el soporte para iODBC. DIR es el directorio de instalación de iODBC. Por omisión, es `/usr/local`.

`--with-esoob[=DIR]`  
Incluye el soporte para Easysoft OOB. DIR es el directorio de instalación de OOB. Por omisión, es `/usr/local/easysoft/oob/client.`

`--with-unixodbc[=DIR]`  
Incluye el soporte para UnixODBC. DIR es el directorio de instalación de UnixODBC. Por omisión, es `/usr/local`.

`--with-openlink[=DIR]`  
Incluye el soporte para OpenLink ODBC. DIR es el directorio de instalación de OpenLink. Por omisión, es `/usr/local`. Es el mismo que para iODBC.

`--with-dbmaker[=DIR]`  
Incluye el soporte para DBMaker. DIR es el directorio de instalación de DBMaker. Por omisión, es la ruta de la última instalación de DBMaker (por ejemplo `/home/dbmaker/3.6`).

Los usuarios de Windows deben habilitar `php_odbc.dll` para utilizar esta extensión.
