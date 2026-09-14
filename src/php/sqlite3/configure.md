---
title: Instalación
source_url: https://www.php.net/manual/es/sqlite3.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 184f3f7bd
order: 85570
---

## Instalación

El soporte de SQLite3 se activa por omisión. Es posible desactivarlo mediante la opción `--without-sqlite3` durante la compilación.

Los usuarios de Windows deben activar la biblioteca `php_sqlite3.dll` para utilizar esta extensión. Esta DLL se incluye con las distribuciones de PHP para Windows.

> [!NOTE]
> Para hacer funcionar esta extensión, algunas bibliotecas DLL deben estar disponibles a través del `PATH` del sistema Windows. Lea la F.A.Q titulada "[Cómo agregar mi carpeta PHP a mi PATH de Windows](#faq.installation.addtopath)" para más información. Copiar las bibliotecas DLL desde la carpeta PHP a la carpeta del sistema de Windows también funciona (ya que la carpeta del sistema está por defecto en el `PATH` del sistema), pero este método no es recomendado. *Esta extensión requiere que los siguientes ficheros estén en el `PATH`:* `libsqlite3.dll`.
