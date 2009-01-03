/*
 * localetime.cpp
 *
 * Copyright (c) 1999-2003 Hans Petter Bieker <bieker@kde.org>
 * Copyright (c) 2008 John Layt <john@layt.net>
 *
 * Requires the Qt widget libraries, available at no cost at
 * http://www.troll.no/
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */

#include <QCheckBox>
#include <QLabel>
#include <QLayout>
#include <QFormLayout>

#include <QComboBox>
#include <QGroupBox>

#include <KDialog>
#include <KConfig>
#include <KConfigGroup>
#include <KStandardDirs>
#include <KDebug>
#include <KCalendarSystem>

#include "toplevel.h"
#include "localetime.h"
#include "localetime.moc"

class StringPair
{
public:
  QChar storeName;
  QString userName;

  static StringPair find( const QList <StringPair> &list, const QChar &c)
  {
    for ( QList<StringPair>::ConstIterator it = list.begin();
	it != list.end();
	++it )
      if ((*it).storeName==c) return (*it);

    StringPair r;
    return r;
  }

};

/*  Sort the string pairs with qHeapSort in the order we want
    ( relative to the userName value and with "MESCORTO" before "MES" )
    */
bool operator< (const StringPair &p1, const StringPair &p2)
{
  return ! (p1.userName<p2.userName);
}

bool operator<= (const StringPair &p1, const StringPair &p2)
{
  return ! (p1.userName<=p2.userName);
}

bool operator> (const StringPair &p1, const StringPair &p2)
{
  return ! (p1.userName>p2.userName);
}

bool operator>= (const StringPair &p1, const StringPair &p2)
{
  return ! (p1.userName>=p2.userName);
}

StringPair KLocaleConfigTime::buildStringPair(const QChar &c, const QString &s) const
{
  StringPair pair;
  pair.storeName=c;
  pair.userName=s;
  return pair;
}

QList<StringPair> KLocaleConfigTime::timeMap() const
{
  QList < StringPair > list;
  list+=buildStringPair('H',ki18n("HH").toString(m_locale));
  list+=buildStringPair('k',ki18n("hH").toString(m_locale));
  list+=buildStringPair('I',ki18n("PH").toString(m_locale));
  list+=buildStringPair('l',ki18n("pH").toString(m_locale));
  list+=buildStringPair('M',ki18nc("Minute", "MM").toString(m_locale));
  list+=buildStringPair('S',ki18n("SS").toString(m_locale));
  list+=buildStringPair('p',ki18n("AMPM").toString(m_locale));

  qSort( list );

  return list;
}

QList <StringPair> KLocaleConfigTime::dateMap() const
{
  QList < StringPair > list;
  list+=buildStringPair('Y',ki18n("YYYY").toString(m_locale));
  list+=buildStringPair('y',ki18n("YY").toString(m_locale));
  list+=buildStringPair('n',ki18n("mM").toString(m_locale));
  list+=buildStringPair('m',ki18nc("Month", "MM").toString(m_locale));
  list+=buildStringPair('b',ki18n("SHORTMONTH").toString(m_locale));
  list+=buildStringPair('B',ki18n("MONTH").toString(m_locale));
  list+=buildStringPair('e',ki18n("dD").toString(m_locale));
  list+=buildStringPair('d',ki18n("DD").toString(m_locale));
  list+=buildStringPair('a',ki18n("SHORTWEEKDAY").toString(m_locale));
  list+=buildStringPair('A',ki18n("WEEKDAY").toString(m_locale));

  qSort( list );

  return list;
}

QString KLocaleConfigTime::userToStore(const QList<StringPair> & list,
		    const QString & userFormat) const
{
  QString result;

  for ( int pos = 0; pos < userFormat.length(); ++pos )
    {
      bool bFound = false;
      for ( QList<StringPair>::ConstIterator it = list.begin();
	    it != list.end() && !bFound;
	    ++it )
	{
	  QString s = (*it).userName;

	  if ( userFormat.mid( pos, s.length() ) == s )
	    {
	      result += '%';
	      result += (*it).storeName;

	      pos += s.length() - 1;

	      bFound = true;
	    }
	}

      if ( !bFound )
	{
	  QChar c = userFormat.at( pos );
	  if ( c == '%' )
	    result += c;

	  result += c;
	}
    }

  return result;
}

QString KLocaleConfigTime::storeToUser(const QList<StringPair> & list,
				       const QString & storeFormat) const
{
  QString result;

  bool escaped = false;
  for ( int pos = 0; pos < storeFormat.length(); ++pos )
    {
      QChar c = storeFormat.at(pos);
      if ( escaped )
	{
	  StringPair it = StringPair::find( list, c );
	  if ( !it.userName.isEmpty() )
	    result += it.userName;
	  else
	    result += c;

	  escaped = false;
	}
      else if ( c == '%' )
	escaped = true;
      else
	result += c;
    }

  return result;
}

KLocaleConfigTime::KLocaleConfigTime(KLocale *_locale,
				     QWidget *parent)
 : QWidget(parent),
   m_locale(_locale)
{
    // Time

    setupUi(this);

    m_groupFormat->setObjectName( QString() );
    m_groupWeek->setObjectName( QString() );

    labCalendarSystem->setObjectName( I18N_NOOP("Calendar system:") );
    m_comboCalendarSystem->setEditable(false);
    connect(m_comboCalendarSystem, SIGNAL(activated(int)),
      this, SLOT(slotCalendarSystemChanged(int)));
    QStringList tmpCalendars;
    tmpCalendars << QString() << QString();
    m_comboCalendarSystem->addItems(tmpCalendars);

    m_labTimeFmt->setObjectName( I18N_NOOP("Time format:") );
    m_comboTimeFmt->setEditable(true);
    connect( m_comboTimeFmt, SIGNAL( editTextChanged(const QString &) ),
      this, SLOT( slotTimeFmtChanged(const QString &) ) );

    m_labDateFmt->setObjectName( I18N_NOOP("Date format:") );
    m_comboDateFmt->setEditable(true);
    connect( m_comboDateFmt, SIGNAL( editTextChanged(const QString &) ),
      this, SLOT( slotDateFmtChanged(const QString &) ) );

    m_labDateFmtShort->setObjectName( I18N_NOOP("Short date format:") );
    m_comboDateFmtShort->setEditable(true);
    connect( m_comboDateFmtShort, SIGNAL( editTextChanged(const QString &) ),
      this, SLOT( slotDateFmtShortChanged(const QString &) ) );

    m_chDateMonthNamePossessive->setObjectName(I18N_NOOP("Use declined form of month name"));
    connect( m_chDateMonthNamePossessive, SIGNAL(clicked()),
        SLOT(slotDateMonthNamePossChanged()));

    labWeekStartDay->setObjectName( I18N_NOOP("First day of the week:") );
    m_comboWeekStartDay->setEditable(false);
    connect (m_comboWeekStartDay, SIGNAL(activated(int)),
            this, SLOT(slotWeekStartDayChanged(int)));

    labWorkingWeekStartDay->setObjectName( I18N_NOOP("First working day of the week:") );
    m_comboWorkingWeekStartDay->setEditable(false);
    connect (m_comboWorkingWeekStartDay, SIGNAL(activated(int)),
            this, SLOT(slotWorkingWeekStartDayChanged(int)));

    labWorkingWeekEndDay->setObjectName( I18N_NOOP("Last working day of the week:") );
    m_comboWorkingWeekEndDay->setEditable(false);
    connect (m_comboWorkingWeekEndDay, SIGNAL(activated(int)),
            this, SLOT(slotWorkingWeekEndDayChanged(int)));

    labWeekDayOfPray->setObjectName( I18N_NOOP("Day of the week for religious observance:") );
    m_comboWeekDayOfPray->setEditable(false);
    connect (m_comboWeekDayOfPray, SIGNAL(activated(int)),
            this, SLOT(slotWeekDayOfPrayChanged(int)));


    updateWeekDayNames();
}


KLocaleConfigTime::~KLocaleConfigTime()
{
}

void KLocaleConfigTime::save()
{
    KSharedConfig::Ptr config = KGlobal::config();
    KConfigGroup group(config, "Locale");
    KConfig ent(KStandardDirs::locate("locale",
        QString::fromLatin1("l10n/%1/entry.desktop")
        .arg(m_locale->country())));
    ent.setLocale(m_locale->language());
    KConfigGroup entGrp = ent.group("KCM Locale");

    QString str;

    str = entGrp.readEntry("CalendarSystem", QString::fromLatin1("gregorian"));
    group.deleteEntry("CalendarSystem", KConfig::Persistent | KConfig::Global);
    if (str != m_locale->calendarType())
      group.writeEntry("CalendarSystem", m_locale->calendarType(), KConfig::Persistent|KConfig::Global);

    str = entGrp.readEntry("TimeFormat", QString::fromLatin1("%H:%M:%S"));
    group.deleteEntry("TimeFormat", KConfig::Persistent | KConfig::Global);
    if (str != m_locale->timeFormat())
      group.writeEntry("TimeFormat", m_locale->timeFormat(), KConfig::Persistent|KConfig::Global);

    str = entGrp.readEntry("DateFormat", QString::fromLatin1("%A %d %B %Y"));
    group.deleteEntry("DateFormat", KConfig::Persistent | KConfig::Global);
    if (str != m_locale->dateFormat())
      group.writeEntry("DateFormat", m_locale->dateFormat(), KConfig::Persistent|KConfig::Global);

    str = entGrp.readEntry("DateFormatShort", QString::fromLatin1("%Y-%m-%d"));
    group.deleteEntry("DateFormatShort", KConfig::Persistent | KConfig::Global);
    if (str != m_locale->dateFormatShort())
      group.writeEntry("DateFormatShort",
            m_locale->dateFormatShort(), KConfig::Persistent|KConfig::Global);

    int firstDay;
    firstDay = entGrp.readEntry("WeekStartDay", 1);  //default to Monday
    group.deleteEntry("WeekStartDay", KConfig::Persistent | KConfig::Global);
    if (firstDay != m_locale->weekStartDay())
        group.writeEntry("WeekStartDay", m_locale->weekStartDay(), KConfig::Persistent|KConfig::Global);

    int firstWorkingDay;
    firstWorkingDay = entGrp.readEntry("WorkingWeekStartDay", 1);  //default to Monday
    group.deleteEntry("WorkingWeekStartDay", KConfig::Persistent | KConfig::Global);
    if (firstWorkingDay != m_locale->workingWeekStartDay())
        group.writeEntry("WorkingWeekStartDay", m_locale->workingWeekStartDay(), KConfig::Persistent|KConfig::Global);

    int lastWorkingDay;
    lastWorkingDay = entGrp.readEntry("WorkingWeekEndDay", 5);  //default to Friday
    group.deleteEntry("WorkingWeekEndDay", KConfig::Persistent | KConfig::Global);
    if (lastWorkingDay != m_locale->workingWeekEndDay())
        group.writeEntry("WorkingWeekEndDay", m_locale->workingWeekEndDay(), KConfig::Persistent|KConfig::Global);

    int prayDay;
    prayDay = entGrp.readEntry("WeekDayOfPray", 7);  //default to Sunday
    group.deleteEntry("WeekDayOfPray", KConfig::Persistent | KConfig::Global);
    if (prayDay != m_locale->weekDayOfPray())
        group.writeEntry("WeekDayOfPray", m_locale->weekDayOfPray(), KConfig::Persistent|KConfig::Global);

    bool b;
    b = entGrp.readEntry("DateMonthNamePossessive", false);
    group.deleteEntry("DateMonthNamePossessive", KConfig::Persistent | KConfig::Global);
    if (b != m_locale->dateMonthNamePossessive())
        group.writeEntry("DateMonthNamePossessive",
                        m_locale->dateMonthNamePossessive(), KConfig::Persistent|KConfig::Global);

    group.sync();
}

void KLocaleConfigTime::showEvent( QShowEvent *e )
{
    // This option makes sense only for languages where nouns are declined
    if ( !m_locale->nounDeclension() )
        m_chDateMonthNamePossessive->hide();
    QWidget::showEvent( e );
}

void KLocaleConfigTime::slotCalendarSystemChanged(int calendarSystem)
{
    kDebug() << "CalendarSystem: " << calendarSystem;

    typedef QVector<QString> CalendarVector;
    CalendarVector calendars(5);
    calendars[0] = "gregorian";
    calendars[1] = "hijri";
    calendars[2] = "hebrew";
    calendars[3] = "jalali";
    calendars[4] = "indic";

    QString calendarType;
    if( calendarSystem >= calendars.size())
        calendarType = calendars.first();
    else
        calendarType = calendars.at(calendarSystem);

    m_locale->setCalendar(calendarType);

    updateWeekDayNames();
    emit localeChanged();
}

void KLocaleConfigTime::slotLocaleChanged()
{
    typedef QVector<QString> CalendarVector;
    CalendarVector calendars(5);
    calendars[0] = "gregorian";
    calendars[1] = "hijri";
    calendars[2] = "hebrew";
    calendars[3] = "jalali";
    calendars[4] = "indic";

    QString calendarType = m_locale->calendarType();
    int calendarSystem = 0;

    CalendarVector::iterator it = qFind(calendars.begin(), calendars.end(),
        calendarType);
    if ( it != calendars.end() )
        calendarSystem = it - calendars.begin();

    kDebug() << "calSys: " << calendarSystem << ": " << calendarType;
    m_comboCalendarSystem->setCurrentIndex( calendarSystem );

    //  m_edTimeFmt->setText( m_locale->timeFormat() );
    m_comboTimeFmt->setEditText( storeToUser( timeMap(), m_locale->timeFormat() ) );
    // m_edDateFmt->setText( m_locale->dateFormat() );
    m_comboDateFmt->setEditText( storeToUser( dateMap(), m_locale->dateFormat() ) );
    //m_edDateFmtShort->setText( m_locale->dateFormatShort() );
    m_comboDateFmtShort->setEditText( storeToUser( dateMap(), m_locale->dateFormatShort() ) );
    m_comboWeekStartDay->setCurrentIndex( m_locale->weekStartDay() - 1 );
    m_comboWorkingWeekStartDay->setCurrentIndex( m_locale->workingWeekStartDay() - 1 );
    m_comboWorkingWeekEndDay->setCurrentIndex( m_locale->workingWeekEndDay() - 1 );
    m_comboWeekDayOfPray->setCurrentIndex( m_locale->weekDayOfPray() );  // First option is None=0

    if ( m_locale->nounDeclension() )
        m_chDateMonthNamePossessive->setChecked( m_locale->dateMonthNamePossessive() );

    kDebug(173) << "converting: " << m_locale->timeFormat();
    kDebug(173) << storeToUser(timeMap(), m_locale->timeFormat()) << endl;
    kDebug(173) << userToStore(timeMap(), QString::fromLatin1("HH:MM:SS AMPM test")) << endl;

}

void KLocaleConfigTime::slotTimeFmtChanged(const QString &t)
{
  //  m_locale->setTimeFormat(t);
    m_locale->setTimeFormat( userToStore( timeMap(), t ) );

    emit localeChanged();
}

void KLocaleConfigTime::slotDateFmtChanged(const QString &t)
{
    // m_locale->setDateFormat(t);
    m_locale->setDateFormat( userToStore( dateMap(), t ) );
    emit localeChanged();
}

void KLocaleConfigTime::slotDateFmtShortChanged(const QString &t)
{
    //m_locale->setDateFormatShort(t);
    m_locale->setDateFormatShort( userToStore( dateMap(), t ) );
    emit localeChanged();
}

void KLocaleConfigTime::slotWeekStartDayChanged(int firstDay) {
    kDebug(173) << "first day is now: " << firstDay;
    m_locale->setWeekStartDay(m_comboWeekStartDay->currentIndex() + 1);
    emit localeChanged();
}

void KLocaleConfigTime::slotWorkingWeekStartDayChanged(int startDay) {
    kDebug(173) << "first working day is now: " << startDay;
    m_locale->setWorkingWeekStartDay(m_comboWorkingWeekStartDay->currentIndex() + 1);
    emit localeChanged();
}

void KLocaleConfigTime::slotWorkingWeekEndDayChanged(int endDay) {
    kDebug(173) << "last working day is now: " << endDay;
    m_locale->setWorkingWeekEndDay(m_comboWorkingWeekEndDay->currentIndex() + 1);
    emit localeChanged();
}

void KLocaleConfigTime::slotWeekDayOfPrayChanged(int prayDay) {
    kDebug(173) << "day of pray is now: " << prayDay;
    m_locale->setWeekDayOfPray(m_comboWeekDayOfPray->currentIndex());  // First option is None=0
    emit localeChanged();
}

void KLocaleConfigTime::slotDateMonthNamePossChanged()
{
    if (m_locale->nounDeclension())
    {
      m_locale->setDateMonthNamePossessive(m_chDateMonthNamePossessive->isChecked());
      emit localeChanged();
    }
}

void KLocaleConfigTime::slotTranslate()
{
  QString str;

  QString sep = QString::fromLatin1("\n");

  QString old;

  // clear() and insertStringList also changes the current item, so
  // we better use save and restore here..
  old = m_comboTimeFmt->currentText();
  m_comboTimeFmt->clear();
  str = i18nc("some reasonable time formats for the language",
	     "HH:MM:SS\n"
	     "pH:MM:SS AMPM");
  m_comboTimeFmt->addItems(str.split( sep));
  m_comboTimeFmt->setEditText(old);

  old = m_comboDateFmt->currentText();
  m_comboDateFmt->clear();
  str = i18nc("some reasonable date formats for the language",
	     "WEEKDAY MONTH dD YYYY\n"
	     "SHORTWEEKDAY MONTH dD YYYY");
  m_comboDateFmt->addItems(str.split( sep));
  m_comboDateFmt->setEditText(old);

  old = m_comboDateFmtShort->currentText();
  m_comboDateFmtShort->clear();
  str = i18nc("some reasonable short date formats for the language",
	     "YYYY-MM-DD\n"
	     "dD.mM.YYYY\n"
	     "DD.MM.YYYY");
  m_comboDateFmtShort->addItems(str.split( sep));
  m_comboDateFmtShort->setEditText(old);

  updateWeekDayNames();

  while ( m_comboCalendarSystem->count() < 5 )
    m_comboCalendarSystem->addItem(QString());
  m_comboCalendarSystem->setItemText
    (0, ki18nc("Calendar System Gregorian", "Gregorian").toString(m_locale));
  m_comboCalendarSystem->setItemText
    (1, ki18nc("Calendar System Hijri", "Hijri").toString(m_locale));
  m_comboCalendarSystem->setItemText
    (2, ki18nc("Calendar System Hebrew", "Hebrew").toString(m_locale));
  m_comboCalendarSystem->setItemText
    (3, ki18nc("Calendar System Jalali", "Jalali").toString(m_locale));
  m_comboCalendarSystem->setItemText
    (4, ki18nc("Calendar System Indic", "Indic").toString(m_locale));

  str = ki18n
    ("<p>The text in this textbox will be used to format "
     "time strings. The sequences below will be replaced:</p>"
     "<table>"
     "<tr><td><b>HH</b></td><td>The hour as a decimal number using a 24-hour "
     "clock (00-23).</td></tr>"
     "<tr><td><b>hH</b></td><td>The hour (24-hour clock) as a decimal number "
     "(0-23).</td></tr>"
     "<tr><td><b>PH</b></td><td>The hour as a decimal number using a 12-hour "
     "clock (01-12).</td></tr>"
     "<tr><td><b>pH</b></td><td>The hour (12-hour clock) as a decimal number "
     "(1-12).</td></tr>"
     "<tr><td><b>MM</b></td><td>The minutes as a decimal number (00-59)."
     "</td></tr>"
     "<tr><td><b>SS</b></td><td>The seconds as a decimal number (00-59)."
     "</td></tr>"
     "<tr><td><b>AMPM</b></td><td>Either \"am\" or \"pm\" according to the "
     "given time value. Noon is treated as \"pm\" and midnight as \"am\"."
     "</td></tr>"
     "</table>").toString(m_locale);
  m_labTimeFmt->setWhatsThis( str );
  m_comboTimeFmt->setWhatsThis(  str );

  QString datecodes = ki18n(
    "<table>"
    "<tr><td><b>YYYY</b></td><td>The year with century as a decimal number."
    "</td></tr>"
    "<tr><td><b>YY</b></td><td>The year without century as a decimal number "
    "(00-99).</td></tr>"
    "<tr><td><b>MM</b></td><td>The month as a decimal number (01-12)."
    "</td></tr>"
    "<tr><td><b>mM</b></td><td>The month as a decimal number (1-12).</td></tr>"
    "<tr><td><b>SHORTMONTH</b></td><td>The first three characters of the month name. "
    "</td></tr>"
    "<tr><td><b>MONTH</b></td><td>The full month name.</td></tr>"
    "<tr><td><b>DD</b></td><td>The day of month as a decimal number (01-31)."
    "</td></tr>"
    "<tr><td><b>dD</b></td><td>The day of month as a decimal number (1-31)."
    "</td></tr>"
    "<tr><td><b>SHORTWEEKDAY</b></td><td>The first three characters of the weekday name."
    "</td></tr>"
    "<tr><td><b>WEEKDAY</b></td><td>The full weekday name.</td></tr>"
    "</table>").toString(m_locale);

  str = ki18n
    ( "<p>The text in this textbox will be used to format long "
      "dates. The sequences below will be replaced:</p>").toString(m_locale) + datecodes;
  m_labDateFmt->setWhatsThis( str );
  m_comboDateFmt->setWhatsThis(  str );

  str = ki18n
    ( "<p>The text in this textbox will be used to format short "
      "dates. For instance, this is used when listing files. "
      "The sequences below will be replaced:</p>").toString(m_locale) + datecodes;
  m_labDateFmtShort->setWhatsThis( str );
  m_comboDateFmtShort->setWhatsThis(  str );

  str = ki18n
    ("<p>This option determines which day will be considered as "
     "the first one of the week.</p>").toString(m_locale);
  m_comboWeekStartDay->setWhatsThis(  str );

  str = ki18n
    ("<p>This option determines which day will be considered as "
     "the first working day of the week.</p>").toString(m_locale);
  m_comboWorkingWeekStartDay->setWhatsThis(  str );

  str = ki18n
    ("<p>This option determines which day will be considered as "
     "the last working day of the week.</p>").toString(m_locale);
  m_comboWorkingWeekEndDay->setWhatsThis(  str );

  str = ki18n
    ("<p>This option determines which day will be considered as "
     "the day of the week for religious observance.</p>").toString(m_locale);
  m_comboWeekDayOfPray->setWhatsThis(  str );

  if ( m_locale->nounDeclension() )
  {
    str = ki18n
      ("<p>This option determines whether possessive form of month "
       "names should be used in dates.</p>").toString(m_locale);
    m_chDateMonthNamePossessive->setWhatsThis(  str );
  }
}

void KLocaleConfigTime::updateWeekDayNames()
{
  const KCalendarSystem * calendar = m_locale->calendar();
  int daysInWeek = calendar->daysInWeek(QDate::currentDate());
  QString weekDayName = i18nc("Day name list, option for no day of religious observance", "None");

  m_comboWeekStartDay->clear();
  m_comboWorkingWeekStartDay->clear();
  m_comboWorkingWeekEndDay->clear();
  m_comboWeekDayOfPray->clear();

  m_comboWeekDayOfPray->insertItem(0, weekDayName);

  for ( int i = 1; i <= daysInWeek; ++i )
  {
    weekDayName = calendar->weekDayName(i);
    m_comboWeekStartDay->insertItem(i - 1, weekDayName);
    m_comboWorkingWeekStartDay->insertItem(i - 1, weekDayName);
    m_comboWorkingWeekEndDay->insertItem(i - 1, weekDayName);
    m_comboWeekDayOfPray->insertItem(i, weekDayName);
  }

  m_comboWeekStartDay->setCurrentIndex( m_locale->weekStartDay() - 1 );
  m_comboWorkingWeekStartDay->setCurrentIndex( m_locale->workingWeekStartDay() - 1 );
  m_comboWorkingWeekEndDay->setCurrentIndex( m_locale->workingWeekEndDay() - 1 );
  m_comboWeekDayOfPray->setCurrentIndex( m_locale->weekDayOfPray() );  // First option is None=0

}
