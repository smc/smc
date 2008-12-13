 

package org.panchanga.common;

import org.panchanga.common.exception.BogusDateException;


// Referenced classes of package calendrica:
//            Date, BogusDateException

public abstract class StandardDate extends Date
{

    public StandardDate()
    {
    }

    public StandardDate(int date)
    {
        super(date);
    }

    public StandardDate(Date date)
        throws BogusDateException
    {
        super(date);
    }

    public StandardDate(int month, int day, int year)
    {
        this.month = month;
        this.day = day;
        this.year = year;
    }

    public StandardDate(int a[])
    {
        fromArray(a);
    }

    public void fromArray(int a[])
    {
        month = a[0];
        day = a[1];
        year = a[2];
    }

    protected String toStringFields()
    {
        return "month=" + month + ",day=" + day + ",year=" + year;
    }

    protected boolean internalEquals(Object obj)
    {
        StandardDate o = (StandardDate)obj;
        if(this == obj)
            return true;
        return o.month == month && o.day == day && o.year == year;
    }

    public int month;
    public int day;
    public int year;
}


 