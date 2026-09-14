---
title: wkhtmltox\PDF\Object::__construct
description: Crea un nuevo objeto PDF
source_url: https://www.php.net/manual/es/wkhtmltox-pdf-object.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wkhtmltox/wkhtmltox/pdf/object/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wkhtmltox
translation_status: ready
translation_reviewed: false
translation_revision: 71e7f31df
order: 101950
---

wkhtmltox\PDF\Object::\_\_construct

Crea un nuevo objeto PDF

## Descripción

```php
public wkhtmltox\PDF\Object::__construct(string $buffer, [array $settings])
```php

Crea un nuevo objeto PDF desde el buffer proporcionado, y las configuraciones opcionales.

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
<td>page</td>
<td>URL o ruta del archivo HTML a convertir</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>useExternalLinks</td>
<td>Establecer en <code>true</code> para convertir los enlaces externos enlaces PDF en la salida</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>useLocalLinks</td>
<td>Establecer en <code>true</code> para convertir los enlaces internos en los datos de entrada en enlaces PDF en la salida</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>produceForms</td>
<td>Establecer en <code>true</code> para convertir los formularios HTML en formularios PDF</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>replacements</td>
<td>no documentado</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>includeInOutline</td>
<td>Establecer en <code>true</code> para incluir las secciones de este objeto en el contorno y la tabla de contenidos</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>pagesCount</td>
<td>Establecer en <code>true</code> para incluir en la tabla de contenidos el número de páginas de este objeto</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>tocXsl</td>
<td>Establecer en hoja de estilo para convertir este objeto en un objeto de tabla de contenidos</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>toc.useDottedLines</td>
<td>Establecer en <code>true</code> para usar líneas de puntos en la tabla de contenidos</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>toc.captionText</td>
<td>El pie de ilustración para la tabla de contenidos</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>toc.forwardLinks</td>
<td>Establecer en <code>true</code> para crear enlaces desde la tabla de contenidos hacia el contenido</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>toc.backLinks</td>
<td>Establecer en <code>true</code> para crear enlaces desde el contenido hacia la tabla de contenidos</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>toc.indentation</td>
<td>La indentación para la tabla de contenidos</td>
<td>2em</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>toc.fontScale</td>
<td>El factor para reducir la fuente de caracteres en todos los niveles de la tabla de contenidos</td>
<td>0.8</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>header.fontSize</td>
<td>El tamaño de la fuente de caracteres a usar en el encabezado</td>
<td>13</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>header.fontName</td>
<td>El nombre de la fuente de caracteres a usar en el encabezado</td>
<td>times</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>header.left</td>
<td>El texto para el lado izquierdo del encabezado</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>header.center</td>
<td>El texto para el centro del encabezado</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>header.right</td>
<td>El texto para el lado derecho del encabezado</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>header.line</td>
<td>Activa o desactiva la regla horizontal bajo el encabezado</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>header.spacing</td>
<td>El espacio entre el encabezado y el contenido</td>
<td>1.8</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>header.htmlUrl</td>
<td>URL o la ruta hacia el archivo HTML a usar en el encabezado</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>footer.fontSize</td>
<td>El tamaño de la fuente de caracteres a usar en el pie de página</td>
<td>13</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>footer.fontName</td>
<td>El nombre de la fuente de caracteres a usar en el pie de página</td>
<td>times</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>footer.left</td>
<td>El texto para el lado izquierdo del pie de página</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>footer.center</td>
<td>El texto para el centro del pie de página</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>footer.right</td>
<td>El texto para el lado derecho del pie de página</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>footer.line</td>
<td>Activa o desactiva la regla horizontal bajo el pie de página</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>footer.spacing</td>
<td>El espacio entre el pie de página y el contenido</td>
<td>1.8</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>footer.htmlUrl</td>
<td>URL o la ruta del archivo HTML a usar en el pie de página</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.username</td>
<td>nombre de usuario a utilizar al conectarse a un sitio web</td>
<td>bart</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.password</td>
<td>contraseña a utilizar al conectarse a un sitio web</td>
<td>elbarto</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.jsdelay</td>
<td>el tiempo en milisegundos a esperar después de cargar una página antes de capturarla</td>
<td>1200</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.zoomFactor</td>
<td>cuánto zoom debe aplicarse al contenido</td>
<td>2.2</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.customHeaders</td>
<td>encabezados personalizados a enviar al solicitar la página web principal</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.repertCustomHeaders</td>
<td>establecer en true para enviar con todas las solicitudes</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.cookies</td>
<td>cookie a enviar al solicitar la página web principal</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.post</td>
<td>string a enviar al realizar una solicitud post a la página web principal</td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.blockLocalFileAccess</td>
<td>impide que los archivos locales y los archivos de tubería accedan a otros archivos locales</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.stopSlowScript</td>
<td>detiene los scripts lentos de javascript</td>
<td>booleano</td>
<td></td>
</tr>
<tr>
<td>load.debugJavascript</td>
<td>permite que javascript lance advertencias</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.loadErrorHandling</td>
<td>define la estrategia de manejo de errores</td>
<td><table>
<tbody>
<tr>
<td>abort</td>
<td>aborta el proceso de conversión</td>
</tr>
<tr>
<td>skip</td>
<td>no añade el objeto a la salida final</td>
</tr>
<tr>
<td>ignore</td>
<td>intenta añadir el objeto a la salida final</td>
</tr>
</tbody>
</table></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>load.proxy</td>
<td></td>
<td></td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>web.background</td>
<td>incluye una imagen de fondo en la salida</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>web.loadImages</td>
<td>incluye imágenes en la salida</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>web.enableJavascript</td>
<td>activa o desactiva javascript</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>web.enableIntelligentShrinking</td>
<td>activa el intento de poner más contenido en la página, se aplica solo a la salida PDF</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>web.minimumFontSize</td>
<td>el tamaño de fuente mínimo permitido</td>
<td>9</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>web.printMediaType</td>
<td>muestra el contenido usando el tipo de medio de impresión en lugar del tipo de medio de pantalla</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>web.defaultEncoding</td>
<td>el contenido a usar cuando no se especifica ninguna codificación</td>
<td>utf-8</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>web.userStyleSheet</td>
<td>URL o ruta hacia una hoja de estilo de usuario especificada</td>
<td>/ruta/hacia/estilo.css</td>
<td>&gt;= 0.1.0</td>
</tr>
<tr>
<td>web.enablePlugins</td>
<td>activa o desactiva los plugins NS</td>
<td>booleano</td>
<td>&gt;= 0.1.0</td>
</tr>
</tbody>
</table>
