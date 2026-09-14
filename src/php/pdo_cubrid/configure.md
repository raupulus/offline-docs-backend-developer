---
title: Instalación
source_url: https://www.php.net/manual/es/ref.pdo-cubrid.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_cubrid/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 59ce48edd
order: 62250
---

## Instalación

Para construir la extensión PDO_CUBRID, el sistema de gestión de bases de datos CUBRID debe estar instalado en el mismo sistema que PHP. PDO_CUBRID es una extensión [PECL](https://pecl.php.net/), por lo tanto, debe seguirse las instrucciones de [???](#install.pecl) para instalar la extensión PDO_CUBRID. Ejecute el comando `configure` para localizar el directorio base de CUBRID de la siguiente manera:

       $ ./configure --with-pdo-cubrid=/path/to/CUBRID[,shared]

      

El comando `configure` tomará por omisión el valor de la variable de entorno `CUBRID`.

No hay biblioteca DLL para esta extensión PECL actualmente disponible. Consulte la sección [Compilación en Windows](#install.windows.building) . Información sobre la instalación manual en Linux y Windows puede encontrarse en el archivo build-guide.html del paquete CUBRID de PECL.
