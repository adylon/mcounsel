"""
Created on 05/23/2023 at 22:31:54
author@ Jonathan Estrada

"""

import tkinter as tk
from tkinter import ttk
import sqlite3

# STARTING SQLITE3 --- 

sql = sqlite3.connect("mcdb.db")

# STARTING SQL CURSOR ---

sqlx = sql.cursor()

# USERNAME AND PASSWORD STORED IN DICTIONARY --- mc45132232023250

up_dic = {

    "Username": ["raul", "sudip"],
    "Password": ["1"]

}


# EMPLOYEE RECORD FETCHALL --- 

def ERF(tree):
    # CLOSING THE ERROR WINDOW ---

    def ERF_CW(clse):
        clse.destroy()

    try:
        erfch = sqlx.execute("SELECT rowid, * FROM EMPLOYEE_RECORD").fetchall()

        for dtree in tree.get_children():
            tree.delete(dtree)

        tree["column"] = ("Index", "ID", "FirstName", "LastName", "NickName", "ID1",
                          "ID2", "Address", "City", "State", "ZipCode", "Phone1", "Email", "BirthDate",
                          "HireDate", "LastRaiseDate", "EmergencyPhone", "EmergencyContact", "W4Allowances",
                          "W4Status", "ID3", "Rate", "Position", "AccessCode", "Picture", "Language",
                          "FoodHandlerCertDate", "BartenderCardDate", "RequireCard", "EnforceScheduling",
                          "ExtendRights", "ClockInOutOnly", "FingerprintAtClockIn", "FingerprintRequired",
                          "ID4", "Level", "Deleted")

        tree["show"] = "headings"

        for ercl in tree["column"]:
            tree.heading(ercl, text=ercl)

        for erins in erfch:
            tree.insert("", "end", values=(erins[0], erins[1], erins[2], erins[3],
                                           erins[4], erins[5], erins[6], erins[7], erins[8], erins[9], erins[10],
                                           erins[11], erins[12], erins[13], erins[14], erins[15], erins[16], erins[17],
                                           erins[18], erins[19], erins[20], erins[21], erins[22], erins[23], erins[24],
                                           erins[25], erins[26], erins[27], erins[28], erins[29], erins[30], erins[31],
                                           erins[32], erins[33], erins[34], erins[35], erins[36]))

    except:
        # ERROR WINDOW FOR EMPLOYEE RECORD

        ewer = tk.Toplevel()

        # Gets the requested values of the height and widht.

        ewerwW = ewer.winfo_reqwidth()
        ewerwH = ewer.winfo_reqheight()

        # Gets both half the screen width/height and window width/height

        ewerR = int(ewer.winfo_screenwidth() / 2 - ewerwW / 2)
        ewerD = int(ewer.winfo_screenheight() / 2 - ewerwH / 2)

        # Positions the window in the center of the page.

        ewer.geometry("+{}+{}".format(ewerR, ewerD))
        ewer.title("Error")
        ewer.geometry("300x150")

        # LABEL FOR ERROR EMPLOYEE SALES TOTALS RECORD ---

        leer = tk.Label(
            ewer, bg='#F7F6EE',
            text="Employee Record is Empty", anchor='c')
        leer.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

        # "OK" BUTTON FOR EMPLOYEE SALES TOTALS RECORD ---

        okerbtt = ttk.Button(ewer, text='OK', command=lambda: ERF_CW(ewer))
        okerbtt.place(relx=.17, rely=.55, relwidth=.31, relheight=.2)

        # "CANCEL" BUTTON FOR EMPLOYEE SALES TOTALS RECORD ---

        clerbtt = ttk.Button(ewer, text='Cancel', command=lambda: ERF_CW(ewer))
        clerbtt.place(relx=.52, rely=.55, relwidth=.31, relheight=.2)

        ewer.mainloop()


# CHECK RECORD FETCHALL --- 

def CRF(tree):
    # CLOSING THE ERROR WINDOW ---

    def CRF_CW(clse):
        clse.destroy()


    try:
        crfch = sqlx.execute("SELECT rowid, * FROM CHECK_RECORD").fetchall()

        for dtree in tree.get_children():
            tree.delete(dtree)

        tree["column"] = ("Index", "ID", "NumberOfSeats", "FlagsTransferred", "TimeOpened",
                          "OpenerID", "OpenerName", "OwnerID", "OwnerName", "OwnerTimeCardID", "TimeClosed",
                          "CloserID", "CloserName", "CloserTimeCardID", "StationClosedID", "Table",
                          "Guests", "OrderTypeID", "RevenueCenterID", "StationOpenedID", "TransfererID",
                          "TransfererName", "TransferTime", "Total", "TaxableSales1", "FlagsTabNameEntered",
                          "FlagsTabNameEntered", "DiscountTotalAmount", "FlagsReopened", "TimeReopened",
                          "FlagsUsed")

        tree["show"] = "headings"

        for crcl in tree["column"]:
            tree.heading(crcl, text=crcl)

        for crins in crfch:
            tree.insert("", "end", values=(crins[0], crins[1], crins[2], crins[3], crins[4],
                                           crins[5], crins[6], crins[7], crins[8], crins[9], crins[10], crins[11],
                                           crins[12], crins[13], crins[14], crins[15], crins[16], crins[17], crins[18],
                                           crins[19], crins[20], crins[21], crins[22], crins[23], crins[24], crins[25],
                                           crins[26], crins[27], crins[28], crins[29], crins[30]))

    except:
        # ERROR WINDOW FOR CHECK RECORD

        ewcr = tk.Toplevel()

        # Gets the requested values of the height and widht.

        ewcrwW = ewcr.winfo_reqwidth()
        ewcrwH = ewcr.winfo_reqheight()

        # Gets both half the screen width/height and window width/height

        ewcrR = int(ewcr.winfo_screenwidth() / 2 - ewcrwW / 2)
        ewcrD = int(ewcr.winfo_screenheight() / 2 - ewcrwH / 2)

        # Positions the window in the center of the page.

        ewcr.geometry("+{}+{}".format(ewcrR, ewcrD))
        ewcr.title("Error")
        ewcr.geometry("300x150")

        # LABEL FOR ERROR CHECK RECORD ---

        lecr = tk.Label(
            ewcr, bg='#F7F6EE',
            text="Check Record is Empty", anchor='c')
        lecr.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

        # "OK" BUTTON FOR CHECK RECORD ---

        okcrbtt = ttk.Button(ewcr, text='OK', command=lambda: CRF_CW(ewcr))
        okcrbtt.place(relx=.17, rely=.55, relwidth=.31, relheight=.2)

        # "CANCEL" BUTTON FOR CHECK RECORD ---

        clcrbtt = ttk.Button(ewcr, text='Cancel', command=lambda: CRF_CW(ewcr))
        clcrbtt.place(relx=.52, rely=.55, relwidth=.31, relheight=.2)

        ewcr.mainloop()


# SEAT RECORD FETCHALL --- 

def SRF(tree):
    # CLOSING THE ERROR WINDOW ---

    def SRF_CW(clse):
        clse.destroy()


    try:
        srfch = sqlx.execute("SELECT rowid, * FROM SEAT_RECORD").fetchall()

        for dtree in tree.get_children():
            tree.delete(dtree)

        tree["column"] = ("Index", "CheckInternal", "SeatNumber", "Key", "FlagsUsed",
                          "Subtotal", "Total", "TaxTotal1", "CreditCardSurcharge", "ItemDiscountTotal")

        tree["show"] = "headings"

        for srcl in tree["column"]:
            tree.heading(srcl, text=srcl)

        for srins in srfch:
            tree.insert("", "end", values=(srins[0], srins[1], srins[2], srins[3],
                                           srins[4], srins[5], srins[6], srins[7], srins[8], srins[9]))

    except:
        # ERROR WINDOW FOR SEAT RECORD

        ewsr = tk.Toplevel()

        # Gets the requested values of the height and widht.

        ewsrwW = ewsr.winfo_reqwidth()
        ewsrwH = ewsr.winfo_reqheight()

        # Gets both half the screen width/height and window width/height

        ewsrR = int(ewsr.winfo_screenwidth() / 2 - ewsrwW / 2)
        ewsrD = int(ewsr.winfo_screenheight() / 2 - ewsrwH / 2)

        # Positions the window in the center of the page.

        ewsr.geometry("+{}+{}".format(ewsrR, ewsrD))
        ewsr.title("Error")
        ewsr.geometry("300x150")

        # LABEL FOR ERROR SEAT RECORD ---

        lesr = tk.Label(
            ewsr, bg='#F7F6EE',
            text="Seat Record is Empty", anchor='c')
        lesr.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

        # "OK" BUTTON FOR SEAT RECORD ---

        oksrbtt = ttk.Button(ewsr, text='OK', command=lambda: SRF_CW(ewsr))
        oksrbtt.place(relx=.17, rely=.55, relwidth=.31, relheight=.2)

        # "CANCEL" BUTTON FOR SEAT RECORD ---

        clsrbtt = ttk.Button(ewsr, text='Cancel', command=lambda: SRF_CW(ewsr))
        clsrbtt.place(relx=.52, rely=.55, relwidth=.31, relheight=.2)

        ewsr.mainloop()


# CHECK ITEM RECORD FETCHALL --- 

def CIRF(tree):
    # CLOSING THE ERROR WINDOW ---

    def CIRF_CW(clse):
        clse.destroy()


    try:
        cirfch = sqlx.execute("SELECT rowid, * FROM CHECK_ITEM_RECORD").fetchall()

        for dtree in tree.get_children():
            tree.delete(dtree)

        tree["column"] = ("Index", "SeatKey", "Key", "Position", "RecordNumber", "ID",
                          "GuestCheckName", "ReportGroupID", "SortKey", "StationID", "OwnerTimeCardID",
                          "OwnerID", "OwnerName", "TimeStamp", "Price", "FlagsPrintModifier", "ApprovedBy",
                          "TaxApplied1", "ItemKey", "PriceNumber", "Level", "FlagsKitchenComment",
                          "FlagsIncludeInPrice", "FlagsDiscounted", "DiscountAmount", "DiscountInternalID",
                          "Qty", "Extension")

        tree["show"] = "headings"

        for circl in tree["column"]:
            tree.heading(circl, text=circl)

        for cirins in cirfch:
            tree.insert("", "end", values=(cirins[0], cirins[1], cirins[2], cirins[3],
                                           cirins[4], cirins[5], cirins[6], cirins[7], cirins[8], cirins[9],
                                           cirins[10], cirins[11], cirins[12], cirins[13], cirins[14], cirins[15],
                                           cirins[16], cirins[17], cirins[18], cirins[19], cirins[20], cirins[21],
                                           cirins[22], cirins[23], cirins[24], cirins[25], cirins[26], cirins[27]))

    except:
        # ERROR WINDOW FOR CHECK ITEM RECORD

        ewcir = tk.Toplevel()

        # Gets the requested values of the height and widht.

        ewcirwW = ewcir.winfo_reqwidth()
        ewcirwH = ewcir.winfo_reqheight()

        # Gets both half the screen width/height and window width/height

        ewcirR = int(ewcir.winfo_screenwidth() / 2 - ewcirwW / 2)
        ewcirD = int(ewcir.winfo_screenheight() / 2 - ewcirwH / 2)

        # Positions the window in the center of the page.

        ewcir.geometry("+{}+{}".format(ewcirR, ewcirD))
        ewcir.title("Error")
        ewcir.geometry("300x150")

        # LABEL FOR ERROR CHECK ITEM RECORD ---

        lecir = tk.Label(
            ewcir, bg='#F7F6EE',
            text="Check Item Record is Empty", anchor='c')
        lecir.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

        # "OK" BUTTON FOR CHECK ITEM RECORD ---

        okcirbtt = ttk.Button(ewcir, text='OK', command=lambda: CIRF_CW(ewcir))
        okcirbtt.place(relx=.17, rely=.55, relwidth=.31, relheight=.2)

        # "CANCEL" BUTTON FOR CHECK ITEM RECORD ---

        clcirbtt = ttk.Button(ewcir, text='Cancel', command=lambda: CIRF_CW(ewcir))
        clcirbtt.place(relx=.52, rely=.55, relwidth=.31, relheight=.2)

        ewcir.mainloop()


# PAYMENT RECORD FETCHALL --- 

def PRF(tree):
    # CLOSING THE ERROR WINDOW ---

    def PRF_CW(clse):
        clse.destroy()


    try:
        prfch = sqlx.execute("SELECT rowid, * FROM PAYMENT_RECORD").fetchall()

        for dtree in tree.get_children():
            tree.delete(dtree)

        tree["column"] = ("Index", "SeatKey", "Key", "Position", "ID", "RevenueCenterID",
                          "Name", "Amount", "Tip", "OwnerID", "OwnerName", "OwnerTimeCardID", "StationID",
                          "TimeStamp", "FlagsVerified", "FlagsApproved", "FlagsTrack2Recorded", "Approval",
                          "Account", "CustomerName", "VoidID", "VoidEmployeeName", "TimeVoided", "VoidEmployeeID")

        tree["show"] = "headings"

        for prcl in tree["column"]:
            tree.heading(prcl, text=prcl)

        for prins in prfch:
            tree.insert("", "end", values=(prins[0], prins[1], prins[2], prins[3], prins[4],
                                           prins[5], prins[6], prins[7], prins[8], prins[9], prins[10], prins[11],
                                           prins[12],
                                           prins[13], prins[14], prins[15], prins[16], prins[17], prins[18], prins[19],
                                           prins[20],
                                           prins[21], prins[22], prins[23]))

    except:
        # ERROR WINDOW FOR PAYMENT RECORD

        ewpr = tk.Toplevel()

        # Gets the requested values of the height and widht.

        ewprwW = ewpr.winfo_reqwidth()
        ewprwH = ewpr.winfo_reqheight()

        # Gets both half the screen width/height and window width/height

        ewprR = int(ewpr.winfo_screenwidth() / 2 - ewprwW / 2)
        ewprD = int(ewpr.winfo_screenheight() / 2 - ewprwH / 2)

        # Positions the window in the center of the page.

        ewpr.geometry("+{}+{}".format(ewprR, ewprD))
        ewpr.title("Error")
        ewpr.geometry("300x150")

        # LABEL FOR ERROR PAYMENT RECORD ---

        lepr = tk.Label(
            ewpr, bg='#F7F6EE',
            text="Payment Record is Empty", anchor='c')
        lepr.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

        # "OK" BUTTON FOR PAYMENT RECORD ---

        okprbtt = ttk.Button(ewpr, text='OK', command=lambda: PRF_CW(ewpr))
        okprbtt.place(relx=.17, rely=.55, relwidth=.31, relheight=.2)

        # "CANCEL" BUTTON FOR PAYMENT RECORD ---

        clprbtt = ttk.Button(ewpr, text='Cancel', command=lambda: PRF_CW(ewpr))
        clprbtt.place(relx=.52, rely=.55, relwidth=.31, relheight=.2)

        ewpr.mainloop()


# DISCOUNT RECORD FETCHALL --- 

def DRF(tree):
    # CLOSING THE ERROR WINDOW ---

    def DRF_CW(clse):
        clse.destroy()


    try:
        drfch = sqlx.execute("SELECT rowid, * FROM DISCOUNT_RECORD").fetchall()

        for dtree in tree.get_children():
            tree.delete(dtree)

        tree["column"] = ("Index", "SeatKey", "Key", "Position", "ID", "IDExplicit",
                          "DiscountInternalID", "Amount", "TimeStamp", "ApprovedByID", "ApprovedByName",
                          "Source")

        tree["show"] = "headings"

        for drcl in tree["column"]:
            tree.heading(drcl, text=drcl)

        for drins in drfch:
            tree.insert("", "end", values=(drins[0], drins[1], drins[2], drins[3], drins[4],
                                           drins[5], drins[6], drins[7], drins[8], drins[9], drins[10], drins[11]))

    except:
        # ERROR WINDOW FOR DISCOUNT RECORD

        ewdr = tk.Toplevel()

        # Gets the requested values of the height and widht.

        ewdrwW = ewdr.winfo_reqwidth()
        ewdrwH = ewdr.winfo_reqheight()

        # Gets both half the screen width/height and window width/height

        ewdrR = int(ewdr.winfo_screenwidth() / 2 - ewdrwW / 2)
        ewdrD = int(ewdr.winfo_screenheight() / 2 - ewdrwH / 2)

        # Positions the window in the center of the page.

        ewdr.geometry("+{}+{}".format(ewdrR, ewdrD))
        ewdr.title("Error")
        ewdr.geometry("300x150")

        # LABEL FOR ERROR DISCOUNT RECORD ---

        ledr = tk.Label(
            ewdr, bg='#F7F6EE',
            text="Discount Record is Empty", anchor='c')
        ledr.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

        # "OK" BUTTON FOR DISCOUNT RECORD ---

        okdrbtt = ttk.Button(ewdr, text='OK', command=lambda: DRF_CW(ewdr))
        okdrbtt.place(relx=.17, rely=.55, relwidth=.31, relheight=.2)

        # "CANCEL" BUTTON FOR DISCOUNT RECORD ---

        cldrbtt = ttk.Button(ewdr, text='Cancel', command=lambda: DRF_CW(ewdr))
        cldrbtt.place(relx=.52, rely=.55, relwidth=.31, relheight=.2)

        ewdr.mainloop()


# DELETE RECORD FETCHALL --- 

def DLRF(tree):
    # CLOSING THE ERROR WINDOW ---

    def DLRF_CW(clse):
        clse.destroy()


    try:
        dlrfch = sqlx.execute("SELECT rowid, * FROM DELETE_RECORD").fetchall()

        for dtree in tree.get_children():
            tree.delete(dtree)

        tree["column"] = ("Index", "Key", "TimeStamp", "OwnerID", "OwnerName", "CheckID",
                          "Amount", "ItemName", "ApprovedByEmployeeID", "ApprovedByName", "ApprovedByTimeCardID")

        tree["show"] = "headings"

        for dlrcl in tree["column"]:
            tree.heading(dlrcl, text=dlrcl)

        for dlrins in dlrfch:
            tree.insert("", "end", values=(dlrins[0], dlrins[1], dlrins[2], dlrins[3],
                                           dlrins[4], dlrins[5], dlrins[6], dlrins[7], dlrins[8], dlrins[9], dlrins[10]))

    except:
        # ERROR WINDOW FOR DELETE RECORD

        ewdlr = tk.Toplevel()

        # Gets the requested values of the height and widht.

        ewdlrwW = ewdlr.winfo_reqwidth()
        ewdlrwH = ewdlr.winfo_reqheight()

        # Gets both half the screen width/height and window width/height

        ewdlrR = int(ewdlr.winfo_screenwidth() / 2 - ewdlrwW / 2)
        ewdlrD = int(ewdlr.winfo_screenheight() / 2 - ewdlrwH / 2)

        # Positions the window in the center of the page.

        ewdlr.geometry("+{}+{}".format(ewdlrR, ewdlrD))
        ewdlr.title("Error")
        ewdlr.geometry("300x150")

        # LABEL FOR ERROR DELETE RECORD ---

        ledlr = tk.Label(
            ewdlr, bg='#F7F6EE',
            text="Delete Record is Empty", anchor='c')
        ledlr.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

        # "OK" BUTTON FOR DELETE RECORD ---

        okdlrbtt = ttk.Button(ewdlr, text='OK', command=lambda: DLRF_CW(ewdlr))
        okdlrbtt.place(relx=.17, rely=.55, relwidth=.31, relheight=.2)

        # "CANCEL" BUTTON FOR DELETE RECORD ---

        cldlrbtt = ttk.Button(ewdlr, text='Cancel', command=lambda: DLRF_CW(ewdlr))
        cldlrbtt.place(relx=.52, rely=.55, relwidth=.31, relheight=.2)

        ewdlr.mainloop()


# TIME CARD RECORD FETCHALL --- 

def TCRF(tree):
    # CLOSING THE ERROR WINDOW ---

    def TCRF_CW(clse):
        clse.destroy()


    try:
        tcrfch = sqlx.execute("SELECT rowid, * FROM TIME_CARD_RECORD").fetchall()

        for dtree in tree.get_children():
            tree.delete(dtree)

        tree["column"] = ("Index", "ID", "OwnerID", "JobID", "PayRate", "RevenueCenterID",
                          "DeleteCount", "TimeIn", "TimeOut", "Edited", "RegularTime", "TotalTime",
                          "AutomaticClockOut", "DailyOvertime", "DailyOTRate", "WeeklyOTRate",
                          "DoubleOTRate", "Day6OTRate", "Day7OTRate", "Cost", "TotalCost", "RegularPay",
                          "NoSales", "DoubleOvertime", "WeeklyOvertime", "Day7Overtime", "DeclaredTips",
                          "Break1TimeIn", "Break1TimeOut", "Break1NewTimeIn", "Break1NewTimeOut", "BreakTime",
                          "Deleted")

        tree["show"] = "headings"

        for tcrcl in tree["column"]:
            tree.heading(tcrcl, text=tcrcl)

        for tcrins in tcrfch:
            tree.insert("", "end", values=(tcrins[0], tcrins[1], tcrins[2], tcrins[3],
                                           tcrins[4], tcrins[5], tcrins[6], tcrins[7], tcrins[8], tcrins[9],
                                           tcrins[10], tcrins[11], tcrins[12], tcrins[13], tcrins[14], tcrins[15],
                                           tcrins[16], tcrins[17], tcrins[18], tcrins[19], tcrins[20], tcrins[21],
                                           tcrins[22], tcrins[23], tcrins[24], tcrins[25], tcrins[26], tcrins[27],
                                           tcrins[28], tcrins[29], tcrins[30], tcrins[31], tcrins[32]))

    except:
        # ERROR WINDOW FOR TIME CARD RECORD

        ewtcr = tk.Toplevel()

        # Gets the requested values of the height and widht.

        ewtcrwW = ewtcr.winfo_reqwidth()
        ewtcrwH = ewtcr.winfo_reqheight()

        # Gets both half the screen width/height and window width/height

        ewtcrR = int(ewtcr.winfo_screenwidth() / 2 - ewtcrwW / 2)
        ewtcrD = int(ewtcr.winfo_screenheight() / 2 - ewtcrwH / 2)

        # Positions the window in the center of the page.

        ewtcr.geometry("+{}+{}".format(ewtcrR, ewtcrD))
        ewtcr.title("Error")
        ewtcr.geometry("300x150")

        # LABEL FOR ERROR TIME CARD RECORD ---

        letcr = tk.Label(
            ewtcr, bg='#F7F6EE',
            text="Time Card Record is Empty", anchor='c')
        letcr.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

        # "OK" BUTTON FOR TIME CARD RECORD ---

        oktcrbtt = ttk.Button(ewtcr, text='OK', command=lambda: TCRF_CW(ewtcr))
        oktcrbtt.place(relx=.17, rely=.55, relwidth=.31, relheight=.2)

        # "CANCEL" BUTTON FOR TIME CARD RECORD ---

        cltcrbtt = ttk.Button(ewtcr, text='Cancel', command=lambda: TCRF_CW(ewtcr))
        cltcrbtt.place(relx=.52, rely=.55, relwidth=.31, relheight=.2)

        ewtcr.mainloop()


# EMPLOYEE SALES TOTALS RECORD FETCHALL --- 

def ESTRF(tree):
    # CLOSING THE ERROR WINDOW ---

    def ESTRF_CW(clse):
        clse.destroy()


    try:
        estrfch = sqlx.execute("SELECT rowid, * FROM EMPLOYEE_SALES_TOTALS_RECORD").fetchall()

        for dtree in tree.get_children():
            tree.delete(dtree)

        tree["column"] = ("Index", "OwnerID", "TimeCardID", "TippedSales", "OwnerNetChargeTips",
                          "NetSales", "TotalSales", "TotalAccountable", "GrossCash", "TipsPaidOut", "CashAndChecks",
                          "CreditCardTotal", "NetCash", "TotalPayments", "GuestCount", "CheckCount",
                          "DiscountTotalCount",
                          "DiscountTotal", "AverageCheckOpenTime", "TipPool1", "TipPool2", "ChargeSales")

        tree["show"] = "headings"

        for estrcl in tree["column"]:
            tree.heading(estrcl, text=estrcl)

        for estrins in estrfch:
            tree.insert("", "end", values=(estrins[0], estrins[1], estrins[2], estrins[3],
                                           estrins[4], estrins[5], estrins[6], estrins[7], estrins[8], estrins[9],
                                           estrins[10], estrins[11], estrins[12], estrins[13], estrins[14], estrins[15],
                                           estrins[16], estrins[17], estrins[18], estrins[19], estrins[20],
                                           estrins[21]))

    except:
        # ERROR WINDOW FOR EMPLOYEE SALES TOTALS RECORD

        ewestr = tk.Toplevel()

        # Gets the requested values of the height and widht.

        ewestrwW = ewestr.winfo_reqwidth()
        ewestrwH = ewestr.winfo_reqheight()

        # Gets both half the screen width/height and window width/height

        ewestrR = int(ewestr.winfo_screenwidth() / 2 - ewestrwW / 2)
        ewestrD = int(ewestr.winfo_screenheight() / 2 - ewestrwH / 2)

        # Positions the window in the center of the page.

        ewestr.geometry("+{}+{}".format(ewestrR, ewestrD))
        ewestr.title("Error")
        ewestr.geometry("300x150")

        # LABEL FOR ERROR EMPLOYEE SALES TOTALS RECORD ---

        leestr = tk.Label(
            ewestr, bg='#F7F6EE',
            text="Employee Sales Totals Record is Empty", anchor='c')
        leestr.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

        # "OK" BUTTON FOR EMPLOYEE SALES TOTALS RECORD ---

        okestrbtt = ttk.Button(ewestr, text='OK', command=lambda: ESTRF_CW(ewestr))
        okestrbtt.place(relx=.17, rely=.55, relwidth=.31, relheight=.2)

        # "CANCEL" BUTTON FOR EMPLOYEE SALES TOTALS RECORD ---

        clestrbtt = ttk.Button(ewestr, text='Cancel', command=lambda: ESTRF_CW(ewestr))
        clestrbtt.place(relx=.52, rely=.55, relwidth=.31, relheight=.2)

        ewestr.mainloop()


# MENU --- 

def menu(usr, pass_):
    if usr in up_dic["Username"] and pass_ in up_dic["Password"]:
        # MENU  BACKGROUND IMAGE ---

        mbi = tk.PhotoImage(file="mc_bg.png")
        mbi1 = tk.Label(root, image=mbi)
        mbi1.place(relwidth=1, relheight=1)

        # FRAME FOR MENU ---

        ffm = tk.Label(root, bg="#BF8C8C", relief="sunken", bd=3)
        ffm.place(relx=.05, rely=.1, relwidth=.9, relheight=.8)

        # BUTTON OF CHOICES TO PICK WHICH TABLE ---

        bcpt = tk.Label(ffm, bg="#A56767", relief="sunken", bd=3)
        bcpt.place(relx=.02, rely=.05, relwidth=.3, relheight=.9)

        # BUTTON OF CHOICES RIDGE ---

        bcr = tk.Label(bcpt, bg="#E3DBDB", bd=3, relief="ridge")
        bcr.place(relx=.05, rely=.03, relwidth=.9, relheight=.94)

        # SERACH LABEL IN MENU ---

        # slm = tk.Label(ffm, bg="#F1EBE9", relief="sunken", bd=3)
        # slm.place(relx=.33, rely=.05, relwidth=.65, relheight=.13)

        # SEARCH LABEL RIDGE ---

        # slr = tk.Label(slm, bg="#F1EBE9", relief="ridge", bd=3)
        # slr.place(relx=.03, rely=.1, relwidth=.94, relheight=.8)

        # SEARCH ENTRY FOR MENU ---

        # sem = tk.Entry(slr, bd=3, relief="sunken")
        # sem.config(font=("Calibri", 12))
        # sem.place(relx=.01, rely=.1, relwidth=.6, relheight=.8)

        # TREEVIEW FOR MENU ---

        tm = ttk.Treeview(ffm)
        tm.place(relx=.33, rely=.05, relwidth=.62, relheight=.86)

        # TREEVIEW Y SCROLL ---

        tys = tk.Scrollbar(ffm, orient="vertical", command=tm.yview)
        tm.config(yscrollcommand=tys.set)
        tys.place(relx=.95, rely=.05, relwidth=.03, relheight=.86)

        # TREEVIEW X SCROLL ---

        txs = tk.Scrollbar(ffm, orient="horizontal", command=tm.xview)
        tm.config(xscrollcommand=txs.set)
        txs.place(relx=.33, rely=.91, relwidth=.65, relheight=.04)

        # BUTTON FOR EMPLOYEE RECORD ---

        ber = ttk.Button(bcr, text="Employee Record", command=lambda: ERF(tm))
        ber.place(relx=.02, rely=.01, relwidth=.96, relheight=.11)

        # BUTTON FOR CHECK RECORD ---

        bfcr = ttk.Button(bcr, text="Check Record", command=lambda: CRF(tm))
        bfcr.place(relx=.02, rely=.12, relwidth=.96, relheight=.11)

        # BUTTON FOR SEAT RECORD ---

        bsr = ttk.Button(bcr, text="Seat Record", command=lambda: SRF(tm))
        bsr.place(relx=.02, rely=.22, relwidth=.96, relheight=.11)

        # BUTTON FOR CHECK ITEM RECORD ---

        bcir = ttk.Button(bcr, text="Check Item Record", command=lambda: CIRF(tm))
        bcir.place(relx=.02, rely=.33, relwidth=.96, relheight=.11)

        # BUTTON FOR PAYMENT RECORD ---

        bpr = ttk.Button(bcr, text="Payment Record", command=lambda: PRF(tm))
        bpr.place(relx=.02, rely=.44, relwidth=.96, relheight=.11)

        # BUTTON FOR DISCOUNT RECORD ---

        bdr = ttk.Button(bcr, text="Discount Record", command=lambda: DRF(tm))
        bdr.place(relx=.02, rely=.55, relwidth=.96, relheight=.11)

        # BUTTON FOR DELETE RECORD ---

        bdlr = ttk.Button(bcr, text="Delete Record", command=lambda: DLRF(tm))
        bdlr.place(relx=.02, rely=.66, relwidth=.96, relheight=.11)

        # BUTTON FOR TIME CARD RECORD ---

        btcr = ttk.Button(bcr, text="Time Card Record", command=lambda: TCRF(tm))
        btcr.place(relx=.02, rely=.77, relwidth=.96, relheight=.11)

        # BUTTON FOR EMPLOYEE SALES TOTALS RECORD ---

        btcr = ttk.Button(bcr, text="Employee Sales Totals\n             Record",
                          command=lambda: ESTRF(tm))
        btcr.place(relx=.02, rely=.88, relwidth=.96, relheight=.11)

        # BUTTON FOR LOGGING OUT --- 

        bflo = tk.Button(root, text="Logout", bg="#FFDAB9", command=lambda: login())
        bflo.place(relx=.78, rely=.02, relwidth=.2, relheight=.05)

        root.mainloop()

    else:
        # ERROR MESSAGE FOR WRONG USERNAME AND PASSWORD ---

        emwup = tk.Label(root, text="Wrong Username or Password", fg="red", bg="white")
        emwup.place(relx=.4, rely=.55)

        root.mainloop()


# LOGIN FRAME --- 

root = tk.Tk()
root.geometry("700x700")
root.title("Merchant Counselors")

# LOGIN --- 

def login():
    # ROOT BACKGROUND IMAGE ---

    rbi = tk.PhotoImage(file="mc_bg.png")
    rbi1 = tk.Label(root, image=rbi)
    rbi1.place(relwidth=1, relheight=1)

    # MURCHANT COUNCELORS LOGO ---

    mcl = tk.PhotoImage(file="mc_pic.png")
    mcl1 = tk.Label(rbi1, image=mcl, bg="black")
    mcl1.place(relx=.25, rely=.14, relheight=.35)

    # ROOT LOGIN USER LABEL ---

    rlul = tk.Label(rbi1, bg="#F1EFEF", text="User:")
    rlul.config(font=("Calibri", 13))
    rlul.place(relx=.3, rely=.6)

    # ROOT USER ENTRY LOGIN ---

    ruel = tk.Entry(rbi1, bd=3, relief="sunken")
    ruel.config(font=("Calibri", 12))
    ruel.place(relx=.37, rely=.6, relwidth=.3, relheight=.04)

    # ROOT LOGIN PASSWORD LABEL ---

    rlpl = tk.Label(rbi1, bg="#F1EFEF", text="Password:")
    rlpl.config(font=("Calibri", 13))
    rlpl.place(relx=.26, rely=.66)

    # ROOT PASSWORD ENTRY LOGIN ---

    rpel = tk.Entry(rbi1, bd=3, relief="sunken", show="*")
    rpel.config(font=("Calibri", 12))
    rpel.place(relx=.37, rely=.66, relwidth=.3, relheight=.04)

    # ROOT LOGIN BUTTON ---

    rlb = ttk.Button(text="Login", command=lambda: menu(ruel.get(), rpel.get()))
    rlb.place(relx=.4, rely=.72, relwidth=.2, relheight=.05)

    root.mainloop()


login()