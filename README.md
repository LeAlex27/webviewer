# webviewer
This program opens a minimalistic window for displaying a web page.
This can be especially useful for web-based messenger UIs such
as Threema Web or WhatsApp Web among others.

## Installation
A package for arch linux is available in the arch user repository.

1. After checkout, the qml ui files need to be compiled into a
resource file using the qt resouce compiler. Go to the location
of the ``resources.qrc`` file and run:
``pyside6-rcc -g python -o resources.py resources.qrc``.
2. Afterwards run
``pip install --user -e [path to checked out repository]``.

## Run
From the command line, run as ``python -m webviewer [URL]``. A list
of available options can be displayed using the `-h` flag. The
webviewer profile is not persistent. To keep the cache and cookies
use the ``--storage-name <storage name>`` flag. For instance, if you
want webviewer to remember its WhatsApp login, use ``whatsapp_web``
as the storage name. ``--strip-user-agent`` is also useful for websites
that check the browser agent (WhatsApp Web does).
 
