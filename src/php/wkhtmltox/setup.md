---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/wkhtmltox.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wkhtmltox/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wkhtmltox
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 101870
---

## Instalación/Configuración

## Requisitos

La fuente de libwkhtmltox y las liberaciones binarias se distribuyen en [wkhtmltopdf.org](http://wkhtmltopdf.org).

> [!CAUTION]
> Los usuarios de Windows necesitan dar el paso adicional de añadir `wkhtmltox.dll` a su `PATH`.

## Instalación

El código fuente de esta extensión, y los binarios para Windows están alojados en [github](https://github.com/krakjoe/wkhtmltox),

Buscando el código fuente y construyendo la extensión:

       
    git clone https://github.com/krakjoe/wkhtmltox
    cd wkhtmltox
    phpize
    ./configure --with-wkhtmltox=/path/to/wkhtmltox/installation
    make
    sudo make install
       
       

Buscando actualizaciones y reconstruyendo la extensión:

       
    cd wkhtmltox
    phpize --clean
    git pull origin master
    phpize
    ./configure --with-wkhtmltox=/path/to/wkhtmltox/installation
    make
    sudo make install
