---
title: Instalación desde paquetes o puertos en OpenBSD
source_url: https://www.php.net/manual/es/install.unix.openbsd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/unix/openbsd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: true
translation_revision: e8ac70bf5
order: 1870
---

## Instalación desde paquetes o puertos en OpenBSD

Esta sección contiene las notas específicas para la instalación de PHP en [OpenBSD](http://www.openbsd.org/).

## Uso de paquetes binarios

Este método es el método recomendado para instalar PHP en OpenBSD. También es el método más simple. El paquete core ha sido separado de los módulos y cada uno de ellos puede ser instalado y eliminado independientemente de los otros. Los ficheros necesarios están en el CD de OpenBSD o en el sitio FTP.

El paquete principal que debe ser instalado es `php`, que contiene el motor base (además de fpm, gettext e iconv) y podría estar disponible en varias versiones. Luego, eche un vistazo a los paquetes de módulos, como `php-mysqli` o `php-imap`. Debe utilizar el comando `phpxs` para activar y desactivar estos módulos en su `php.ini`.

Ejemplo de instalación de PHP en OpenBSD con Ports

```php
## pkg_add php
## pkg_add php-apache
## pkg_add php-mysqli
  (instalar las bibliotecas PEAR)
## pkg_add pear

Siga las instrucciones mostradas con cada paquete!

  (para eliminar paquetes)
## pkg_delete php
## pkg_delete php-apache
## pkg_delete php-mysqli
## pkg_delete pear

    
```

Lea la página de manual Unix [packages(7)](http://www.openbsd.org/cgi-bin/man.cgi?query=packages) para más detalles sobre los paquetes binarios de OpenBSD.

## Uso de puertos

También es posible compilar PHP utilizando [el árbol de puertos](http://www.openbsd.org/faq/ports/ports.html). Este método es recomendado para usuarios experimentados de OpenBSD. El puerto PHP está dividido en core y extensiones. El directorio extensiones genera los subpaquetes de todos los módulos PHP. Si no desea crear estos módulos, puede utilizar el comando en línea `no_*` FLAVOR. Por ejemplo, para no compilar el módulo imap, utilice FLAVOR con el valor `no_imap`.

## Problemas comunes

- Apache y Nginx ya no son el servidor por defecto en OpenBSD, pero pueden ser fácilmente encontrados en los puertos y los paquetes. El nuevo servidor por defecto también se llama 'httpd'.

- La instalación por defecto de Apache funciona en un [contexto chroot(2)](http://www.openbsd.org/cgi-bin/man.cgi?query=chroot), que limitará el acceso de los scripts PHP al directorio `/var/www`. Por lo tanto, debe crear un directorio `/var/www/tmp` para que las sesiones PHP sean almacenadas, o utilizar otra solución de almacenamiento. Además, los sockets de bases de datos deben ser colocados en este directorio, o utilizar la interfaz `localhost`. Si utiliza funciones de red con ficheros como `/etc`, por ejemplo `/etc/resolv.conf`, y `/etc/services`, deberá hacerlos accesibles también en `/var/www/etc`. El paquete OpenBSD PEAR instala automáticamente los directorios correctos.

- El paquete OpenBSD para la extensión [gd](http://www.libgd.org/) requiere Xorg. A menos que ya esté incluido después de la instalación añadiendo el conjunto de ficheros `xbase.tgz`, esto puede ser añadido posteriormente (ver [OpenBSD FAQ#4](https://www.openbsd.org/faq/faq4.html#FilesNeeded)).
