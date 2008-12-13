/*jadclipse*/// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) radix(10) lradix(10) 
// Source File Name:   ProtoDate.java

package org.panchanga.common;

import java.io.Serializable;

import org.panchanga.common.exception.BogusDateException;
import org.panchanga.gregorian.Gregorian;

// Referenced classes of package calendrica:
//            Gregorian, BogusDateException, Date, StandardDate

public abstract class ProtoDate
    implements Cloneable, Serializable
{
    private static class ec
    {

        private static final double coeff19th[] = {
            -2.0000000000000002E-005D, 0.00029700000000000001D, 0.025184000000000002D, -0.18113299999999999D, 0.55303999999999998D, -0.86193799999999998D, 0.67706599999999995D, -0.212591D
        };
        private static final double coeff18th[] = {
            -9.0000000000000002E-006D, 0.0038440000000000002D, 0.083562999999999998D, 0.86573599999999995D, 4.8675750000000004D, 15.845535D, 31.332267000000002D, 38.291998999999997D, 28.316289000000001D, 11.636203999999999D, 
            2.0437940000000001D
        };
        private static final double coeff17th[] = {
            196.58332999999999D, -4.0674999999999999D, 0.021916700000000001D
        };





        ec()
        {
        }
    }

    private static class et
    {

        private static final double coeffLongitude[] = {
            280.46645000000001D, 36000.769829999997D, 0.0003032D
        };
        private static final double coeffAnomaly[] = {
            357.52910000000003D, 35999.050300000003D, -0.00015589999999999999D, -4.7999999999999996E-007D
        };
        private static final double coeffInclination[] = {
            23.439291109999999D, -0.013004167000000001D, -1.6388999999999999E-007D, 5.0360000000000004E-007D
        };
        private static final double coeffEccentricity[] = {
            0.016708616999999999D, -4.2036999999999997E-005D, -1.236E-007D
        };






        et()
        {
        }
    }

    private static class sl
    {

        private static final int coefficients[] = {
            403406, 195207, 119433, 112392, 3891, 2819, 1721, 0, 660, 350, 
            334, 314, 268, 242, 234, 158, 132, 129, 114, 99, 
            93, 86, 78, 72, 68, 64, 46, 38, 37, 32, 
            29, 28, 27, 27, 25, 24, 21, 21, 20, 18, 
            17, 14, 13, 13, 13, 12, 10, 10, 10, 10
        };
        private static final double multipliers[] = {
            0.016210430000000001D, 628.30348067D, 628.30821523999998D, 628.29634301999999D, 1256.605691D, 1256.6098400000001D, 628.32476599999995D, 0.0081300000000000001D, 1256.5931D, 575.33849999999995D, 
            -0.33931D, 7771.3771500000003D, 786.04191000000003D, 0.054120000000000001D, 393.02098000000001D, -0.34860999999999998D, 1150.67698D, 157.74337D, 52.966700000000003D, 588.49270000000001D, 
            52.961100000000002D, -39.807000000000002D, 522.37689999999998D, 550.76469999999995D, 2.6107999999999998D, 157.73849999999999D, 1884.9103D, -77.5655D, 2.6488999999999998D, 1179.0626999999999D, 
            550.75750000000005D, -79.613900000000001D, 1884.8981000000001D, 21.321899999999999D, 1097.7103D, 548.68560000000002D, 254.4393D, -557.3143D, 606.97739999999999D, 21.3279D, 
            1097.7163D, -77.528199999999998D, 1884.9191000000001D, 2.0781000000000001D, 294.24630000000002D, -0.079899999999999999D, 469.41140000000001D, -0.68289999999999995D, 214.63249999999999D, 1572.0840000000001D
        };
        private static final double addends[] = {
            4.7219639999999998D, 5.9374580000000003D, 1.1155889999999999D, 5.7816159999999996D, 5.5473999999999997D, 1.512D, 4.1897000000000002D, 1.163D, 5.415D, 4.3150000000000004D, 
            4.5529999999999999D, 5.1980000000000004D, 5.9889999999999999D, 2.911D, 1.423D, 0.060999999999999999D, 2.3170000000000002D, 3.1930000000000001D, 2.8279999999999998D, 0.52000000000000002D, 
            4.6500000000000004D, 4.3499999999999996D, 2.75D, 4.5D, 3.23D, 1.22D, 0.14000000000000001D, 3.4399999999999999D, 4.3700000000000001D, 1.1399999999999999D, 
            2.8399999999999999D, 5.96D, 5.0899999999999999D, 1.72D, 2.5600000000000001D, 1.9199999999999999D, 0.089999999999999997D, 5.9800000000000004D, 4.0300000000000002D, 4.4699999999999998D, 
            0.79000000000000004D, 4.2400000000000002D, 2.0099999999999998D, 2.6499999999999999D, 4.9800000000000004D, 0.93000000000000005D, 2.21D, 3.5899999999999999D, 1.5D, 2.5499999999999998D
        };





        sl()
        {
        }
    }

    private static class nu
    {

        private static final double coeffa[] = {
            124.90000000000001D, -1934.134D, 0.0020630000000000002D
        };
        private static final double coeffb[] = {
            201.11000000000001D, 72001.537700000001D, 0.00056999999999999998D
        };




        nu()
        {
        }
    }

    private static class ll
    {

        private static final double coeffMeanMoon[] = {
            218.3164591D, 481267.88134235999D, -0.0013267999999999999D, 1.855835023689734E-006D, -1.5338834862103876E-008D
        };
        private static final double coeffElongation[] = {
            297.85020420000001D, 445267.11151680001D, -0.0016299999999999999D, 1.8319447192361523E-006D, -8.8444699951355417E-009D
        };
        private static final double coeffSolarAnomaly[] = {
            357.52910919999999D, 35999.050290899999D, -0.00015359999999999999D, 4.0832993058391183E-008D
        };
        private static final double coeffLunarAnomaly[] = {
            134.96341140000001D, 477198.8676313D, 0.0089969999999999998D, 1.4347408140719379E-005D, -6.7971723762914631E-008D
        };
        private static final double coeffMoonFromNode[] = {
            93.272099299999994D, 483202.01752729999D, -0.0034028999999999999D, -2.8360748723766307E-007D, 1.1583324645839848E-009D
        };
        private static final double coeffE[] = {
            1.0D, -0.002516D, -7.4000000000000003E-006D
        };
        private static final byte argsLunarElongation[] = {
            0, 2, 2, 0, 0, 0, 2, 2, 2, 2, 
            0, 1, 0, 2, 0, 0, 4, 0, 4, 2, 
            2, 1, 1, 2, 2, 4, 2, 0, 2, 2, 
            1, 2, 0, 0, 2, 2, 2, 4, 0, 3, 
            2, 4, 0, 2, 2, 2, 4, 0, 4, 1, 
            2, 0, 1, 3, 4, 2, 0, 1, 2, 2
        };
        private static final byte argsSolarAnomaly[] = {
            0, 0, 0, 0, 1, 0, 0, -1, 0, -1, 
            1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 
            1, 0, 1, -1, 0, 0, 0, 1, 0, -1, 
            0, -2, 1, 2, -2, 0, 0, -1, 0, 0, 
            1, -1, 2, 2, 1, -1, 0, 0, -1, 0, 
            1, 0, 1, 0, 0, -1, 2, 1, 0, 0
        };
        private static final byte argsLunarAnomaly[] = {
            1, -1, 0, 2, 0, 0, -2, -1, 1, 0, 
            -1, 0, 1, 0, 1, 1, -1, 3, -2, -1, 
            0, -1, 0, 1, 2, 0, -3, -2, -1, -2, 
            1, 0, 2, 0, -1, 1, 0, -1, 2, -1, 
            1, -2, -1, -1, -2, 0, 1, 4, 0, -2, 
            0, 2, 1, -2, -3, 2, 1, -1, 3, -1
        };
        private static final byte argsMoonFromNode[] = {
            0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 
            0, 0, 0, -2, 2, -2, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 
            0, 0, 0, 0, 0, -2, 2, 0, 2, 0, 
            0, 0, 0, 0, 0, -2, 0, 0, 0, 0, 
            -2, -2, 0, 0, 0, 0, 0, 0, 0, -2
        };
        private static final int sineCoefficients[] = {
            6288774, 1274027, 658314, 213618, -185116, -114332, 58793, 57066, 53322, 45758, 
            -40923, -34720, -30383, 15327, -12528, 10980, 10675, 10034, 8548, -7888, 
            -6766, -5163, 4987, 4036, 3994, 3861, 3665, -2689, -2602, 2390, 
            -2348, 2236, -2120, -2069, 2048, -1773, -1595, 1215, -1110, -892, 
            -810, 759, -713, -700, 691, 596, 549, 537, 520, -487, 
            -399, -381, 351, -340, 330, 327, -323, 299, 294, 0
        };













        ll()
        {
        }
    }

    private static class nm
    {

        private static final double coeffJDE[] = {
            2451550.0976499999D, 36524.908822833051D, 0.0001337D, -1.4999999999999999E-007D, 7.2999999999999996E-010D
        };
        private static final double coeffE[] = {
            1.0D, -0.002516D, -7.4000000000000003E-006D
        };
        private static final double coeffSolarAnomaly[] = {
            2.5533999999999999D, 35998.960422026496D, -2.1800000000000001E-005D, -1.1000000000000001E-007D
        };
        private static final double coeffLunarAnomaly[] = {
            201.5643D, 477197.67640106793D, 0.0107438D, 1.239E-005D, -5.8000000000000003E-008D
        };
        private static final double coeffMoonArgument[] = {
            160.71080000000001D, 483200.81131396897D, -0.0016341000000000001D, -2.2699999999999999E-006D, 1.0999999999999999E-008D
        };
        private static final double coeffOmega[] = {
            124.77460000000001D, -1934.1313612299998D, 0.0020690999999999999D, 2.1500000000000002E-006D
        };
        private static final byte eFactor[] = {
            0, 1, 0, 0, 1, 1, 2, 0, 0, 1, 
            0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0
        };
        private static final byte solarCoeff[] = {
            0, 1, 0, 0, -1, 1, 2, 0, 0, 1, 
            0, 1, 1, -1, 2, 0, 3, 1, 0, 1, 
            -1, -1, 1, 0
        };
        private static final byte lunarCoeff[] = {
            1, 0, 2, 0, 1, 1, 0, 1, 1, 2, 
            3, 0, 0, 2, 1, 2, 0, 1, 2, 1, 
            1, 1, 3, 4
        };
        private static final byte moonCoeff[] = {
            0, 0, 0, 2, 0, 0, 0, -2, 2, 0, 
            0, 2, -2, 0, 0, -2, 0, -2, 2, 2, 
            2, -2, 0, 0
        };
        private static final double sineCoeff[] = {
            -0.40720000000000001D, 0.17241000000000001D, 0.016080000000000001D, 0.01039D, 0.0073899999999999999D, -0.0051399999999999996D, 0.0020799999999999998D, -0.0011100000000000001D, -0.00056999999999999998D, 0.00055999999999999995D, 
            -0.00042000000000000002D, 0.00042000000000000002D, 0.00038000000000000002D, -0.00024000000000000001D, -6.9999999999999994E-005D, 4.0000000000000003E-005D, 4.0000000000000003E-005D, 3.0000000000000001E-005D, 3.0000000000000001E-005D, -3.0000000000000001E-005D, 
            3.0000000000000001E-005D, -2.0000000000000002E-005D, -2.0000000000000002E-005D, 2.0000000000000002E-005D
        };
        private static final double addConst[] = {
            299.76999999999998D, 251.88D, 251.83000000000001D, 349.42000000000002D, 84.659999999999997D, 141.74000000000001D, 207.13999999999999D, 154.84D, 34.520000000000003D, 207.19D, 
            291.33999999999997D, 161.72D, 239.56D, 331.55000000000001D
        };
        private static final double addCoeff[] = {
            0.107408D, 0.016320999999999999D, 26.641886D, 36.412478D, 18.206239D, 53.303770999999998D, 2.453732D, 7.3068600000000004D, 27.261239D, 0.121824D, 
            1.844379D, 24.198153999999999D, 25.513099D, 3.5925180000000001D
        };
        private static final double addExtra[] = {
            -0.0091730000000000006D, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0
        };
        private static final double addFactor[] = {
            0.00032499999999999999D, 0.000165D, 0.000164D, 0.000126D, 0.00011D, 6.2000000000000003E-005D, 6.0000000000000002E-005D, 5.5999999999999999E-005D, 4.6999999999999997E-005D, 4.1999999999999998E-005D, 
            4.0000000000000003E-005D, 3.6999999999999998E-005D, 3.4999999999999997E-005D, 2.3E-005D
        };

















        nm()
        {
        }
    }

    private static class sfj
    {

        private static final double siderealCoeff[] = {
            280.46061837000002D, 13185000.770053742D, 0.00038793299999999997D, 2.5833118057349522E-008D
        };



        sfj()
        {
        }
    }


    public ProtoDate()
    {
    }

    public ProtoDate(int date)
    {
        fromFixed(date);
    }

    public ProtoDate(Date date)
        throws BogusDateException
    {
        fromDate(date);
    }

    public abstract void fromFixed(int i);

    public void fromDate(Date fromDate)
        throws BogusDateException
    {
        convert(fromDate, this);
    }

    public abstract void fromArray(int ai[]);

    public static void convert(Date fromDate, ProtoDate toDate)
        throws BogusDateException
    {
        toDate.fromFixed(fromDate.toFixed());
    }

    public static int difference(Date date1, Date date2)
        throws BogusDateException
    {
        return date2.toFixed() - date1.toFixed();
    }

    public static int difference(int date1, Date date2)
        throws BogusDateException
    {
        return date2.toFixed() - date1;
    }

    public static int difference(Date date1, int date2)
        throws BogusDateException
    {
        return date2 - date1.toFixed();
    }

    public static int difference(int date1, int date2)
    {
        return date2 - date1;
    }

    public static double mod(double x, double y)
    {
        return x - y * Math.floor(x / y);
    }

    public static int mod(int x, int y)
    {
        return (int)((double)x - (double)y * Math.floor((double)x / (double)y));
    }

    public static int quotient(double x, double y)
    {
        return (int)Math.floor(x / y);
    }

    public static int adjustedMod(int m, int n)
    {
        return mod(m - 1, n) + 1;
    }

    public static int dayOfWeekFromFixed(int date)
    {
        return mod(date, 7);
    }

    public static int kDayOnOrBefore(int date, int k)
    {
        return date - dayOfWeekFromFixed(date - k);
    }

    public static int kDayOnOrAfter(int date, int k)
    {
        return kDayOnOrBefore(date + 6, k);
    }

    public static int kDayNearest(int date, int k)
    {
        return kDayOnOrBefore(date + 3, k);
    }

    public static int kDayAfter(int date, int k)
    {
        return kDayOnOrBefore(date + 7, k);
    }

    public static int kDayBefore(int date, int k)
    {
        return kDayOnOrBefore(date - 1, k);
    }

    public static int nthKDay(int n, int k, int date)
    {
        return n <= 0 ? kDayAfter(date, k) + 7 * n : kDayBefore(date, k) + 7 * n;
    }

    public static int signum(double x)
    {
        if(x < 0.0D)
            return -1;
        return x <= 0.0D ? 0 : 1;
    }

    public static double square(double x)
    {
        return x * x;
    }

    public static double poly(double x, double a[])
    {
        double result = a[0];
        for(int i = 1; i < a.length; i++)
            result += a[i] * Math.pow(x, i);

        return result;
    }

    public static double localFromUniversal(double uTime, double zone)
    {
        return uTime + zone / 1440D;
    }

    public static double universalFromLocal(double lTime, double zone)
    {
        return lTime - zone / 1440D;
    }

    public static int locationOffset(double longitude, double zone)
    {
        return (int)(4D * longitude - zone);
    }

    public static double localFromStandard(double sTime, double offset)
    {
        return sTime + offset / 1440D;
    }

    public static double standardFromLocal(double lTime, double offset)
    {
        return lTime - offset / 1440D;
    }

    public static double momentFromJD(double jd)
    {
        return jd + -1721424.5D;
    }

    public static double jdFromMoment(double moment)
    {
        return moment - -1721424.5D;
    }

    public static int fixedFromJD(double jd)
    {
        return (int)Math.floor(momentFromJD(jd));
    }

    public static double jdFromFixed(int date)
    {
        return jdFromMoment(date);
    }

    public static double degrees(double theta)
    {
        return mod(theta, 360D);
    }

    public static double radiansToDegrees(double theta)
    {
        return degrees((theta / 3.1415926535897931D) * 180D);
    }

    public static double degreesToRadians(double theta)
    {
        return (degrees(theta) * 3.1415926535897931D) / 180D;
    }

    public static double sinDegrees(double theta)
    {
        return Math.sin(degreesToRadians(theta));
    }

    public static double cosDegrees(double theta)
    {
        return Math.cos(degreesToRadians(theta));
    }

    public static double tanDegrees(double theta)
    {
        return Math.tan(degreesToRadians(theta));
    }

    public static double arcTanDegrees(double x, int quad)
    {
        double deg = radiansToDegrees(Math.atan(x));
        return quad != 1 && quad != 4 ? deg + 180D : deg;
    }

    public static double arcSinDegrees(double x)
    {
        return radiansToDegrees(Math.asin(x));
    }

    public static double arcCosDegrees(double x)
    {
        return radiansToDegrees(Math.acos(x));
    }

    public static double localFromApparent(double moment)
    {
        return moment - equationOfTime(moment);
    }

    public static double apparentFromLocal(double moment)
    {
        return moment + equationOfTime(moment);
    }

    public static double solarMoment(int date, double latitude, double longitude, double riseOrSet)
    {
        double approx = (double)(new Gregorian(date)).dayNumber() + 0.5D + riseOrSet + longitude / -360D;
        double anomaly = 0.98560000000000003D * approx - 3.2890000000000001D;
        double sun = degrees(anomaly + 1.9159999999999999D * sinDegrees(anomaly) + 282.63400000000001D + 0.02D * sinDegrees(2D * anomaly));
        double rightAscension = arcTanDegrees(cosDegrees(23.441884000000002D) * tanDegrees(sun), 1 + quotient(sun, 90D));
        double declination = arcSinDegrees(sinDegrees(23.441884000000002D) * sinDegrees(sun));
        double local = (double)signum(riseOrSet) * arcCosDegrees((cosDegrees(90.833332999999996D) - sinDegrees(declination) * sinDegrees(latitude)) / cosDegrees(declination) / cosDegrees(latitude));
        return mod((local + rightAscension) / 360D - 0.27592D - 0.00273792D * approx, 1.0D);
    }

    public static double sunrise(int date, double latitude, double longitude)
    {
        return solarMoment(date, latitude, longitude, -0.25D);
    }

    public static double sunset(int date, double latitude, double longitude)
    {
        return solarMoment(date, latitude, longitude, 0.25D);
    }

    public static double universalFromEphemeris(double jd)
    {
        return jd - ephemerisCorrection(momentFromJD(jd));
    }

    public static double ephemerisFromUniversal(double jd)
    {
        return jd + ephemerisCorrection(momentFromJD(jd));
    }

    public static double julianCenturies(double moment)
    {
        return (ephemerisFromUniversal(moment) - J2000) / 36525D;
    }

    public static double ephemerisCorrection(double moment)
    {
        int year = Gregorian.yearFromFixed((int)moment);
        double theta = (double)difference(Gregorian.toFixed(1, 1, 1900), Gregorian.toFixed(7, 1, year)) / 36525D;
        double result;
        if(1988 <= year && year <= 2019)
            result = (double)(year - 1933) / 86400D;
        else
        if(1900 <= year && year <= 1987)
            result = poly(theta, ec.coeff19th);
        else
        if(1800 <= year && year <= 1899)
            result = poly(theta, ec.coeff18th);
        else
        if(1620 <= year && year <= 1799)
        {
            result = poly(year - 1600, ec.coeff17th) / 86400D;
        } else
        {
            double x = 0.5D + (double)difference(Gregorian.toFixed(1, 1, 1810), Gregorian.toFixed(1, 1, year));
            return ((x * x) / 41048480D - 15D) / 86400D;
        }
        return result;
    }

    public static double equationOfTime(double jd)
    {
        double c = (jd - J2000) / 36525D;
        double longitude = poly(c, et.coeffLongitude);
        double anomaly = poly(c, et.coeffAnomaly);
        double inclination = poly(c, et.coeffInclination);
        double eccentricity = poly(c, et.coeffEccentricity);
        double y = square(tanDegrees(inclination / 2D));
        return (y * sinDegrees(2D * longitude) + -2D * eccentricity * sinDegrees(anomaly) + 4D * eccentricity * y * sinDegrees(anomaly) * cosDegrees(2D * longitude) + -0.5D * y * y * sinDegrees(4D * longitude) + -1.25D * eccentricity * eccentricity * sinDegrees(2D * anomaly)) / 6.2831853071795862D;
    }

    public static double solarLongitude(double jd)
    {
        double c = julianCenturies(jd);
        double sigma = 0.0D;
        for(int i = 0; i < sl.coefficients.length; i++)
            sigma += (double)sl.coefficients[i] * Math.sin(sl.multipliers[i] * c + sl.addends[i]);

        double longitude = 4.9353929000000001D + 628.33196167999995D * c + 9.9999999999999995E-008D * sigma;
        return radiansToDegrees(longitude + aberration(c) + nutation(c));
    }

    public static double nutation(double c)
    {
        double a = poly(c, nu.coeffa);
        double b = poly(c, nu.coeffb);
        return -8.3399999999999994E-005D * sinDegrees(a) + -6.3999999999999997E-006D * sinDegrees(b);
    }

    public static double aberration(double c)
    {
        return 1.7E-006D * cosDegrees(177.63D + 35999.018479999999D * c) - 9.7299999999999993E-005D;
    }

    public static double dateNextSolarLongitude(double jd, double l)
    {
        double next = degrees(l * Math.ceil(solarLongitude(jd) / l));
        double lo = jd;
        double hi = jd + (l / 360D) * 400D;
        double x;
        for(x = (hi + lo) / 2D; hi - lo > 1.0000000000000001E-005D; x = (hi + lo) / 2D)
            if(next != 0.0D ? solarLongitude(x) >= next : l >= solarLongitude(x))
                hi = x;
            else
                lo = x;

        return x;
    }

    public static double lunarLongitude(double uTime)
    {
        double c = julianCenturies(uTime);
        double meanMoon = degrees(poly(c, ll.coeffMeanMoon));
        double elongation = degrees(poly(c, ll.coeffElongation));
        double solarAnomaly = degrees(poly(c, ll.coeffSolarAnomaly));
        double lunarAnomaly = degrees(poly(c, ll.coeffLunarAnomaly));
        double moonFromNode = degrees(poly(c, ll.coeffMoonFromNode));
        double e = poly(c, ll.coeffE);
        double sigma = 0.0D;
        for(int i = 0; i < ll.argsLunarElongation.length; i++)
        {
            double x = ll.argsSolarAnomaly[i];
            sigma += (double)ll.sineCoefficients[i] * Math.pow(e, Math.abs(x)) * sinDegrees((double)ll.argsLunarElongation[i] * elongation + x * solarAnomaly + (double)ll.argsLunarAnomaly[i] * lunarAnomaly + (double)ll.argsMoonFromNode[i] * moonFromNode);
        }

        double longitude = 9.9999999999999995E-007D * sigma;
        double venus = 0.0039579999999999997D * sinDegrees(119.75D + c * 131.84899999999999D);
        double jupiter = 0.00031799999999999998D * sinDegrees(53.090000000000003D + c * 479264.28999999998D);
        double flatEarth = 0.0019620000000000002D * sinDegrees(meanMoon - moonFromNode);
        return degrees(meanMoon + longitude + venus + jupiter + flatEarth + radiansToDegrees(nutation(c)));
    }

    public static double newMoonTime(int k)
    {
        double c = (double)k / 1236.8499999999999D;
        double JDE = poly(c, nm.coeffJDE);
        double e = poly(c, nm.coeffE);
        double solarAnomaly = poly(c, nm.coeffSolarAnomaly);
        double lunarAnomaly = poly(c, nm.coeffLunarAnomaly);
        double moonArgument = poly(c, nm.coeffMoonArgument);
        double omega = poly(c, nm.coeffOmega);
        double correction = -0.00017000000000000001D * sinDegrees(omega);
        for(int ix = 0; ix < nm.sineCoeff.length; ix++)
            correction += nm.sineCoeff[ix] * Math.pow(e, nm.eFactor[ix]) * sinDegrees((double)nm.solarCoeff[ix] * solarAnomaly + (double)nm.lunarCoeff[ix] * lunarAnomaly + (double)nm.moonCoeff[ix] * moonArgument);

        double additional = 0.0D;
        for(int ix = 0; ix < nm.addConst.length; ix++)
            additional += nm.addFactor[ix] * sinDegrees(nm.addConst[ix] + nm.addCoeff[ix] * (double)k + nm.addExtra[ix] * c * c);

        return universalFromEphemeris(JDE + correction + additional);
    }

    public static double newMoonAtOrAfter(double jd)
    {
        Gregorian date = new Gregorian((int)Math.floor(momentFromJD(jd)));
        int approx = (int)Math.floor((((double)((StandardDate) (date)).year + (double)date.dayNumber() / 365.25D) - 2000D) * 12.368499999999999D) - 1;
        int error = 0;
        for(int i = approx; newMoonTime(i) < jd; i++)
            error++;

        return newMoonTime(approx + error);
    }

    public static double newMoonBefore(double jd)
    {
        return newMoonAtOrAfter(newMoonAtOrAfter(jd) - 45D);
    }

    public static double lunarSolarAngle(double jd)
    {
        return degrees(lunarLongitude(jd) - solarLongitude(jd));
    }

    public static double lunarPhaseAtOrBefore(double phase, double jd)
    {
        boolean close = degrees(lunarSolarAngle(jd) - phase) < 40D;
        double yesterday = jd - 1.0D;
        double orig = 2451550.2599999998D + 29.530588853000001D * (phase / 360D);
        double epsilon = 9.9999999999999995E-007D;
        double tau = yesterday - mod(yesterday - orig, 29.530588853000001D);
        double lo = close ? jd - 4D : tau - 2D;
        double hi = close ? jd : tau + 2D;
        double x;
        for(x = (hi + lo) / 2D; hi - lo > epsilon; x = (hi + lo) / 2D)
        {
            double lunSolAngle = lunarSolarAngle(x);
            if(phase <= lunSolAngle && lunSolAngle <= phase + 90D)
                hi = x;
            else
                lo = x;
        }

        return x;
    }

    public static double newMoonAtOrBefore(double jd)
    {
        return lunarPhaseAtOrBefore(0.0D, jd);
    }

    public static double fullMoonAtOrBefore(double jd)
    {
        return lunarPhaseAtOrBefore(180D, jd);
    }

    public static double firstQuarterMoonAtOrBefore(double jd)
    {
        return lunarPhaseAtOrBefore(90D, jd);
    }

    public static double lastQuarterMoonAtOrBefore(double jd)
    {
        return lunarPhaseAtOrBefore(270D, jd);
    }

    public static double siderealFromJD(double jd)
    {
        double c = (jd - J2000) / 36525D;
        return poly(c, sfj.siderealCoeff) / 360D;
    }

    public String toString()
    {
        return getClass().getName() + "[" + toStringFields() + "]";
    }

    protected abstract String toStringFields();

    public abstract boolean equals(Object obj);

    public static final int JANUARY = 1;
    public static final int FEBRUARY = 2;
    public static final int MARCH = 3;
    public static final int APRIL = 4;
    public static final int MAY = 5;
    public static final int JUNE = 6;
    public static final int JULY = 7;
    public static final int AUGUST = 8;
    public static final int SEPTEMBER = 9;
    public static final int OCTOBER = 10;
    public static final int NOVEMBER = 11;
    public static final int DECEMBER = 12;
    public static final int SUNDAY = 0;
    public static final int MONDAY = 1;
    public static final int TUESDAY = 2;
    public static final int WEDNESDAY = 3;
    public static final int THURSDAY = 4;
    public static final int FRIDAY = 5;
    public static final int SATURDAY = 6;
    public static final int FIRST = 1;
    public static final int LAST = -1;
    public static final double JD_START = -1721424.5D;
    public static final double J2000 = jdFromMoment(0.5D + (double)Gregorian.toFixed(1, 1, 2000));
    public static final double MEAN_TROPICAL_YEAR = 365.24219900000003D;
    public static final double MEAN_SYNODIC_MONTH = 29.530588853000001D;
    public static final double NEW = 0D;
    public static final double FIRST_QUARTER = 90D;
    public static final double FULL = 180D;
    public static final double LAST_QUARTER = 270D;

}


 