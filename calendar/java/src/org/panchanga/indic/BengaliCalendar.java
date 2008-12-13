package org.panchanga.indic;

import java.util.Date;

import org.panchanga.common.ProtoDate;
import org.panchanga.common.exception.BogusDateException;
import org.panchanga.gregorian.Gregorian;




/**
 * @author Santhosh.thottingal
 */
public class BengaliCalendar {

    String bn_months[] = { "Boishakh", "Joishtho", "Asharh ", "Srabon ",
        "Bhadro ", "Ashshin ", "Kartik ", "Ogrohaeon ", "Poush ", "Magh ",
        "Falgun ", "Choitro", };

    private int MSum(int start, int cond) {
        int total = 0;
        for (int i = start; HinduSolar.zodiac(HinduSolar.sunriseAtUjjain(i)) != cond; i++) {
            total++;
        }
        return total;
    }
    private int bengaliYear(int month, int year) {

        if (1 <= month && month <= 4)
            return year - 593+78;
        else
            return year - 594+79;
    }

    /**
     * oriyaHinduSolar[date_Integer] Input: Fixed number for RD date.
     * Output: Bengali calendar date of day at sunrise on RD date. 
     * 
     * @throws BogusDateException
     */

    public void bengaliHinduSolar(Date date) throws BogusDateException {
        int year1 = 0, year2 = 0;
        double samk2 = 0;
        double srise2 = 0;
        double aparahna2 = 0;
        int kyTime = OldHinduSolar.dayCount(Gregorian.toFixed(10, 29, 2008));

        /* We find rise1, month1, year1, approx1, begin1 and day1 at kyTime - 1 because under certain criteria, the Bengal calendar date is behind the HinduSolar calendar date by a day. */

        double rise1 = HinduSolar.sunriseAtUjjain(kyTime - 1);
        double rise2 = HinduSolar.sunriseAtUjjain(kyTime);
        int month1 = HinduSolar.zodiac(rise1);
        int month2 = HinduSolar.zodiac(rise2);
        year1 = HinduSolar.calendarYear(rise1) - HinduSolar.SOLAR_ERA;
        // HinduSolar.SOLAR_ERA; = Years from Kali Yuga until Saka era. =
        // (AD+3101)-(AD-78) =3179

        int approx1 = kyTime - 4
            - ProtoDate.quotient(HinduSolar.solarLongitude(rise1) % 1800, 60);
        int begin1 = approx1 + MSum(approx1, month1);
        int day1 = kyTime - begin1;
        double samk1 = HinduSolar.samkranti(78 + year1, month1);
        /* srise1 is the IST for sunrise for the day of samk1 if the IST for samk1 falls before midnight. Otherwise srise1 gives the IST for sunrise for the following day. If the latter is true, then samk1 < srise1. */
        double srise1 = HinduSolar.sunriseAtUjjain((int)OldHinduSolar
            .dayCount(Math.abs(samk1)))
            + OldHinduSolar.EPOCH;

        /* midnight1 is the midnight following samk1. */
        double midnight1 = Math.floor(samk1) + 1;

        /* The explanation for aparahna1 is similar to that for srise1. */
        if (month1 != month2) {
            /*
             * If month1!= month2, then month2 is the new month. We need the
             * IST for the samkranti, the sunrise and the aparahna for the day
             * of the samkranti and the Saka year for month2.
             */
            year2 = HinduSolar.calendarYear(rise2) - HinduSolar.SOLAR_ERA;
            ;
            samk2 = HinduSolar.samkranti(78 + year2, month2);
            srise2 = HinduSolar.sunriseAtUjjain((int)OldHinduSolar
                .dayCount(Math.abs(samk2)))
                + OldHinduSolar.EPOCH;
            double midnight2 = Math.floor(samk1) + 1;
            if ((srise2 <= samk2) && (samk2 < midnight2)) {

                System.out.println(bn_months[(month2) - 1] + "-" + 1 + "-"
                    + bengaliYear(month2,year2));
            }
            if ((srise1 <= samk1) && (samk1 < midnight1)) {

                System.out.println(bn_months[(month2) - 1] + "-" + (day1 + 1)
                    + "-" + bengaliYear(month2,year2));
            }

        }

        if (month1 == month2) {
            if ((srise1 <= samk1) && (samk1 < midnight1)) {

                System.out.println(bn_months[month1 - 1] + "-" + (day1 + 1)
                    + "-" + bengaliYear(month1,year1));
            }
            else {
                System.out.println(bn_months[(month1) - 1] + "-" + (day1)
                    + "-" + bengaliYear(month1,year1));
            }

        }

    }

    public static void main(String[] args) {
        BengaliCalendar mlCalendar = new BengaliCalendar();
        try {
            mlCalendar.bengaliHinduSolar(new Date());
        }
        catch (BogusDateException e) {
            e.printStackTrace();
        }
    }

}
