#include "mainwindow.h"
#include <QProcess>
#include <iostream>
#include <QTemporaryFile>
#include <QTranslator>
#include <QtDebug>
#include <QString>
#include <QMessageBox>
//
QString tempFileName;
MainWindow::MainWindow( QWidget * parent, Qt::WFlags f) : QMainWindow(parent, f)
{
    setupUi(this);
    connect(getButton, SIGNAL(clicked()), this, SLOT(getProverb()));
    //connect(getButton, SIGNAL(returnPressed()), this, SLOT(getProverb()));
    connect(aboutButton, SIGNAL(clicked()), this, SLOT(about()));
    QTemporaryFile tempFile;
    if (tempFile.open())
    {
        tempFileName = tempFile.fileName();
        qDebug()<<"Temp file name" <<tempFileName;
    }
    else
        qDebug()<<"Cannot open/create temporary file";
}
//

void MainWindow::getProverb(void)
{
    const char* systemCommand;
    std::string command;
    command = lineEdit->text().toUtf8().data();
    if (command == "")
        command = "fortune fortune-ml"+command+" >"+tempFileName.toUtf8().data();   // തിരയാന്‍ ഒരു വാക്കും തന്നില്ലെങ്കില്‍ ഏതെങ്കിലും പഴഞ്ചൊല്ല് കാണിക്കാനുള്ള വിദ്യ
    else
        command = "fortune fortune-ml -m "+command+" >"+tempFileName.toUtf8().data();
    //std::cout<<command<<"\n";
    systemCommand = command.c_str();
    system(systemCommand);
    loadFile(tempFileName);
}

void MainWindow::loadFile(const QString &fileName)
{
        QFile file(fileName);

        if (!file.open(QFile::ReadOnly | QFile::Text))
                 {
                        qDebug()<<"Cannot open temporary file";
                        return;
                 }
        QTextStream in(&file);
        QApplication::setOverrideCursor(Qt::WaitCursor);
        textEdit->setPlainText(in.readAll());
        QApplication::restoreOverrideCursor();

        QTextDocument *document = textEdit->document();
        QTextCursor highlightCursor(document);
        QTextCursor cursor(document);
        QTextCursor startOfLine(document);
        QTextCursor deletePercentage(document);
        cursor.beginEditBlock();
        QTextCharFormat plainFormat(highlightCursor.charFormat());
        QTextCharFormat colorFormat = plainFormat;
        colorFormat.setFontItalic(true);
        colorFormat.setForeground(Qt::darkBlue);
        while (!deletePercentage.isNull() && !deletePercentage.atEnd())       // % ചിഹ്നം നീക്കാന്‍
        {
             deletePercentage = document->find("%", deletePercentage, QTextDocument::FindWholeWords);
             if (!deletePercentage.isNull())
             {
                 deletePercentage.movePosition(QTextCursor::WordRight, QTextCursor::KeepAnchor);
                 deletePercentage.removeSelectedText();
             }
         }
        while (!startOfLine.isNull() && !startOfLine.atEnd())           // എല്ലാ വരിയുടെയും തുടക്കത്തില്‍ '*  ' ചേര്‍ക്കാന്‍
        {
            startOfLine.movePosition(QTextCursor::StartOfLine);
            startOfLine.insertText("*  ");
            startOfLine.movePosition(QTextCursor::Down);
        }
        while (!highlightCursor.isNull() && !highlightCursor.atEnd())       // ആവശ്യപ്പെട്ട വാക്ക് നീലനിരത്തില്‍ ചരിച്ചെഴുതാന്‍
        {
             highlightCursor = document->find(lineEdit->text(), highlightCursor);
             if (!highlightCursor.isNull())
             {
                 highlightCursor.movePosition(QTextCursor::WordRight, QTextCursor::KeepAnchor);
                 highlightCursor.mergeCharFormat(colorFormat);
             }
         }
        cursor.endEditBlock();
}

void MainWindow::about(void)
{
   /* QMessageBox::about(this, tr("About Kuttans"),
             tr("<h2 align=\"center\"><b>Proverb</h2><p><h4 align=\"center\">GUI for fortune-ml<p><h4 align=\"center\">"));*/
About tabdialog(".");
tabdialog.exec();
}
