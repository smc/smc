 
package org.panchanga.common;

import org.panchanga.common.exception.BogusDateException;
import org.panchanga.gregorian.Gregorian;


// Referenced classes of package calendrica:
//            Date, BogusDateException, Gregorian, ProtoDate

public class ISO extends Date
{

    public ISO()
    {
    }

    public ISO(int date)
    {
        super(date);
    }

    public ISO(Date date)
        throws BogusDateException
    {
        super(date);
    }

    public ISO(int week, int day, int year)
    {
        this.week = week;
        this.day = day;
        this.year = year;
    }

    public static int toFixed(int week, int day, int year)
    {
        return ProtoDate.nthKDay(week, 0, Gregorian.toFixed(12, 28, year - 1)) + day;
    }

    public int toFixed()
    {
        return toFixed(week, day, year);
    }

    public void fromFixed(int date)
    {
        int approx = Gregorian.yearFromFixed(date - 3);
        year = date < toFixed(1, 1, approx + 1) ? approx : approx + 1;
        week = ProtoDate.quotient(date - toFixed(1, 1, year), 7D) + 1;
        day = ProtoDate.adjustedMod(date, 7);
    }

    public void fromArray(int a[])
    {
        week = a[0];
        day = a[1];
        year = a[2];
    }

    protected String toStringFields()
    {
        return "week=" + week + ",day=" + day + ",year=" + year;
    }

    public boolean equals(Object obj)
    {
        if(this == obj)
            return true;
        if(!(obj instanceof ISO))
            return false;
        ISO o = (ISO)obj;
        return o.week == week && o.day == day && o.year == year;
    }

    public int week;
    public int day;
    public int year;
}


 