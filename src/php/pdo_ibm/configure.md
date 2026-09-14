---
title: Instalación
source_url: https://www.php.net/manual/es/ref.pdo-ibm.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_ibm/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_ibm
translation_status: ready
translation_reviewed: true
translation_revision: 9e2d8231b
order: 62330
---

## Instalación

Para compilar la extensión PDO_IBM, el cliente DB2 v9.1 o superior debe ser instalado en el mismo sistema que PHP. El cliente DB2 puede ser descargado desde el sitio de IBM de [desarrollo de aplicaciones](http://www.ibm.com/software/data/db2/ad).

> [!NOTE]
> El cliente DB2 v9.1 o superior soporta los accesos directos a DB2 para los sistemas Linux, UNIX y los servidores Windows v8 y v9.1.
>
> El cliente DB2 v9.1 soporta asimismo los accesos a DB2 UDB para i5 y DB2 UDB para los servidores z/OS utilizando el [producto de conexión DB2](http://www.ibm.com/software/data/db2/db2connect) de pago.

PDO_IBM es una extensión [PECL](https://pecl.php.net/); por lo tanto, las instrucciones de [???](#install.pecl) deben ser seguidas para instalar la extensión PDO_IBM. Ejecute el comando `configure` para que apunte hacia el directorio que contiene los ficheros de encabezado y las bibliotecas del cliente DB2 de la siguiente manera:

     bash$ ./configure --with-pdo-ibm=/path/to/sqllib[,shared]

      

El comando `configure` utiliza por omisión el valor de la variable de entorno `DB2DIR`.
