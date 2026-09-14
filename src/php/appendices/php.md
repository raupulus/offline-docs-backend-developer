---
title: Opciones de PHP
source_url: https://www.php.net/manual/es/configure.options.php.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/configure/php.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 91da56315
order: 60
---

### Opciones de PHP

`--enable-maintainer-mode`  
Habilita las reglas y dependencias de make que no son útiles (y en ocasiones confusas) para el instalador ocasional.

`--with-config-file-path=PATH`  
Establece la ruta en la que se buscará `php.ini`, el valor predeterminado es `PREFIX/lib`.

`--disable-short-tags`  
Deshabilita por defecto el formato corto de la etiqueta de inicio \<?.

`--with-libdir`  
Especifica el directorio donde se encuentran las bibliotecas para compilar PHP en un sistema Unix. Para sistemas de 64 bits, se requiere especificar este argumento con el directorio `lib64`, como por ejemplo: `--with-libdir=lib64`.

`--enable-zts`  
Habilita la seguridad de hilos. Antes de PHP 8.0.0 en sistemas no Windows, la opción se llamaba `--enable-maintainer-zts`.
