# SOTA-logger
Simple app to log SOTA contacts and convert from csv to ADIF logs

http://www.adif.org.uk/
Sample ADI File
Generated on 2011-11-22 at 02:15:23Z for WN4AZY

<adif_ver:5>3.0.5
<programid:7>monolog
<USERDEF1:14:N>EPC
<USERDEF2:19:E>SweaterSize,{S,M,L}
<USERDEF3:15:N>ShoeSize,{5:20}

<EOH>

<qso_date:8>19900620
<time_on:4>1523
<call:5>VK9NS
<band:3>20M
<mode:4>RTTY
<sweatersize:1>M
<shoesize:2>11
<app_monolog_compression:3>off
<eor>

<qso_date:8>20101022
<time_on:4>0111
<call:5>ON4UN
<band:3>40M
<mode:3>PSK
<submode:5>PSK63
<epc:5>32123
<app_monolog_compression:3>off
<eor>


From http://www.sotadata.org.uk/ActivatorCSVInfo.htm

SOTA Activator TSV/CSV file format

 

This facility lets you upload a large number of QSOs in one bulk transaction. You need to create a Comma Separated Variable (CSV) or Tab Separated Variable (TSV) file with the fields laid out as shown in the example below. You then submit this file, which is checked for errors before presenting you with the option to save the QSOs to your database. You can mix activation records, chaser records and S2S (summit to summit) records all in the same file. When you import an activation the chase and S2S records are ignored. If your file includes chaser and S2S records you must import the file as both an activation and a chaser for all records to be imported. You can include multiple activations in this file but all records for each activation must be together. Each activation is deemed to end when the <My Summit> reference changes. If you activate the same summit on several days you must upload each activation in a separate file otherwise the file will be assumed to only contain a single activation.

The new prefered Version 2 (V2) format consists of upto ten fields as follows

<V2> <My Callsign><My Summit> <Date> <Time> <Band> <Mode> <His Callsign>

or

<V2> <My Callsign><My Summit> <Date> <Time> <Band> <Mode> <His Callsign><His Summit>

or

<V2> <My Callsign><My Summit> <Date> <Time> <Band> <Mode> <His Callsign><His Summit> <Notes or Comments>

Each field is separated by either a Comma (CSV) or Tab (TSV). Each QSO is a single record and there is one record to a line, terminated in <CR><LF>.

Here is an example:

V2,G3WGV,G/LD-008,24/04/03,1202,7.0MHz,CW,G4ELZ,
V2,G3WGV,G/LD-008,24/04/03,1204,7.0MHz,CW,G3NOH,,PSE QSL Direct
V2,G3WGV,G/LD-008,24/04/03,1227,144MHz,FM,GW4GTE,,Dave
V2,G3WGV,G/LD-008,24/04/03,1228,144MHz,FM,GW0TLK/M
V2,G3WGV,G/SC-008,08/06/03,1404,7.0MHz,CW,GM0AAA/P
V2,G3WGV,G/SC-008,08/06/03,1405,7.0MHz,CW,ON4CK/P
V2,G3WGV,G/SC-008,08/06/03,1407,7.0MHz,CW,DL0DAN/P
V2,G3WGV,G/SC-008,08/06/03,1410,14.0MHz,CW,YU7LS

Field notes

Field

Comments

My Callsign

This is the callsign you used for the QSO. No spaces in the callsign please

My Summit

This MUST be the full SOTA reference of the summit you where activating, as shown in the above example

Date

The date of the QSO. Most date formats are accepted but be careful about USA vs. International date format.  Use of International date format (DD/MM/YY) is recommended

Time

The time in UTC. Either HHMM or HH:MM will work. Use the 24 hour clock!

Band

You can enter the frequency in MHz (14.285MHz) or pick from the following:

 

160m: 1.8MHz

 

80m: 3.5MHz

 

60m: 5MHz

 

40m: 7MHz

 

30m: 10MHz

 

20m: 14MHz

 

17m: 18MHz

 

15m: 21MHz

 

12m: 24MHz

 

10m: 28MHz

 

6m: 50MHz

 

2m: 144MHz

 

70cm: 432MHz

 

23cm: 1240MHz

Mode

CW, SSB, FM, Data, AM, Other work

His Callsign

The callsign of the station worked.  No spaces in the callsign please

His Summit

This field is only needed if the station was also activating a SOTA summit. This is the full SOTA reference of the summit the chasing station was activating, as shown in the above example. If there is no <His Summit> you can leave this blank. If there is a comment then you must insert a TAB or comma to mark the field as being blank. See entries for G3NOH or GW4GTE

Notes or Comments

An optional field for recording short notes about the QSO. This could include the Operator's name and location, Signal Report, QSL information, or almost anything else. ,
You can embed a TAB or comma in this field. If you do you must enclose the entire Notes field in double-quotes.

 

The easiest way to create your TSV/CSV file is using Excel.  This allows you to arrange your log data in columns then save it as either a TSV or CSV file.  Either is accepted by the SOTA program.

 

Common errors

Spaces in the callsigns.  Our callsigns do not have spaces in them!

Date or time out of order.  The input parser will show an error if the log is not in sequential order

Errors in the SOTA reference number.  Spaces in the reference, leaving off the ITU prefix, or specifying a reference that does not exist will all result in an error being reported.

If an error is detected then it is shown in Red and you should then modify the file to correct the error and resubmit it. Once you get an error free report, you should carefully check that everything is correct before saving it. As soon as you have saved the data you will be able to see the effect in the various Activator tables.