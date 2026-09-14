---
title: CGI y configuraciones de línea de comandos
source_url: https://www.php.net/manual/es/install.unix.commandline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/unix/commandline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_revision: 40a850f73
order: 1800
---

## CGI y configuraciones de línea de comandos

Por defecto, PHP se construye como un programa CLI y CGI, que puede ser utilizado para el procesamiento de CGI. Si está ejecutando un servidor web PHP tiene soporte para los módulos, por lo general debe irse por esta solución por razones de rendimiento. Sin embargo, la versión CGI permite a los usuarios ejecutar diferentes páginas con PHP bajo diferentes identificadores de usuarios.

> [!WARNING]
> Un servidor desplegado en modo CGI se expone a varias vulnerabilidades posibles. Por favor, lea nuestra [sección sobre la seguridad en modo CGI](#security.cgi-bin) para aprender cómo protegerse contra estos ataques.

## Pruebas

Si has construido PHP como un programa CGI, puede probar su construcción escribiendo `make test`. Siempre es una buena idea probar su construcción. De esta manera usted puede encontrar un problema al principio con PHP en la plataforma, en lugar de tener que luchar con él más adelante.

## Utilización de variables

Algunos [servidores suministrando variables de entorno](#reserved.variables.server) no se definen en las actuales [especificación CGI/1.1](https://datatracker.ietf.org/doc/html/rfc3875). Sólo las siguientes variables no se definen: `AUTH_TYPE`, `CONTENT_LENGTH`, `CONTENT_TYPE`, `GATEWAY_INTERFACE`, `PATH_INFO`, `PATH_TRANSLATED`, `QUERY_STRING`, `REMOTE_ADDR`, `REMOTE_HOST`, `REMOTE_IDENT`, `REMOTE_USER`, `REQUEST_METHOD`, `SCRIPT_NAME`, `SERVER_NAME`, `SERVER_PORT`, `SERVER_PROTOCOL` y `SERVER_SOFTWARE`. Todo lo demás debe ser tratado como "extensiones de proveedor".
