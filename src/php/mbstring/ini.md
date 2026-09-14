---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/mbstring.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: d4d5216e7
order: 45620
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [mbstring.language](#ini.mbstring.language) | "neutral" | `INI_ALL` |  |
| [mbstring.detect_order](#ini.mbstring.detect-order) | NULL | `INI_ALL` |  |
| [mbstring.http_input](#ini.mbstring.http-input) | "pass" | `INI_ALL` | Obsoleta |
| [mbstring.http_output](#ini.mbstring.http-output) | "pass" | `INI_ALL` | Obsoleta |
| [mbstring.internal_encoding](#ini.mbstring.internal-encoding) | NULL | `INI_ALL` | Obsoleta |
| [mbstring.substitute_character](#ini.mbstring.substitute-character) | NULL | `INI_ALL` |  |
| [mbstring.func_overload](#ini.mbstring.func-overload) | "0" | `INI_SYSTEM` | Obsoleta desde PHP 7.2.0; eliminada desde PHP 8.0.0. |
| [mbstring.encoding_translation](#ini.mbstring.encoding-translation) | "0" | `INI_PERDIR` |  |
| [mbstring.http_output_conv_mimetypes](#ini.mbstring.http-output-conv-mimetypes) | "^(text/\|application/xhtml\\xml)" | `INI_ALL` |  |
| [mbstring.strict_detection](#ini.mbstring.strict-detection) | "0" | `INI_ALL` |  |
| [mbstring.regex_retry_limit](#ini.mbstring.regex-retry-limit) | "1000000" | `INI_ALL` | Disponible a partir de PHP 7.4.0. |
| [mbstring.regex_stack_limit](#ini.mbstring.regex-stack-limit) | "100000" | `INI_ALL` | Disponible a partir de PHP 7.3.5. |

Opciones de configuración de mbstring

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`mbstring.language` `string`  
El ajuste de lenguaje nacional predeterminado (NLS) usado en mbstring. Se ha de observar que esta opción define automágicamente `mbstring.internal_encoding`, por lo que se debe colocar `mbstring.internal_encoding` tras `mbstring.language` en `php.ini`

`mbstring.encoding_translation` `bool`  
Habilita el filtro de codificación de caracteres transparente para las consultas HTTP entrantes, la cual lleva a cabo la detección y la conversión de la codificación de entrada a la codificación de caracteres interna.

`mbstring.internal_encoding` `string`  
> [!WARNING]
> Esta funcionalidad obsoleta *será* ciertamente *eliminada* en el futuro.

Define la codificación de caracteres interna.

Los usuarios deberían dejarla vacía y establecer [`default_charset`](#ini.default-charset) en su lugar.

`mbstring.http_input` `string`  
> [!WARNING]
> Esta funcionalidad obsoleta *será* ciertamente *eliminada* en el futuro.

Define la codificación de caracteres predeterminada de entrada de HTTP.

Los usuarios deberían dejarla vacía y establecer [`default_charset`](#ini.default-charset) en su lugar.

`mbstring.http_output` `string`  
> [!WARNING]
> Esta funcionalidad obsoleta *será* ciertamente *eliminada* en el futuro.

Define la codificación de caracteres predeterminada de salida de HTTP (la salida será convertida de la codificación interna a la codificación de salida de HTTP).

Los usuarios deberían dejarla vacía y establecer [`default_charset`](#ini.default-charset) en su lugar.

`mbstring.detect_order` `string`  
Define el orden de detección de códigos de caracteres predeterminado. Véase también `mb_detect_order`.

`mbstring.substitute_character` `string`  
Define el caracter de sustitución para juegos de caracteres inválidos. Véase también `mb_substitute_character` para valores compatibles.

`mbstring.func_overload` `string`  
> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.2.0, y *ELIMINADA* a partir de PHP 8.0.0. Depender de esta funcionalidad está altamente desaconsejado.

Reemplaza determinadas funciones de único byte por sus equivalentes en mbstring. Véase la sección [Sobrecarga de funciones](#mbstring.overload) para más información.

Este ajuste sólo puede ser cambiado en el fichero `php.ini`

`mbstring.http_output_conv_mimetypes` `string`  

`mbstring.strict_detection` `bool`  
Habilita la detección estricta de codificaciones. Consulte `mb_detect_encoding` para obtener una descripción y ejemplos.

`mbstring.regex_retry_limit` `int`  
Limita la cantidad de retroceso que se puede realizar durante una coincidencia de mbregex.

Esta configuración solo tiene efecto al enlazar con oniguruma \>= 6.8.0.

`mbstring.regex_stack_limit` `int`  
Limita la profundidad de la pila de las expresiones regulares de mbstring.

De acuerdo a la [especificación de HTML 4.01](http://www.w3.org/TR/REC-html40/interact/forms.html#adef-accept-charset), se permite que los navegadores envíen un formulario con una codificación diferente a la utilizada por la página. Véase `mb_http_input` para consultar los juegos de caracteres utilizados por los navegadores.

Pese a que la mayoría de navegadores son capaces de averiguar la codificación de un determinado documento HTML, es aconsejable utilizar el parámetro `charset` en la cabecera `Content-Type` de HTTP con un valor apropiado, mediante `header` o mediante el ajuste ini [default_charset](#ini.sect.data-handling).

Ejemplos de ajustes de `php.ini`

    ; Establecer el lenguaje predeterminado
    mbstring.language        = Neutral; Establecer el lenguaje neutral(UTF-8) (predeterminado)
    mbstring.language        = English; Establecer como lenguaje el inglés
    mbstring.language        = Japanese; Establecer como lenguaje el japonés

    ;; Establecer la codificación interna predeterminada
    ;; Nota: Asegúrese de usar una codificación que funcione con PHP
    mbstring.internal_encoding    = UTF-8  ; Establecer la codificación interna a UTF-8

    ;; Traducción de codificación HTTP entrante habilitada
    mbstring.encoding_translation = On

    ;; Establecer la codificación de caracteres predeterminada de HTTP entrante
    ;; Nota: Un script no podrá cambiar el ajuste http_input.
    mbstring.http_input           = pass    ; Sin conversión.
    mbstring.http_input           = auto    ; Establecer la entrada HTTP en automático
                                    ; "auto" se expande de acuerdo a mbstring.language
    mbstring.http_input           = SJIS    ; Establecer la entrada HTTP a SJIS
    mbstring.http_input           = UTF-8,SJIS,EUC-JP ; Especificar el orden

    ;; Establecer la codificación de caracteres predeterminada de HTTP saliente
    mbstring.http_output          = pass    ; Sin conversión
    mbstring.http_output          = UTF-8   ; Establecer la codificación de salida HTTP a UTF-8

    ;; Establecer el orden predeterminado de la detección de juegos de caracteres
    mbstring.detect_order         = auto    ; Orden de detección automático
    mbstring.detect_order         = ASCII,JIS,UTF-8,SJIS,EUC-JP ; Especificar el orden

    ;; Establecer el carácter de sustitución predeterminado
    mbstring.substitute_character = 12307   ; Especificar un valor Unicode
    mbstring.substitute_character = none    ; No imprimir el carácter
    mbstring.substitute_character = long    ; Ejemplo de long: U+3000,JIS+7E7E

Ajustes de `php.ini` para usuarios de `EUC-JP`

    ;; Deshabilitar el almacenamiento en el búfer de salida
    output_buffering      = Off

    ;; Establecer el juego de caracteres de las cabeceras HTTP
    default_charset       = EUC-JP

    ;; Establecer como lenguaje predeterminado el japonés
    mbstring.language = Japanese

    ;; Habilitar la traducción de la codificación del HTTP entrante.
    mbstring.encoding_translation = On

    ;; Establecer en automática la conversión de la codificación de HTTP entrante
    mbstring.http_input   = auto

    ;; Convertir la salida de HTTP a EUC-JP
    mbstring.http_output  = EUC-JP

    ;; Establecer EUC-JP como codificación interna
    mbstring.internal_encoding = EUC-JP

    ;; No imprimir caracteres inválidos
    mbstring.substitute_character = none

Ajustes de `php.ini` para usuarios de `SJIS`

    ;; Habilitar el almacenamiento en el búfer de salida
    output_buffering     = On

    ;; Establecer mb_output_handler para habilitar la conversión de los datos de salida
    output_handler       = mb_output_handler

    ;; Establecer el juego de caracteres de las cabeceras HTTP
    default_charset      = Shift_JIS

    ;; Establecer como lenguaje predeterminado el japonés
    mbstring.language = Japanese

    ;; Establecer en automático la conversión del juego de caracteres http entrante
    mbstring.http_input  = auto

    ;; Convertir a SJIS
    mbstring.http_output = SJIS

    ;; Establecer EUC-JP como codificación interna
    mbstring.internal_encoding = EUC-JP

    ;; No imprimir caracteres inválidos
    mbstring.substitute_character = none
