---
title: Instalación
source_url: https://www.php.net/manual/es/ref.pdo-informix.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_informix/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_informix
translation_status: ready
translation_reviewed: false
translation_revision: 9e2d8231b
order: 62350
---

## Instalación

Para compilar la extensión PDO_INFORMIX, debe estar instalado el SDK Client Informix 2.81 UC1 o superior en el mismo sistema que PHP. El SDK Client Informix está disponible en el [Sitio de Soporte IBM Informix](https://www.ibm.com/support/pages/download-informix-products).

PDO_INFORMIX es una extensión [PECL](https://pecl.php.net/), por lo que se deben seguir las instrucciones en [???](#install.pecl) para instalar la extensión PDO_INFORMIX. Se debe escribir el comando `configure` para indicar la ruta de los ficheros de encabezado del SDK Client Informix así como las bibliotecas de la siguiente manera:

       bash$ ./configure --with-pdo-informix=/path/to/SDK[,shared]

      

El comando `configure` utiliza por omisión la variable de entorno `INFORMIXDIR`.
