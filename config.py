from csv import *
file1 = open("C:\\Users\\Administrator.SHBD-3\\Desktop\\project\\online_booking.csv" , "w" , newline = "")
file2 = open("C:\\Users\\Administrator.SHBD-3\\Desktop\\project\\online_booking1.csv" , "w" , newline = "")
file3 = open("C:\\Users\\Administrator.SHBD-3\\Desktop\\project\\online_booking2.csv" , "w" , newline = "")
data1 = writer(file1)
data2 = writer(file2)
data3 = writer(file3)
lst1 = [[1 , 'DL34Q1420' , 'Delhi' , 'Dehradun' , '1300'] , [2 , 'DL23E3546' , 'Delhi' , 'Dehradun' , '1550'] , [3 , "DL47A3784" , 'Delhi' , 'Dehradun' , '2100'] , [1 , "DL98F6789" , "Delhi" , "Manali" , "0200"] , [2 , "DL98R6795" , "Delhi" , "Manali" , "0845"] , [3 , "DL67B7440" , "Delhi" , "Manali" , "1550"] , [1 , "DL64K7034" , "Delhi" , "Shimla" , "0110"] , [2 , "DL87T6479" , "Delhi" , "Shimla" , "1025"] , [3 , "DL45D1298" , "Delhi" , "Shimla" , "1500"]]
lst2 = [[1 , "MH54F4125" , "Mumbai" , "Dehradun" , '1800'] , [2 , "MH42D4512" , "Mumbai" , "Dehradun" , "2100"] , [3 , "MH84C5410" , "Mumbai" , "Dehradun" , "2350"] , [1 , "MH04V5410" , "Mumbai" , "Manali" , "0500"] , [2 , "MH35Z2465" , "Mumbai" , "Manali" , "0730"] , [3 , "MH87A1450" , "Mumbai" , "Manali" , "2130"] , [1 , "MH51M5421" , "Mumbai" , "Shimla" , "0345"] , [2 , "MH78M1541" , "Mumbai" , "Shimla" , "1655"] , [3 , "MH84T9451" , "Mumbai" , "Shimla" , "2135"]]
lst3 = [[1 , "WB65V5451" , "Kolkata" , "Dehradun" , "1100"] , [2 , "WB54H5420" , "Kolkata" , "Dehradun" , "1830"] , [3 , "WB54T5472" , "Kolkata" , "Dehradun" , "2145"] , [1 , "WB45T5789" , "Kolkata" , "Manali" , "0530"] , [2 , "WB98X3549" , "Kolkata" , "Manali" , "2150"] , [3 , "WB78B1579" , "Kolkata" , "Manali" , "2340"] , [1 , "WB85F4568" , "Kolkata" , "Shimla" , "1250"] , [2 , "WB25Y9878" , "Kolkata" , "Shimla" , "1500"] , [3 , "WB39L6945" , "Kolkata" , "Shimla" , "2120"]]
data1.writerows(lst1)
data1.writerows(lst2)
data1.writerows(lst3)
lst4 = [[1 , "22439" , "NDLS" , "JAT" , "0600"] , [2 , "02425" , "NDLS" , "JAT" , "2110"] , [3 , "02461" , "NDLS" , "JAT" , "1730"] , [1 , "02952" , "NDLS" , "KOTA" , "1700"] , [2 , "02416" , "NDLS" , "KOTA" , "2200"] , [3 , "02926" , "NDLS" , "KOTA" , "1645"] , [1 , "02002" , "NDLS" , "MTJ" , "0530"] , [2 , "02626" , "NDLS" , "MTJ" , "1135"] , [3 , "06528" , "NDLS" , "MTJ" , "2135"]]
lst5 = [[1 , "09027" , "MMCT" , "JAT" , "1215"] , [2 , "07596" , "MMCT" , "JAT" , "1545"] , [3 , "10647" , "MMCT" , "JAT" , "2150"] , [1 , "02951" , "MMCT" , "KOTA" , "1730"] , [2 , "02953" , "NDLS" , "KOTA" , "1740"] , [3 , "02413" , "MMCT" , "KOTA" , "1825"] , [1 , "02953" , "MMCT" , "MTJ" , "1740"] , [2 , "02903" , "MMCT" , "MTJ" , "2125"] , [3 , "02925" , "MMCT" , "MTJ" , "1200"]]
lst6 = [[1 , "02331" , "KOAA" , "JAT" , "2355"] , [2 , "22317" , "KOAA" , "JAT" , "1310"] , [3 , "13151" , "KOAA" , "JAT" , "1145"] , [1 , "12938" , "KOAA" , "KOTA" , "2300"] , [2 , "18009" , "KOAA" , "KOTA" , "1300"] , [3 , "19607" , "KOAA" , "KOTA" , "1125"] , [1 , "02496" , "KOAA" , "MTJ" , "2245"] , [2 , "12319" , "KOAA" , "MTJ" , "1310"] , [3 , "13167" , "KOAA" , "MTJ" , "1210"]]
data2.writerows(lst4)
data2.writerows(lst5)
data2.writerows(lst6)
lst7 = [[1 , "UK995" , "DEL" , "BOM" , "1810"] , [2 , "AI887" , "DEL" , "BOM" , "0650"] , [3 , "G8324" , "DEL" , "BOM" , "1840"] , [1 , "G8336" , "DEL" , "CCU" , "2035"] , [2 , "AI176" , "DEL" , "CCU" , "1200"] , [3 , "I5993" , "DEL" , "CCU" , "0815"] , [1 , "UK833" , "DEL" , "MAA" , "0815"] , [2 , "AI429" , "DEL" , "MAA" , "0955"] , [3 , "6E2406" , "DEL" , "MAA" , "0930"]]
lst8 = [[1 , "G8321" , "BOM" , "DEL" , "1830"] , [2 , "SG779" , "BOM" , "DEL" , "0600"] , [3 , "UK970" , "BOM" , "DEL" , "0845"] , [1 , "G8322" , "BOM" , "CCU" , "2135"] , [2 , "SG384" , "BOM" , "CCU" , "1950"] , [3 , "I5802" , "BOM" , "CCU" , "0540"] , [1 , "SG323" , "BOM" , "MAA" , "2105"] , [2 , "G8302" , "BOM" , "MAA" , "2035"] , [3 , "UK825" , "BOM" , "MAA" , "0820"]]
lst9 = [[1 , "G8303" , "MAA" , "BOM" , "1650"] , [2 , "SG322" , "MAA" , "BOM" , "0630"] , [3 , "UK826" , "MAA" , "BOM" , "1145"] , [1 , "AI440" , "MAA" , "DEL" , "0620"] , [2 , "UK838" , "MAA" , "DEL" , "1200"] , [3 , "SG8139" , "MAA" , "DEL" , "2125"] , [1 , "I5811" , "MAA" , "CCU" , '0750'] , [2 , "SG3309" , "MAA" , "CCU" , "1735"] , [3 , "6E545" , "MAA" , "CCU" , "0810"]]
lst10 = [[1 , "I5911" , "CCU" , "DEL" , "1745"] , [2 , "G8833" , "CCU" , "DEL" , "1420"] , [3 , "UK738" , "CCU" , "DEL" , "1230"] , [1 , "I5510" , "CCU" , "BOM" , " 0510"] , [2 , "G8102" , "CCU" , "BOM" , "1650"] , [3 , "6E328" , "CCU" , "BOM" , "2345"] , [1 , "I5510" , "CCU" , "MAA" , "0510"] , [2 , "6E456" , "CCU" , "MAA" , "1200"] , [3 , "AI9745" , "CCU" , "MAA" , "0800"]]
data3.writerows(lst7)
data3.writerows(lst8)
data3.writerows(lst9)
data3.writerows(lst10)
file1.close()
file2.close()
file3.close()



