package org.panchanga.indic;

import java.util.Date;

import org.panchanga.common.ProtoDate;
import org.panchanga.common.exception.BogusDateException;
import org.panchanga.gregorian.Gregorian;

/**
 * @author Santhosh.thottingal
 */
public class TamilCalendar {
    String ta_months[] = { "Cittirai","Vaikasi", "Ani", "Adi", "Avadi",
        "Purattasi", "Aippasi", "Karthikai", "Markazhi", "Tai", "Masi",
        "Paikuni",  };

    private int MSum(int start, int cond) {
        int total = 0;
        for (int i = start; HinduSolar.zodiac(HinduSolar.sunriseAtUjjain(i)) != cond; i++) {
            total++;
        }
        return total;
    }


 
    /**
     * malayaliHinduSolar[date_Integer] Input: Fixed number for RD date.
     * Output: Malayali calendar date of day at sunrise on RD date. Output may
     * differ from the actual Malayali calendar date by a day.
     * 
     * @throws BogusDateException
     */

    public void malayaliHinduSolar(Date date) throws BogusDateException {
        int year1 = 0, year2 = 0;
        double samk2 = 0;
        double srise2 = 0;
        int kyTime = OldHinduSolar.dayCount(Gregorian.toFixed(11, 4, 2008));

        /*
         * We find rise2 and month2 at kyTime + 1 because under certain
         * criteria, the Tamil calendar date is ahead of the HinduSolar
         * calendar date by a day.
         */

        double rise1 = HinduSolar.sunriseAtUjjain(kyTime);
        double rise2 = HinduSolar.sunriseAtUjjain(kyTime + 1);
        int month1 = HinduSolar.zodiac(rise1);
        int month2 = HinduSolar.zodiac(rise2);
        year1 = HinduSolar.calendarYear(rise1) - HinduSolar.SOLAR_ERA;
        // HinduSolar.SOLAR_ERA; = Years from Kali Yuga until Saka era. =
        // (AD+3101)-(AD-78) =3179

        int approx1 = kyTime - 3
        - ProtoDate.quotient(HinduSolar.solarLongitude(rise1) % 1800, 60);
        int begin1 = approx1 + MSum(approx1, month1);
        int day1 = kyTime - begin1 + 1;
        double samk1 = HinduSolar.samkranti(78 + year1, month1);
        double srise1 = HinduSolar.sunriseAtUjjain((int)OldHinduSolar
            .dayCount(Math.abs(samk1)))
            + OldHinduSolar.EPOCH;
        /*
         * srise1 is the IST for sunrise for the day of samk1 if the IST for
         * samk1 falls before midnight. Otherwise srise1 gives the IST for
         * sunrise for the following day. If the latter is true, then samk1
         * falls after sunset for the same day.
         */

        double sset1 = HinduSolar.sunsetAtUjjain((int)OldHinduSolar
            .dayCount(Math.abs(samk1)))
            + OldHinduSolar.EPOCH;

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
            double sset2 = HinduSolar.sunsetAtUjjain((int)OldHinduSolar
                .dayCount(Math.abs(samk1)))
                + OldHinduSolar.EPOCH;
            if ((srise2 <= samk2) && (samk2 < sset2)) {
                /*
                 * If samk1 falls between srise2 and sset2 on the same
                 * day, the Tamil rule and the Orissa rule will both agree.
                 */
                System.out.println(ta_months[month2 - 1] + "-"
                    + 1 + "-" + year2);
            }
            else {
                System.out.println(ta_months[(month2) - 1] + "-"
                    + (day1 + 1) + "-" +year2);
            }
        }

        if (month1 == month2) {
            if ((srise1 <= samk1) && (samk1 < sset1)) {
                /*
                 * If samk1 falls between srise1 and aparahna1 on the same
                 * day, the Tamil rule and the Orissa rule will both agree.
                 */
                System.out.println(ta_months[(month1) - 1] + "-"
                    + (day1 + 1) + "-" + year1);
            }
            else {
                System.out.println(ta_months[(month1) - 1] + "-"
                    + (day1) + "-" +   year1);
            }

        }

    }

    public static void main(String[] args) {
        TamilCalendar mlCalendar = new TamilCalendar();
        try {
            mlCalendar.malayaliHinduSolar(new Date());
        }
        catch (BogusDateException e) {
            e.printStackTrace();
        }
    }

}
