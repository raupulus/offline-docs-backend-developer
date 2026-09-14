---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/fann.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fann/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fann
translation_status: ready
translation_reviewed: true
translation_revision: 765b2d6ee
order: 22310
---

## Instalación/Configuración

## Requisitos

PHP \>= 5.2.0 y libfann \>= 2.1.0

## Instalación

La extensión FANN PHP debería funcionar en todos los sistemas Linux.

### Instalación de la biblioteca FANN

Antes de comenzar la instalación, asegúrese de que *libfann* esté instalado en su sistema. Forma parte del repositorio principal en la mayoría de las distribuciones Linux (busque *fann*). Se necesita una versión de desarrollo.

Si no está instalado, debe instalarse primero. Descárguelo desde el [sitio oficial](http://leenissen.dk/fann/wp/) o obténgalo desde el repositorio de su distribución. Por ejemplo en Fedora:

    $ sudo yum install fann-devel

        

o en Ubuntu:

    $ sudo apt-get install libfann-dev

        

Si la biblioteca se reinstala manualmente, entonces todos los archivos antiguos de la biblioteca deben eliminarse antes de reinstalar, de lo contrario podría vincularse la versión antigua de la biblioteca.

### Instalación PECL

Esta extensión está disponible en PECL. La instalación es muy sencilla. Ejecute simplemente:

    $ sudo pecl install fann

        

### Manual de instalación

Para los desarrolladores y las personas interesadas en los últimos cambios, se puede compilar el controlador a partir del código fuente más reciente en [Github](https://github.com/bukka/php-fann). Vaya a Github y haga clic en el botón "Download ZIP". Luego ejecute:

    $ unzip php-fann-master.zip
    $ cd php-fann-master
    $ phpize
    $ ./configure
    $ make all
    $ sudo make install

        

Aplique los siguientes cambios a php.ini:

- Asegúrese de que la variable *extension_dir* apunte hacia el directorio que contiene *fann.so*. La construcción mostrará dónde instala el controlador PHP con una salida que se parece a:

      Installing '/usr/lib/php/extensions/no-debug-non-zts-20060613/fann.so'

            

  Asegúrese de que sea el mismo que el directorio de extensión PHP ejecutando:

      $ php -i | grep extension_dir
        extension_dir => /usr/lib/php/extensions/no-debug-non-zts-20060613 =>
                         /usr/lib/php/extensions/no-debug-non-zts-20060613

            

  Si no es así, cambie la variable *extension_dir* en php.ini o mueva *fann.so*.

- Para cargar la extensión al iniciar PHP, añada una línea:

      extension=fann.so

            

## Tipos de recursos
