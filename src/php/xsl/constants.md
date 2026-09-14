---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/xsl.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_revision: f9c4a68ef
order: 104070
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`XSL_CLONE_AUTO` (`int`)  

`XSL_CLONE_NEVER` (`int`)  

`XSL_CLONE_ALWAYS` (`int`)  

`LIBXSLT_VERSION` (`int`)  
versión libxslt como 10117.

`LIBXSLT_DOTTED_VERSION` (`string`)  
versión de libxslt como la 1.1.17.

`LIBEXSLT_VERSION` (`int`)  
versión de libexslt como la 813.

`LIBEXSLT_DOTTED_VERSION` (`string`)  
versión de libexslt como la 1.1.17.

`XSL_SECPREF_NONE` (`int`)  
Desactivar todas las restricciones de seguridad.

`XSL_SECPREF_READ_FILE` (`int`)  
Deshabilita la lectura de archivos.

`XSL_SECPREF_WRITE_FILE` (`int`)  
Deshabilita la escritura de archivos.

`XSL_SECPREF_CREATE_DIRECTORY` (`int`)  
No permite crear directorios.

`XSL_SECPREF_READ_NETWORK` (`int`)  
No permite leer los archivos de la red.

`XSL_SECPREF_WRITE_NETWORK` (`int`)  
Deshabilita la escritura de archivos de red.

`XSL_SECPREF_DEFAULT` (`int`)  
Deshabilita todo acceso de escritura, es decir, una máscara de bits de `XSL_SECPREF_WRITE_NETWORK` \| `XSL_SECPREF_CREATE_DIRECTORY` \| `XSL_SECPREF_WRITE_FILE`.
