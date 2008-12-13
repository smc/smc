/*jadclipse*/// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) radix(10) lradix(10) 
// Source File Name:   FixedVector.java

package org.panchanga.common;

import java.util.Vector;

public class FixedVector extends Vector
{

    public FixedVector(int initialCapacity, int capacityIncrement)
    {
        super(initialCapacity, capacityIncrement);
    }

    public FixedVector(int initialCapacity)
    {
        super(initialCapacity);
    }

    public FixedVector()
    {
    }

    public final synchronized void addFixed(int fixed)
    {
        super.addElement(new Integer(fixed));
    }

    public final synchronized int fixedAt(int index)
    {
        return ((Integer)super.elementAt(index)).intValue();
    }
}



 