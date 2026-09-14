---
title: wkhtmltox\PDF\Converter::__construct
description: Crea un nuevo conversor de PDF
source_url: https://www.php.net/manual/es/wkhtmltox-pdf-converter.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wkhtmltox/wkhtmltox/pdf/converter/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wkhtmltox
translation_status: ready
translation_reviewed: false
translation_revision: c80bf6d45
order: 101920
---

wkhtmltox\PDF\Converter::\_\_construct

Crea un nuevo conversor de PDF

## Descripción

```php
public wkhtmltox\PDF\Converter::__construct([array $settings])
```php

Crea un nuevo conversor de PDF, utilizando opcionalmente una configuración.

## Parámetros

`settings`  
<table>
<thead>
<tr>
<th>Nombre</th>
<th>Descripción</th>
<th>Valores</th>
<th>Registro de cambios</th>
</tr>
</thead>
<tbody>
<tr>
<td>size.pageSize</td>
<td>Tamaño del papel del documento final</td>
<td>A4</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>size.width</td>
<td>Ancho del documento final</td>
<td>210mm</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>size.height</td>
<td>Altura del documento final</td>
<td>297mm</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>orientation</td>
<td>Orientación del documento final</td>
<td><table>
<tbody>
<tr>
<td>Landscape</td>
</tr>
<tr>
<td>Portrait</td>
</tr>
</tbody>
</table></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>colorMode</td>
<td>Modo de color del documento final</td>
<td><table>
<tbody>
<tr>
<td>Color</td>
</tr>
<tr>
<td>Greyscale</td>
</tr>
</tbody>
</table></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>resolution</td>
<td>Resolución del documento final</td>
<td>La mayoría de las veces, no tiene ningún efecto</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>dpi</td>
<td>DPI a usar al imprimir</td>
<td>80</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>pageOffset</td>
<td>Entero a añadir a los números de página generados para el encabezado, el pie de página y el índice</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>copies</td>
<td></td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>collate</td>
<td>Si se deben intercalar las copias</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>outline</td>
<td>Genera un índice PDF</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>outlineDepth</td>
<td>Profundidad máxima del índice</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>dumpOutline</td>
<td>Ruta del archivo para extraer el índice XML</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>out</td>
<td>Ruta para el archivo final, si es "-" se usa stdout</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>documentTitle</td>
<td>Título del documento final</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>useCompression</td>
<td>Activa o desactiva la compresión sin pérdida</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>margin.top</td>
<td>Tamaño del margen superior</td>
<td>2cm</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>margin.bottom</td>
<td>Tamaño del margen inferior</td>
<td>2cm</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>margin.left</td>
<td>Tamaño del margen izquierdo</td>
<td>2cm</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>margin.right</td>
<td>Tamaño del margen derecho</td>
<td>2cm</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>imageDPI</td>
<td>DPI máximo para las imágenes en el documento final</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>imageQuality</td>
<td>El factor de compresión jpeg para las imágenes en el documento final</td>
<td>94</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.cookieJar</td>
<td>Ruta hacia el archivo utilizado para cargar y almacenar las cookies</td>
<td>/tmp/cookies.txt</td>
<td>&gt;= 0.1.0</td>
</tr>
</tbody>
</table>
