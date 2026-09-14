---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/intl.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 911fe79de
order: 39960
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [intl.default_locale](#ini.intl.default-locale) |  | `INI_ALL` |  |
| [intl.error_level](#ini.intl.error-level) | 0 | `INI_ALL` |  |
| [intl.use_exceptions](#ini.intl.use-exceptions) | 0 | `INI_ALL` | Disponible a partir de PECL 3.0.0a1 |

Opciones de configuración de internacionalización

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`intl.default_locale` `string`  
La configuración local a utilizar con las funciones intl cuando ninguna está especificada (ya sea si se omite en el argumento correspondiente, o si el valor pasado es `null`). Estas son configuraciones locales ICU, y no configuraciones locales del sistema. Las configuraciones locales ICU internas así como sus datos pueden ser exploradas aquí <https://unicode-org.github.io/icu/userguide/locale/>.

Por omisión, está vacía, lo que fuerza el uso de la configuración local ICU por omisión. Una vez definida, la configuración ini no puede ser reestablecida a este valor por omisión. No se recomienda utilizar este valor por omisión, sabiendo que depende del entorno del servidor.

`intl.error_level` `int`  
El tipo de mensajes de error generados cuando ocurre un error en las funciones ICU. Es un [nivel de error PHP](#errorfunc.constants), como `E_WARNING`. Puede valer `0` para inhibir los mensajes. Esto no afecta los valores devueltos que indican un error o los valores devueltos por la función `intl_get_error_code` o por los métodos de clase específicos que permiten recuperar los códigos y mensajes de error.

El valor por omisión es `0`.

`intl.use_exceptions` `int`  
Si vale `true`, se emitirá una excepción cuando ocurra un error en una función intl. La excepción será de tipo `IntlException`. La excepción se emitirá además del mensaje de error generado debido a la definición de la opción de configuración [intl.error_level](#ini.intl.error-level).

Por omisión, vale `false`.
