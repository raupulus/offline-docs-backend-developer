---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/svn.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 89870
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`SVN_REVISION_HEAD` (`int`)  
Número mágico (-1) especificando la revisión HEAD

<!-- -->

`SVN_AUTH_PARAM_DEFAULT_USERNAME` (`string`)  
Proiedad para el nombre de usuario por omisión a ser usada cuando realice una autenticación básica

`SVN_AUTH_PARAM_DEFAULT_PASSWORD` (`string`)  
Propiedad para la clave por omisión a ser usada cuando realice una autenticación básica

`SVN_AUTH_PARAM_NON_INTERACTIVE` (`string`)  

`SVN_AUTH_PARAM_DONT_STORE_PASSWORDS` (`string`)  

`SVN_AUTH_PARAM_NO_AUTH_CACHE` (`string`)  

`SVN_AUTH_PARAM_SSL_SERVER_FAILURES` (`string`)  

`SVN_AUTH_PARAM_SSL_SERVER_CERT_INFO` (`string`)  

`SVN_AUTH_PARAM_CONFIG` (`string`)  

`SVN_AUTH_PARAM_SERVER_GROUP` (`string`)  

`SVN_AUTH_PARAM_CONFIG_DIR` (`string`)  

`PHP_SVN_AUTH_PARAM_IGNORE_SSL_VERIFY_ERRORS` (`string`)  
Propiedad personalizada para ignorar los errores de verificación del certificado SSL

<!-- -->

`SVN_FS_CONFIG_FS_TYPE` (`string`)  
Llave de configuración que determina el tipo de sistema de archivos

`SVN_FS_TYPE_BDB` (`string`)  
Sistema de archivos es una implemetación Berkeley-DB

`SVN_FS_TYPE_FSFS` (`string`)  
Implementación del sistema de ficheros nativo

<!-- -->

`SVN_PROP_REVISION_DATE` (`string`)  
svn:date

`SVN_PROP_REVISION_ORIG_DATE` (`string`)  
svn:original-date

`SVN_PROP_REVISION_AUTHOR` (`string`)  
svn:author

`SVN_PROP_REVISION_LOG` (`string`)  
svn:log

<!-- -->

`SVN_WC_STATUS_NONE` (`int`)  
Estado no existe

`SVN_WC_STATUS_UNVERSIONED` (`int`)  
El artículo no está versionado en la copia de trabajo

`SVN_WC_STATUS_NORMAL` (`int`)  
El artículo existe, nada más está ocurriendo

`SVN_WC_STATUS_ADDED` (`int`)  
El artículo está programado para su adición

`SVN_WC_STATUS_MISSING` (`int`)  
El artículo está versionado pero la copia de trabajo está ausante

`SVN_WC_STATUS_DELETED` (`int`)  
El artículo está programado para ser borrado

`SVN_WC_STATUS_REPLACED` (`int`)  
El artículo fue borrado y luego re-agregado

`SVN_WC_STATUS_MODIFIED` (`int`)  
El artículo (texto o propiedades) fue modificado

`SVN_WC_STATUS_MERGED` (`int`)  
Las modificaciones locales del artículo fueron unidas con las modificaciones del repositorio

`SVN_WC_STATUS_CONFLICTED` (`int`)  
Las modificaciones locales del artículo discreparon con las modificaciones de repositorio

`SVN_WC_STATUS_IGNORED` (`int`)  
El artículo está desversionado pero configurado para ser ignorado

`SVN_WC_STATUS_OBSTRUCTED` (`int`)  
Artículo desversionado está en el camino de un recurso versionado

`SVN_WC_STATUS_EXTERNAL` (`int`)  
Rura desversionada que está poblada usando svn:externals

`SVN_WC_STATUS_INCOMPLETE` (`int`)  
El directorio no contiene la lista completa de entradas

<!-- -->

`SVN_NODE_NONE` (`int`)  
Ausente

`SVN_NODE_FILE` (`int`)  
Archivo

`SVN_NODE_DIR` (`int`)  
Directorio

`SVN_NODE_UNKNOWN` (`int`)  
Algo que la subversión no puede identificar
