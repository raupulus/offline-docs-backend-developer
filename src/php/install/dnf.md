---
title: Instalación a partir de paquetes en distribuciones GNU/Linux que utilizan DNF
source_url: https://www.php.net/manual/es/install.unix.dnf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/unix/dnf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: true
translation_revision: ee1ce6a0e
order: 1820
---

## Instalación a partir de paquetes en distribuciones GNU/Linux que utilizan DNF

Aunque PHP puede ser instalado desde el código fuente, también está disponible a través de paquetes en sistemas que usan DNF, como Red Hat Enterprise Linux OpenSUSE, Fedora, CentOS, Rocky Linux y Oracle Enterprise Linux.

> [!WARNING]
> Las versiones provenientes de terceros son consideradas no oficiales y no son directamente soportadas por el proyecto PHP. Cualquier bug encontrado debe ser reportado al proveedor de estas versiones no oficiales, a menos que pueda ser reproducido utilizando las versiones provenientes de [ la zona de descargas oficial](https://www.php.net/downloads.php).

Los paquetes pueden instalarse mediante el comando `dnf`.

## Instalación de paquetes

Para empezar, es importante señalar que se pueden desear otros paquetes vinculados, como `php-pear` para [PEAR](https://pear.php.net/), o `php-mysqlnd` para la extensión [ MySQL](#book.mysqlnd).

Entonces, antes de instalar un paquete, conviene asegurarse de que la lista de paquetes está actualizada. Normalmente, esto se hace ejecutando el comando `dnf update`.

Ejemplo de instalación DNF

```php
## dnf install php php-common

   
```

DNF instalará automáticamente la configuración de PHP para el servidor web, pero puede ser necesario reiniciarlo para que los cambios surtan efecto. Por ejemplo :

Reiniciar Apache una vez instalado PHP

```php
## sudo systemctl restart httpd

   
```

## Mejor control de la configuración

En la última sección, PHP ha sido instalado sólo con los módulos básicos. Es muy probable que se requieran módulos adicionales, tales como [MySQL](#book.mysql), [cURL](#book.curl), [GD](#book.image), etc. También se pueden instalar mediante la función `dnf`.

Métodos para listar paquetes PHP adicionales

```php
## dnf search php

   
```

La lista de paquetes incluirá un gran número de paquetes incluyendo componentes básicos de PHP, como `php-cli`, `php-fpm` y `php-devel`, así como numerosas extensiones de PHP. Cuando se instalan extensiones, los paquetes adicionales se instalarán automáticamente si es necesario para satisfacer las dependencias de estos paquetes.

Instalación de PHP con MySQL, GD

```php
## dnf install php-mysqlnd php-gd

   
```

DNF añadirá automáticamente las líneas apropiadas a los distintos archivos vinculados a `php.ini`, como `/etc/php/8.3/php.ini`, `/etc/php/8.3/conf.d/*.ini`, etc. y dependiendo de la extensión añadirá entradas similares a `extension=foo.so`. Sin embargo, es necesario reiniciar el servidor web (como Apache) para que estos cambios surtan efecto.
