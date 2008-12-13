package org.panchanga.indic;
/*
 *******************************************************************************
 * Copyright (C) 1996-2008, International Business Machines Corporation and    *
 * others. All Rights Reserved.                                                *
 *******************************************************************************
 */




/**
 * <code>IndianCalendar</code> is a subclass of <code>GregorianCalendar</code>
 * that numbers years since the birth of the Buddha.  This is the civil calendar
 * which is accepted by government of India as Indian National Calendar. 
 * The two calendars most widely used in India today are the Vikrama calendar 
 * followed in North India and the Shalivahana or Saka calendar which is followed 
 * in South India and Maharashtra.

 * A variant of the Shalivahana Calendar was reformed and standardized as the 
 * Indian National calendar in 1957.
 * <p>
 * Some details of Indian National Calendar (to be implemented) :
 * The Months
 * Month          Length      Start date (Gregorian)
 * =================================================
 * 1 Chaitra      30/31          March 22*
 * 2 Vaisakha     31             April 21
 * 3 Jyaistha     31             May 22
 * 4 Asadha       31             June 22
 * 5 Sravana      31             July 23
 * 6 Bhadra       31             August 23
 * 7 Asvina       30             September 23
 * 8 Kartika      30             October 23
 * 9 Agrahayana   30             November 22
 * 10 Pausa       30             December 22
 * 11 Magha       30             January 21
 * 12 Phalguna    30             February 20

 * In leap years, Chaitra has 31 days and starts on March 21 instead.
 * The leap years of Gregorian calendar and Indian National Calendar are in synchornization. 
 * So When its a leap year in Gregorian calendar then Chaitra has 31 days.
 *
 * The Years
 * Years are counted in the Saka Era, which starts its year 0 in 78AD (by gregorian calendar).
 * So for eg. 9th June 2006 by Gregorian Calendar, is same as 19th of Jyaistha in 1928 of Saka 
 * era by Indian National Calendar.
 * <p>
 * The Indian Calendar has only one allowable era: <code>Saka Era</code>.  If the
 * calendar is not in lenient mode (see <code>setLenient</code>), dates before
 * 1/1/1 Saka Era are rejected with an <code>IllegalArgumentException</code>.
 * <p>
 * This class should not be subclassed.</p>
 * <p>
 * IndianCalendar usually should be instantiated using 
 * {@link com.ibm.icu.util.Calendar#getInstance(ULocale)} passing in a <code>ULocale</code>
 * with the tag <code>"@calendar=Indian"</code>.</p>
 * 
 * @see com.ibm.icu.util.Calendar
 * @see com.ibm.icu.util.GregorianCalendar
 *
 * @stable ICU 3.8
 */
public class SakaCalendar   {
    // jdk1.4.2 serialver
    private static final long serialVersionUID = 3617859668165014834L;

    /** 
     * Constant for Chaitra, the 1st month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int CHAITRA = 0;

    /** 
     * Constant for Vaisakha, the 2nd month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int VAISAKHA = 1;

    /** 
     * Constant for Jyaistha, the 3rd month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int JYAISTHA = 2;

    /** 
     * Constant for Asadha, the 4th month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int ASADHA = 3; 

    /** 
     * Constant for Sravana, the 5th month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int SRAVANA = 4 ;

    /** 
     * Constant for Bhadra, the 6th month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int BHADRA = 5 ;

    /** 
     * Constant for Asvina, the 7th month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int ASVINA = 6 ;

    /** 
     * Constant for Kartika, the 8th month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int KARTIKA = 7 ;

    /** 
     * Constant for Agrahayana, the 9th month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int AGRAHAYANA = 8 ;

    /** 
     * Constant for Pausa, the 10th month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int PAUSA = 9 ;

    /** 
     * Constant for Magha, the 11th month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int MAGHA = 10;

    /** 
     * Constant for Phalguna, the 12th month of the Indian year. 
     * @stable ICU 3.8
     */
    public static final int PHALGUNA = 11;

    //-------------------------------------------------------------------------
    // Constructors...
    //-------------------------------------------------------------------------

    /**
     * Constant for the Indian Era.  This is the only allowable <code>ERA</code>
     * value for the Indian calendar.
     *
     * @see com.ibm.icu.util.Calendar#ERA
     * @stable ICU 3.8
     */
    public static final int IE = 0;





    //-------------------------------------------------------------------------
    // The only practical difference from a Gregorian calendar is that years
    // are numbered since the Saka Era.  A couple of overrides will
    // take care of that....
    //-------------------------------------------------------------------------

    // Starts in 78 AD, 
    private static final int INDIAN_ERA_START = 78;

    // The Indian year starts 80 days later than the Gregorian year.
    private static final int INDIAN_YEAR_START = 80;



    /**
     * {@inheritDoc}
     * @stable ICU 3.8
     */
    protected int handleGetMonthLength(int extendedYear, int month) {
        if (month < 0 || month > 11) {
          
            extendedYear += month/12;// floorDivide(month, 12, remainder);
      
            month =  month%12;
        }

        if(isGregorianLeap(extendedYear + INDIAN_ERA_START) && month == 0) {
            return 31;
        }

        if(month >= 1 && month <=5) {
            return 31;
        }

        return 30;
    }


    private static final int LIMITS[][] = {
        // Minimum  Greatest     Least    Maximum
        //           Minimum   Maximum
        {        0,        0,        0,        0}, // ERA
        { -5000000, -5000000,  5000000,  5000000}, // YEAR
        {        0,        0,       11,       11}, // MONTH
        {        1,        1,       52,       53}, // WEEK_OF_YEAR
        {/*                                   */}, // WEEK_OF_MONTH
        {        1,        1,       30,       31}, // DAY_OF_MONTH
        {        1,        1,      365,      366}, // DAY_OF_YEAR
        {/*                                   */}, // DAY_OF_WEEK
        {       -1,       -1,        5,        5}, // DAY_OF_WEEK_IN_MONTH
        {/*                                   */}, // AM_PM
        {/*                                   */}, // HOUR
        {/*                                   */}, // HOUR_OF_DAY
        {/*                                   */}, // MINUTE
        {/*                                   */}, // SECOND
        {/*                                   */}, // MILLISECOND
        {/*                                   */}, // ZONE_OFFSET
        {/*                                   */}, // DST_OFFSET
        { -5000000, -5000000,  5000000,  5000000}, // YEAR_WOY
        {/*                                   */}, // DOW_LOCAL
        { -5000000, -5000000,  5000000,  5000000}, // EXTENDED_YEAR
        {/*                                   */}, // JULIAN_DAY
        {/*                                   */}, // MILLISECONDS_IN_DAY
    };


    /**
     * {@inheritDoc}
     * @stable ICU 3.8
     */
    protected int handleGetLimit(int field, int limitType) {
        return LIMITS[field][limitType];
    }

 


    /*
     * This routine converts an Indian date to the corresponding Julian date"
     * @param year   The year in Saka Era according to Indian calendar.
     * @param month  The month according to Indian calendar (between 1 to 12)
     * @param date   The date in month 
     */
    private static double IndianToJD(int year, int month, int date) {
        int leapMonth, gyear, m;
        double start, jd;

        gyear = year + INDIAN_ERA_START;


        if(isGregorianLeap(gyear)) {
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
            m = Math.min(m, 5);
            jd += m * 31;
            if (month >= 8) {
                m = month - 7;
                jd += m * 30;
            }
            jd += date - 1;
        }

        return jd;
    }

    /*
     * The following function is not needed for basic calendar functioning.
     * This routine converts a gregorian date to the corresponding Julian date"
     * @param year   The year in standard Gregorian calendar (AD/BC) .
     * @param month  The month according to Gregorian calendar (between 0 to 11)
     * @param date   The date in month 
     */
    private static double gregorianToJD(int year, int month, int date) {
        double JULIAN_EPOCH = 1721425.5;
        double jd = (JULIAN_EPOCH - 1) +
        (365 * (year - 1)) +
        Math.floor((year - 1) / 4) +
        (-Math.floor((year - 1) / 100)) +
        Math.floor((year - 1) / 400) +
        Math.floor((((367 * month) - 362) / 12) +
            ((month <= 2) ? 0 :
                (isGregorianLeap(year) ? -1 : -2)
            ) +
            date);

        return jd;
    }

    /*
     * The following function is not needed for basic calendar functioning.
     * This routine converts a julian day (jd) to the corresponding date in Gregorian calendar"
     * @param jd The Julian date in Julian Calendar which is to be converted to Indian date"
     */
    private static int[] jdToGregorian(double jd) {
        double JULIAN_EPOCH = 1721425.5;
        double wjd, depoch, quadricent, dqc, cent, dcent, quad, dquad, yindex, yearday, leapadj;
        int year, month, day;

        wjd = Math.floor(jd - 0.5) + 0.5;
        depoch = wjd - JULIAN_EPOCH;
        quadricent = Math.floor(depoch / 146097);
        dqc = depoch % 146097;
        cent = Math.floor(dqc / 36524);
        dcent = dqc % 36524;
        quad = Math.floor(dcent / 1461);
        dquad = dcent % 1461;
        yindex = Math.floor(dquad / 365);
        year = (int)((quadricent * 400) + (cent * 100) + (quad * 4) + yindex);

        if (!((cent == 4) || (yindex == 4))) {
            year++;
        }

        yearday = wjd - gregorianToJD(year, 1, 1);
        leapadj = ((wjd < gregorianToJD(year, 3, 1)) ? 0
            :
                (isGregorianLeap(year) ? 1 : 2)
        );

        month = (int)Math.floor((((yearday + leapadj) * 12) + 373) / 367);
        day = (int)(wjd - gregorianToJD(year, month, 1)) + 1;

        int[] julianDate = new int[3];

        julianDate[0] = year;
        julianDate[1] = month;
        julianDate[2] = day;

        return julianDate;
    }

    /*
     * The following function is not needed for basic calendar functioning.
     * This routine checks if the Gregorian year is a leap year"
     * @param year      The year in Gregorian Calendar
     */
    private static boolean isGregorianLeap(int year)
    {
        return ((year % 4) == 0) &&
        (!(((year % 100) == 0) && ((year % 400) != 0)));
    }

    public static int[] GregorianToIndian(  int[] gregorianDay){
        int[] indDate=new int[3];;
        double jdAtStartOfGregYear;
        int leapMonth, IndianYear, yday, IndianMonth, IndianDayOfMonth, mday;
        // gregorianDay Stores gregorian date  

        //  gregorianDay = jdToGregorian(julianDay);                    // Gregorian date for Julian day
        IndianYear = gregorianDay[0] - INDIAN_ERA_START;            // Year in Saka era
        jdAtStartOfGregYear = gregorianToJD(gregorianDay[0], 1, 1); // JD at start of Gregorian year
        double julianDay=gregorianToJD( gregorianDay[0],  gregorianDay[1],  gregorianDay[2]);
        yday = (int)(julianDay - jdAtStartOfGregYear);              // Day number in Gregorian year (starting from 0)

        if (yday < INDIAN_YEAR_START) {
            //  Day is at the end of the preceding Saka year
            IndianYear -= 1;
            leapMonth = isGregorianLeap(gregorianDay[0] - 1) ? 31 : 30; // Days in leapMonth this year, previous Gregorian year
            yday += leapMonth + (31 * 5) + (30 * 3) + 10;
        } else {
            leapMonth = isGregorianLeap(gregorianDay[0]) ? 31 : 30; // Days in leapMonth this year
            yday -= INDIAN_YEAR_START;
        }

        if (yday < leapMonth) {
            IndianMonth = 0;
            IndianDayOfMonth = yday + 1;
        } else {
            mday = yday - leapMonth;
            if (mday < (31 * 5)) {
                IndianMonth = (int)Math.floor(mday / 31) + 1;
                IndianDayOfMonth = (mday % 31) + 1;
            } else {
                mday -= 31 * 5;
                IndianMonth = (int)Math.floor(mday / 30) + 6;
                IndianDayOfMonth = (mday % 30) + 1;
            }
        }
        /*Month is 0 based.converting it to 1 based*/
        if(IndianMonth == 12) {
            IndianMonth = 1;
        } else {
            IndianMonth = IndianMonth +1;  
        }
        indDate[0]=IndianYear;
        indDate[1]=IndianMonth;
        indDate[2]=IndianDayOfMonth;
        System.out.println(IndianDayOfMonth);
        System.out.println(IndianMonth);
        System.out.println(IndianYear);
        return indDate;

    }
 
    public static void main(String args[]){
        //     System.out.println(jdToGregorian(IndianToJD(1123, 4, 5)));
        int[] greg={2008,12,31};
        int[] indDate=new int[3];
        indDate=GregorianToIndian(greg);
        greg= jdToGregorian(IndianToJD(indDate[0],indDate[1],indDate[2]));
        System.out.println(greg[0]+"/"+greg[1]+"/"+greg[2]);
    }
}
