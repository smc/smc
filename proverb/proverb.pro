TEMPLATE = app
QT = gui \
    core
CONFIG += qt \
    release \
    warn_on \
    console
DESTDIR = bin
OBJECTS_DIR = build
MOC_DIR = build
UI_DIR = build
FORMS = ui/mainwindow.ui \
    ui/about.ui
HEADERS = src/mainwindow.h \
    src/tabdialog.h
SOURCES = src/mainwindow.cpp \
    src/main.cpp \
    src/tabdialog.cpp
RESOURCES += icons.qrc
TRANSLATIONS += proverb_ml.ts
OTHER_FILES += 
#QMAKE_LFLAGS += -static