---
title: Instalación
source_url: https://www.php.net/manual/es/ref.pdo-odbc.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_odbc/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_odbc
translation_status: ready
translation_reviewed: false
translation_revision: 8a058e9ac
order: 62430
---

## Instalación

1.  PDO_ODBC está incluido en las fuentes de PHP. Puede compilarse la extensión PDO_ODBC ya sea de forma estática o como módulo compartido utilizando los siguientes comandos `configure`.

    ibm_db2  
        ./configure --with-pdo-odbc=ibm-db2,/opt/IBM/db2/V8.1/

                

    Para construir PDO_ODBC con el sabor ibm-db2, deben haberse instalado previamente los encabezados de desarrollo de la aplicación DB2 en la misma máquina donde se compila PDO_ODBC. Los encabezados de desarrollo de la aplicación DB2 son una opción de instalación en los servidores DB2 y también están disponibles como parte de DB2 Application Development Client gratuitamente disponibles para descarga desde el IBM developerWorks [sitio](https://www.ibm.com/developerworks/downloads/im/db2express/index.html).

    Si no se especifica una ubicación para las bibliotecas y los encabezados de DB2 en el comando `configure`, PDO_ODBC tomará por omisión `/home/db2inst1/sqllib`.

    unixODBC  
        ./configure --with-pdo-odbc=unixODBC,/usr/local

                

    Si no se especifica una ubicación para las bibliotecas y los encabezados de unixODBC en el comando `configure`, PDO_ODBC tomará por omisión `/usr/local`.

    generic  
        ./configure --with-pdo-odbc=generic,/usr/local,libname,ldflags,cflags
