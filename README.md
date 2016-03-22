# FSH_coverage_measurements

Script to use for coverage measurements with FSH8.  Waterfall plot, position vs freq and histogram plotted.  CSV file is saved to disk with 
max power in measurement band at freq and posistion.

Usage:
1. Setup FSH frequency band. i.e. for GSM measurements you might sweep from 920 to 980MHz. Set required RBW and select trace to clear.
2. Connect FSH to PC via USB or LAN and open FSH View.  
3. Make sure GPS is connected and has a pos fix.
4. In FSH View, instrument menu, choose multiple transfer. Select continuous updates and choose time interval. Choose output folder. Press start.
5. Wait for measurements to complete and press stop.
6. Save python script in output folder.
7. Select antenna cal file
8. In Google earth Pro import data: File -> import -> choose output file.csv
9. Apply style template
10. Create new
11. Color tab: Set color from field, select 3rd field(E field)
12. Select start end end colors from palette. 
13. Make number of buckets 64.
14.  Icon tab: Use same icon for all fields. Choose the one without the line around it.
15. Heigth tab: Set height from field, select field 3, Mapping method to continuous.
16. Press OK.  (You can save the template but it ddoes not save all the setttings - bug in google earth 7.1.5.1557)

Notes: Play around with the import settings to get what you want.

TO DO: Automate klm generation from python.
