# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 5.14.1
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x03l\
i\
mport QtQuick 2.\
14\x0aimport QtQuic\
k.Window 2.14\x0aim\
port QtWebEngine\
 1.10\x0aimport Qt.\
labs.platform 1.\
1\x0a\x0a\x0aWindow {\x0a   \
 id: window\x0a    \
visible: true\x0a  \
  width: 1280\x0a  \
  height: 800\x0a  \
  \x0a    title: we\
bEngineView.titl\
e\x0a    \x0a    WebEn\
gineView {\x0a     \
   id: webEngine\
View\x0a        anc\
hors.fill: paren\
t\x0a        url: w\
ebsite\x0a    }\x0a   \
 \x0a    SystemTray\
Icon {\x0a        v\
isible: true\x0a   \
     icon.source\
: webEngineView.\
icon\x0a\x0a        me\
nu: Menu {\x0a     \
       MenuItem \
{\x0a              \
  text: qsTr(\x22Sh\
ow window\x22)\x0a    \
            onTr\
iggered: {\x0a     \
               w\
indow.show()\x0a   \
                \
 window.raise()\x0a\
                \
}\x0a            }\x0a\
            Menu\
Item {\x0a         \
       text: qsT\
r(\x22Hide window\x22)\
\x0a               \
 onTriggered: wi\
ndow.hide()\x0a    \
        }\x0a      \
      MenuItem {\
\x0a               \
 text: qsTr(\x22Qui\
t\x22)\x0a            \
    onTriggered:\
 Qt.quit()\x0a     \
       }\x0a       \
 }\x0a    }\x0a}\x0a\
"

qt_resource_name = b"\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01o \xc6l\x1f\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
