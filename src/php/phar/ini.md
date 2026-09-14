---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/phar.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_revision: 525aa5f19
order: 64900
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [phar.readonly](#ini.phar.readonly) | "1" | `INI_ALL` |  |
| [phar.require_hash](#ini.phar.require-hash) | "1" | `INI_ALL` |  |
| [phar.cache_list](#ini.phar.cache-list) | "" | `INI_SYSTEM` |  |

Opciones de Configuración de Flujos y Sistema de Ficheros

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`phar.readonly` `bool`  
Esta opción deshabilita la modificación o creación de archivos Phar usando el flujo `phar` o el soporte para escritura de objetos `Phar`. Este ajuste debería estar siempre activado en máquinas de producción, ya que el soporte para escritura conveniente de la extensión phar podría permitir la simple creación de un virus basado en PHP al asociarse con otras vulnerabilidades de seguridad comunes.

> [!NOTE]
> Este ajuste sólo puede ser desactivado en php.ini por motivos de seguridad. Si `phar.readonly` está deshabilitado en php.ini, un usuario puede habilitar `phar.readonly` en un script o deshabilitarlo después. Si `phar.readonly` está habilitado en php.ini, un scrip puede "re-habilitar" inofensivamente la variable INI, pero no puede deshabilitarla.

`phar.require_hash` `bool`  
Esta opción forzará a todos los archivos Phar abiertos a que contengan algún tipo de signatura (actualmente está soportadas MD5, SHA1, SHA256 y SHA512), y rehusará procesar cualquer archivo Phar que no contenga una signatura.

> [!NOTE]
> Este ajuste sólo puede ser desactivado en php.ini por motivos de seguridad. Si `phar.require_hash` está deshabilitado en php.ini, un usuario puede habilitar `phar.require_hash` en un script o deshabilitarlo después. Si `phar.require_hash` está habilitado en php.ini, un scrip puede "re-habilitar" inofensivamente la variable INI, pero no puede deshabilitarla.
>
> Este ajuste no afecta a la lectura de ficheros tar planos con la clase `PharData`.

> [!CAUTION]
> `phar.require_hash` no proporciona ninguna seguridad per se, es simplemente una medida contra la ejecución accidental de archivos Phar corruptos, porque cualquiera que pueda alterar el Phar podría corregir fácilmente la firma.

`phar.cache_list` `string`  
Permite mapear archivos phar para que sean preanalizados en el arranque del servidor web, proporcionando una mejora de rendimiento que saca ficheros en ejecución de un archivo phar casi tan rápido como si esos ficheros se ejecutaran desde una instalación tradicional basada en disco.

Ejemplo de uso de phar.cache_list

    en php.ini (windows):
    phar.cache_list =C:\ruta\a\phar1.phar;C:\ruta\a\phar2.phar
    en php.ini (unix):
    phar.cache_list =/ruta/a/phar1.phar:/ruta/a/phar2.phar
