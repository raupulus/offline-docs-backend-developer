---
title: imagegrabwindow
description: Captura una ventana
source_url: https://www.php.net/manual/es/function.imagegrabwindow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagegrabwindow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: 9960a09a5
order: 32150
---

imagegrabwindow

Captura una ventana

## Descripción

```php
imagegrabwindow(int $handle, [bool $client_area]): GdImage
```php

Captura una ventana o el espacio de su cliente, utilizando un gestor de ventanas (propiedad HWND de la instancia COM).

> [!NOTE]
> Esta función solo está disponible en Windows.

## Parámetros

`handle`  
El identificador HWND de la ventana.

`client_area`  
Incluir o no el espacio del cliente de la ventana de la aplicación.

## Valores devueltos

Devuelve un objeto imagen en caso de éxito, o `false` si ocurre un error.

## Errores/Excepciones

Se emite una alerta de tipo E_NOTICE si `window_handle` es un gestor de ventana no válido. Se emite una alerta de tipo E_WARNING si la API de Windows es demasiado antigua.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |
| 8.0.0 | `client_area` ahora espera un `bool` ; anteriormente esperaba un `int`. |

## Ejemplos

Ejemplo con `imagegrabwindow`

Captura una ventana (por ejemplo, IE).

```
<?php
$browser = new COM("InternetExplorer.Application");
$handle = $browser->HWND;
$browser->Visible = true;
$im = imagegrabwindow($handle);
$browser->Quit();
imagepng($im, "iesnap.png");
?>

    
```php

Captura una ventana (por ejemplo, IE) pero con su contenido.

```
<?php
$browser = new COM("InternetExplorer.Application");
$handle = $browser->HWND;
$browser->Visible = true;
$browser->Navigate("http://www.libgd.org");

/* ¿Funciona siempre? */
while ($browser->Busy) {
    com_message_pump(4000);
}
$im = imagegrabwindow($handle, 0);
$browser->Quit();
imagepng($im, "iesnap.png");
?>

    
```php

## Véase también

imagegrabscreen
