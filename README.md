# webviewer
## Installation
1. First go to the checkout and run
``python setup.py rcc``
to compile ``main.qml`` into a python module.

2. For an editable (develeoper) installations, install with
``pip install --user -e [path to checked out repository]``
Alternatively, for a nornal installation, run without ``-e``.


## Run
From the command line, run as ``python3 -m webviewer.main [URL]``
