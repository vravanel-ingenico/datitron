#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gperrio
#
# Created:     16/11/2012
# Copyright:   (c) gperrio 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

month2016 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month2017 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month2018 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getDay(nDay, month):
    i = 1

    while nDay - month[i] > 0 and i < 12:
        nDay = nDay - month[i]
        i = i + 1
    pass

    return nDay, i

def main():
    yPrefix2016 = "2016"
    yPrefix2017 = "2017"
    yPrefix2018 = "2018"
    offset2016 = 3
    offset2017 = 1
    offset2018 = 0

    while 1:
        cMonth = month2016;
        cOffset = offset2016
        yPrefix = yPrefix2016
        
        i = raw_input()

        if i == "":
            break
        pass

        if i[0] == '7':
            cMonth = month2017
            cOffset = offset2017
            yPrefix = yPrefix2017
        pass
		
        if i[0] == '8':
            cMonth = month2018
            cOffset = offset2018
            yPrefix = yPrefix2018
        pass
        
        if len(i) != 5 or i[0] != '6' and i[0] != '7' and i[0] != '8' or i[4] > '5' or i[3] != '.':
            continue
        pass

        nWeek = int(i[1])*10 + int(i[2])

        if nWeek > 52:
            continue
        pass

        nDay = cOffset + (nWeek-1)*7 + int(i[4])

        realDay, nMonth = getDay(nDay, cMonth)

        print i, " -> ", realDay, nMonth, yPrefix, "\n"
    pass

if __name__ == '__main__':
    main()
