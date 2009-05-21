#ifndef MAINWINDOW_H
#define MAINWINDOW_H
//
#include <QMainWindow>
#include "ui_mainwindow.h"
#include "tabdialog.h"
//
class MainWindow : public QMainWindow, public Ui::MainWindow
{
Q_OBJECT
public:
	MainWindow( QWidget * parent = 0, Qt::WFlags f = 0 );

private slots:
        void getProverb(void);
        void about(void);

private:
        void loadFile(const QString &fileName);

};
#endif




