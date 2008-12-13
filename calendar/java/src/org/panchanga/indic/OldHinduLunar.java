 

package org.panchanga.indic;

import org.panchanga.common.Date;
import org.panchanga.common.ProtoDate;
import org.panchanga.common.exception.BogusDateException;


// Referenced classes of package calendrica:
//            Date, BogusDateException, ProtoDate, OldHinduSolar

public class OldHinduLunar extends Date
{

    public OldHinduLunar()
    {
    }

    public OldHinduLunar(int date)
    {
        super(date);
    }

    public OldHinduLunar(Date date)
        throws BogusDateException
    {
        super(date);
    }

    public OldHinduLunar(int month, boolean leap, int day, int year)
    {
        this.month = month;
        this.leap = leap;
        this.day = day;
        this.year = year;
    }

    public static int toFixed(int month, boolean leap, int day, int year)
    {
        double mina = (double)(12 * year - 1) * 30.43822337962963D;
        double lunarNewYear = 29.530581807581694D * (double)(ProtoDate.quotient(mina, 29.530581807581694D) + 1);
        return (int)Math.floor((double)OldHinduSolar.EPOCH + lunarNewYear + 29.530581807581694D * (double)(leap || Math.ceil((lunarNewYear - mina) / 0.90764157204793605D) > (double)month ? month - 1 : month) + (double)(day - 1) * 0.9843527269193898D + 0.75D);
    }

    public int toFixed()
    {
        return toFixed(month, leap, day, year);
    }

    public void fromFixed(int date)
    {
        double rise = (double)OldHinduSolar.dayCount(date) + 0.25D;
        double newMoon = rise - ProtoDate.mod(rise, 29.530581807581694D);
        leap = 0.90764157204793605D >= ProtoDate.mod(newMoon, 30.43822337962963D) && ProtoDate.mod(newMoon, 30.43822337962963D) > 0.0D;
        month = 1 + (int)ProtoDate.mod(Math.ceil(newMoon / 30.43822337962963D), 12D);
        day = 1 + ProtoDate.mod(ProtoDate.quotient(rise, 0.9843527269193898D), 30);
        year = (int)Math.ceil((newMoon + 30.43822337962963D) / 365.25868055555554D) - 1;
    }

    public void fromArray(int a[])
    {
        month = a[0];
        leap = a[1] != 0;
        day = a[2];
        year = a[3];
    }

    public static boolean isLeapYear(int lYear)
    {
        return ProtoDate.mod((double)lYear * 365.25868055555554D - 30.43822337962963D, 29.530581807581694D) >= 29.530581807581694D - ProtoDate.mod(365.25868055555554D, 29.530581807581694D);
    }

    protected String toStringFields()
    {
        return "month=" + month + ",leap=" + leap + ",day=" + day + ",year=" + year;
    }

    public boolean equals(Object obj)
    {
        if(this == obj)
            return true;
        if(!(obj instanceof OldHinduLunar))
            return false;
        OldHinduLunar o = (OldHinduLunar)obj;
        return o.month == month && o.leap == leap && o.day == day && o.year == year;
    }

    public int month;
    public boolean leap;
    public int day;
    public int year;
    public static final double ARYA_LUNAR_MONTH = 29.530581807581694D;
    public static final double ARYA_LUNAR_DAY = 0.9843527269193898D;
}



 