---
title: Instalación
source_url: https://www.php.net/manual/es/ibm-db2.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30600
---

## Instalación

Para compilar la extensión ibm_db2, los archivos de encabezado y de biblioteca de la aplicación de desarrollo de DB2 deben estar presentes en el sistema. DB2 no los instala por omisión, por lo que podría ser necesario volver a la instalación de DB2 y añadir esta opción. El cliente de desarrollo de aplicación DB2 incluye los archivos de encabezado y está disponible libremente para su descarga desde el [sitio de soporte](https://www.ibm.com/developerworks/downloads/im/db2express/index.html) de la base de datos universal.

Si los archivos de encabezado y de biblioteca de la aplicación de desarrollo de DB2 se añaden en un sistema Linux o Unix donde DB2 ya está instalado, el comando `db2iupdt -e` deberá ejecutarse para actualizar los enlaces simbólicos hacia los archivos de encabezado y de biblioteca de las instancias DB2.

ibm_db2 es una extensión [PECL](https://pecl.php.net/), por lo que se deben seguir las instrucciones presentes en [???](#install.pecl) para instalar la extensión ibm_db2 para PHP. Ejecute el comando `configure` para indicar la ubicación de los archivos de encabezado y de biblioteca de DB2 de la siguiente manera:

    bash$ ./configure --with-IBM_DB2=/ruta/versus/DB2

      

El comando `configure` toma el valor por omisión de `/opt/IBM/db2/V8.1`.

> [!NOTE]
> Si el controlador ibm_db2 se utiliza con IIS (Microsoft Internet Information Server), podría ser necesario tomar las siguientes medidas:
>
> Instalar DB2 con el sistema de seguridad extendido.
>
> Añadir la ruta hacia el binario PHP a la variable de entorno
>
> PATH
>
> del sistema (Por omisión:
>
> C:\php\\
>
> ).
>
> Crear otra variable de entorno que contenga la ruta hacia el archivo PHP.INI (p. ej.:
>
> PHPRC = C:\php\\
>
> ).
>
> Añadir el usuario IUSR_COMPUTERNAME al grupo DB2USERS.
