---
title: '"email.mime": Creating email and MIME objects from scratch'
source_url: https://docs.python.org/es/3
source_path: library/email.mime.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2490
---

# "email.mime": Creating email and MIME objects from scratch

**Código fuente:** Lib/email/mime/

======================================================================

Este módulo forma parte de la API heredada de correo electrónico
("Compat32"). Su funcionalidad se sustituye parcialmente por el
"contentmanager" en la nueva API, pero en ciertas aplicaciones estas
clases pueden seguir siendo útiles, incluso en código no heredado.

Normalmente, se obtiene una estructura de objeto de mensaje pasando un
archivo o algún texto a un analizador, que analiza el texto y retorna
el objeto de mensaje principal. Sin embargo, también puede crear una
estructura de mensajes completa desde cero, o incluso objetos
individuales "Message" a mano. De hecho, también puede tomar una
estructura existente y agregar nuevos objetos "Message", moverlos,
etc. Esto compone una interfaz muy conveniente para cortar y gestionar
mensajes MIME.

Puede crear una nueva estructura de objeto mediante la creación de una
instancia de "Message", añadiendo accesorios y todos los encabezados
necesarios manualmente. Para mensajes MIME sin embargo, el paquete
"email" proporciona subclases convenientes para facilitar las cosas.

Descripción de las clases:

class email.mime.base.MIMEBase(_maintype, _subtype, *, policy=compat32, **_params)

   Módulo: "email.mime.base"

   Esta es la clase básica para todas las subclases específicas
   "Message" para MIME. Normalmente no creará instancias específicas
   de la "MIMEBase", aunque es posible. La "MIMEBase" se proporciona
   principalmente como una clase básica conveniente para subclases más
   específicas, apropiadas para MIME.

   *_maintype* es el tipo principal *Content-Type* (por ejemplo *text*
   o *image*), y *_subtype* es el tipo menor *Content-Type* (por
   ejemplo *plain* o *gif*). *_params* es un diccionario de parámetro
   clave/valor y se pasa directamente a "Message.add_header".

   Si se especifica *policy*, (por defecto, la directiva "compat32")
   se pasará a "Message".

   La clase "MIMEBase" siempre agrega un encabezado *Content-Type*
   (basado en *_maintype*, *_subtype* y *_params*), y un encabezado
   *MIME-Versión* (siempre establecido en "1.0").

   Distinto en la versión 3.6: Se ha añadido el parámetro *policy* de
   solo palabra clave.

class email.mime.nonmultipart.MIMENonMultipart

   Módulo: "email.mime.nonmultipart"

   Una subclase de "MIMEBase", es una clase base intermedia para los
   mensajes MIME que no son *multipart*. El propósito principal de
   esta clase es evitar el uso del método "attach()", que solo tiene
   sentido para los mensajes *multipart*. Si se llama a "attach()", se
   lanza una excepción "MultipartConversionError".

class email.mime.multipart.MIMEMultipart(_subtype='mixed', boundary=None, _subparts=None, *, policy=compat32, **_params)

   Módulo: "email.mime.multipart"

   Una subclase de "MIMEBase", se trata de una clase base intermedia
   para los mensajes MIME que son *multipart*. El valor predeterminado
   opcional de *_subtype* es *mixed*, pero se puede utilizar para
   especificar el subtipo del mensaje. Se agregará un encabezado
   *Content-Type* de *multipart/_subtype* al objeto del mensaje.
   También se agregará un encabezado *MIME-Version*.

   El *boundary* opcional es la cadena de límite multiparte. Cuando
   "None" (valor predeterminado), el límite se calcula cuando es
   necesario (por ejemplo, cuando se serializa el mensaje).

   *_subparts* es una secuencia de subpartes iniciales para la carga
   útil. Debe ser posible convertir esta secuencia en una lista.
   Siempre puede adjuntar nuevas subpartes al mensaje mediante el
   método "Message.attach".

   El valor predeterminado del argumento *policy* opcional es
   "compat32".

   Los parámetros adicionales para el encabezado *Content-Type* se
   toman de los argumentos de palabra clave, o se pasan al argumento
   *_params*, que es un diccionario de palabras clave.

   Distinto en la versión 3.6: Se ha añadido el parámetro *policy* de
   solo palabra clave.

class email.mime.application.MIMEApplication(_data, _subtype='octet-stream', _encoder=email.encoders.encode_base64, *, policy=compat32, **_params)

   Módulo: "email.mime.application"

   Una subclase de "MIMENonMultipart", la clase "MIMEApplication" se
   utiliza para representar objetos de mensaje MIME de tipo principal
   *application*. *_data* contiene los bytes de la aplicación sin
   procesar. *_subtype* opcional especifica el subtipo MIME y el valor
   predeterminado es *octet-stream*.

   *_encoder* opcional es una recurso invocable (es decir, una
   función) que realizará la codificación real de los datos para el
   transporte. Este invocable toma un argumento, que es la instancia
   "MIMEApplication". Debe utilizar "get_payload()" y "set_payload()"
   para cambiar la carga útil a la forma codificada. También debe
   agregar cualquier *Content-Transfer-Encoding* u otros encabezados
   al objeto del mensaje según sea necesario. La codificación
   predeterminada es base64. Consulte el módulo "email.encoders" para
   obtener una lista de los codificadores integrados.

   El valor predeterminado del argumento *policy* opcional es
   "compat32".

   *_params* se pasan directamente al constructor de la clase base.

   Distinto en la versión 3.6: Se ha añadido el parámetro *policy* de
   solo palabra clave.

class email.mime.audio.MIMEAudio(_audiodata, _subtype=None, _encoder=email.encoders.encode_base64, *, policy=compat32, **_params)

   Módulo: "email.mime.audio"

   Una subclase de "MIMENonMultipart", la clase "MIMEAudio" se utiliza
   para crear objetos de mensaje MIME de tipo principal *audio*.
   *_audiodata* contiene los bytes del audio sin procesar. Si estos
   datos pueden ser decodificados como au, wav, aiff, or aifc,
   entonces el subtipo se incluirá automáticamente en el encabezado
   *Content-Type*. De lo contrario, puede especificar explícitamente
   el subtipo de audio mediante el argumento *_subtype*. Si no se pudo
   adivinar el tipo secundario y no se ha proporcionado *_subtype*, se
   lanza "TypeError".

   *_encoder* opcional es un recurso invocable (es decir, una función)
   que realizará la codificación real de los datos de audio para el
   transporte. Este invocable toma un argumento, que es la instancia
   "MIMEAudio". Debe utilizar "get_payload()" y "set_payload()" para
   cambiar la carga útil a la forma codificada. También debe agregar
   cualquier *Content-Transfer-Encoding* u otros encabezados al objeto
   del mensaje según sea necesario. La codificación predeterminada es
   base64. Consulte el módulo "email.encoders" para obtener una lista
   de los codificadores integrados.

   El valor predeterminado del argumento *policy* opcional es
   "compat32".

   *_params* se pasan directamente al constructor de la clase base.

   Distinto en la versión 3.6: Se ha añadido el parámetro *policy* de
   solo palabra clave.

class email.mime.image.MIMEImage(_imagedata, _subtype=None, _encoder=email.encoders.encode_base64, *, policy=compat32, **_params)

   Módulo: "email.mime.image"

   Una subclase de "MIMENonMultipart", la clase "MIMEImage" se utiliza
   para crear objetos de mensaje MIME de tipo principal *image*.
   *_imagedata* contiene los bytes de la imagen sin procesar. Si se
   puede detectar el tipo de dato (intentando con jpeg, png, gif,
   tiff, rgb, pbm, pgm, ppm, rast, xbm, bmp, webp, y exr), entonces el
   subtipo se incluirá automáticamente en el encabezado *Content-
   Type*. De lo contrario, puede especificar explícitamente el subtipo
   de imagen mediante el argumento *_subtype*. Si no se pudo adivinar
   el tipo secundario y no se ha proporcionado *_subtype*, se lanza
   "TypeError".

   *_encoder* opcional es un recurso invocable (es decir, una función)
   que realizará la codificación real de los datos de imagen para el
   transporte. Este invocable toma un argumento, que es la instancia
   "MIMEImage". Debe utilizar "get_payload()" y "set_payload()" para
   cambiar la carga útil a la forma codificada. También debe agregar
   cualquier *Content-Transfer-Encoding* u otros encabezados al objeto
   del mensaje según sea necesario. La codificación predeterminada es
   base64. Consulte el módulo "email.encoders" para obtener una lista
   de los codificadores integrados.

   El valor predeterminado del argumento *policy* opcional es
   "compat32".

   *_params* se pasan directamente al constructor "MIMEBase".

   Distinto en la versión 3.6: Se ha añadido el parámetro *policy* de
   solo palabra clave.

class email.mime.message.MIMEMessage(_msg, _subtype='rfc822', *, policy=compat32)

   Módulo: "email.mime.message"

   Una subclase de "MIMENonMultipart", la clase "MIMEMessage" se
   utiliza para crear objetos MIME de tipo principal *message*. *_msg*
   se utiliza como la carga y debe ser una instancia de la clase
   "Message" (o una subclase de la misma), de lo contrario se lanza un
   "TypeError".

   *_subtype* opcional establece el subtipo del mensaje; por defecto
   es *rfc822*.

   El valor predeterminado del argumento *policy* opcional es
   "compat32".

   Distinto en la versión 3.6: Se ha añadido el parámetro *policy* de
   solo palabra clave.

class email.mime.text.MIMEText(_text, _subtype='plain', _charset=None, *, policy=compat32)

   Módulo: "email.mime.text"

   Una subclase de "MIMENonMultipart", la clase "MIMEText" se utiliza
   para crear objetos MIME de tipo principal *text*. *_text* es la
   cadena de caracteres de la carga útil. *_subtype* es el tipo menor
   y el valor predeterminado es *plain*. *_charset* es el paquete de
   caracteres del texto y se pasa como argumento al constructor
   "MIMENonMultipart"; el valor predeterminado es "us-ascii" si la
   cadena contiene sólo puntos de código "ascii", y "utf-8" en caso
   contrario. El parámetro *_charset* acepta una cadena o una
   instancia "Charset".

   A menos que el argumento *_charset* se establezca explícitamente
   como "None", el objeto MIMEText creado tendrá a la vez un
   encabezado *Content-Type* con un parámetro "charset", y un
   encabezado *Content-Transfer-Encoding*. Esto significa que una
   llamada posterior a "set_payload" no dará lugar a una carga
   codificada, incluso si se pasa un conjunto de caracteres en el
   comando "set_payload". Puede "restablecer" este comportamiento
   eliminando el encabezado "Content-Transfer-Encoding", después de lo
   cual una llamada a "set_payload" codificará automáticamente la
   nueva carga útil (y agregará un nuevo encabezado *Content-Transfer-
   Encoding*).

   El valor predeterminado del argumento *policy* opcional es
   "compat32".

   Distinto en la versión 3.5: *_charset* también acepta instancias
   "Charset".

   Distinto en la versión 3.6: Se ha añadido el parámetro *policy* de
   solo palabra clave.
