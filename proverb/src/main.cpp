#include <QApplication>
#include <QTranslator>
#include "mainwindow.h"
#include "tabdialog.h"
//
int main(int argc, char ** argv)
{
	QApplication app( argc, argv );

        QTranslator translator;
        translator.load("/usr/bin/proverb_ml");
        app.installTranslator(&translator);

	MainWindow win;
	win.show(); 
	app.connect( &app, SIGNAL( lastWindowClosed() ), &app, SLOT( quit() ) );
	return app.exec();
}
