---
title: Instalación
source_url: https://www.php.net/manual/es/ref.pdo-sqlite.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_sqlite/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_sqlite
translation_status: ready
translation_revision: '859713422'
order: 62700
---

## Instalación

El controlador PDO_SQLITE PDO está habilitado por omisión. Para deshabilitarlo, se puede usar `--without-pdo-sqlite[=DIR]`, donde el parámetro opcional `[=DIR]` es el directorio base de instalación de sqlite. A partir de PHP 7.4.0 se requiere [libsqlite](http://sqlite.org/) ≥ 3.5.0. Anteriormente, si libsqlite incluido podría haberse usado en su lugar, por omisión, si `[=DIR]` era omitido.

> [!NOTE]
> Para hacer funcionar esta extensión, algunas bibliotecas DLL deben estar disponibles a través del `PATH` del sistema Windows. Lea la F.A.Q titulada "[Cómo agregar mi carpeta PHP a mi PATH de Windows](#faq.installation.addtopath)" para más información. Copiar las bibliotecas DLL desde la carpeta PHP a la carpeta del sistema de Windows también funciona (ya que la carpeta del sistema está por defecto en el `PATH` del sistema), pero este método no es recomendado. *Esta extensión requiere que los siguientes ficheros estén en el `PATH`:* `libsqlite3.dll`.
