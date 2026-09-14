---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/soap.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_revision: d4d5216e7
order: 75080
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [soap.wsdl_cache_enabled](#ini.soap.wsdl-cache-enabled) | 1 | `INI_ALL` |  |
| [soap.wsdl_cache_dir](#ini.soap.wsdl-cache-dir) | /tmp | `INI_ALL` |  |
| [soap.wsdl_cache_ttl](#ini.soap.wsdl-cache-ttl) | 86400 | `INI_ALL` |  |
| [soap.wsdl_cache](#ini.soap.wsdl-cache) | 1 | `INI_ALL` |  |
| [soap.wsdl_cache_limit](#ini.soap.wsdl-cache-limit) | 5 | `INI_ALL` |  |

Opciones de configuración de SOAP

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`soap.wsdl_cache_enabled` `integer`  
Activa o desactiva la función de almacenamiento en caché de WSDL.

`soap.wsdl_cache_dir` `string`  
Define el nombre del directorio donde la extensión SOAP guardará los ficheros en caché.

`soap.wsdl_cache_ttl` `integer`  
Define el número de segundos (tiempo de vida) por los que los ficheros en caché serán usados en lugar de los originales.

`soap.wsdl_cache` `integer`  
Si la opción `soap.wsdl_cache_enabled` está activada, este ajuste determina el tipo de almacenamiento en caché. Puede ser cualquiera de estos tipos: `WSDL_CACHE_NONE` (`0`), `WSDL_CACHE_DISK` (`1`), `WSDL_CACHE_MEMORY` (`2`) o `WSDL_CACHE_BOTH` (`3`). También puede definirse usando el array `options` del constructor de `SoapClient` o de `SoapServer`.

`soap.wsdl_cache_limit` `integer`  
Número máximo de ficheros WSDL almacenados en caché de memoria. Si se añaden más ficheros a una caché de memoria llena, se eliminarán los ficheros más antiguos de la misma.
