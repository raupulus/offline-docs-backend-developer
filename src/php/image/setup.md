---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/image.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9ba738103
order: 32570
---

## Instalación/Configuración

## Requisitos

Si se dispone de la biblioteca GD (disponible en <http://www.libgd.org/>) también se podrán crear y manipular imágenes.

Los formatos de imágenes que se podrán manipular dependen de la versión de GD que se instale, y de todas las demás bibliotecas que GD necesita para tratar estas imágenes.

> [!NOTE]
> Se requiere libgd-2.1.0 o superior. Alternativamente, utilice la biblioteca GD proporcionada con PHP.

> [!NOTE]
> La biblioteca GD requiere zlib \>= 1.2.0.4.

También se puede mejorar GD añadiendo formatos de imágenes adicionales.

| Formato de imagen | Biblioteca a descargar | Notas |
|----|----|----|
| `gif` |  |  |
| `avif` |  |  |
| `jpeg` | <http://www.ijg.org/> | Al compilar la biblioteca jpeg (antes de la de PHP), debe utilizarse la opción de configuración `--enable-shared`. De lo contrario, se recibirá un error indicando que `libjpeg.(a|so) not found` al intentar configurar PHP antes de compilarlo. |
| `png` | <http://www.libpng.org/pub/png/libpng.html> |  |
| `xpm` | <http://www.ibiblio.org/pub/Linux/libs/X/!INDEX.html> | Es probable que ya disponga de esta biblioteca si su sistema tiene un entorno X. |
| `webp` |  |  |

Formatos de imágenes soportados

Puede querer extender GD para hacerla funcionar con diferentes tipos de fuentes. La biblioteca [FreeType 2](http://www.freetype.org/) es soportada.

## Tipos de recursos

Esta extensión define los siguientes tipos de recursos :

| Nombre | Descripción | Notas |
|----|----|----|
| `gd` | Recurso de imagen, utilizado por funciones como `imagecreatefrompng` | Anterior a PHP 8.0.0 |
| `gd font` | Recurso de fuente creado internamente por `imageloadfont` | Anterior a PHP 8.1.0 |

Lista de recursos en GD
