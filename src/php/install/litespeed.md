---
title: Servidor Web LiteSpeed/Servidor Web OpenLiteSpeed en sistemas Unix
source_url: https://www.php.net/manual/es/install.unix.litespeed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/unix/litespeed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: true
translation_revision: e8ac70bf5
order: 1850
---

## Servidor Web LiteSpeed/Servidor Web OpenLiteSpeed en sistemas Unix

LiteSpeed PHP es una compilación optimizada de PHP construida para funcionar con los productos LiteSpeed a través de la API LiteSpeed. LSPHP funciona como su propio proceso y tiene su propio binario autónomo, que puede ser utilizado como un simple binario en línea de comandos para ejecutar scripts PHP desde la línea de comandos.

LSAPI es una API altamente optimizada que permite la comunicación entre LiteSpeed y motores web de terceros. Su protocolo es similar a FCGI, pero es más eficiente.

Esta documentación cubrirá la instalación y configuración de PHP con LSAPI para un servidor Web LiteSpeed y un servidor Web OpenLiteSpeed.

Se asumirá que LSWS o OLS está instalado con sus rutas y flags por omisión. El directorio de instalación por omisión para ambos servidores Web es /usr/local/lsws y ambos pueden ser ejecutados desde el subdirectorio bin.

Tenga en cuenta que a lo largo de esta documentación, los números de versión han sido reemplazados por un `x` para garantizar que esta documentación permanezca correcta en el futuro, reemplácelos, si es necesario, por los números de versión correspondientes.

1.  Para obtener e instalar LiteSpeed Web Server o OpenLiteSpeed Web Server, visite la [página de instalación](https://docs.litespeedtech.com/products/lsws/installation/) de la documentación de LiteSpeed Web Server o la [página de instalación](https://docs.openlitespeed.org/installation/source/). de la documentación OpenLiteSpeed

2.  Descargue y descomprima el código fuente de PHP:

        mkdir /home/php
        cd /home/php
        wget http://us1.php.net/get/php-x.x.x.tar.gz/from/this/mirror
        tar -zxvf php-x.x.x.tar.gz
        cd php-x.x.x

3.  Configure y construya PHP. Aquí es donde PHP puede ser personalizado con diversas opciones, tales como las extensiones que serán activadas. Ejecute ./configure --help para obtener una lista de las opciones disponibles. En el ejemplo, se utilizarán las opciones de configuración recomendadas por omisión para LiteSpeed Web Server:

        ./configure ... '--with-litespeed'
        make
        sudo make install

4.  Verificar la instalación de LSPHP

    Una de las formas más simples de verificar si la instalación de PHP ha tenido éxito es ejecutar el siguiente código:

        cd /usr/local/lsws/fcgi-bin/
        ./lsphp5 -v

    Esto debería devolver información sobre la nueva versión de PHP:

        PHP 5.6.17 (litespeed) (built: Mar 22 2016 11:34:19)
        Copyright (c) 1997-2014 The PHP Group
        Zend Engine v2.6.0, Copyright (c) 1998-2015 Zend Technologies

    Observe el `litespeed` entre paréntesis. Esto significa que el binario PHP ha sido construido con soporte LSAPI.

Después de seguir los pasos anteriores, LiteSpeed / OpenLiteSpeed Web Server debería ahora funcionar con soporte de PHP como una extensión SAPI. Existen muchas otras opciones de configuración disponibles para LSWS / OLS y PHP. Para más información, consulte la documentación de LiteSpeed en [PHP](https://docs.litespeedtech.com/extapp/php/configuration/control/).

Uso de LSPHP desde la línea de comandos:

El modo de línea de comandos LSPHP (LSAPI + PHP) se utiliza para procesar scripts PHP en ejecución en un servidor remoto que no necesariamente tiene un servidor web en ejecución. Se utiliza para procesar scripts PHP residentes en un servidor web local (separado). Esta configuración es adecuada para la escalabilidad del servicio ya que el procesamiento PHP se descarga a un servidor remoto.

Iniciar lsphp desde la línea de comandos en un servidor remoto: LSPHP es un ejecutable y puede ser iniciado manualmente y ligado a direcciones IPv4, IPv6 o direcciones de socket de dominio Unix con la opción de línea de comandos -b socket_address

Ejemplos:

Hacer que LSPHP se ligue al puerto 3000 en todas las direcciones IPv4 e IPv6:

    /path/to/lsphp -b [::]:3000

Hacer que LSPHP se ligue al puerto 3000 en todas las direcciones IPv4:

    /path/to/lsphp -b *:3000

Hacer que LSPHP se ligue a la dirección 192.168.0.2:3000:

    /path/to/lsphp -b 192.168.0.2:3000

Hacer que LSPHP acepte las solicitudes en el socket de dominio Unix `/tmp/lsphp_manual.sock`:

    /path/to/lsphp -b /tmp/lsphp_manual.sock

Las variables de entorno pueden ser añadidas antes del ejecutable LSPHP:

    PHP_LSAPI_MAX_REQUESTS=500 PHP_LSAPI_CHILDREN=35 /path/to/lsphp -b IP_address:port

Hoy en día, LiteSpeed PHP puede ser utilizado con LiteSpeed Web Server, OpenLiteSpeed Web Server y Apache mod_lsapi. Para los pasos de configuración del lado del servidor, visite las páginas de documentación para [LiteSpeed Web Server](https://docs.litespeedtech.com/extapp/php/getting_started/) y [OpenLiteSpeed](https://docs.openlitespeed.org/kb/category/php/).

LSPHP también puede ser instalado de varias otras maneras.

CentOS: En CentOS, LSPHP puede ser instalado desde el depósito LiteSpeed o el depósito Remi utilizando [RPM](https://docs.litespeedtech.com/extapp/php/getting_started/#litespeed-repo-search-packages).

Debian: En Debian, LSPHP puede ser instalado desde el depósito LiteSpeed utilizando [apt](https://docs.litespeedtech.com/extapp/php/getting_started/#litespeed-repo-search-packages).

cPanel: Ver la [página de documentación](https://docs.litespeedtech.com/cp/cpanel/quickstart/#easyapache-integration) respectiva sobre cómo instalar LSPHP con cPanel y LSWS/OLS utilizando EasyApache 4.

Plesk: Plesk puede ser utilizado con LSPHP en CentOS, CloudLinux, Debian y Ubuntu, para más detalles sobre esto, visite la [página de documentación](https://docs.litespeedtech.com/cp/plesk/) respectiva.
