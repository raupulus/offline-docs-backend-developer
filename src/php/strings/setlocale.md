---
title: setlocale
description: Establece la información de configuración local
source_url: https://www.php.net/manual/es/function.setlocale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/setlocale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: ec01a42be
order: 89030
---

setlocale

Establece la información de configuración local

## Descripción

```php
setlocale(int $category, string $locales, string ...$rest): string
```php

Firma alternativa (no soportada con argumentos nombrados):

```php
setlocale(int $category, array $locale_array): string
```

Establece la información de configuración local.

> [!WARNING]
> La información de configuración local se mantiene por proceso, no por hilo. Si está ejecutando PHP en una API de servidor multihilo, puede experimentar cambios repentinos en la configuración local mientras se ejecuta un script, aunque el script nunca haya llamado a `setlocale`. Esto ocurre debido a otros scripts que se ejecutan en diferentes hilos del mismo proceso al mismo tiempo, cambiando la configuración local del proceso usando `setlocale`. En Windows, la información de configuración local se mantiene por hilo a partir de PHP 7.0.5.

## Parámetros

`category`  
`category` es una constante nombrada que especifica la categoría de las funciones afectadas por la configuración local:

- `LC_ALL` para todas las categorías siguientes

- `LC_COLLATE` para comparación de strings, ver `strcoll`

- `LC_CTYPE` para clasificación y conversión de caracteres, por ejemplo `ctype_alpha`

- `LC_MONETARY` para `localeconv`

- `LC_NUMERIC` para el separador decimal (Ver también `localeconv`)

- `LC_TIME` para el formato de fecha y hora con `strftime`

- `LC_MESSAGES` para respuestas del sistema (disponible si PHP fue compilado con `libintl`)

`locales`  
Si `locales` es la cadena vacía `""` o es `null`, los nombres de configuración local se establecerán a partir de los valores de las variables de entorno con los mismos nombres que las categorías anteriores, o de "LANG".

Si `locales` es `"0"`, la configuración local no se ve afectada, solo se devuelve la configuración actual.

Si `locales` va seguido de parámetros adicionales, entonces cada parámetro se intenta establecer como nueva configuración local hasta que tenga éxito. Esto es útil si una configuración local es conocida bajo diferentes nombres en diferentes sistemas o para proporcionar una alternativa para una configuración local posiblemente no disponible.

`rest`  
Parámetros opcionales de string para intentar como configuraciones locales hasta que tenga éxito.

`locale_array`  
Cada elemento del array se intenta establecer como nueva configuración local hasta que tenga éxito. Esto es útil si una configuración local es conocida bajo diferentes nombres en diferentes sistemas o para proporcionar una alternativa para una configuración local posiblemente no disponible.

> [!NOTE]
> En Windows, setlocale(LC_ALL, '') establece los nombres de configuración local a partir de la configuración regional/idioma del sistema (accesible a través del Panel de Control).

## Valores devueltos

Devuelve la nueva configuración local actual, o `false` si la funcionalidad de configuración local no está implementada en su plataforma, la configuración local especificada no existe o el nombre de la categoría no es válido.

Un nombre de categoría no válido también causa un mensaje de advertencia. Los nombres de categoría/configuración local se pueden encontrar en [RFC 1766](https://datatracker.ietf.org/doc/html/rfc1766) y [ISO 639](http://www.loc.gov/standards/iso639-2/php/code_list.php). Diferentes sistemas tienen diferentes esquemas de nombres para configuraciones locales.

> [!NOTE]
> El valor de retorno de `setlocale` depende del sistema en el que se está ejecutando PHP. Devuelve exactamente lo que devuelve la función `setlocale` del sistema.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Pasar un entero `0` como argumento `locales` ya no está soportado y ahora lanza un `TypeError`. |

## Ejemplos

Ejemplos de `setlocale`

```php
<?php
/* Establecer configuración local a holandés */
setlocale(LC_ALL, 'nl_NL');

/* Salida: vrijdag 22 december 1978 */
echo strftime("%A %e %B %Y", mktime(0, 0, 0, 12, 22, 1978));

/* probar diferentes nombres posibles de configuración local para alemán */
$loc_de = setlocale(LC_ALL, 'de_DE@euro', 'de_DE', 'de', 'ge');
echo "Configuración local preferida para alemán en este sistema es '$loc_de'";
?>

    
```

Recuperar la configuración actual de `setlocale`

```php
<?php
/* Recuperar la configuración actual */
$current = setlocale(LC_ALL, null);

echo "Configuración local actual '$current'";
?>

    
```

Ejemplos de `setlocale` para Windows

```php
<?php
/* Establecer configuración local a holandés */
setlocale(LC_ALL, 'nld_nld');

/* Salida: vrijdag 22 december 1978 */
echo strftime("%A %d %B %Y", mktime(0, 0, 0, 12, 22, 1978));

/* probar diferentes nombres posibles de configuración local para alemán */
$loc_de = setlocale(LC_ALL, 'de_DE@euro', 'de_DE', 'deu_deu');
echo "Configuración local preferida para alemán en este sistema es '$loc_de'";
?>

    
```

## Notas

> [!TIP]
> Los usuarios de Windows encontrarán información útil sobre las cadenas `locales` en el sitio web de MSDN de Microsoft. Las cadenas de idioma soportadas se pueden encontrar en la [documentación de cadenas de idioma](http://msdn.microsoft.com/en-us/library/39cwe7zf.aspx) y las cadenas de país/región soportadas en la [documentación de cadenas de país/región](http://msdn.microsoft.com/en-us/library/cdax410z.aspx).
