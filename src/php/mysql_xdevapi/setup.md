---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/mysql-xdevapi.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: f88b2cc04
order: 54780
---

## Instalación/Configuración

## Requisitos

Esta extensión requiere un servidor MySQL 8+ con el complemento X activado (por omisión).

Las bibliotecas prerrequisitos para compilar esta extensión son: Boost (1.53.0 o superior), OpenSSL y Protobuf.

## Instalación

Esta extensión [PECL](https://pecl.php.net/) no está integrada en PHP.

Un ejemplo de procedimiento de instalación en Ubuntu 18.04 con PHP 7.2:

    // Dependencias
    $ apt install build-essential libprotobuf-dev libboost-dev openssl protobuf-compiler liblz4-tool zstd

    // PHP con las extensiones deseadas; php7.2-dev es requerido para compilar
    $ apt install php7.2-cli php7.2-dev php7.2-mysql php7.2-pdo php7.2-xml

    // Compilar esta extensión
    $ pecl install mysql_xdevapi

El comando `pecl install` no activa las extensiones PHP (por omisión) y activar las extensiones PHP puede hacerse de varias maneras. Otro ejemplo con PHP 7.2 en Ubuntu 18.04:

    // Crear su propio fichero ini
    $ echo "extension=mysql_xdevapi.so" > /etc/php/7.2/mods-available/mysql_xdevapi.ini

    // Utilizar el comando 'phpenmod' (nota: específico de Debian/Ubuntu)
    $ phpenmod -v 7.2 -s ALL mysql_xdevapi

    // Una alternativa a 'phpenmod' es crear un enlace simbólico manualmente
    // $ ln -s /etc/php/7.2/mods-available/mysql_xdevapi.ini /etc/php/7.2/cli/conf.d/20-mysql_xdevapi.ini

    // Veamos qué extensiones MySQL están activadas ahora
    $ php -m |grep mysql

    mysql_xdevapi
    mysqli
    mysqlnd
    pdo_mysql

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/mysql_xdevapi>.

## Compilar a partir de las fuentes

Consideraciones para compilar esta extensión a partir de las fuentes.

- El nombre de la extensión es 'mysql_xdevapi', por lo tanto, utilice `--enable-mysql-xdevapi`.

- Boost; requerido, utilice opcionalmente la opción de configuración --with-boost=DIR o defina la variable de entorno MYSQL_XDEVAPI_BOOST_ROOT. Solo se requieren los ficheros de encabezado boost; no los binarios.

- Google Protocol Buffers (protobuf): requerido, utilice opcionalmente la opción de configuración --with-protobuf=DIR o defina la variable de entorno MYSQL_XDEVAPI_PROTOBUF_ROOT.

  Opcionalmente utilice `make protobufs` para generar los ficheros protobuf (\*.pb.cc/.h), y `make clean-protobufs` para eliminar los ficheros protobuf generados.

  Nota específica para Windows: según su entorno, la biblioteca estática con un runtime DLL multi-thread puede ser necesaria. Para preparar, utilice las siguientes opciones: *-Dprotobuf_MSVC_STATIC_RUNTIME=OFF -Dprotobuf_BUILD_SHARED_LIBS=OFF*

- Google Protocol Buffers / protoc: requerido, asegúrese de que el correcto 'protoc' esté disponible en el PATH durante la compilación. Esto es particularmente importante ya que los scripts batch del SDK PHP Windows pueden sobrescribir el entorno.

- Bison: requerido, y disponible en el PATH.

  Nota específica para bison Windows: se recomienda encarecidamente utilizar bison proporcionado con el SDK PHP elegido, de lo contrario, un error similar a "zend_globals_macros.h(39): error C2375: 'zendparse': redefinition; different linkage Zend/zend_language_parser.h(214): note: see declaration of 'zendparse'" puede ser el resultado. Además, los scripts batch del SDK PHP Windows pueden sobrescribir el entorno.

- Nota específica para Windows: para preparar el entorno, consulte la documentación oficial de construcción de Windows para [el SDK actual](https://wiki.php.net/internals/windows/stepbystepbuild_sdk_2).

  Se recomienda utilizar las barras invertidas '\\' en lugar de una barra '/' para todos los caminos.
