---
title: Instalación
source_url: https://www.php.net/manual/es/ref.pdo-oci.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_oci/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_oci
translation_status: ready
translation_reviewed: false
translation_revision: 86177fa03
order: 62410
---

## Instalación

Si la base de datos Oracle se encuentra en la misma máquina que PHP, el software de la base de datos contiene ya las bibliotecas necesarias. Cuando PHP se encuentra en una máquina diferente, utilícense las bibliotecas gratuitas [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html). Para más detalles consúltese la sección sobre [Requisitos OCI8](#oci8.requirements).

## PHP 8.4

Esta extensión ha sido movida al módulo [PECL](https://pecl.php.net/) y no será integrada en PHP a partir de PHP 8.4.0

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/PDO_OCI>.

## PHP \< 8.4

Utilícese `--with-pdo-oci[=DIR]` para instalar la extensión PDO Oracle OCI, donde la opción `[=DIR]` es el directorio Oracle Home. `[=DIR]` corresponde por omisión a la variable de entorno `$ORACLE_HOME`.

Utilícese `--with-pdo-oci=instantclient,prefix,version` para un SDK Oracle Instant Client, donde prefix y version están configurados.

    // Utilización de $ORACLE_HOME
    $ ./configure --with-pdo-oci

    // Utilización de OIC para Linux con 10.2.0.3 RPMs con el prefijo /usr
    $ ./configure --with-pdo-oci=instantclient,/usr,10.2.0.3
