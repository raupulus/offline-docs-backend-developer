---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/imagick.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 9a1574126
order: 37890
---

## Instalación/Configuración

## Requisitos

### Configuración necesaria para la instalación en plataformas distintas de Windows

Se requiere ImageMagick \>= 6.2.4. El número de formatos soportados por Imagick depende totalmente de los soportados por la instalación de ImageMagick. Por ejemplo, Imagemagick necesita ghostscript para realizar las operaciones relativas a los PDF.

## Instalación

Esta extensión [PECL](https://pecl.php.net/) no está integrada en PHP.

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/imagick>.

> [!NOTE]
> El nombre oficial de esta extensión es *imagick*.

Los usuarios de Windows pueden descargar una DLL preconstruida desde el sitio de PECL : [PECL](https://pecl.php.net/package/imagick). Estos paquetes contienen ya la DLL de extensión (`php_imagick.dll`) que debe ser colocada en el [extension_dir](#ini.extension-dir). Contienen también las DLL de ImageMagick, que deben ser colocadas en algún lugar del `PATH`. A partir de Imagick 3.6.0, contienen también archivos de configuración XML en `config`; para usarlos en lugar de los valores por omisión integrados, deben ser colocados en `%USERPROFILE%/.config/ImageMagick`, o alternativamente en el camino dado por la variable de entorno `MAGICK_CONFIGURE_PATH`. Consúltense la [Documentación sobre los archivos de configuración de ImageMagick](http://www.imagemagick.org/script/resources.php) para más detalles.
