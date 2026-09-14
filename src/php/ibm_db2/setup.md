---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/ibm-db2.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_revision: 020edc73b
order: 31140
---

## Instalación/Configuración

## Requisitos

Para conectar a IBM DB2 Universal Database para Linux, Unix y Windows, o a IBM Cloudscape, o a Apache Derby, se debe instalar el cliente de IBM DB2 Universal Database en el mismo equipo en que se ejecuta PHP. Esta extensión se ha desarrollado y probado con DB2 Version 8.2.

Para conectar a IBM DB2 Universal Database en z/OS o iSeries, es necesario también IBM DB2 Connect o un software enrutador DRDA equivalente.

### Requisitos en Linux y Unix

El usuario que invoca el ejecutable de PHP o el SAPI debe especificar la instancia de DB2 antes de acceder a estas funciones. Se puede establecer el nombre de la instancia de DB2 en `php.ini` utilizando la opción de configuración `ibm_db2.instance_name`, o se puede cargar el perfil de la instancia de DB2 antes de invocar el ejecutable de PHP.

Si se ha creado una instancia de DB2 llamada `db2inst1` en `/home/db2inst1/`, por ejemplo, se puede añadir la siguiente línea a `php.ini`:

    ibm_db2.instance_name=db2inst1

        

Si no se establece esta opción en `php.ini`, se debe ejecutar el siguiente comando para modificar las variables de entorno y habilitar el acceso a DB2:

    bash$ source /home/db2inst1/sqllib/db2profile

        

Para permitir que el servidor web con PHP acceda a estas funciones, se debe establecer la opción de configuración `ibm_db2.instance_name` en `php.ini`, o cargar el entorno de la instancia de DB2 en el script de inicio del servidor web (típicamente `/etc/init.d/httpd` o `/etc/init.d/apache`).

## Tipos de recursos

La extensión ibm_db2 devuelve recursos de conexión, recursos de sentencias, y recursos de juegos de resultados.
