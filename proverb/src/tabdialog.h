#ifndef TABDIALOG_H
#define TABDIALOG_H
#include <QDialog>
#include "ui_about.h"

class About : public QDialog, private Ui::aboutDialog
{
    Q_OBJECT
public:
    About(const QString &fileName, QWidget *parent = 0);
private:
};

#endif
