---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/apcu.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_reviewed: false
translation_revision: 804d8a054
order: 5120
---

## Instalación/Configuración

## Instalación

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/apcu>.

> [!TIP]
> PHP 7 cuenta con un módulo separado ([apcu-bc](https://pecl.php.net/apcu_bc)) para garantizar la retrocompatibilidad con APC.
>
> En modo retrocompatibilidad, APCu registra las funciones APC aplicables con prototipos retrocompatibles.
>
> Cuando una función APC acepta el argumento `cache_type`, este último es ignorado por la versión retrocompatible de la función y omitido del prototipo de la versión APCu.

> [!WARNING]
> A partir de PHP 8.0.0, apcu-bc ya no es aceptado.

> [!NOTE]
> Con Windows, APCu requiere un directorio temporal en el que el servidor web esté autorizado a escribir. Se verifican sucesivamente las variables de entorno TMP, TEMP y USERPROFILE en este orden y se termina intentando el directorio WINDOWS si ninguna de estas variables ha sido definida.

> [!NOTE]
> Para obtener más detalles técnicos sobre la implementación, consúltese el [ archivo TECHNOTES proporcionado por los desarrolladores ](https://github.com/php/pecl-caching-apc/blob/master/TECHNOTES.txt).

Las fuentes de APCu están disponibles [aquí](https://github.com/krakjoe/apcu).
