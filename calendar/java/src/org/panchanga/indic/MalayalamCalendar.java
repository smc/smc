package org.panchanga.indic;

import java.util.Date;

import org.panchanga.common.ProtoDate;
import org.panchanga.common.exception.BogusDateException;
import org.panchanga.gregorian.Gregorian;

 


/**
 * @author Santhosh.thottingal
 */
public class MalayalamCalendar {
    String ml_months[] = { "chingam", "kanni", "thulam", "vrishchikam",
        "dhanu", "makaram", "kumbham", "meenam", "medam", "edavam",
        "midhunam", "karkkidakam", };

    private int MSum(int start, int cond) {
        int total = 0;
        for (int i = start; HinduSolar.zodiac(HinduSolar.sunriseAtUjjain(i)) != cond; i++) {
            total++;
        }
        return total;
    }

 

    /*
     * ujjainAparahna[kyTime_] Input : Hindu moment. Output : Hindu moment.
     * We're computing the IST for aparahna at Ujjain. Accuracy tested within
     * about 5 minutes.
     */
    private double ujjainAparahna(int kyTime) {
        return HinduSolar.sunriseAtUjjain(kyTime) + 0.6
            * (HinduSolar.sunriseAtUjjain(kyTime) - HinduSolar.sunriseAtUjjain(kyTime));
    }

    /*
     * Input: (solar)month number. Output: malayali month number. The Malayali
     * calendar uses the Kollem era, not the Saka traditional era. Starting
     * month of the nirayana year is month 5, the solar month that links with
     * rasi 5. For example, if month = 5, then malayaliMonth = 1.
     */
    private int malayaliMonth(int month) {

        return HinduSolar.adjustedMod(month - 4, 12);
    }

    /*
     * malayaliYear[m_, n_] Input : (solar) month and Saka year. Output :
     * Kollem year. The Malayali calendar uses the Kollem era, not the Saka
     * traditional era. Starting month of the nirayana year is month 5, the
     * solar month that links with rasi 5. Hence malayaliYear number changes
     * to a new year at month 5 and not month 1. =AD-824 or AD-825. Saka=
     * AD-78
     */
    private int malayaliYear(int month, int year) {

        if (1 <= month && month <= 4)
            return year - 747;
        else
            return year - 746;
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
        double aparahna2 = 0;
        int kyTime = OldHinduSolar.dayCount(Gregorian.toFixed(12, 27, 2009));
		System.out.println("Day Count" + kyTime);
		System.out.println("Gregorian.toFixed"+Gregorian.toFixed(12, 27, 2009));
        /*
         * We find rise2 and month2 at kyTime + 1 because under certain
         * criteria, the Malayali calendar date is ahead of the HinduSolar
         * calendar date by a day. Then we make necessary changes to obtain
         * the malayaliMonth and malayaliYear.
         */
        double rise1 = HinduSolar.sunriseAtUjjain(kyTime);
        System.out.println("Sunrise Ujjain" + rise1);
        double rise2 = HinduSolar.sunriseAtUjjain(kyTime + 1);
        int month1 = HinduSolar.zodiac(rise1);
        System.out.println("Month1 "+ month1);
        
        int month2 = HinduSolar.zodiac(rise2);
        System.out.println("Month2 "+ month2);
        year1 = HinduSolar.calendarYear(rise1) - HinduSolar.SOLAR_ERA;
        // HinduSolar.SOLAR_ERA; = Years from Kali Yuga until Saka era. =
        // (AD+3101)-(AD-78) =3179
        System.out.println("HinduSolar.calendarYear(rise1)"+ HinduSolar.calendarYear(rise1) );
        
        System.out.println("Year1 "+ year1);
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
        double aparahna1 = ujjainAparahna((int)OldHinduSolar.dayCount(Math
            .abs(samk1)))
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
            aparahna2 = ujjainAparahna((int)OldHinduSolar.dayCount(Math
                .abs(samk2)))
                + OldHinduSolar.EPOCH;
            if ((srise2 <= samk2) && (samk2 < aparahna2)) {
                /*
                 * If samk1 falls between srise1 and aparahna1 on the same
                 * day, the Malayali rule and the Orissa rule will both agree.
                 */
                System.out.println(ml_months[malayaliMonth(month2) - 1] + "-"
                    + 1 + "-" + malayaliYear(month2, year2));
            }
            else {
                System.out.println(ml_months[malayaliMonth(month2) - 1] + "-"
                    + (day1 + 1) + "-" + malayaliYear(month2, year2));
            }
        }
        System.out.println(month1);
        if (month1 == month2) {
            if ((srise1 <= samk1) && (samk1 < aparahna1)) {
                /*
                 * If samk1 falls between srise1 and aparahna1 on the same
                 * day, the Malayali rule and the Orissa rule will both agree.
                 */
                System.out.println(ml_months[malayaliMonth(month1) - 1] + "-"
                    + (day1 + 1) + "-" + malayaliYear(month1, year1));
            }
            else {
                System.out.println(ml_months[malayaliMonth(month1) - 1] + "-"
                    + (day1) + "-" + malayaliYear(month1, year1));
            }

        }

    }

    public static void main(String[] args) {
        MalayalamCalendar mlCalendar = new MalayalamCalendar();
        try {
            mlCalendar.malayaliHinduSolar(new Date());
        }
        catch (BogusDateException e) {
            e.printStackTrace();
        }
    }

}
