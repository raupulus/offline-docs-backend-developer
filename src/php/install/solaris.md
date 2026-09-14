---
title: Instalación en Solaris
source_url: https://www.php.net/manual/es/install.unix.solaris.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/unix/solaris.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: true
translation_revision: 4eeb07225
order: 1880
---

## Instalación en Solaris

Esta sección contiene las notas y consejos de instalación de PHP en las distribuciones Solaris.

## Software necesario

La instalación Solaris generalmente omite los compiladores C y sus utilidades. Lea [esta FAQ](#faq.installation.needgnu) para saber por qué las versiones GNU de algunas de estas herramientas son necesarias.

Para descomprimir la distribución PHP, se necesita

- tar

- gzip o

- bzip2

Para compilar PHP, se necesita

- gcc (recomendado, otros compiladores C también pueden funcionar)

- make

- GNU sed

Para construir las extensiones adicionales o modificar el código de PHP, también se puede necesitar

- re2c

- bison

- m4

- autoconf

- automake

Además, también se deberán instalar (y tal vez compilar) todas las bibliotecas necesarias para las extensiones como MySQL, Oracle, etc.

## Uso de paquetes

La instalación Solaris puede simplificarse utilizando pkgadd para instalar la mayoría de los componentes. El sistema de paquetes de imágenes (IPS) para Solaris 11 Express también contiene los componentes necesarios para la instalación utilizando el comando pkg.
