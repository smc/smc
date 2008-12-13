 
package org.panchanga.indic;

import org.panchanga.common.Date;
import org.panchanga.common.Julian;
import org.panchanga.common.ProtoDate;
import org.panchanga.common.StandardDate;
import org.panchanga.common.exception.BogusDateException;


// Referenced classes of package calendrica:
//            StandardDate, Julian, BogusDateException, ProtoDate, 
//            Date

public class OldHinduSolar extends StandardDate
{

    public OldHinduSolar()
    {
    }

    public OldHinduSolar(int date)
    {
        super(date);
    }

    public OldHinduSolar(Date date)
        throws BogusDateException
    {
        super(date);
    }

    public OldHinduSolar(int month, int day, int year)
    {
        super(month, day, year);
    }

    public static int toFixed(int month, int day, int year)
    {
        return (int)Math.floor(((double)EPOCH + (double)year * 365.25868055555554D + (double)(month - 1) * 30.43822337962963D + (double)day) - 0.25D);
    }

    public int toFixed()
    {
        return toFixed(super.month, super.day, super.year);
    }

    public void fromFixed(int date)
    {
        double rise = (double)dayCount(date) + 0.25D;
        super.year = ProtoDate.quotient(rise, 365.25868055555554D);
        super.month = 1 + ProtoDate.mod(ProtoDate.quotient(rise, 30.43822337962963D), 12);
        super.day = 1 + (int)Math.floor(ProtoDate.mod(rise, 30.43822337962963D));
    }

    public static int dayCount(int date)
    {
        return date - EPOCH;
    }

    public static double dayCount(double date)
    {
        return date - (double)EPOCH;
    }

    public static int jovianYear(int date)
    {
        return ProtoDate.mod(ProtoDate.quotient(dayCount(date), 361.02268109734672D), 60) + 1;
    }

    public boolean equals(Object obj)
    {
        if(!(obj instanceof OldHinduSolar))
            return false;
        else
            return internalEquals(obj);
    }

    public static final int EPOCH = Julian.toFixed(2, 18, Julian.BCE(3102));
    public static final double ARYA_SIDEREAL_YEAR = 365.25868055555554D;
    public static final double ARYA_SOLAR_MONTH = 30.43822337962963D;
    public static final double ARYA_JOVIAN_PERIOD = 4332.2721731681604D;

}