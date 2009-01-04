/*
 	Copyright (c) 2008-2009 Santhosh Thottingal <santhosh.thottingal@gmail.com>
	Copyright (c) 2008-2009 Praveen Arimbrathodiyil <pravi.a@gmail.com>
 
    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Library General Public
    License as published by the Free Software Foundation; either
    version 2 of the License, or (at your option) any later version.
 
    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Library General Public License for more details.
 
    You should have received a copy of the GNU Library General Public License
    along with this library; see the file COPYING.LIB.  If not, write to
    the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
    Boston, MA 02110-1301, USA.
*/

// Derived indic kde calendar class

#include "kcalendarsystemindic.h"

#include "kdebug.h"
#include "klocale.h"
#include <math.h>
#include <QtCore/QDate>
#include <QtCore/QCharRef>
class KCalendarSystemSaka{
//-------------------------------------------------------------------------
// The only practical difference from a Gregorian calendar is that years
// are numbered since the Saka Era.  A couple of overrides will
// take care of that....
//-------------------------------------------------------------------------

// Starts in 78 AD, 
private:
	static const int SAKA_ERA_START = 78;
	// The Saka year starts 80 days later than the Gregorian year.
	static const int SAKA_YEAR_START = 80;
public:
	static int get_era_start(void) { return SAKA_ERA_START; }	
	static int get_year_start(void) { return SAKA_YEAR_START; }	
        static double gregorianToJD(int year, int month, int date);
	static int getMonthLength(int greg_year, int greg_month);
        static double SakaToJD(int year, int month, int date);

};
int KCalendarSystemSaka::getMonthLength(int greg_year, int greg_month)
{
}
/*
 * This routine converts an Indian date to the corresponding Julian date"
 * year   The year in Saka Era according to Indian calendar.
 * month  The month according to Indian calendar (between 1 to 12)
 * date   The date in month 
 */
 double KCalendarSystemSaka::gregorianToJD(int year, int month, int date) {
	QDate qdate(year,month,date);
	return qdate.toJulianDay();
 }
 double KCalendarSystemSaka::SakaToJD(int year, int month, int date) {
	int leapMonth, gyear, m;
	double start, jd;

	gyear = year + get_era_start();


	if(QDate::isLeapYear(gyear)) {
		leapMonth = 31;
		start = gregorianToJD(gyear, 3, 21);
	} else {
		leapMonth = 30;
		start = gregorianToJD(gyear, 3, 22);
	}

	if (month == 1) {
		jd = start + (date - 1);
	} else {
		jd = start + leapMonth;
		m = month - 2;
		m= (m<5) ? m : 5;
		jd += m * 31;
		if (month >= 8) {
			m = month - 7;
			jd += m * 30;
		}
		jd += date - 1;
	}

	return jd;
}


KCalendarSystemIndic::KCalendarSystemIndic( const KLocale * locale )
                         : KCalendarSystem( locale ), d( 0 )
{
}

KCalendarSystemIndic::~KCalendarSystemIndic()
{
}

QString KCalendarSystemIndic::calendarType() const
{
    return QLatin1String( "indic" );
}

QDate KCalendarSystemIndic::epoch() const
{
    return QDate::fromJulianDay( 1721426 );
}

QDate KCalendarSystemIndic::earliestValidDate() const
{
    return QDate::fromJulianDay( 1 );
}

QDate KCalendarSystemIndic::latestValidDate() const
{
    // Set to last day of year 9999 until confirm date formats & widets support > 9999
    // In Indic this is 9999-12-31, which is  is jd 5373484
    // Can't call setDate( 9999, 12, 31 ) as it creates circular reference!
    return QDate::fromJulianDay( 5373484 );
}

bool KCalendarSystemIndic::isValid( int year, int month, int day ) const
{
    // Limit to max year 9999 for now, QDate allows to be greater
    if ( year <= 9999 ) {
        return QDate::isValid( year, month, day );
    }

    return false;
}

bool KCalendarSystemIndic::isValid( const QDate &date ) const
{
    return KCalendarSystem::isValid( date );
}

bool KCalendarSystemIndic::setDate( QDate &date, int year, int month, int day ) const
{
    return KCalendarSystem::setDate( date, year, month, day );
}

// Deprecated
bool KCalendarSystemIndic::setYMD( QDate &date, int y, int m, int d ) const
{
    return KCalendarSystem::setDate( date, y, m, d );
}

int KCalendarSystemIndic::year( const QDate &date ) const
{
    // Saka Year lags behind Gregorian Year by 80 days.
    // Saka Year starts on March 22 normally and
    // on March 21 in leap years.

    int saka_year, saka_start=22;
    saka_year = KCalendarSystem::year( date ) - KCalendarSystemSaka::get_era_start();
    if (KCalendarSystem::isLeapYear(date.year())) {
    	saka_start=21;
    }
    if ((date.month() <=3) && (date.day() < saka_start)) {
    	--saka_year;
    }

    return saka_year;
}

int KCalendarSystemIndic::month( const QDate &date ) const
{
	int month, day;
	// It is based on the table from wikipedia
	int Saka[12][2] = 
	{{11,21},{12,20},{1, 22},{2,21},{3,22},{4,22},{5,23},{6,23},{7,23},{8,23},{9,22},{10,22}};
	  
	month=KCalendarSystem::month( date );
	day=KCalendarSystem::day( date );

	// In a Leap Year Chaithram starts in March 21

	if (KCalendarSystem::isLeapYear(date.year()))
		Saka[2][1]=21;
	
	// We need to handle days before Jan 21 separately.
	if (month > 1 ) {
		if (day > Saka[month-1][1])
			return Saka[month-1][0];
		return Saka[month-2][0];
	}
	if (day > Saka[month-1][1])
		return Saka[month-1][0];
	return Saka[11][0];
}

int KCalendarSystemIndic::day( const QDate &date ) const
{
    double jdAtStartOfGregYear;
    int leapMonth, IndianYear, yday, sakaMonth, sakaDayOfMonth, mday;
    int sakaYear =  KCalendarSystemIndic::year(date);        // Year in Saka era
    jdAtStartOfGregYear = KCalendarSystemSaka::gregorianToJD( date.year(), 1, 1); // JD at start of Gregorian year
    double julianDay=KCalendarSystemSaka::gregorianToJD( date.year(),  date.month(),  date.day());
    yday = (int)(julianDay - jdAtStartOfGregYear);              // Day number in Gregorian year (starting from 0)
    if (yday < KCalendarSystemSaka::get_year_start()) {
    	//  Day is at the end of the preceding Saka year
	sakaYear -= 1;
	leapMonth = KCalendarSystem::isLeapYear(date.year() - 1) ? 31 : 30; // Days in leapMonth this year, previous Gregorian year
	yday += leapMonth + (31 * 5) + (30 * 3) + 10;
    } else {
    	leapMonth = KCalendarSystem::isLeapYear(date.year()) ? 31 : 30; // Days in leapMonth this year
	yday -= KCalendarSystemSaka::get_year_start();
    }
    if (yday < leapMonth) {
    	sakaMonth = 0;
	sakaDayOfMonth = yday + 1;
    } else {
    	mday = yday - leapMonth;
                if (mday < (31 * 5)) {
                        sakaMonth = (int)floor(mday / 31) + 1;
                        sakaDayOfMonth = (mday % 31) + 1;
                } else {
                        mday -= 31 * 5;
			sakaMonth = (int)floor(mday / 30) + 6;
                        sakaDayOfMonth = (mday % 30) + 1;
                }
        }
    return sakaDayOfMonth;
}

QDate KCalendarSystemIndic::addYears( const QDate &date, int nyears ) const
{
    QDate result = date;
    int y = year( date ) + nyears;
    setYMD( result, y, month( date ), day( date ) );
    return result;
}

QDate KCalendarSystemIndic::addMonths( const QDate &date, int nmonths ) const
{
QDate result = date;

    while ( nmonths > 0 ) {
        result = addDays( result, daysInMonth( result ) );
        --nmonths;
    }

    while ( nmonths < 0 ) {
        // get the number of days in the previous month to be consistent with
        // addMonths where nmonths > 0
        int nDaysInMonth = daysInMonth( addDays( result, -day( result ) ) );
        result = addDays( result, -nDaysInMonth );
        ++nmonths;
    }

    return result;
}

QDate KCalendarSystemIndic::addDays( const QDate &date, int ndays ) const
{
    return KCalendarSystem::addDays( date, ndays );
}

int KCalendarSystemIndic::monthsInYear( const QDate &date ) const
{
    Q_UNUSED( date )
    return 12;
}

int KCalendarSystemIndic::weeksInYear( const QDate &date ) const
{
    return KCalendarSystem::weeksInYear( date );
}

int KCalendarSystemIndic::weeksInYear( int year ) const
{
    return KCalendarSystem::weeksInYear( year );
}

int KCalendarSystemIndic::daysInYear( const QDate &date ) const
{
    return KCalendarSystem::daysInYear( date );
}

int KCalendarSystemIndic::daysInMonth( const QDate &date ) const
{
	int month, day;
	month=date.month();
	day=date.day();
	if (month > 6)
		return 30;
	if (month>1)
		return 31;
	if (KCalendarSystem::isLeapYear(date.year()))
		return 31;
	return 30;
}

int KCalendarSystemIndic::daysInWeek( const QDate &date ) const
{
    Q_UNUSED( date );
    return 7;
}

int KCalendarSystemIndic::dayOfYear( const QDate &date ) const
{
QDate first;
    setYMD( first, year( date ), 1, 1 );

    return first.daysTo( date ) + 1;

}

int KCalendarSystemIndic::dayOfWeek( const QDate &date ) const
{
    return KCalendarSystem::dayOfWeek( date );
}

int KCalendarSystemIndic::weekNumber( const QDate &date, int * yearNum ) const
{
    return KCalendarSystem::weekNumber( date, yearNum );
}

bool KCalendarSystemIndic::isLeapYear( int year ) const
{
    return QDate::isLeapYear( year );
}

bool KCalendarSystemIndic::isLeapYear( const QDate &date ) const
{
    return KCalendarSystem::isLeapYear( date );
}

QString KCalendarSystemIndic::monthName( int month, int year, MonthNameFormat format ) const
{
    Q_UNUSED( year );

    if ( format == ShortNamePossessive ) {
        switch ( month ) {
        case 1:
            return ki18nc( "of Chaitra",   "of Chaitra" ).toString( locale() );
        case 2:
            return ki18nc( "of Vaisakha",  "of Vaisakha" ).toString( locale() );
        case 3:
            return ki18nc( "of Jyaistha",     "of Jyaistha" ).toString( locale() );
        case 4:
            return ki18nc( "of Asadha",     "of Asadha" ).toString( locale() );
        case 5:
            return ki18nc( "of Sravana", "of Sravana" ).toString( locale() );
        case 6:
            return ki18nc( "of Bhadra",      "of Bhadra" ).toString( locale() );
        case 7:
            return ki18nc( "of Asvina",      "of Asvina" ).toString( locale() );
        case 8:
            return ki18nc( "of Kartika",    "of Kartika" ).toString( locale() );
        case 9:
            return ki18nc( "of Agrahayana", "of Agrahayana" ).toString( locale() );
        case 10:
            return ki18nc( "of Pausa",   "of Pausa" ).toString( locale() );
        case 11:
            return ki18nc( "of Magha",  "of Magha" ).toString( locale() );
        case 12:
            return ki18nc( "of Phalguna",  "of Phalguna" ).toString( locale() );
        default:
            return QString();
        }
    }

    if ( format == LongNamePossessive ) {
        switch ( month ) {
        case 1:
            return ki18n( "of Chaitra" ).toString( locale() );
        case 2:
            return ki18n( "of Vaisakha" ).toString( locale() );
        case 3:
            return ki18n( "of Jyaistha" ).toString( locale() );
        case 4:
            return ki18n( "of Asadha" ).toString( locale() );
        case 5:
            return ki18n( "of Sravana" ).toString( locale() );
        case 6:
            return ki18n( "of Bhadra" ).toString( locale() );
        case 7:
            return ki18n( "of Asvina" ).toString( locale() );
        case 8:
            return ki18n( "of Kartika" ).toString( locale() );
        case 9:
            return ki18n( "of Agrahayana" ).toString( locale() );
        case 10:
            return ki18n( "of Pausa" ).toString( locale() );
        case 11:
            return ki18n( "of Magha" ).toString( locale() );
        case 12:
            return ki18n( "of Phalguna" ).toString( locale() );
        default:
            return QString();
        }
    }

    if ( format == ShortName ) {
        switch ( month ) {
        case 1:
            return ki18nc( "Chaitra", "Chai" ).toString( locale() );
        case 2:
            return ki18nc( "Vaisakha", "Vai" ).toString( locale() );
        case 3:
            return ki18nc( "Jyaishtha", "Jyai" ).toString( locale() );
        case 4:
            return ki18nc( "Asadha", "Asa" ).toString( locale() );
        case 5:
            return ki18nc( "Sravana", "Sra" ).toString( locale() );
        case 6:
            return ki18nc( "Bhadra", "Bha" ).toString( locale() );
        case 7:
            return ki18nc( "Asvina", "Asvi" ).toString( locale() );
        case 8:
            return ki18nc( "Kartika", "Kar" ).toString( locale() );
        case 9:
            return ki18nc( "Agrahayana", "Agra" ).toString( locale() );
        case 10:
            return ki18nc( "Pausa", "Pausha" ).toString( locale() );
        case 11:
            return ki18nc( "Magha", "Magha" ).toString( locale() );
        case 12:
            return ki18nc( "Phalguna", "Phal" ).toString( locale() );
        default:
            return QString();
        }
    }

    // Default to LongName
    switch ( month ) {
    case 1:
        return ki18n( "Chaitra" ).toString( locale() );
    case 2:
        return ki18n( "Vaisakha" ).toString( locale() );
    case 3:
        return ki18n( "Jyaishtha" ).toString( locale() );
    case 4:
        return ki18n( "Asadha" ).toString( locale() );
    case 5:
        return ki18n( "Sravana" ).toString( locale() );
    case 6:
        return ki18n( "Bhadra" ).toString( locale() );
    case 7:
        return ki18n( "Asvina" ).toString( locale() );
    case 8:
        return ki18n( "Kartika" ).toString( locale() );
    case 9:
        return ki18n( "Agrahayana" ).toString( locale() );
    case 10:
        return ki18n( "Pausha" ).toString( locale() );
    case 11:
        return ki18n( "Magha" ).toString( locale() );
    case 12:
        return ki18n( "Phalguna" ).toString( locale() );
    default:
        return QString();
    }
}

QString KCalendarSystemIndic::monthName( const QDate &date, MonthNameFormat format ) const
{
    return KCalendarSystem::monthName( date, format );
}


QString KCalendarSystemIndic::weekDayName( int weekDay, WeekDayNameFormat format ) const
{
    if ( format == ShortDayName ) {
        switch ( weekDay ) {
        case 1:  return ki18nc( "Somvar",    "Som" ).toString( locale() );
        case 2:  return ki18nc( "Mangalvar",   "Mangal" ).toString( locale() );
        case 3:  return ki18nc( "Budhavar", "Budha" ).toString( locale() );
        case 4:  return ki18nc( "Brihaspativar",  "Briha" ).toString( locale() );
        case 5:  return ki18nc( "Shukravar",    "Shukra" ).toString( locale() );
        case 6:  return ki18nc( "Shanivar",  "Shani" ).toString( locale() );
        case 7:  return ki18nc( "Ravivar",    "Ravi" ).toString( locale() );
        default: return QString();
        }
    }

    switch ( weekDay ) {
    case 1:  return ki18n( "Somvar" ).toString( locale() );
    case 2:  return ki18n( "Mangalvar" ).toString( locale() );
    case 3:  return ki18n( "Budhavar" ).toString( locale() );
    case 4:  return ki18n( "Brihaspativar" ).toString( locale() );
    case 5:  return ki18n( "Shukravar" ).toString( locale() );
    case 6:  return ki18n( "Shanivar" ).toString( locale() );
    case 7:  return ki18n( "Ravivar" ).toString( locale() );
    default: return QString();
    }
}

QString KCalendarSystemIndic::weekDayName( const QDate &date, WeekDayNameFormat format ) const
{
    return KCalendarSystem::weekDayName( date, format );
}

QString KCalendarSystemIndic::yearString( const QDate &pDate, StringFormat format ) const
{
    return KCalendarSystem::yearString( pDate, format );
}

QString KCalendarSystemIndic::monthString( const QDate &pDate, StringFormat format ) const
{
    return KCalendarSystem::monthString( pDate, format );
}

QString KCalendarSystemIndic::dayString( const QDate &pDate, StringFormat format ) const
{
    return KCalendarSystem::dayString( pDate, format );
}

int KCalendarSystemIndic::yearStringToInteger( const QString &sNum, int &iLength ) const
{
    return KCalendarSystem::yearStringToInteger( sNum, iLength );
}

int KCalendarSystemIndic::monthStringToInteger( const QString &sNum, int &iLength ) const
{
    return KCalendarSystem::monthStringToInteger( sNum, iLength );
}

int KCalendarSystemIndic::dayStringToInteger( const QString &sNum, int &iLength ) const
{
    return KCalendarSystem::dayStringToInteger( sNum, iLength );
}

QString KCalendarSystemIndic::formatDate( const QDate &date, KLocale::DateFormat format ) const
{
    return KCalendarSystem::formatDate( date, format );
}

QDate KCalendarSystemIndic::readDate( const QString &str, bool *ok ) const
{
    return KCalendarSystem::readDate( str, ok );
}

QDate KCalendarSystemIndic::readDate( const QString &intstr, const QString &fmt, bool *ok ) const
{
    return KCalendarSystem::readDate( intstr, fmt, ok );
}

QDate KCalendarSystemIndic::readDate( const QString &str, KLocale::ReadDateFlags flags, bool *ok ) const
{
    return KCalendarSystem::readDate( str, flags, ok );
}

int KCalendarSystemIndic::weekStartDay() const
{
    return KCalendarSystem::weekStartDay();
}

int KCalendarSystemIndic::weekDayOfPray() const
{
    return 7; // sunday
}

bool KCalendarSystemIndic::isLunar() const
{
    return false;
}

bool KCalendarSystemIndic::isLunisolar() const
{
    return false;
}

bool KCalendarSystemIndic::isSolar() const
{
    return true;
}

bool KCalendarSystemIndic::isProleptic() const
{
    return false;
}

bool KCalendarSystemIndic::julianDayToDate( int jd, int &year, int &month, int &day ) const
{
    QDate date = QDate::fromJulianDay( jd );

    if ( date.isValid() ) {
        year = date.year();
        month = date.month();
        day = date.day();
    }

    return date.isValid();
}

bool KCalendarSystemIndic::dateToJulianDay( int year, int month, int day, int &jd ) const
{
    QDate date;

    if ( date.setDate( year, month, day ) ) {
        jd = date.toJulianDay();
        return true;
    }

    return false;
}
