---
title: wkhtmltox\Image\Converter::__construct
description: Crea un nuevo convertidor de imágenes
source_url: https://www.php.net/manual/es/wkhtmltox-image-converter.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wkhtmltox/wkhtmltox/image/converter/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wkhtmltox
translation_status: ready
translation_reviewed: false
translation_revision: 71e7f31df
order: 101880
---

wkhtmltox\Image\Converter::\_\_construct

Crea un nuevo convertidor de imágenes

## Descripción

```php
public wkhtmltox\Image\Converter::__construct([string $buffer], [array $settings])
```php

Crea un convertidor de imágenes, utilizando opcionalmente un buffer de entrada así como una configuración

## Parámetros

`buffer`  
HTML

`settings`  
<table>
<thead>
<tr>
<th>Nombre</th>
<th>Descripción</th>
<th>Valor</th>
<th>Registro de cambios</th>
</tr>
</thead>
<tbody>
<tr>
<td>in</td>
<td>URL o ruta del archivo de entrada, si se usa la salida "-"</td>
<td>/ruta/hacia/marcado.html</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>out</td>
<td>Ruta del archivo de salida, si es "-" se usa stdout; por omisión, se usa un buffer interno</td>
<td>/ruta/hacia/salida.png</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>fmt</td>
<td>Formato de salida a usar</td>
<td><table>
<tbody>
<tr>
<td>""</td>
<td>predeterminado</td>
</tr>
<tr>
<td>jpg</td>
<td>salida como JPEG</td>
</tr>
<tr>
<td>png</td>
<td>salida como PNG</td>
</tr>
<tr>
<td>bmp</td>
<td>salida como mapa de bits</td>
</tr>
<tr>
<td>svg</td>
<td>salida como SVG</td>
</tr>
</tbody>
</table></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>transparent</td>
<td>En la salida PNG o SVG, hace el fondo transparente</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>screenWidth</td>
<td>El ancho de pantalla a usar para el renderizado en píxeles</td>
<td>800</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>smartWidth</td>
<td>Cuando es <code>true</code>, el ancho de la pantalla se extiende al ancho del contenido</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>quality</td>
<td>Factor de compresión a usar cuando la salida es una imagen JPEG</td>
<td>94</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>crop.left</td>
<td>Izquierda/coordenada X de la ventana a capturar, en píxeles</td>
<td>200</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>crop.top</td>
<td>Arriba/coordenada Y de la ventana a capturar, en píxeles</td>
<td>200</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>crop.width</td>
<td>Ancho de la ventana a capturar, en píxeles</td>
<td>200</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>crop.height</td>
<td>Altura de la ventana a capturar, en píxeles</td>
<td>200</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.cookieJar</td>
<td>Ruta del archivo utilizado para cargar y almacenar las cookies.</td>
<td>/tmp/cookies.txt</td>
<td>&gt;= 0.1.0</td>
</tr>
</tbody>
</table>
