 
package org.panchanga.indic;

import org.panchanga.common.Date;
import org.panchanga.common.ProtoDate;
import org.panchanga.common.StandardDate;
import org.panchanga.common.exception.BogusDateException;
import org.panchanga.gregorian.Gregorian;


// Referenced classes of package calendrica:
//            StandardDate, BogusDateException, OldHinduSolar, ProtoDate, 
//            Gregorian, Date

public class HinduSolar extends StandardDate
{

    public HinduSolar()
    {
    }

    public HinduSolar(int date)
    {
        super(date);
    }

    public HinduSolar(Date date)
        throws BogusDateException
    {
        super(date);
    }

    public HinduSolar(int month, int day, int year)
    {
        super(month, day, year);
    }

    public static int toFixed(int month, int day, int year)
        throws BogusDateException
    {
        return (new HinduSolar(month, day, year)).toFixed();
    }

    public int toFixed()
        throws BogusDateException
    {
        int approx = (int)Math.floor(((double)(super.year + 3179 + (super.month - 1) / 12) * 365.2587564814815D + (double)OldHinduSolar.EPOCH + (double)super.day) - 9D);
        int aTry;
        HinduSolar tryDate;
        for(aTry = approx; precedes(tryDate = new HinduSolar(aTry), this); aTry++);
        int result;
        if(tryDate.equals(this))
            result = aTry;
        else
            throw new BogusDateException();
        return result;
    }

    public void fromFixed(int date)
    {
        int kyTime = OldHinduSolar.dayCount(date);
        double rise = sunrise(kyTime);
        super.month = zodiac(rise);
        super.year = calendarYear(rise) - 3179;
        int approx = kyTime - 3 - ProtoDate.quotient(ProtoDate.mod(solarLongitude(rise), 1800D), 60D);
        int begin;
        for(begin = approx; zodiac(sunrise(begin)) != super.month; begin++);
        super.day = (kyTime - begin) + 1;
    }

    public static double hinduSineTable(int entry)
    {
        double exact = 3438D * ProtoDate.sinDegrees(((double)entry * 225D) / 60D);
        double error = 0.215D * (double)ProtoDate.signum(exact) * (double)ProtoDate.signum(Math.abs(exact) - 1716D);
        return (double)Math.round(exact + error);
    }

    public static double hinduSine(double theta)
    {
        double entry = theta / 225D;
        double fraction = ProtoDate.mod(entry, 1.0D);
        return fraction * hinduSineTable((int)Math.ceil(entry)) + (1.0D - fraction) * hinduSineTable((int)Math.floor(entry));
    }

    public static double hinduArcsin(double units)
    {
        boolean neg = units < 0.0D;
        if(neg)
            units = -units;
        int pos;
        for(pos = 0; units > hinduSineTable(pos); pos++);
        double val = hinduSineTable(pos - 1);
        double result = 225D * ((double)(pos - 1) + (units - val) / (hinduSineTable(pos) - val));
        if(neg)
            result = -result;
        return result;
    }

    public static double meanPosition(double kyTime, double period)
    {
        return 21600D * ProtoDate.mod(kyTime / period, 1.0D);
    }

    public static double truePosition(double kyTime, double period, double size, double anomalistic, 
            double change)
    {
        double aLong = meanPosition(kyTime, period);
        double days = kyTime + 714402296627D;
        double offset = hinduSine(meanPosition(days, anomalistic));
        double contraction = (Math.abs(offset) * change * size * 1.0D) / 3438D;
        double equation = hinduArcsin(offset * (size - contraction));
        return ProtoDate.mod(aLong - equation, 21600D);
    }

    public static double solarLongitude(double kyTime)
    {
        return truePosition(kyTime, 365.2587564814815D, 0.03888888888888889D, 365.25878920258134D, 0.023809523809523808D);
    }

    public static int zodiac(double kyTime)
    {
        return ProtoDate.quotient(solarLongitude(kyTime), 1800D) + 1;
    }

    public static boolean precedes(HinduSolar d1, HinduSolar d2)
    {
        return ((StandardDate) (d1)).year < ((StandardDate) (d2)).year || ((StandardDate) (d1)).year == ((StandardDate) (d2)).year && (((StandardDate) (d1)).month < ((StandardDate) (d2)).month || ((StandardDate) (d1)).month == ((StandardDate) (d2)).month && ((StandardDate) (d1)).day < ((StandardDate) (d2)).day);
    }

    public static int calendarYear(double kyTime)
    {
        double mean = 21600D * ProtoDate.mod(kyTime / 365.2587564814815D, 1.0D);
        double real = solarLongitude(kyTime);
        int year = ProtoDate.quotient(kyTime, 365.2587564814815D);
        if(real > 20000D && 1000D > mean)
            return year - 1;
        if(mean > 20000D && 1000D > real)
            return year + 1;
        else
            return year;
    }

    public static double equationOfTime(double kyTime)
    {
        double offset = hinduSine(meanPosition(714402296627D + kyTime, 365.25878920258134D));
        double equationSun = offset * (Math.abs(offset) / 3713040D - 0.03888888888888889D);
        return (((dailyMotion(kyTime) * equationSun * 365.2587564814815D * 1.0D) / 21600D) * 1.0D) / 21600D;
    }

    public static double ascensionalDifference(double kyTime, double latitude)
    {
        double sinDecl = 0.40634089586969169D * hinduSine(tropicalLongitude(kyTime));
        double diurnalRadius = hinduSine(5400D - hinduArcsin(sinDecl));
        double tan = hinduSine(latitude) / hinduSine(5400D + latitude);
        double earthSine = sinDecl * tan;
        return hinduArcsin((-3438D * earthSine) / diurnalRadius);
    }

    public static double tropicalLongitude(double kyTime)
    {
        double midnight = Math.floor(kyTime);
        double precession = 1620D - Math.abs(1620D - ProtoDate.mod(0.002464006636472327D * midnight, 6480D));
        return ProtoDate.mod(solarLongitude(kyTime) - precession, 21600D);
    }

    public static int risingSign(double kyTime)
    {
        int index = ProtoDate.mod(ProtoDate.quotient(tropicalLongitude(kyTime), 1800D), 6);
        return rs[index];
    }

    public static double dailyMotion(double kyTime)
    {
        double meanMotion = 59.136159275335849D;
        double anomaly = meanPosition(714402296627D + kyTime, 365.25878920258134D);
        double epicycle = 0.03888888888888889D - Math.abs(hinduSine(anomaly)) / 3713040D;
        int entry = ProtoDate.quotient(anomaly, 225D);
        double sineTableStep = hinduSineTable(entry + 1) - hinduSineTable(entry);
        double equationOfMotionFactor = sineTableStep * -0.0044444444444444444D * epicycle;
        return meanMotion * (equationOfMotionFactor + 1.0D);
    }

    public static double solarSiderealDifference(double kyTime)
    {
        return (dailyMotion(kyTime) * (double)risingSign(kyTime) * 1.0D) / 1800D;
    }

    public static double sunrise(double kyTime)
    {
        return kyTime + 0.25D + equationOfTime(kyTime) + 4.6169893048655071E-005D * (ascensionalDifference(kyTime, 1389D) + solarSiderealDifference(kyTime) / 4D);
    }

    public static double sunriseAtUjjain(int kyTime)
    {
        int d = kyTime + OldHinduSolar.EPOCH;
        double latitude = 23.149999999999999D;
        double longitude = 75.766666666666666D;
        return (double)kyTime + ProtoDate.sunrise(d, latitude, longitude);
    }


    public static double sunsetAtUjjain(int kyTime) {
        int d = kyTime + OldHinduSolar.EPOCH;
        double latitude = 23.149999999999999D;
        double longitude = 75.766666666666666D;
        return (double)kyTime + ProtoDate.sunset(d, latitude, longitude);
    } 
    public static double samkranti(int gYear, int m)
        throws BogusDateException
    {
        int diff = 3179 + ((StandardDate) (new Gregorian(OldHinduSolar.EPOCH))).year;
        int hYear = gYear - diff;
        int ny = toFixed(m, 1, hYear) - OldHinduSolar.EPOCH;
        double lo = (double)ny - 0.875D;
        double hi = (double)ny + 0.375D;
        double begin;
        for(begin = (hi + lo) / 2D; hi - lo >= 9.9999999999999995E-008D; begin = (hi + lo) / 2D)
            if(m != 1 ? solarLongitude(begin) >= (double)((m - 1) * 1800) : solarLongitude(begin) < 1800D)
                hi = begin;
            else
                lo = begin;

        return begin + (double)OldHinduSolar.EPOCH;
    }

    public static double meshaSamkranti(int gYear)
    {
        double result = 0.0D;
        try
        {
            result = samkranti(gYear, 1);
        }
        catch(BogusDateException _ex) { }
        return result;
    }

    public boolean equals(Object obj)
    {
        if(!(obj instanceof HinduSolar))
            return false;
        else
            return internalEquals(obj);
    }

    public static final double SIDEREAL_YEAR = 365.2587564814815D;
    public static final double CREATION = 714402296627D;
    public static final double ANOMALISTIC_YEAR = 365.25878920258134D;
    public static final int SOLAR_ERA = 3179;
    private static final short rs[] = {
        1670, 1795, 1935, 1935, 1795, 1670
    };

}



 