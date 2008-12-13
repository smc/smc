 
package org.panchanga.common;

import org.panchanga.common.exception.BogusDateException;
import org.panchanga.gregorian.Gregorian;


// Referenced classes of package calendrica:
//            StandardDate, Gregorian, BogusDateException, ProtoDate, 
//            FixedVector, Date

public class Julian extends StandardDate
{

    public Julian()
    {
    }

    public Julian(int date)
    {
        super(date);
    }

    public Julian(Date date)
        throws BogusDateException
    {
        super(date);
    }

    public Julian(int month, int day, int year)
    {
        super(month, day, year);
    }

    public static int toFixed(int month, int day, int year)
    {
        int y = year >= 0 ? year : year + 1;
        return (EPOCH - 1) + 365 * (y - 1) + ProtoDate.quotient(y - 1, 4D) + ProtoDate.quotient(367 * month - 362, 12D) + (month > 2 ? isLeapYear(year) ? -1 : -2 : 0) + day;
    }

    public int toFixed()
    {
        return toFixed(super.month, super.day, super.year);
    }

    public void fromFixed(int date)
    {
        int approx = ProtoDate.quotient(4 * (date - EPOCH) + 1464, 1461D);
        super.year = approx > 0 ? approx : approx - 1;
        int priorDays = date - toFixed(1, 1, super.year);
        int correction = date >= toFixed(3, 1, super.year) ? ((int) (isLeapYear(super.year) ? 1 : 2)) : 0;
        super.month = ProtoDate.quotient(12 * (priorDays + correction) + 373, 367D);
        super.day = (date - toFixed(super.month, 1, super.year)) + 1;
    }

    public static int BCE(int n)
    {
        return -n;
    }

    public static int CE(int n)
    {
        return n;
    }

    public static boolean isLeapYear(int jYear)
    {
        return ProtoDate.mod(jYear, 4) == (jYear <= 0 ? 3 : 0);
    }

    public static int nicaeanRuleEaster(int jYear)
    {
        int shiftedEpact = ProtoDate.mod(14 + 11 * ProtoDate.mod(jYear, 19), 30);
        int paschalMoon = toFixed(4, 19, jYear) - shiftedEpact;
        return ProtoDate.kDayAfter(paschalMoon, 0);
    }

    public static int easter(int gYear)
    {
        int century = 1 + ProtoDate.quotient(gYear, 100D);
        int shiftedEpact = ProtoDate.mod(((14 + 11 * ProtoDate.mod(gYear, 19)) - ProtoDate.quotient(3 * century, 4D)) + ProtoDate.quotient(5 + 8 * century, 25D), 30);
        int adjustedEpact = shiftedEpact != 0 && (shiftedEpact != 1 || 10 >= ProtoDate.mod(gYear, 19)) ? shiftedEpact : shiftedEpact + 1;
        int paschalMoon = Gregorian.toFixed(4, 19, gYear) - adjustedEpact;
        return ProtoDate.kDayAfter(paschalMoon, 0);
    }

    public static int pentecost(int gYear)
    {
        return easter(gYear) + 49;
    }

    public static FixedVector inGregorian(int jMonth, int jDay, int gYear)
    {
        int jan1 = Gregorian.toFixed(1, 1, gYear);
        int dec31 = Gregorian.toFixed(12, 31, gYear);
        int y = ((StandardDate) (new Julian(jan1))).year;
        int date1 = toFixed(jMonth, jDay, y);
        int date2 = toFixed(jMonth, jDay, y + 1);
        FixedVector result = new FixedVector(1, 1);
        if(jan1 <= date1 && date1 <= dec31)
            result.addFixed(date1);
        if(jan1 <= date2 && date2 <= dec31)
            result.addFixed(date2);
        return result;
    }

    public static FixedVector easternOrthodoxChristmas(int gYear)
    {
        return inGregorian(12, 25, gYear);
    }

    public boolean equals(Object obj)
    {
        if(!(obj instanceof Julian))
            return false;
        else
            return internalEquals(obj);
    }

    public static final int EPOCH = Gregorian.toFixed(12, 30, 0);

}


 