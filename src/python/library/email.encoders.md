---
title: '"email.encoders": Encoders'
source_url: https://docs.python.org/es/3
source_path: library/email.encoders.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2410
---

# "email.encoders": Encoders

**Código fuente:** Lib/email/encoders.py

======================================================================

Este módulo forma parte de la anterior API de correo electrónico
("Compat32"). En la nueva API, la funcionalidad la proporciona el
parámetro *cte* del método "set_content()".

Este módulo está obsoleto en Python 3. Las funciones que aparecen aquí
no deberían ser llamadas explícitamente ya que la clase "MIMEText"
establece el tipo de contenido y el encabezado CTE utilizando los
valores del *_subtype* y del *_charset* que se pasan cuando se
instancia esa clase.

El texto que viene a continuación corresponde a la documentación
original del módulo.

Cuando se crean objetos "Message" desde 0, a menudo se necesita
codificar el contenido del mensaje para transportarlo a través de
servidores de correo electrónico adecuados. Esto es así especialmente
para el tipo de mensajes *image/** y *text/** que contienen datos
binarios.

The "email" package provides some convenient encoders in its
"encoders" module.  These encoders are actually used by the
"MIMEAudio" and "MIMEImage" class constructors to provide default
encodings.  All encoder functions take exactly one argument, the
message object to encode.  They usually extract the payload, encode
it, and reset the payload to this newly encoded value.  They should
also set the *Content-Transfer-Encoding* header as appropriate.

Ten en cuenta que estas funciones no sirven para un mensaje con
múltiples partes. En lugar de aplicarlo al mensaje completo, las
funciones deben aplicarse a cada subparte individual. Si se pasa un
mensaje de múltiples partes como argumento se activara un mensaje de
error "TypeError".

A continuación, una lista de las funciones de codificación
facilitadas:

email.encoders.encode_quopri(msg)

   Codifica el contenido en formularios entrecomillados e imprimibles
   y marca el encabezado *Content-Transfer-Encoding* como "quoted-
   printable" [1]. Es un buen codificador para usar cuando la mayoría
   del contenido son datos imprimibles normales pero hay algún dato
   que no es imprimible.

email.encoders.encode_base64(msg)

   Codifica el contenido en un formulario base64 y marca el encabezado
   *Content-Transfer-Encoding* como "base64". Esta codificación es
   buena cuando la mayoría del contenido son datos no imprimibles ya
   que es un formulario más compacto que formularios entrecomillados e
   imprimibles. La desventaja es que incluye el texto que no es leíble
   por los humanos.

email.encoders.encode_7or8bit(msg)

   Esto, en realidad, no modifica el contenido del mensaje, pero fija
   el encabezado *Content-Transfer-Encoding* a "7bit" u "8bit", lo que
   considere más adecuado en función del contenido del mensaje.

email.encoders.encode_noop(msg)

   Esto no hace nada; ni siquiera fija el encabezado *Content-
   Transfer-Encoding*.

-[ Notas ]-

[1] El codificado con "encode_quopri()" también codifica todas las
    tabulaciones y caracteres de espacios en los datos.
