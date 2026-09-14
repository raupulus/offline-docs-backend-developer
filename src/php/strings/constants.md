---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/string.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 5cadfd39b
order: 88580
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`CRYPT_SALT_LENGTH` (`int`)  

`CRYPT_STD_DES` (`int`)  
Indica si los hash basados en DES estándar son admitidos en `crypt`. Siempre `1`.

`CRYPT_EXT_DES` (`int`)  
Indica si los hash extendidos basados en DES son admitidos en `crypt`. Siempre `1`.

`CRYPT_MD5` (`int`)  
Indica si los hash MD5 son admitidos en `crypt`. Siempre `1`.

`CRYPT_BLOWFISH` (`int`)  
Indica si los hash Blowfish son admitidos en `crypt`. Siempre `1`.

`CRYPT_SHA256` (`int`)  
Indica si los hash SHA-256 son admitidos en `crypt`. Siempre `1`.

`CRYPT_SHA512` (`int`)  
Indica si los hash SHA-512 son admitidos en `crypt`. Siempre `1`.

`HTML_SPECIALCHARS` (`int`)  

`HTML_ENTITIES` (`int`)  

`ENT_COMPAT` (`int`)  

`ENT_QUOTES` (`int`)  

`ENT_NOQUOTES` (`int`)  

`ENT_IGNORE` (`int`)  

`ENT_SUBSTITUTE` (`int`)  

`ENT_DISALLOWED` (`int`)  

`ENT_HTML401` (`int`)  

`ENT_XML1` (`int`)  

`ENT_XHTML` (`int`)  

`ENT_HTML5` (`int`)  

`CHAR_MAX` (`int`)  

`LC_CTYPE` (`int`)  
Clasificación de caracteres y conversión afectada por la configuración de locale.

`LC_NUMERIC` (`int`)  
Separador decimal afectado por la configuración de locale.

`LC_TIME` (`int`)  
Formato de fechas y horas afectado por la configuración de locale.

`LC_COLLATE` (`int`)  
Comparación de strings afectada por la configuración de locale.

`LC_MONETARY` (`int`)  
Formato monetario afectado por la configuración de locale.

`LC_ALL` (`int`)  
Afecta todas las funciones que una de las otras constantes `LC_*` afecta.

`LC_MESSAGES` (`int`)  
Respuestas del sistema afectadas por la configuración de locale. Disponible si PHP ha sido compilado con `libintl`.

`STR_PAD_LEFT` (`int`)  

`STR_PAD_RIGHT` (`int`)  

`STR_PAD_BOTH` (`int`)  

`ALT_DIGITS` (`int`)  
Símbolos alternativos para los dígitos.

`ABDAY_1` (`int`)  
Nombre abreviado del primer día de la semana.

`ABDAY_2` (`int`)  
Nombre abreviado del segundo día de la semana.

`ABDAY_3` (`int`)  
Nombre abreviado del tercer día de la semana.

`ABDAY_4` (`int`)  
Nombre abreviado del cuarto día de la semana.

`ABDAY_5` (`int`)  
Nombre abreviado del quinto día de la semana.

`ABDAY_6` (`int`)  
Nombre abreviado del sexto día de la semana.

`ABDAY_7` (`int`)  
Nombre abreviado del séptimo día de la semana.

`DAY_1` (`int`)  
Nombre del primer día de la semana.

`DAY_2` (`int`)  
Nombre del segundo día de la semana.

`DAY_3` (`int`)  
Nombre del tercer día de la semana.

`DAY_4` (`int`)  
Nombre del cuarto día de la semana.

`DAY_5` (`int`)  
Nombre del quinto día de la semana.

`DAY_6` (`int`)  
Nombre del sexto día de la semana.

`DAY_7` (`int`)  
Nombre del séptimo día de la semana.

`ABMON_1` (`int`)  
Nombre abreviado del primer mes del año.

`ABMON_2` (`int`)  
Nombre abreviado del segundo mes del año.

`ABMON_3` (`int`)  
Nombre abreviado del tercer mes del año.

`ABMON_4` (`int`)  
Nombre abreviado del cuarto mes del año.

`ABMON_5` (`int`)  
Nombre abreviado del quinto mes del año.

`ABMON_6` (`int`)  
Nombre abreviado del sexto mes del año.

`ABMON_7` (`int`)  
Nombre abreviado del séptimo mes del año.

`ABMON_8` (`int`)  
Nombre abreviado del octavo mes del año.

`ABMON_9` (`int`)  
Nombre abreviado del noveno mes del año.

`ABMON_10` (`int`)  
Nombre abreviado del décimo mes del año.

`ABMON_11` (`int`)  
Nombre abreviado del undécimo mes del año.

`ABMON_12` (`int`)  
Nombre abreviado del duodécimo mes del año.

`MON_1` (`int`)  
Nombre del primer mes del año.

`MON_2` (`int`)  
Nombre del segundo mes del año.

`MON_3` (`int`)  
Nombre del tercer mes del año.

`MON_4` (`int`)  
Nombre del cuarto mes del año.

`MON_5` (`int`)  
Nombre del quinto mes del año.

`MON_6` (`int`)  
Nombre del sexto mes del año.

`MON_7` (`int`)  
Nombre del séptimo mes del año.

`MON_8` (`int`)  
Nombre del octavo mes del año.

`MON_9` (`int`)  
Nombre del noveno mes del año.

`MON_10` (`int`)  
Nombre del décimo mes del año.

`MON_11` (`int`)  
Nombre del undécimo mes del año.

`MON_12` (`int`)  
Nombre del duodécimo mes del año.

`AM_STR` (`int`)  
String para Ante meridiem.

`PM_STR` (`int`)  
String para Post meridiem.

`D_T_FMT` (`int`)  
String que puede ser utilizada como string de formato para `strftime` para representar la hora y la fecha.

`D_FMT` (`int`)  
String que puede ser utilizada como string de formato para `strftime` para representar la fecha.

`T_FMT` (`int`)  
String que puede ser utilizada como string de formato para `strftime` para representar la hora.

`T_FMT_AMPM` (`int`)  
String que puede ser utilizada como string de formato para `strftime` para representar la hora en formato de 12 horas con ante/post meridiem.

`ERA` (`int`)  
Era alternativa.

`ERA_YEAR` (`int`)  
Año en formato de era alternativa.

`ERA_D_T_FMT` (`int`)  
Fecha y hora en formato de era alternativa (string que puede ser utilizada en `strftime`).

`ERA_D_FMT` (`int`)  
Fecha en formato de era alternativa (string que puede ser utilizada en `strftime`).

`ERA_T_FMT` (`int`)  
Hora en formato de era alternativa (string que puede ser utilizada en `strftime`).

`INT_CURR_SYMBOL` (`int`)  
Símbolo de moneda internacional.

`CURRENCY_SYMBOL` (`int`)  
Símbolo de moneda local.

`CRNCYSTR` (`int`)  
Mismo valor que `CURRENCY_SYMBOL`.

`MON_DECIMAL_POINT` (`int`)  
Carácter del punto decimal.

`MON_THOUSANDS_SEP` (`int`)  
Separador de miles (grupos de tres dígitos).

`MON_GROUPING` (`int`)  
Como el elemento `"grouping"`.

`POSITIVE_SIGN` (`int`)  
Signo para valores positivos.

`NEGATIVE_SIGN` (`int`)  
Signo para valores negativos.

`INT_FRAC_DIGITS` (`int`)  
Decimal internacional.

`FRAC_DIGITS` (`int`)  
Decimal local.

`P_CS_PRECEDES` (`int`)  
Devuelve 1 si `CURRENCY_SYMBOL` precede a un valor positivo.

`P_SEP_BY_SPACE` (`int`)  
Devuelve 1 si un espacio separa `CURRENCY_SYMBOL` de un valor positivo.

`N_CS_PRECEDES` (`int`)  
Devuelve 1 si `CURRENCY_SYMBOL` precede a un valor negativo.

`N_SEP_BY_SPACE` (`int`)  
Devuelve 1 si un espacio separa `CURRENCY_SYMBOL` de un valor negativo.

`P_SIGN_POSN` (`int`)  
- Devuelve 0 si los paréntesis rodean la cantidad y `CURRENCY_SYMBOL`.

- Devuelve 1 si el string de signo precede a la cantidad y `CURRENCY_SYMBOL`.

- Devuelve 2 si el string de signo sigue a la cantidad y `CURRENCY_SYMBOL`.

- Devuelve 3 si el string de signo precede inmediatamente a `CURRENCY_SYMBOL`.

- Devuelve 4 si el string de signo sigue inmediatamente a `CURRENCY_SYMBOL`.

`N_SIGN_POSN` (`int`)  
Posición del signo para valores negativos.

`DECIMAL_POINT` (`int`)  
Carácter del punto decimal.

`RADIXCHAR` (`int`)  
Mismo valor que `DECIMAL_POINT`.

`THOUSANDS_SEP` (`int`)  
Carácter de separación para los miles (grupos de tres dígitos).

`THOUSEP` (`int`)  
Mismo valor que `THOUSANDS_SEP`.

`GROUPING` (`int`)  

`YESEXPR` (`int`)  
String regex para coincidir con la entrada `"yes"`.

`NOEXPR` (`int`)  
String regex para coincidir con la entrada `"no"`.

`YESSTR` (`int`)  
String de salida para `"yes"`.

`NOSTR` (`int`)  
String de salida para `"no"`.

`CODESET` (`int`)  
Devuelve un string con el nombre del juego de caracteres.
