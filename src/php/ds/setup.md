---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/ds.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 16640
---

## Instalación/Configuración

## Requisitos

PHP 7 es requerido por la extensión y el polyfill de compatibilidad.

## Instalación

La forma más sencilla de instalar la extensión es a través de [PECL](https://pecl.php.net/package/ds)

    pecl install ds

       

Asimismo, se puede construir directamente a partir de la fuente:

    # Dependencias que podrían ser necesarias instalar
    # sudo apt-get install git build-essential php7.0-dev

    git clone https://github.com/php-ds/extension "php-ds"
    cd php-ds

    # Compilar e instalar la extensión
    phpize
    ./configure
    make
    make install

    # Limpiar los ficheros de compilación
    make clean
    phpize --clean

       

> [!NOTE]
> Si se utiliza Composer, se recomienda encarecidamente incluir [php-ds/php-ds](https://packagist.org/packages/php-ds/php-ds) en el proyecto para que el código sea siempre funcional en un entorno donde la extensión no esté instalada. La extensión tendrá prioridad si está instalada.
