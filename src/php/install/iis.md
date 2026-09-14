---
title: Instalación con IIS para Windows
source_url: https://www.php.net/manual/es/install.windows.iis.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/windows/iis.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: true
translation_revision: e8ac70bf5
order: 1930
---

## Instalación con IIS para Windows

## Instalar IIS

Los Servicios de Información de Internet (Internet Information Services - IIS) están integrados en Windows. En Windows Server, el rol IIS puede ser añadido a través del Administrador del Servidor. El módulo CGI debe ser incluido. En los escritorios Windows, IIS debe ser añadido a través del Panel de Control. La documentación de Microsoft proporciona [instrucciones detalladas para habilitar IIS](https://docs.microsoft.com/en-us/previous-versions/ms181052(v=vs.80)). Para el desarrollo, [IIS/Express](https://www.microsoft.com/en-us/download/details.aspx?id=48264) también puede ser utilizado.

> [!NOTE]
> La versión No-Thread Safe (NTS) de PHP debe ser instalada cuando se utiliza el gestor FastCGI con IIS.

## Configurar PHP con IIS

En el Administrador de IIS, instale el módulo FastCGI y añada una correspondencia de gestor para `.php` al camino de `php-cgi.exe` (no `php.exe`)

El comando `APPCMD` puede ser utilizado para crear scripts de configuración de IIS.

## Ejemplo de script batch

Línea de comandos para configurar IIS y PHP

    @echo off

    REM descargar el archivo .ZIP de la versión de PHP desde http://windows.php.net/downloads/

    REM ruta del directorio en el que el archivo .ZIP de PHP ha sido descomprimido (sin \ final)
    set phppath=c:\php

    REM Elimina los gestores PHP actuales
    %windir%\system32\inetsrv\appcmd clear config /section:system.webServer/fastCGI
    REM La siguiente comanda generará un mensaje de error si PHP no está instalado. Esto puede ser ignorado.
    %windir%\system32\inetsrv\appcmd set config /section:system.webServer/handlers /-[name='PHP_via_FastCGI']

    REM Configura el gestor PHP
    %windir%\system32\inetsrv\appcmd set config /section:system.webServer/fastCGI /+[fullPath='%phppath%\php-cgi.exe']
    %windir%\system32\inetsrv\appcmd set config /section:system.webServer/handlers /+[name='PHP_via_FastCGI',path='*.php',verb='*',modules='FastCgiModule',scriptProcessor='%phppath%\php-cgi.exe',resourceType='Unspecified']
    %windir%\system32\inetsrv\appcmd set config /section:system.webServer/handlers /accessPolicy:Read,Script

    REM Configura las variables FastCGI
    %windir%\system32\inetsrv\appcmd set config -section:system.webServer/fastCgi /[fullPath='%phppath%\php-cgi.exe'].instanceMaxRequests:10000
    %windir%\system32\inetsrv\appcmd.exe set config -section:system.webServer/fastCgi /+"[fullPath='%phppath%\php-cgi.exe'].environmentVariables.[name='PHP_FCGI_MAX_REQUESTS',value='10000']"
    %windir%\system32\inetsrv\appcmd.exe set config -section:system.webServer/fastCgi /+"[fullPath='%phppath%\php-cgi.exe'].environmentVariables.[name='PHPRC',value='%phppath%\php.ini']"
