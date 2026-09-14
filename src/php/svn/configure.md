---
title: Instalación
source_url: https://www.php.net/manual/es/svn.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_revision: 997700a58
order: 89860
---

## Instalación

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/svn>

Si `./configure` está teniendo problemas para encontrar los archivos SVN (Por ejemplo, Subversion fue instalado con un prefijo de directorio diferente), use `./configure --with-svn=$USR_PATH` para especificar el directorio donde `include/subversion-1/` está ubicado.

No hay biblioteca DLL para esta extensión PECL actualmente disponible. Consulte la sección [Compilación en Windows](#install.windows.building) .

> [!WARNING]
> Si la extensión es compilada contra libsvn 1.3, las funciones que trabajan con copias fallarán cuando trabaje en copias creadas por Subversion 1.4.
