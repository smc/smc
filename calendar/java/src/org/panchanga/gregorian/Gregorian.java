 

package org.panchanga.gregorian;

import org.panchanga.common.Date;
import org.panchanga.common.ProtoDate;
import org.panchanga.common.StandardDate;
import org.panchanga.common.exception.BogusDateException;


// Referenced classes of package calendrica:
//            StandardDate, BogusDateException, ProtoDate, Date

public class Gregorian extends StandardDate
{

    public Gregorian()
    {
    }

    public Gregorian(int date)
    {
        super(date);
    }

    public Gregorian(Date date)
        throws BogusDateException
    {
        super(date);
    }

    public Gregorian(int month, int day, int year)
    {
        super(month, day, year);
    }

    public static int toFixed(int month, int day, int year)
    {
        return ((0 + 365 * (year - 1) + ProtoDate.quotient(year - 1, 4D)) - ProtoDate.quotient(year - 1, 100D)) + ProtoDate.quotient(year - 1, 400D) + ProtoDate.quotient(367 * month - 362, 12D) + (month > 2 ? isLeapYear(year) ? -1 : -2 : 0) + day;
    }

    public int toFixed()
    {
        return toFixed(super.month, super.day, super.year);
    }

    public void fromFixed(int date)
    {
        super.year = yearFromFixed(date);
        int priorDays = date - toFixed(1, 1, super.year);
        int correction = date >= toFixed(3, 1, super.year) ? ((int) (isLeapYear(super.year) ? 1 : 2)) : 0;
        super.month = ProtoDate.quotient(12 * (priorDays + correction) + 373, 367D);
        super.day = (date - toFixed(super.month, 1, super.year)) + 1;
    }

    public static boolean isLeapYear(int year)
    {
        boolean result = false;
        if(ProtoDate.mod(year, 4) == 0)
        {
            int n = ProtoDate.mod(year, 400);
            if(n != 100 && n != 200 && n != 300)
                result = true;
        }
        return result;
    }

    public static int yearFromFixed(int date)
    {
        int d0 = date - 1;
        int n400 = ProtoDate.quotient(d0, 146097D);
        int d1 = ProtoDate.mod(d0, 146097);
        int n100 = ProtoDate.quotient(d1, 36524D);
        int d2 = ProtoDate.mod(d1, 36524);
        int n4 = ProtoDate.quotient(d2, 1461D);
        int d3 = ProtoDate.mod(d2, 1461);
        int n1 = ProtoDate.quotient(d3, 365D);
        int _tmp = ProtoDate.mod(d3, 365) + 1;
        int year = 400 * n400 + 100 * n100 + 4 * n4 + n1;
        return n100 != 4 && n1 != 4 ? year + 1 : year;
    }

    public int dayNumber()
    {
        return ProtoDate.difference(toFixed(12, 31, super.year - 1), toFixed());
    }

    public int daysRemaining()
    {
        return ProtoDate.difference(toFixed(), toFixed(12, 31, super.year));
    }

    public static int independenceDay(int year)
    {
        return toFixed(7, 4, year);
    }

    public static int laborDay(int year)
    {
        return ProtoDate.nthKDay(1, 1, toFixed(9, 1, year));
    }

    public static int memorialDay(int year)
    {
        return ProtoDate.nthKDay(-1, 1, toFixed(5, 31, year));
    }

    public static int electionDay(int year)
    {
        return ProtoDate.nthKDay(1, 2, toFixed(11, 2, year));
    }

    public static int daylightSavingsStart(int year)
    {
        return ProtoDate.nthKDay(1, 0, toFixed(4, 1, year));
    }

    public static int daylightSavingsEnd(int year)
    {
        return ProtoDate.nthKDay(-1, 0, toFixed(10, 31, year));
    }

    public static int christmas(int year)
    {
        return toFixed(12, 25, year);
    }

    public static int advent(int year)
    {
        return ProtoDate.kDayNearest(toFixed(11, 30, year), 0);
    }

    public static int epiphany(int year)
    {
        return christmas(year - 1) + 12;
    }

    public boolean equals(Object obj)
    {
        if(!(obj instanceof Gregorian))
            return false;
        else
            return internalEquals(obj);
    }

    public static final int EPOCH = 1;
}


 