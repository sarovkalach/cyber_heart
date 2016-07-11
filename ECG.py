#!/usr/bin/python
# coding: utf8
import numpy
import pylab
b=numpy.genfromtxt(open('workfile.csv','r'))
pylab.title(u'Диаграмма ЭКГ')
pylab.xlabel(u'Время, с')
pylab.ylabel(u' Потенциал')
pylab.plot(b[:,0],b[:,1],'g-')
pylab.grid(True)
pylab.show()
