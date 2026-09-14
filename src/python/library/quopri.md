---
title: '"quopri" --- Encode and decode MIME quoted-printable data'
source_url: https://docs.python.org/es/3
source_path: library/quopri.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3620
---

# "quopri" --- Encode and decode MIME quoted-printable data

**Código fuente:** Lib/quopri.py

======================================================================

Este módulo realiza la codificación y descodificación de transporte
imprimible entre comillas, tal como se define en **RFC 1521**: "MIME
(Multipurpose Internet Mail Extensions) Parte Uno: Mecanismos para
especificar y describir el formato de los cuerpos de mensajes de
Internet". La codificación imprimible entre comillas está diseñada
para datos donde hay relativamente pocos caracteres no imprimibles; el
esquema de codificación base64 disponible a través del módulo "base64"
es más compacto si hay muchos caracteres de este tipo, como cuando se
envía un archivo gráfico.

quopri.decode(input, output, header=False)

   Descodificar el contenido del archivo *input* y escribir los datos
   binarios descodificados resultantes en el archivo *output*. *input*
   y *output* deben ser *objetos de archivo binario*.  Si el argumento
   opcional *header* está presente y true, el carácter de subrayado se
   descodificará como espacio. Esto se utiliza para decodificar
   encabezados codificados en "Q" como se describe en **RFC 1522**:
   "MIME (Multipurpose Internet Mail Extensions) Parte dos:
   Extensiones de encabezado de mensaje para texto no ASCII".

quopri.encode(input, output, quotetabs, header=False)

   Codifique el contenido del archivo *input* y escriba los datos
   imprimibles entre comillas resultantes en el archivo *output*.
   *input* y *output* deben ser *objetos de archivo binario*.
   *quotetabs*, un indicador no opcional que controla si codificar
   espacios incrustados y pestañas; cuando true codifica dicho espacio
   en blanco incrustado, y cuando false los deja sin codificar. Tenga
   en cuenta que los espacios y pestañas que aparecen al final de las
   líneas siempre están codificados, según **RFC 1521**.  *header* es
   un indicador que controla si los espacios están codificados como
   guiones bajos según **RFC 1522**.

quopri.decodestring(s, header=False)

   Como "decode()", excepto que acepta una fuente "bytes" y retorna el
   correspondiente "bytes" decodificado.

quopri.encodestring(s, quotetabs=False, header=False)

   Como "encode()", excepto que acepta un origen "bytes" y retorna el
   codificado correspondiente "bytes". De forma predeterminada, envía
   un valor "False" al parámetro *quotetabs* de la función "encode()".

Ver también:

  Módulo "base64"
     Codificar y decodificar datos MIME base64
