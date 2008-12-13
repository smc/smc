 
package org.panchanga.common;

import java.io.Serializable;

// Referenced classes of package calendrica:
//            ProtoDate

public class Time
    implements Cloneable, Serializable
{

    public Time()
    {
    }

    public Time(double moment)
    {
        fromMoment(moment);
    }

    public Time(int hour, int minute, double second)
    {
        this.hour = hour;
        this.minute = minute;
        this.second = second;
    }

    public static double toMoment(int hour, int minute, double second)
    {
        return (double)hour / 24D + (double)minute / 1440D + second / 86400D;
    }

    public double toMoment()
    {
        return toMoment(hour, minute, second);
    }

    public void fromMoment(double moment)
    {
        hour = (int)Math.floor(ProtoDate.mod(moment * 24D, 24D));
        minute = (int)Math.floor(ProtoDate.mod(moment * 24D * 60D, 60D));
        second = ProtoDate.mod(moment * 24D * 60D * 60D, 60D);
    }

    public String toString()
    {
        return getClass().getName() + "[hour=" + hour + ",minute=" + minute + ",second=" + second + "]";
    }

    public boolean equals(Object obj)
    {
        if(this == obj)
            return true;
        if(!(obj instanceof Time))
            return false;
        Time o = (Time)obj;
        return o.hour == hour && o.minute == minute && o.second == second;
    }

    public int hour;
    public int minute;
    public double second;
}



 