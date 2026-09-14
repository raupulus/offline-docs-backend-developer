---
title: http://
description: Acceso a URLs HTTP(s)
source_url: https://www.php.net/manual/es/wrappers.http.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/http.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 8bc832a46
order: 4670
---

http://

https://

Acceso a URLs HTTP(s)

## Descripción

Permite el acceso en modo solo lectura a ficheros accesibles mediante HTTP. Por omisión, se utiliza una solicitud HTTP 1.0 GET. Se envía un encabezado `Host:` con la solicitud, para gestionar los hosts virtuales basados en nombres. Si se ha configurado una versión de navegador con la opción [user_agent](#ini.user-agent) en su archivo `php.ini` o mediante el contexto de flujo, también será incluida en su solicitud.

El flujo permite acceder al cuerpo (*body*) del recurso. Los encabezados se almacenan en la variable `$http_response_header`.

Si se necesita conocer la URL del recurso desde el cual proviene el documento (tras la ejecución de todas las redirecciones), deberá analizarse la serie de encabezados devueltos por el flujo.

La directiva [from](#ini.from) será utilizada para el encabezado `From:` si ha sido definida, y no será sobrescrita por los [???](#context).

## Uso

- `http://example.com`

- `http://example.com/fichero.php?var1=val1&var2=val2`

- `http://user:password@example.com`

- `https://example.com`

- `https://example.com/fichero.php?var1=val1&var2=val2`

- `https://user:password@example.com`

## Opciones

| Atributo                                                | Soportado |
|---------------------------------------------------------|-----------|
| Restringido por [allow_url_fopen](#ini.allow-url-fopen) | Sí        |
| Permite la lectura                                      | Sí        |
| Permite la escritura                                    | No        |
| Permite la adición                                      | No        |
| Permite la lectura y escritura simultáneamente          | N/A       |
| Soporte de la función `stat`                            | No        |
| Soporte de la función `unlink`                          | No        |
| Soporte de la función `rename`                          | No        |
| Soporte de la función `mkdir`                           | No        |
| Soporte de la función `rmdir`                           | No        |

Resumen de la envoltura {role="stream_wrapper"}

## Ejemplos

Detecta la última URL tras redirecciones

```php
<?php
$url = 'http://www.example.com/redirecting_page.php';

$fp = fopen($url, 'r');

$meta_data = stream_get_meta_data($fp);
foreach ($meta_data['wrapper_data'] as $response) {

    /* ¿Hemos sido redirigidos? */
    if (strtolower(substr($response, 0, 10)) == 'location: ') {

        /* actualización de $url con la ruta tras redirección */
        $url = substr($response, 10);
    }

}

?>

   
```

## Notas

> [!NOTE]
> HTTPS solo es soportado si la extensión [openssl](#book.openssl) está activa.

Las conexiones HTTP son de solo lectura; la escritura de datos o la copia de ficheros a un recurso HTTP no son soportadas.

El envío de solicitudes *POST* y *PUT*, por ejemplo, puede realizarse mediante los [contextos HTTP](#context.http).

## Véase también

\$http_response_header

stream_get_meta_data
