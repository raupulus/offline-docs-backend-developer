---
title: Instalación
source_url: https://www.php.net/manual/es/image.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9ba738103
order: 31340
---

## Instalación

Para activar el soporte de GD, es necesario compilar PHP con la opción `--with-gd[=DIR]`, donde DIR es el directorio de instalación de GD. Se recomienda utilizar la versión de GD que se distribuye con PHP, utilizando simplemente la opción `--with-gd`. La biblioteca GD requiere libpng y libjpeg para compilar. A partir de PHP 7.4.0, `--with-gd` se convierte en `--enable-gd` (si es necesario activar la extensión completa) y `--with-external-gd` (para elegir utilizar una libgd externa, en lugar de la proporcionada).

En Windows, es necesario incluir la biblioteca `php_gd.dll` como extensión en el archivo `php.ini`. Anterior a PHP 8.0.0, la DLL se llamaba `php_gd2.dll`.

Se amplían las capacidades de GD para manejar otros formatos de imagen especificando las siguientes opciones de compilación `--with-XXXX`:

| Formato de imagen | Opción de compilación |
|----|----|
| `avif` | Para activar el soporte de la biblioteca avif, añadir la opción `--with-avif`. Disponible a partir de PHP 8.1.0. |
| `jpeg` | Para activar el soporte de la biblioteca JPEG, añadir la opción `--with-jpeg-dir=DIR`. Jpeg 6b, 7 u 8 son soportados. A partir de PHP 7.4.0, utilizar en su lugar `--with-jpeg` |
| `png` | Para activar el soporte de la biblioteca PNG, añadir la opción `--with-png-dir=DIR`. Tenga en cuenta que libpng requiere la biblioteca [zlib](#zlib.requirements) y, por lo tanto, será necesario añadir también `--with-zlib-dir[=DIR]` en su línea de compilación. A partir de PHP 7.4.0, `--with-png-dir` y `--with-zlib-dir` han sido eliminadas. libpng y zlib son necesarias. |
| `xpm` | Para activar el soporte de la biblioteca XPM, añadir la opción `--with-xpm-dir=DIR`. Si el script de compilación no es capaz de encontrar las bibliotecas necesarias, será necesario añadir la ruta hacia las bibliotecas X11. A partir de PHP 7.4.0, utilizar en su lugar `--with-xpm` |
| `webp` | Para activar el soporte de WebP, añadir `--with-vpx-dir=DIR`. A partir de PHP 7.4.0, utilizar en su lugar `--with-webp` |

Formatos de imagen soportados

> [!NOTE]
> Al compilar PHP con libpng, es necesario utilizar la misma versión que la vinculada a la biblioteca GD.

Se amplían las capacidades de GD para manejar diferentes tipos de fuentes de caracteres añadiendo las siguientes opciones `--with-XXXX` de compilación:

| Biblioteca | Opción de configuración |
|----|----|
| `FreeType 2` | Para activar el soporte de FreeType 2, añadir la opción `--with-freetype-dir=DIR`. A partir de PHP 7.4.0 utilizar `--with-freetype` en su lugar, que depende de pkg-config. |
| `cadenas TrueType` | Para activar el soporte de cadenas TrueType, añadir la opción `--enable-gd-native-ttf`. (Esta opción no tiene efecto y ha sido eliminada desde PHP 7.2.0.) |

Bibliotecas de fuentes soportadas
