package org.panchanga.indic;

import java.util.Date;

import org.panchanga.common.ProtoDate;
import org.panchanga.common.exception.BogusDateException;
import org.panchanga.gregorian.Gregorian;

 


/**
 * @author Santhosh.thottingal
 */
public class OriyaCalendar {
    String or_months[] = { "Chaitra", "Baisakhi", "Jyaistha", "Ashadha", "Srabana", "Bhadrapada", "Asvina", "Karthika", "Margashira", "Pausa", "Magha", "Phalguna"};

    private int MSum(int start, int cond) {
        int total = 0;
        for (int i = start; HinduSolar.zodiac(HinduSolar.sunriseAtUjjain(i)) != cond; i++) {
            total++;
        }
        return total;
    }

    /**
     * oriyaHinduSolar[date_Integer] Input: Fixed number for RD date.
     * Output: Oriya calendar date of day at sunrise on RD date. 
     * 
     * @throws BogusDateException
     */

    public void oriyaHinduSolar(Date date) throws BogusDateException {
        int year = 0;
        int kyTime = OldHinduSolar.dayCount(Gregorian.toFixed(10, 28, 2008));
        /*
         * kyTime gives the number of days of RD date since the start of Kali
         * Yuga or we can say in Hindu moment.
         */
        /*
         * We find the rise, month, year, approx, begin and day at kyTime + 1
         * because the Orissa calendar date is ahead of the HinduSolar
         * calendar date by a day.
         */

        double rise = HinduSolar.sunriseAtUjjain(kyTime + 1);
        int month = HinduSolar.zodiac(rise);
        year = HinduSolar.calendarYear(rise) - HinduSolar.SOLAR_ERA;
        // HinduSolar.SOLAR_ERA; = Years from Kali Yuga until Saka era. =
        // (AD+3101)-(AD-78) =3179
        /* year determines the Saka year in which kyTime + 1 falls. */

        int approx = kyTime - 2
            - ProtoDate.quotient(HinduSolar.solarLongitude(rise) % 1800, 60);
        /*
         * approx is a day in Hindu moment that falls in the previous solar
         * month.
         */

        int begin = approx + MSum(approx, month);
        int day = kyTime - begin + 1;
        /*
         * day gives the day count from the starting day of month to kyTime +
         * 1.
         */
        day = day + 1;
        System.out.println("Year:" + year);
        System.out.println("Month:" +or_months[month-1]);
        System.out.println("Day:" + day);
    }

    public static void main(String[] args) {
        OriyaCalendar mlCalendar = new OriyaCalendar();
        try {
            mlCalendar.oriyaHinduSolar(new Date());
        }
        catch (BogusDateException e) {
            e.printStackTrace();
        }
    }

}
