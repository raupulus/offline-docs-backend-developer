---
title: '"email": Ejemplos'
source_url: https://docs.python.org/es/3
source_path: library/email.examples.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2430
---

# "email": Ejemplos

Aquí hay algunos ejemplos de cómo usar el paquete "email" para leer,
escribir y enviar mensajes de correo electrónico simples, así como
mensajes MIME más complejos.

Primero, veamos cómo crear y enviar un mensaje de texto simple (tanto
el contenido de texto como las direcciones pueden contener caracteres
unicode):

   # Import smtplib for the actual sending function
   import smtplib

   # Import the email modules we'll need
   from email.message import EmailMessage

   # Open the plain text file whose name is in textfile for reading.
   with open(textfile) as fp:
       # Create a text/plain message
       msg = EmailMessage()
       msg.set_content(fp.read())

   # me == the sender's email address
   # you == the recipient's email address
   msg['Subject'] = f'The contents of {textfile}'
   msg['From'] = me
   msg['To'] = you

   # Send the message via our own SMTP server.
   s = smtplib.SMTP('localhost')
   s.send_message(msg)
   s.quit()

El análisis de los encabezados **RFC 822** se pueden hacer fácilmente
usando las clases del módulo "parser":

   # Import the email modules we'll need
   #from email.parser import BytesParser
   from email.parser import Parser
   from email.policy import default

   # If the e-mail headers are in a file, uncomment these two lines:
   # with open(messagefile, 'rb') as fp:
   #     headers = BytesParser(policy=default).parse(fp)

   #  Or for parsing headers in a string (this is an uncommon operation), use:
   headers = Parser(policy=default).parsestr(
           'From: Foo Bar <user@example.com>\n'
           'To: <someone_else@example.com>\n'
           'Subject: Test message\n'
           '\n'
           'Body would go here\n')

   #  Now the header items can be accessed as a dictionary:
   print('To: {}'.format(headers['to']))
   print('From: {}'.format(headers['from']))
   print('Subject: {}'.format(headers['subject']))

   # You can also access the parts of the addresses:
   print('Recipient username: {}'.format(headers['to'].addresses[0].username))
   print('Sender name: {}'.format(headers['from'].addresses[0].display_name))

Aquí hay un ejemplo de cómo enviar un mensaje MIME que contiene un
grupo de fotos familiares que pueden residir en un directorio:

   # Import smtplib for the actual sending function.
   import smtplib

   # Here are the email package modules we'll need.
   from email.message import EmailMessage

   # Create the container email message.
   msg = EmailMessage()
   msg['Subject'] = 'Our family reunion'
   # me == the sender's email address
   # family = the list of all recipients' email addresses
   msg['From'] = me
   msg['To'] = ', '.join(family)
   msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

   # Open the files in binary mode.  You can also omit the subtype
   # if you want MIMEImage to guess it.
   for file in pngfiles:
       with open(file, 'rb') as fp:
           img_data = fp.read()
       msg.add_attachment(img_data, maintype='image',
                                    subtype='png')

   # Send the email via our own SMTP server.
   with smtplib.SMTP('localhost') as s:
       s.send_message(msg)

Aquí hay un ejemplo de cómo enviar todo el contenido de un directorio
como un mensaje de correo electrónico: [1]

   #!/usr/bin/env python3

   """Send the contents of a directory as a MIME message."""

   import os
   import smtplib
   # For guessing MIME type based on file name extension
   import mimetypes

   from argparse import ArgumentParser

   from email.message import EmailMessage
   from email.policy import SMTP

   def main():
       parser = ArgumentParser(description="""\
   Send the contents of a directory as a MIME message.
   Unless the -o option is given, the email is sent by forwarding to your local
   SMTP server, which then does the normal delivery process.  Your local machine
   must be running an SMTP server.
   """)
       parser.add_argument('-d', '--directory',
                           help="""Mail the contents of the specified directory,
                           otherwise use the current directory.  Only the regular
                           files in the directory are sent, and we don't recurse to
                           subdirectories.""")
       parser.add_argument('-o', '--output',
                           metavar='FILE',
                           help="""Print the composed message to FILE instead of
                           sending the message to the SMTP server.""")
       parser.add_argument('-s', '--sender', required=True,
                           help='The value of the From: header (required)')
       parser.add_argument('-r', '--recipient', required=True,
                           action='append', metavar='RECIPIENT',
                           default=[], dest='recipients',
                           help='A To: header value (at least one required)')
       args = parser.parse_args()
       directory = args.directory
       if not directory:
           directory = '.'
       # Create the message
       msg = EmailMessage()
       msg['Subject'] = f'Contents of directory {os.path.abspath(directory)}'
       msg['To'] = ', '.join(args.recipients)
       msg['From'] = args.sender
       msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

       for filename in os.listdir(directory):
           path = os.path.join(directory, filename)
           if not os.path.isfile(path):
               continue
           # Guess the content type based on the file's extension.  Encoding
           # will be ignored, although we should check for simple things like
           # gzip'd or compressed files.
           ctype, encoding = mimetypes.guess_file_type(path)
           if ctype is None or encoding is not None:
               # No guess could be made, or the file is encoded (compressed), so
               # use a generic bag-of-bits type.
               ctype = 'application/octet-stream'
           maintype, subtype = ctype.split('/', 1)
           with open(path, 'rb') as fp:
               msg.add_attachment(fp.read(),
                                  maintype=maintype,
                                  subtype=subtype,
                                  filename=filename)
       # Now send or store the message
       if args.output:
           with open(args.output, 'wb') as fp:
               fp.write(msg.as_bytes(policy=SMTP))
       else:
           with smtplib.SMTP('localhost') as s:
               s.send_message(msg)

   if __name__ == '__main__':
       main()

Aquí hay un ejemplo de cómo descomprimir un mensaje MIME como el
anterior, en un directorio de archivos:

   #!/usr/bin/env python3

   """Unpack a MIME message into a directory of files."""

   import os
   import email
   import mimetypes

   from email.policy import default

   from argparse import ArgumentParser

   def main():
       parser = ArgumentParser(description="""\
   Unpack a MIME message into a directory of files.
   """)
       parser.add_argument('-d', '--directory', required=True,
                           help="""Unpack the MIME message into the named
                           directory, which will be created if it doesn't already
                           exist.""")
       parser.add_argument('msgfile')
       args = parser.parse_args()

       with open(args.msgfile, 'rb') as fp:
           msg = email.message_from_binary_file(fp, policy=default)

       try:
           os.mkdir(args.directory)
       except FileExistsError:
           pass

       counter = 1
       for part in msg.walk():
           # multipart/* are just containers
           if part.get_content_maintype() == 'multipart':
               continue
           # Applications should really sanitize the given filename so that an
           # email message can't be used to overwrite important files
           filename = part.get_filename()
           if not filename:
               ext = mimetypes.guess_extension(part.get_content_type())
               if not ext:
                   # Use a generic bag-of-bits extension
                   ext = '.bin'
               filename = f'part-{counter:03d}{ext}'
           counter += 1
           with open(os.path.join(args.directory, filename), 'wb') as fp:
               fp.write(part.get_payload(decode=True))

   if __name__ == '__main__':
       main()

Aquí hay un ejemplo de cómo crear un mensaje HTML con una versión
alternativa de texto sin formato. Para hacer las cosas un poco más
interesantes, incluimos una imagen relacionada en la parte html, y
guardamos una copia de lo que vamos a enviar en el disco, además de
enviarlo.

   #!/usr/bin/env python3

   import smtplib

   from email.message import EmailMessage
   from email.headerregistry import Address
   from email.utils import make_msgid

   # Create the base text message.
   msg = EmailMessage()
   msg['Subject'] = "Pourquoi pas des asperges pour ce midi ?"
   msg['From'] = Address("Pepé Le Pew", "pepe", "example.com")
   msg['To'] = (Address("Penelope Pussycat", "penelope", "example.com"),
                Address("Fabrette Pussycat", "fabrette", "example.com"))
   msg.set_content("""\
   Salut!

   Cette recette [1] sera sûrement un très bon repas.

   [1] http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718

   --Pepé
   """)

   # Add the html version.  This converts the message into a multipart/alternative
   # container, with the original text message as the first part and the new html
   # message as the second part.
   asparagus_cid = make_msgid()
   msg.add_alternative("""\
   <html>
     <head></head>
     <body>
       <p>Salut!</p>
       <p>Cette
           <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718">
               recette
           </a> sera sûrement un très bon repas.
       </p>
       <img src="cid:{asparagus_cid}">
     </body>
   </html>
   """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
   # note that we needed to peel the <> off the msgid for use in the html.

   # Now add the related image to the html part.
   with open("roasted-asparagus.jpg", 'rb') as img:
       msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                        cid=asparagus_cid)

   # Make a local copy of what we are going to send.
   with open('outgoing.msg', 'wb') as f:
       f.write(bytes(msg))

   # Send the message via local SMTP server.
   with smtplib.SMTP('localhost') as s:
       s.send_message(msg)

Si nos enviaron el mensaje del último ejemplo, aquí hay una forma en
que podríamos procesarlo:

   import os
   import sys
   import tempfile
   import mimetypes
   import webbrowser

   # Import the email modules we'll need
   from email import policy
   from email.parser import BytesParser

   def magic_html_parser(html_text, partfiles):
       """Return safety-sanitized html linked to partfiles.

       Rewrite the href="cid:...." attributes to point to the filenames in partfiles.
       Though not trivial, this should be possible using html.parser.
       """
       raise NotImplementedError("Add the magic needed")

   # In a real program you'd get the filename from the arguments.
   with open('outgoing.msg', 'rb') as fp:
       msg = BytesParser(policy=policy.default).parse(fp)

   # Now the header items can be accessed as a dictionary, and any non-ASCII will
   # be converted to unicode:
   print('To:', msg['to'])
   print('From:', msg['from'])
   print('Subject:', msg['subject'])

   # If we want to print a preview of the message content, we can extract whatever
   # the least formatted payload is and print the first three lines.  Of course,
   # if the message has no plain text part printing the first three lines of html
   # is probably useless, but this is just a conceptual example.
   simplest = msg.get_body(preferencelist=('plain', 'html'))
   print()
   print(''.join(simplest.get_content().splitlines(keepends=True)[:3]))

   ans = input("View full message?")
   if ans.lower()[0] == 'n':
       sys.exit()

   # We can extract the richest alternative in order to display it:
   richest = msg.get_body()
   partfiles = {}
   if richest['content-type'].maintype == 'text':
       if richest['content-type'].subtype == 'plain':
           for line in richest.get_content().splitlines():
               print(line)
           sys.exit()
       elif richest['content-type'].subtype == 'html':
           body = richest
       else:
           print("Don't know how to display {}".format(richest.get_content_type()))
           sys.exit()
   elif richest['content-type'].content_type == 'multipart/related':
       body = richest.get_body(preferencelist=('html'))
       for part in richest.iter_attachments():
           fn = part.get_filename()
           if fn:
               extension = os.path.splitext(part.get_filename())[1]
           else:
               extension = mimetypes.guess_extension(part.get_content_type())
           with tempfile.NamedTemporaryFile(suffix=extension, delete=False) as f:
               f.write(part.get_content())
               # again strip the <> to go from email form of cid to html form.
               partfiles[part['content-id'][1:-1]] = f.name
   else:
       print("Don't know how to display {}".format(richest.get_content_type()))
       sys.exit()
   with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
       f.write(magic_html_parser(body.get_content(), partfiles))
   webbrowser.open(f.name)
   os.remove(f.name)
   for fn in partfiles.values():
       os.remove(fn)

   # Of course, there are lots of email messages that could break this simple
   # minded program, but it will handle the most common ones.

Hasta el aviso, el resultado de lo anterior es:

   To: Penelope Pussycat <penelope@example.com>, Fabrette Pussycat <fabrette@example.com>
   From: Pepé Le Pew <pepe@example.com>
   Subject: Pourquoi pas des asperges pour ce midi ?

   Salut!

   Cette recette [1] sera sûrement un très bon repas.

-[ Notas al pie ]-

[1] Gracias a *Matthew Dixon Cowles* por la inspiración y ejemplos
    originales.
