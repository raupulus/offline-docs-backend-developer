---
title: Instalación
source_url: https://www.php.net/manual/es/yaz.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_reviewed: false
translation_revision: ba08db880
order: 107720
---

## Instalación

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/yaz>

No hay biblioteca DLL para esta extensión PECL actualmente disponible. Consulte la sección [Compilación en Windows](#install.windows.building) .

> [!NOTE]
> `php_yaz.dll` depende de `yaz.dll`. El `yaz.dll` es parte del ZIP Win32 del sitio de PHP. También es parte de la instalación de Windows YAZ disponible del área [WIN32 YAZ](http://ftp.indexdata.dk/pub/yaz/win32/).
>
> En Windows, no se debe olvidar agregar al `PATH` el directorio de PHP, para que el sistema pueda encontrar el fichero `yaz.dll`.

> [!WARNING]
> Las extensiones [IMAP](#book.imap), [recode](#book.recode) y [YAZ](#book.yaz) no pueden ser utilizadas simultáneamente ya que utilizan un símbolo interno común. Nota: Yaz 2.0 y superior ya no sufre de este problema.
