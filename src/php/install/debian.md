---
title: Instalación desde paquetes en Debian GNU/Linux y distribuciones similares
source_url: https://www.php.net/manual/es/install.unix.debian.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/unix/debian.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 1810
---

## Instalación desde paquetes en Debian GNU/Linux y distribuciones similares

Aunque PHP puede ser instalado desde el código fuente, también está disponible a través de paquetes provenientes de [Debian GNU/Linux](http://www.debian.org/). Esto también es cierto para otras distribuciones basadas en Debian, tales como Ubuntu, Kali Linux y Linux Mint.

> [!WARNING]
> Las versiones provenientes de terceros son consideradas no oficiales y no son directamente soportadas por el proyecto PHP. Cualquier bug encontrado debe ser reportado al proveedor de estas versiones no oficiales, a menos que pueda ser reproducido utilizando las versiones provenientes de [ la zona de descargas oficial](https://www.php.net/downloads.php).

Los paquetes pueden ser instalados utilizando la comando `apt` o la comando `aptitude`. Esta página de manual utiliza estos dos comandos de manera intercambiable.

## Uso de APT

En primer lugar, tenga en cuenta que otros paquetes pueden ser deseables, como `libapache-mod-php` para la integración con Apache 2, y `php-pear` para PEAR.

Luego, antes de instalar un paquete, es prudente asegurarse de que la lista de paquetes esté actualizada. Generalmente, esto se hace utilizando el comando `apt update`.

Ejemplo de instalación en Debian con Apache 2

```php
## apt install php-common libapache2-mod-php php-cli

   
```

APT instalará y activará automáticamente el módulo PHP para Apache 2, así como todas sus dependencias. Apache deberá ser reiniciado para que los cambios sean efectivos. Por ejemplo:

Detener y reiniciar Apache una vez instalado PHP

```php
## /etc/init.d/apache2 stop
## /etc/init.d/apache2 start

   
```

## Un mejor control de la configuración

En el ejemplo anterior, PHP fue instalado con solo los componentes principales. Es probable que se necesiten módulos adicionales, tales como [MySQL](#book.mysql), [cURL](#book.curl), [GD](#book.image), etc. También pueden ser instalados a través del comando `apt`.

Métodos para listar los paquetes PHP adicionales

```php
## apt-cache search php
## apt search php | grep -i mysql
## aptitude search php

   
```

La lista de paquetes incluirá un gran número de paquetes que incluyen los componentes básicos de PHP, tales como `php-cgi`, `php-cli`, y `php-dev`, así como numerosas extensiones PHP. Durante la instalación de las extensiones, se instalarán automáticamente paquetes adicionales si es necesario para satisfacer las dependencias de estos paquetes.

Instalar PHP con MySQL y cURL

```php
## apt install php-mysql php-curl

   
```

APT agregará automáticamente las líneas correctas a los ficheros relacionados con `php.ini`, como `/etc/php/7.4/php.ini`, `/etc/php/7.4/conf.d/*.ini`, etc., y según la extensión, agregará entradas similares a `extension=foo.so`. Además, reiniciar el servidor web (Apache, por ejemplo) es necesario para que estos cambios sean efectivos.

## Problemas comunes

- Si los scripts PHP no son interpretados por el servidor web, es probable que PHP no haya sido añadido a los ficheros de configuración del servidor web, es decir, en Debian, `/etc/apache2/apache2.conf` o equivalente. Consulte el manual de Debian para más detalles.

- Si una extensión ha sido aparentemente instalada pero sus funciones no están definidas, asegúrese de que las líneas adecuadas han sido insertadas en los ficheros .ini y/o que el servidor web ha sido reiniciado después de la instalación.
