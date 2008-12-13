 

package org.panchanga.indic;

import org.panchanga.common.Date;
import org.panchanga.common.FixedVector;
import org.panchanga.common.ProtoDate;
import org.panchanga.common.exception.BogusDateException;
import org.panchanga.gregorian.Gregorian;

 

// Referenced classes of package calendrica:
//            Date, BogusDateException, OldHinduLunar, OldHinduSolar, 
//            HinduSolar, ProtoDate, Gregorian, FixedVector

public class HinduLunar extends Date
{

    public HinduLunar()
    {
    }

    public HinduLunar(int date)
    {
        super(date);
    }

    public HinduLunar(Date date)
        throws BogusDateException
    {
        super(date);
    }

    public HinduLunar(int month, boolean leapMonth, int day, boolean leapDay, int year)
    {
        this.month = month;
        this.leapMonth = leapMonth;
        this.day = day;
        this.leapDay = leapDay;
        this.year = year;
    }

    public static int toFixed(int month, boolean leapMonth, int day, boolean leapDay, int year)
        throws BogusDateException
    {
        return (new HinduLunar(month, leapMonth, day, leapDay, year)).toFixed();
    }

    public int toFixed()
        throws BogusDateException
    {
        int kyYear = year + 3044;
        int mean = OldHinduLunar.toFixed(month, leapMonth, day, kyYear);
        double approx;
        if(precedes(new HinduLunar(mean + 15), this))
            approx = (double)mean + 29.530587946071719D;
        else
        if(precedes(this, new HinduLunar(mean - 15)))
            approx = (double)mean - 29.530587946071719D;
        else
            approx = mean;
        double lo = approx - 4D;
        double hi = approx + 4D;
        double d;
        for(d = (lo + hi) / 2D; hi - lo > 2D; d = (lo + hi) / 2D)
            if(!precedes(new HinduLunar((int)Math.floor(d)), this))
                hi = d;
            else
                lo = d;

        int aTry = (int)Math.floor(d);
        int result;
        if((new HinduLunar(aTry)).equals(this))
            result = aTry;
        else
        if((new HinduLunar(aTry + 1)).equals(this))
            result = aTry + 1;
        else
        if((new HinduLunar(aTry - 1)).equals(this))
            result = aTry - 1;
        else
            throw new BogusDateException();
        return result;
    }

    public void fromFixed(int date)
    {
        int kyTime = OldHinduSolar.dayCount(date);
        double rise = HinduSolar.sunrise(kyTime);
        day = lunarDay(rise);
        leapDay = day == lunarDay(HinduSolar.sunrise(kyTime - 1));
        double lastNewMoon = newMoon(rise);
        double nextNewMoon = newMoon(Math.floor(lastNewMoon) + 35D);
        int solarMonth = HinduSolar.zodiac(lastNewMoon);
        leapMonth = solarMonth == HinduSolar.zodiac(nextNewMoon);
        month = ProtoDate.adjustedMod(solarMonth + 1, 12);
        year = HinduSolar.calendarYear(nextNewMoon) - 3044 - (!leapMonth || month != 1 ? 0 : -1);
    }

    public void fromArray(int a[])
    {
        month = a[0];
        leapMonth = a[1] != 0;
        day = a[2];
        leapDay = a[3] != 0;
        year = a[4];
    }

    public static double newMoon(double kyTime)
    {
        double tomorrow = kyTime + 1.0D;
        double estimate = tomorrow - ProtoDate.mod(tomorrow, 29.530587946071719D);
        double lo = estimate - 0.66666666666666663D;
        double hi = estimate + 0.66666666666666663D;
        double aTry;
        for(aTry = (hi + lo) / 2D; kyTime >= lo && (hi > kyTime || HinduSolar.zodiac(lo) != HinduSolar.zodiac(hi)); aTry = (hi + lo) / 2D)
            if(lunarPhase(aTry) < 10800D)
                hi = aTry;
            else
                lo = aTry;

        return aTry <= kyTime ? aTry : newMoon(Math.floor(kyTime) - 20D);
    }

    public static boolean precedes(HinduLunar d1, HinduLunar d2)
    {
        return d1.year < d2.year || d1.year == d2.year && (d1.month < d2.month || d1.month == d2.month && (d1.leapMonth && !d2.leapMonth || d1.leapMonth == d2.leapMonth && (d1.day < d2.day || d1.day == d2.day && !d1.leapDay && d2.leapDay)));
    }

    public static double lunarDayStart(double kyTime, double k, double accuracy)
    {
        double tomorrow = kyTime + 1.0D;
        double part = (((k - 1.0D) * 1.0D) / 30D) * 29.530587946071719D;
        double estimate = tomorrow - ProtoDate.mod(tomorrow - part, 29.530587946071719D);
        double lo = estimate - 0.66666666666666663D;
        double hi = estimate + 0.66666666666666663D;
        double aTry;
        for(aTry = (hi + lo) / 2D; kyTime >= lo && hi - lo >= accuracy; aTry = (hi + lo) / 2D)
        {
            double diffX = lunarPhase(aTry) - (k - 1.0D) * 720D;
            if(0.0D < diffX && diffX < 10800D || diffX < -10800D)
                hi = aTry;
            else
                lo = aTry;
        }

        return aTry <= kyTime ? aTry : lunarDayStart(kyTime - 20D, k, accuracy);
    }

    public static double lunarLongitude(double kyTime)
    {
        return HinduSolar.truePosition(kyTime, 27.321674162683866D, 0.088888888888888892D, 27.554597974680476D, 0.023809523809523808D);
    }

    public static double lunarPhase(double kyTime)
    {
        return ProtoDate.mod(lunarLongitude(kyTime) - HinduSolar.solarLongitude(kyTime), 21600D);
    }

    public static int lunarDay(double kyTime)
    {
        return ProtoDate.quotient(lunarPhase(kyTime), 720D) + 1;
    }

    public static int lunarMansion(int date)
    {
        double rise = HinduSolar.sunrise(OldHinduSolar.dayCount(date));
        return ProtoDate.quotient(lunarLongitude(rise), 800D) + 1;
    }

    public static int newYear(int gYear)
    {
        double mesha = HinduSolar.meshaSamkranti(gYear);
        double m1 = lunarDayStart(OldHinduSolar.dayCount(mesha), 1.0D, 1.0000000000000001E-005D);
        double m0 = lunarDayStart(m1 - 27D, 1.0D, 1.0000000000000001E-005D);
        double aNewMoon = HinduSolar.zodiac(m0) != HinduSolar.zodiac(m1) ? m1 : m0;
        int hDay = (int)Math.floor(aNewMoon);
        double rise = HinduSolar.sunrise(hDay);
        return OldHinduSolar.EPOCH + hDay + (aNewMoon >= rise && lunarDay(HinduSolar.sunrise(hDay + 1)) != 2 ? 1 : 0);
    }

    public static int karana(int n)
    {
        if(n == 1)
            return 0;
        if(n > 57)
            return n - 50;
        else
            return ProtoDate.adjustedMod(n - 1, 7);
    }

    public static int yoga(double kyTime)
    {
        return (int)Math.floor(ProtoDate.mod((HinduSolar.solarLongitude(kyTime) + lunarLongitude(kyTime)) / 800D, 27D)) + 1;
    }

    public static FixedVector sacredWednesdaysInGregorian(int gYear)
    {
        return sacredWednesdays(Gregorian.toFixed(1, 1, gYear), Gregorian.toFixed(12, 31, gYear));
    }

    public static FixedVector sacredWednesdays(int start, int end)
    {
        int wed = ProtoDate.kDayOnOrAfter(start, 3);
        FixedVector result = new FixedVector();
        for(; wed <= end; wed += 7)
        {
            HinduLunar hDate = new HinduLunar(wed);
            if(hDate.day == 8)
                result.addFixed(wed);
        }

        return result;
    }

    protected String toStringFields()
    {
        return "month=" + month + ",leapMonth=" + leapMonth + ",day=" + day + ",leapDay=" + leapDay + ",year=" + year;
    }

    public boolean equals(Object obj)
    {
        if(this == obj)
            return true;
        if(!(obj instanceof HinduLunar))
            return false;
        HinduLunar o = (HinduLunar)obj;
        return o.month == month && o.leapMonth == leapMonth && o.day == day && o.leapDay == leapDay && o.year == year;
    }

    public int month;
    public boolean leapMonth;
    public int day;
    public boolean leapDay;
    public int year;
    public static final int LUNAR_ERA = 3044;
    public static final double SYNODIC_MONTH = 29.530587946071719D;
    public static final double SIDEREAL_MONTH = 27.321674162683866D;
    public static final double ANOMALISTIC_MONTH = 27.554597974680476D;
}

 
 