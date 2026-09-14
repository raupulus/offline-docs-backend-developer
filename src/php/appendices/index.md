---
title: Opciones de configuración
source_url: https://www.php.net/manual/es/configure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/configure/index.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 2bb07c8c4
order: 40
---

## Opciones de configuración

## Listado de opciones de configuración del núcleo

A continuación se muestra una lista parcial de las opciones de configuración utilizadas por el script `configure` de PHP al compilar en entornos de tipo Unix. La mayoría de las opciones de configuración se enumeran en su ubicación correspondiente de las páginas de referencia de cada extensión, no aquí. Para obtener una lista completa y actualizada de las opciones de configuración, se debe ejecutar `./configure --help` en el directorio de código fuente de PHP después de haber ejecutado `autoconf` (véase también el capítulo de [Instalación](#install)). También puede ser de interés consultar la documentación de [GNU configure](http://www.airs.com/ian/configure/) para obtener información sobre otras opciones de `configure` como `--prefix=PREFIX`.

> [!NOTE]
> Estas opciones se utilizan únicamente durante la compilación. Si se desea modificar la configuración en tiempo de ejecución de PHP, consúltese el capítulo sobre [Configuración en tiempo de ejecución](#configuration).

- [Otras opciones](#configure.options.misc)

- [Comportamiento de PHP](#configure.options.php)

- [Servidor](#configure.options.servers)

## Opciones de configuración en PHP
