# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 5.14.1
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x02\xf6\
i\
mport QtQuick 2.\
14\x0aimport QtQuic\
k.Controls 2.14\x0a\
import QtQuick.L\
ayouts 1.14\x0a\x0a\x0aDi\
alog {\x0a    prope\
rty string origi\
n: \x22origin\x22\x0a    \
property int fea\
ture: -1\x0a\x0a    ti\
tle: qsTr(\x22Featu\
re request\x22)\x0a   \
 modal: true\x0a   \
 standardButtons\
: Dialog.Yes | D\
ialog.No\x0a\x0a    pr\
operty var featu\
reRequestNames: \
[qsTr(\x22geolocati\
on\x22),\x0a        qs\
Tr(\x22audio captur\
e\x22),\x0a        qsT\
r(\x22video capture\
\x22),\x0a        qsTr\
(\x22audio and vide\
o capture\x22),\x0a   \
     qsTr(\x22deskt\
op video capture\
\x22),\x0a        qsTr\
(\x22desktop audio \
and video captur\
e\x22),\x0a        qsT\
r(\x22notifications\
\x22)]\x0a\x0a    RowLayo\
ut {\x0a        anc\
hors.fill: paren\
t\x0a\x0a        Label\
 {\x0a            t\
ext: \x22The site \x22\
 + origin + \x22 is\
 requesting \x22\x0a  \
                \
+ \x22access for:\x5cn\
\x22\x0a              \
    + featureReq\
uestNames[featur\
e]\x0a        }\x0a   \
 }\x0a}\x0a\
\x00\x00\x06p\
i\
mport QtQuick 2.\
14\x0aimport QtQuic\
k.Window 2.14\x0aim\
port QtWebEngine\
 1.10\x0aimport Qt.\
labs.platform 1.\
1\x0aimport Qt.labs\
.settings 1.0\x0a\x0a\x0a\
Window {\x0a    id:\
 window\x0a    visi\
ble: true\x0a    wi\
dth: 1280\x0a    he\
ight: 800\x0a    \x0a \
   title: webEng\
ineView.title\x0a\x0a \
   Settings {\x0a  \
      category: \
\x22window\x22\x0a\x0a      \
  property alias\
 x: window.x\x0a   \
     property al\
ias y: window.y\x0a\
        property\
 alias width: wi\
ndow.width\x0a     \
   property alia\
s height: window\
.height\x0a    }\x0a  \
  \x0a    WebEngine\
View {\x0a        i\
d: webEngineView\
\x0a        anchors\
.fill: parent\x0a  \
      url: websi\
te\x0a\x0a        onFe\
aturePermissionR\
equested: {\x0a    \
        featureP\
ermissionDialog.\
origin = securit\
yOrigin.toString\
()\x0a            f\
eaturePermission\
Dialog.feature =\
 feature\x0a       \
     featurePerm\
issionDialog.ope\
n()\x0a        }\x0a  \
  }\x0a\x0a    Feature\
PermissionDialog\
 {\x0a        id: f\
eaturePermission\
Dialog\x0a        a\
nchors.centerIn:\
 parent\x0a\x0a       \
 onAccepted: {\x0a \
           webEn\
gineView.grantFe\
aturePermission(\
origin, feature,\
 true)\x0a        }\
\x0a\x0a        onReje\
cted: {\x0a        \
    webEngineVie\
w.grantFeaturePe\
rmission(origin,\
 feature, false)\
\x0a        }\x0a    }\
\x0a    \x0a    System\
TrayIcon {\x0a     \
   visible: true\
\x0a        icon.so\
urce: webEngineV\
iew.icon\x0a\x0a      \
  menu: Menu {\x0a \
           MenuI\
tem {\x0a          \
      text: qsTr\
(\x22Show window\x22)\x0a\
                \
onTriggered: {\x0a \
                \
   window.show()\
\x0a               \
     window.rais\
e()\x0a            \
    }\x0a          \
  }\x0a            \
MenuItem {\x0a     \
           text:\
 qsTr(\x22Hide wind\
ow\x22)\x0a           \
     onTriggered\
: window.hide()\x0a\
            }\x0a  \
          MenuIt\
em {\x0a           \
     text: qsTr(\
\x22Quit\x22)\x0a        \
        onTrigge\
red: Qt.quit()\x0a \
           }\x0a   \
     }\x0a    }\x0a}\x0a\
"

qt_resource_name = b"\
\x00\x1b\
\x0c/\xbc\xbc\
\x00F\
\x00e\x00a\x00t\x00u\x00r\x00e\x00P\x00e\x00r\x00m\x00i\x00s\x00s\x00i\x00o\x00n\
\x00D\x00i\x00a\x00l\x00o\x00g\x00.\x00q\x00m\x00l\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00<\x00\x00\x00\x00\x00\x01\x00\x00\x02\xfa\
\x00\x00\x01o\xfc\xd0\xac\xdc\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01o\xfc\xcf\x9c\x85\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
