from bs4 import BeautifulSoup as bs
import pandas as pd
import shutil
import os
import time
import getpass
import sqlite3

# STARTING SQLITE3 CURSOR --- 

sql = sqlite3.connect("mcdb.db")

sqlx = sql.cursor()

# USERNAME AND PASSWORD STORED IN DICTIONARY --- 

up_dic = {
	
	"Username": ["raul", "sudip"],
	"Password": ["1"]

}

print("                                            ___           ___")
print("                                           /\\__\\         /\\  \\")
print("                                          /::|  |       /::\\  \\")
print("                                         /:|:|  |      /:/\\:\\  \\")
print("                                        /:/|:|__|__   /:/  \\:\\  \\")
print("                                       /:/ |::::\\__\\ /:/__/ \\:\\__\\")
print("                                       \\/__/~~/:/  / \\:\\  \\  \\/__/")
print("                                             /:/  /   \\:\\  \\")
print("                                            /:/  /     \\:\\  \\")
print("                                           /:/  /       \\:\\__\\")
print("                                           \\/__/         \\/__/")
print("\n")
print("\n")
user = input("                                              Username:~?> ")
pass_ = getpass.getpass("                                              Password:~?> ")
print("\n")
print("")
time.sleep(3)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("\n")
print("                                                Please Wait...\n")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
time.sleep(4)
print("\n")
print("                         :::   :::  :::::::::::::::::::  :::::::: :::    :::    :::    ::::    ::::::::::::::")
print("                       :+:+: :+:+: :+:       :+:    :+::+:    :+::+:    :+:  :+: :+:  :+:+:   :+:    :+:")
print("                     +:+ +:+:+ +:++:+       +:+    +:++:+       +:+    +:+ +:+   +:+ :+:+:+  +:+    +:+")
print("                    +#+  +:+  +#++#++:++#  +#++:++#: +#+       +#++:++#+++#++:++#++:+#+ +:+ +#+    +#+")
print("                   +#+       +#++#+       +#+    +#++#+       +#+    +#++#+     +#++#+  +#+#+#    +#+")
print("                  #+#       #+##+#       #+#    #+##+#    #+##+#    #+##+#     #+##+#   #+#+#    #+#")
print("                 ###       ################    ### ######## ###    ######     ######    ####    ###")
print("            ::::::::  :::::::: :::    :::::::    ::: :::::::: :::::::::::::       :::::::: :::::::::  ::::::::")
print("          :+:    :+::+:    :+::+:    :+::+:+:   :+::+:    :+::+:       :+:      :+:    :+::+:    :+::+:    :+:")
print("         +:+       +:+    +:++:+    +:+:+:+:+  +:++:+       +:+       +:+      +:+    +:++:+    +:++:+")
print("        +#+       +#+    +:++#+    +:++#+ +:+ +#++#++:++#+++#++:++#  +#+      +#+    +:++#++:++#: +#++:++#++")
print("       +#+       +#+    +#++#+    +#++#+  +#+#+#       +#++#+       +#+      +#+    +#++#+    +#+       +#+")
print("      #+#    #+##+#    #+##+#    #+##+#   #+#+##+#    #+##+#       #+#      #+#    #+##+#    #+##+#    #+#")
print("     ########  ########  ######## ###    #### ######## ############################ ###    ### ########\n")
time.sleep(3)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
time.sleep(3)

# EMPLOYEE RECORD TABLE --- 

mcer_tb = """CREATE TABLE EMPLOYEE_RECORD(

	"ID" TEXT,
	"FIRST_NAME" TEXT,
	"LAST_NAME" TEXT,
	"NICK_NAME" TEXT,
	"ID1" TEXT,
	"ID2" TEXT,
	"ADDRESS" TEXT,
	"CITY" TEXT,
	"STATE" TEXT,
	"ZIP_CODE" TEXT,
	"PHONE1" TEXT,
	"EMAIL" TEXT,
	"BIRTH_DATE" TEXT,
	"HIRE_DATE" TEXT,
	"LAST_RAISE_DATE" TEXT,
	"EMERGENCY_PHONE" TEXT,
	"EMERGENCY_CONTACT" TEXT,
	"W4_ALLOWANCES" TEXT,
	"W4_STATUS" TEXT,
	"ID3" TEXT,
	"RATE" TEXT,
	"POSITION" TEXT,
	"ACCESS_CODE" TEXT,
	"PICTURE" TEXT,
	"LANGUAGE" TEXT,
	"FOOD_HANDLER_CERT_DATE" TEXT,
	"BARTENDER_CARD_DATE" TEXT,
	"REQUIRE_CARD" TEXT,
	"ENFORCE_SCHEDULING" TEXT,
	"EXTEND_RIGHTS" TEXT,
	"CLOCK_IN_OUT_ONLY" TEXT,
	"FINGERPRINT_CLOCK_IN" TEXT,
	"FINGERPRINT_REQUIRED" TEXT,
	"ID4" TEXT,
	"LEVEL" TEXT,
	"DELETED" TEXT

	)"""

try:
	sqlx.execute(mcer_tb)

except:
	None

# CHECK RECORD TABLE --- 

mccr_tb = """CREATE TABLE CHECK_RECORD(

	"ID" TEXT,
	"NUMBER_OF_SEATS" TEXT,
	"FLAGS_TRANSFERRED" TEXT,
	"TIME_OPENED" TEXT,
	"OPENER_ID" TEXT,
	"OPENER_NAME" TEXT,
	"OWNER_ID" TEXT,
	"OWNER_NAME" TEXT,
	"OWNER_TIME_CARD_ID" TEXT,
	"TIME_CLOSED" TEXT,
	"CLOSER_ID" TEXT,
	"CLOSER_NAME" TEXT,
	"CLOSER_TIME_CARD_ID" TEXT,
	"STATION_CLOSED_ID" TEXT,
	"TABLE" TEXT,
	"GUESTS" TEXT,
	"ORDER_TYPE_ID" TEXT,
	"REVENUE_CENTER_ID" TEXT,
	"STATION_OPENED_ID" TEXT,
	"TRANSFERER_ID" TEXT,
	"TRANSFERER_NAME" TEXT,
	"TRANSFER_TIME" TEXT,
	"TOTAL" TEXT,
	"TAXABLE_SALES1" TEXT,
	"FLAGS_TAB_NAME_ENTERED" TEXT,
	"FLAGS_BEVERAGES_ORDERED" TEXT,
	"DISCOUNT_TOTAL_AMOUNT" TEXT,
	"FLAGS_REOPENED" TEXT,
	"TIME_REOPENED" TEXT,
	"FLAGS_USED" TEXT

	)"""

try:
	sqlx.execute(mccr_tb)

except:
	None

# SEAT RECORD TABLE --- 

mcsr_tb = """CREATE TABLE SEAT_RECORD(

	"CHECK_INTERNAL" TEXT,
	"SEAT_NUMBER" TEXT,
	"KEY" TEXT,
	"FLAGS_USED" TEXT,
	"SUBTOTAL" TEXT,
	"TOTAL" TEXT,
	"TAX_TOTAL1" TEXT,
	"CREDIT_CARD_SURCHARGE" TEXT,
	"ITEM_DISCOUNT_TOTAL" TEXT

	)"""

try:
	sqlx.execute(mcsr_tb)

except:
	None

# CHECK ITEM RECORD TABLE --- 

mccir_tb = """CREATE TABLE CHECK_ITEM_RECORD(

	"SEAT_KEY" TEXT,
	"KEY" TEXT,
	"POSITION" TEXT,
	"RECORD_NUMBER" TEXT,
	"ID" TEXT,
	"GUEST_CHECK_NAME" TEXT,
	"REPORT_GROUP_ID" TEXT,
	"SORT_KEY" TEXT,
	"STATION_ID" TEXT,
	"OWNER_TIME_CARD_ID" TEXT,
	"OWNER_ID" TEXT,
	"OWNER_NAME" TEXT,
	"TIME_STAMP" TEXT,
	"PRICE" TEXT,
	"FLAGS_PRINT_MODIFIER" TEXT,
	"APPROVED_BY" TEXT,
	"TAX_APPLIED_1" TEXT,
	"ITEM_KEY" TEXT,
	"PRICE_NUMBER" TEXT,
	"LEVEL" TEXT,
	"FLAGS_KITCHEN_COMMENT" TEXT,
	"FLAGS_INCLUDE_IN_PRICE" TEXT,
	"FLAGS_DISCOUNTED" TEXT,
	"DISCOUNT_AMOUNT" TEXT,
	"DISCOUNT_INTERNAL_ID" TEXT,
	"QTY" TEXT,
	"EXTENSION" TEXT

	)"""

try:
	sqlx.execute(mccir_tb)

except:
	None

# PAYMENT RECORD TABLE --- 

mcpr_tb = """CREATE TABLE PAYMENT_RECORD(

	"SEAT_KEY" TEXT,
	"KEY" TEXT,
	"POSITION" TEXT,
	"ID" TEXT,
	"REVENUE_CENTER_ID" TEXT,
	"NAME" TEXT,
	"AMOUNT" TEXT,
	"TIP" TEXT,
	"OWNER_ID" TEXT,
	"OWNER_NAME" TEXT,
	"OWNER_TIME_CARD_ID" TEXT,
	"STATION_ID" TEXT,
	"TIME_STAMP" TEXT,
	"FLAGS_VERIFIED" TEXT,
	"FLAGS_APPROVED" TEXT,
	"FLAGS_TRACK2_RECORDED" TEXT,
	"APPROVAL" TEXT,
	"ACCOUNT" TEXT,
	"CUSTOMER_NAME" TEXT,
	"VOID_ID" TEXT,
	"VOID_EMPLOYEE_NAME" TEXT,
	"TIME_VOIDED" TEXT,
	"VOID_EMPLOYEE_ID" TEXT

	)"""

try:
	sqlx.execute(mcpr_tb)

except:
	None

# DISCOUNT RECORD TABLE --- 

mcdr_tb = """CREATE TABLE DISCOUNT_RECORD(

	"SEAT_KEY" TEXT,
	"KEY" TEXT,
	"POSITION" TEXT,
	"ID" TEXT,
	"ID_EXPLICIT" TEXT,
	"DISCOUNT_INTERNAL_ID" TEXT,
	"AMOUNT" TEXT,
	"TIME_STAMP" TEXT,
	"APPROVED_BY_ID" TEXT,
	"APPROVED_BY_NAME" TEXT,
	"SOURCE" TEXT

	)"""

try:
	sqlx.execute(mcdr_tb)

except:
	None

# DELETE RECORD TABLE --- 

mcdlt_tb = """CREATE TABLE DELETE_RECORD(

	"KEY" TEXT,
	"TIME_STAMP" TEXT,
	"OWNER_ID" TEXT,
	"OWNER_NAME" TEXT,
	"CHECK_ID" TEXT,
	"AMOUNT" TEXT,
	"ITEM_NAME" TEXT,
	"APPROVED_BY_EMPLOYEE_ID" TEXT,
	"APPROVED_BY_NAME" TEXT,
	"APPROVED_BY_TIME_CARD_ID" TEXT

	)"""

try:
	sqlx.execute(mcdlt_tb)

except:
	None

# TIME CARD RECORD TABLE --- 

mctc_tb = """CREATE TABLE TIME_CARD_RECORD(

	"ID" TEXT,
	"OWNER_ID" TEXT,
	"JOB_ID" TEXT,
	"PAY_RATE" TEXT,
	"REVENUE_CENTER_ID" TEXT,
	"DELETE_COUNT" TEXT,
	"TIME_IN" TEXT,
	"TIME_OUT" TEXT,
	"EDITED" TEXT,
	"REGULAR_TIME" TEXT,
	"TOTAL_TIME" TEXT,
	"AUTOMATIC_CLOCK_OUT" TEXT,
	"DAILY_OVERTIME" TEXT,
	"DAILY_OT_RATE" TEXT,
	"WEEKLY_OT_RATE" TEXT,
	"DOUBLE_OT_RATE" TEXT,
	"DAY6_OT_RATE" TEXT,
	"DAY7_OT_RATE" TEXT,
	"COST" TEXT,
	"TOTAL_COST" TEXT,
	"REGULAR_PAY" TEXT,
	"NO_SALES" TEXT,
	"DOUBLE_OVERTIME" TEXT,
	"WEEKLY_OVERTIME" TEXT,
	"DAY7_OVERTIME" TEXT,
	"DECLARED_TIPS" TEXT,
	"BREAK1_TIME_IN" TEXT,
	"BREAK1_TIME_OUT" TEXT,
	"BREAK1_NEW_TIME_IN" TEXT,
	"BREAK1_NEW_TIME_OUT" TEXT,
	"BREAK_TIME" TEXT,
	"DELETED" TEXT

	)"""

try:
	sqlx.execute(mctc_tb)

except:
	None

# EMPLOYEE SALES TOTALS RECORD TABLE --- 

mcestr_tb = """CREATE TABLE EMPLOYEE_SALES_TOTALS_RECORD(

	"OWNER_ID" TEXT,
	"TIME_CARD_ID" TEXT,
	"TIPPED_SALES" TEXT,
	"OWNER_NET_CHARGE_TIPS" TEXT,
	"NET_SALES" TEXT,
	"TOTAL_SALES" TEXT,
	"TOTAL_ACCOUNTABLE" TEXT,
	"GROSS_CASH" TEXT,
	"TIPS_PAID_OUT" TEXT,
	"CASH_AND_CHECKS" TEXT,
	"CREDIT_CARD_TOTAL" TEXT,
	"NET_CASH" TEXT,
	"TOTAL_PAYMENTS" TEXT,
	"GUEST_COUNT" TEXT,
	"CHECK_COUNT" TEXT,
	"DISCOUNT_TOTAL_COUNT" TEXT,
	"DISCOUNT_TOTAL" TEXT,
	"AVERAGE_CHECK_OPEN_TIME" TEXT,
	"TIP_POOL1" TEXT,
	"TIP_POOL2" TEXT,
	"CHARGE_SALES" TEXT

	)"""

try:
	sqlx.execute(mcestr_tb)

except:
	None

if user in up_dic["Username"] and pass_ in up_dic["Password"]:
	# MOVING ANY FILES FTPQ TO MC_FTPQ DIRECTORY --- 

	while True:
		try:
			# CREATING MC_FTPQ DIRECTORY --- 

			os.mkdir("mc_ftpq")

		except:
			time.sleep(.1)

		print(" --- Moving FTP files to mc_ftpq directory ---\n")
		print("\n")
		time.sleep(3)

		# PATHS FOR DOWNLOADS AND MC_FTPQ DIRECTORY --- 


		# MOVING FTPQ FILES TO MC_FTPQ DIRECTORY --- 

		for dl in os.listdir(dlp):
			if "FTPQ" in dl:
				print(" "+dl+" ----> [[ Copy Status: Success ]]\n")
				dlf = dlp+"\\"+dl
				shutil.move(dlf, mc_ftpq)
				bl = True
				break

			else:
				bl = False

		if bl == True:
			# CONVERTING FTP FILES TO XML --- 

			mcfl = mc_ftpq+"\\"+dl
			with open(mcfl, "r") as mcxml:
				mcont = mcxml.read()
				mcsp = bs(mcont, "lxml")

				# EMPLOYEE RECORD --- 

				def ER():
					# EMPLOYEE RECORD DICTIONARY --- 

					mcer_dc = {
	
						"ID": [],
						"FirstName": [],
						"LastName": [],
						"NickName": [],
						"ID1": [],
						"ID2": [],
						"Address": [],
						"City": [],
						"State": [],
						"ZipCode": [],
						"Phone1": [],
						"Email": [],
						"BirthDate": [],
						"HireDate": [],
						"LastRaiseDate":[],
						"EmergencyPhone": [],
						"EmergencyContact": [],
						"W4Allowances": [],
						"W4Status": [],
						"ID3": [],
						"Rate": [],
						"Position": [],
						"AccessCode": [],
						"Picture": [],
						"Language": [],
						"FoodHandlerCertDate": [],
						"BartenderCardDate": [],
						"RequireCard": [],
						"EnforceScheduling":[],
						"ExtendRights": [],
						"ClockInOutOnly": [],
						"FingerprintAtClockIn": [],
						"FingerprintRequired": [],
						"ID4": [],
						"Level": [],
						"Deleted": []

					}

					print(" -----------------------------")
					print(" |   EMPLOYEE RECORD TABLE   |")
					print(" -----------------------------\n")
					time.sleep(3)

					mcer = mcsp.find_all("employeerecord")
					for mcer1 in mcer:
						# APPENDING ID IN EMPLOYEE RECORD DATABASE --- 

						try:
							mcer_dc["ID"].append(mcer1.find("id").text)

						except:
							mcer_dc["ID"].append("NaN")

						# APPENDING FIRST NAME IN EMPLOYEE RECORD DATABASE --- 

						try:
							mcer_dc["FirstName"].append(mcer1.find("firstname").text)

						except:
							mcer_dc["FirstName"].append("NaN")

						# APPENDING LAST NAME IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["LastName"].append(mcer1.find("lastname").text)

						except:
							mcer_dc["LastName"].append("NaN")

						# APPENDING NICK NAME IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["NickName"].append(mcer1.find("nickname").text)

						except:
							mcer_dc["NickName"].append("NaN")

						# APPENDING ID1 IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["ID1"].append(mcer1.find("id1").text)

						except:
							mcer_dc["ID1"].append("NaN")

						# APPENDING ID2 IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["ID2"].append(mcer1.find("id2").text)

						except:
							mcer_dc["ID2"].append("NaN")

						# APPENDING ADDRESS IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["Address"].append(mcer1.find("address").text)

						except:
							mcer_dc["Address"].append("NaN")

						# APPENDING CITY IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["City"].append(mcer1.find("city").text)

						except:
							mcer_dc["City"].append("NaN")

						# APPENDING STATE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["State"].append(mcer1.find("state").text)

						except:
							mcer_dc["State"].append("NaN")

						# APPENDING ZIP CODE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["ZipCode"].append(mcer1.find("zipcode").text)

						except:
							mcer_dc["ZipCode"].append("NaN")

						# APPENDING PHONE1 IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["Phone1"].append(mcer1.find("phone1").text)

						except:
							mcer_dc["Phone1"].append("NaN")

						# APPENDING EMAIL IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["Email"].append(mcer1.find("email").text)

						except:
							mcer_dc["Email"].append("NaN")

						# APPENDING BIRTH DATE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["BirthDate"].append(mcer1.find("birthdate").text)

						except:
							mcer_dc["BirthDate"].append("NaN")

						# APPENDING HIRE DATE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["HireDate"].append(mcer1.find("hiredate").text)

						except:
							mcer_dc["HireDate"].append("NaN")

						# APPENDING LAST RAISE DATE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["LastRaiseDate"].append(mcer1.find("lastraisedate").text)

						except:
							mcer_dc["LastRaiseDate"].append("NaN")

						# APPENDING EMERGENCY PHONE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["EmergencyPhone"].append(mcer1.find("emergencyphone").text)

						except:
							mcer_dc["EmergencyPhone"].append("NaN")

						# APPENDING EMERGENCY CONTACT IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["EmergencyContact"].append(mcer1.find("emergencycontact").text)

						except:
							mcer_dc["EmergencyContact"].append("NaN")

						# APPENDING W4 ALLOWANCES IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["W4Allowances"].append(mcer1.find("w4allowances").text)

						except:
							mcer_dc["W4Allowances"].append("NaN")

						# APPENDING W4 STATUS IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["W4Status"].append(mcer1.find("w4status").text)

						except:
							mcer_dc["W4Status"].append("NaN")

						# APPENDING ID3 IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["ID3"].append(mcer1.find("id3").text)

						except:
							mcer_dc["ID3"].append("NaN")

						# APPENDING RATE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["Rate"].append(mcer1.find("rate").text)

						except:
							mcer_dc["Rate"].append("NaN")

						# APPENDING POSITION IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["Position"].append(mcer1.find("position").text)

						except:
							mcer_dc["Position"].append("NaN")

						# APPENDING ACCESS CODE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["AccessCode"].append(mcer1.find("accesscode").text)

						except:
							mcer_dc["AccessCode"].append("NaN")

						# APPENDING PICTURE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["Picture"].append(mcer1.find("picture").text)

						except:
							mcer_dc["Picture"].append("NaN")

						# APPENDING LANGUAGE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["Language"].append(mcer1.find("language").text)

						except:
							mcer_dc["Language"].append("NaN")

						# APPENDING FOOD HANDLER CERT DATE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["FoodHandlerCertDate"].append(mcer1.find("foodhandlercertdate").text)

						except:
							mcer_dc["FoodHandlerCertDate"].append("NaN")

						# APPENDING BARTENDER CARD DATE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["BartenderCardDate"].append(mcer1.find("bartendercarddate").text)

						except:
							mcer_dc["BartenderCardDate"].append("NaN")

						# APPENDING REQUIRE CARD DATE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["RequireCard"].append(mcer1.find("requirecard").text)

						except:
							mcer_dc["RequireCard"].append("NaN")

						# APPENDING ENFORCE SCHEDULING DATE IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["EnforceScheduling"].append(mcer1.find("enforcescheduling").text)

						except:
							mcer_dc["EnforceScheduling"].append("NaN")

						# APPENDING EXTEND RIGHTS IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["ExtendRights"].append(mcer1.find("extendrights").text)

						except:
							mcer_dc["ExtendRights"].append("NaN")

						# APPENDING CLOCK IN OUT ONLY IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["ClockInOutOnly"].append(mcer1.find("clockinoutonly").text)

						except:
							mcer_dc["ClockInOutOnly"].append("NaN")

						# APPENDING FINGERPRINT AT CLOCK IN IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["FingerprintAtClockIn"].append(mcer1.find("fingerprintatclockin").text)

						except:
							mcer_dc["FingerprintAtClockIn"].append("NaN")

						# APPENDING FINGERPRINT REQUIRED IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["FingerprintRequired"].append(mcer1.find("fingerprintrequired").text)

						except:
							mcer_dc["FingerprintRequired"].append("NaN")

						# APPENDING ID4 IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["ID4"].append(mcer1.find("id4").text)

						except:
							mcer_dc["ID4"].append("NaN")

						# APPENDING LEVEL IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["Level"].append(mcer1.find("level").text)

						except:
							mcer_dc["Level"].append("NaN")

						# APPENDING DELETED IN EMPLOYEE RECORD DATABASE ---

						try:
							mcer_dc["Deleted"].append(mcer1.find("deleted").text)

						except:
							mcer_dc["Deleted"].append("NaN")

					# INPUT EMPLOYEE RECORD TABLE INTO DATABASE --- 

					mcer_pd = pd.DataFrame(mcer_dc)
					print(mcer_pd)

					for mcer2 in range(len(mcer_pd)):
						mcer3 = mcer_pd.iloc[mcer2]
						sqlx.execute("INSERT INTO EMPLOYEE_RECORD VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", mcer3)

					sql.commit()
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
					print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
					time.sleep(3)


				ER()

				# CHECK RECORD --- 

				def CR():
					# CHECK RECORD DICTIONARY --- 

					mccr_dc = {

					"ID": [],
					"NumberOfSeats": [],
					"FlagsTransferred": [],
					"TimeOpened": [],
					"OpenerID": [],
					"OpenerName": [],
					"OwnerID": [],
					"OwnerName": [],
					"OwnerTimeCardID": [],
					"TimeClosed": [],
					"CloserID": [],
					"CloserName": [],
					"CloserTimeCardID": [],
					"StationClosedID": [],
					"Table": [],
					"Guests": [],
					"OrderTypeID": [],
					"RevenueCenterID": [],
					"StationOpenedID": [],
					"TransfererID":[],
					"TransfererName": [],
					"TransferTime": [],
					"Total": [],
					"TaxableSales1": [],
					"FlagsTabNameEntered": [],
					"FlagsBeveragesOrdered": [],
					"DiscountTotalAmount": [],
					"FlagsReopened": [],
					"TimeReopened": [],
					"FlagsUsed": []

					}

					print(" --------------------------")
					print(" |   CHECK RECORD TABLE   |")
					print(" --------------------------\n")
					time.sleep(3)

					mccr = mcsp.find_all("checkrecord")
					for mccr1 in mccr:
						# APPENDING ID INTO CHECK RECORD DATABASE --- 

						try:
							mccr_dc["ID"].append(mccr1.find("id").text)

						except:
							mccr_dc["ID"].append("NaN")

						# APPENDING NUMBER OF SEATS INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["NumberOfSeats"].append(mccr1.find("numberofseats").text)

						except:
							mccr_dc["NumberOfSeats"].append("NaN")

						# APPENDING FLAGS TRANSFERRED INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["FlagsTransferred"].append(mccr1.find("flagstransferred").text)

						except:
							mccr_dc["FlagsTransferred"].append("NaN")

						# APPENDING TIME OPENED INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["TimeOpened"].append(mccr1.find("timeopened").text)

						except:
							mccr_dc["TimeOpened"].append("NaN")

						# APPENDING OPENER ID INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["OpenerID"].append(mccr1.find("openerid").text)

						except:
							mccr_dc["OpenerID"].append("NaN")

						# APPENDING OPENER NAME INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["OpenerName"].append(mccr1.find("openername").text)

						except:
							mccr_dc["OpenerName"].append("NaN")

						# APPENDING OWNER ID INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["OwnerID"].append(mccr1.find("ownerid").text)

						except:
							mccr_dc["OwnerID"].append("NaN")

						# APPENDING OWNER NAME INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["OwnerName"].append(mccr1.find("ownername").text)

						except:
							mccr_dc["OwnerName"].append("NaN")

						# APPENDING OWNER TIME CARD ID INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["OwnerTimeCardID"].append(mccr1.find("ownertimecardid").text)

						except:
							mccr_dc["OwnerTimeCardID"].append("NaN")

						# APPENDING TIME CLOSED INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["TimeClosed"].append(mccr1.find("timeclosed").text)

						except:
							mccr_dc["TimeClosed"].append("NaN")

						# APPENDING CLOSER ID INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["CloserID"].append(mccr1.find("closerid").text)

						except:
							mccr_dc["CloserID"].append("NaN")

						# APPENDING CLOSER NAME INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["CloserName"].append(mccr1.find("closername").text)

						except:
							mccr_dc["CloserName"].append("NaN")

						# APPENDING CLOSER TIME CARD ID INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["CloserTimeCardID"].append(mccr1.find("closertimecardid").text)

						except:
							mccr_dc["CloserTimeCardID"].append("NaN")

						# APPENDING STATION CLOSED ID INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["StationClosedID"].append(mccr1.find("stationclosedid").text)

						except:
							mccr_dc["StationClosedID"].append("NaN")

						# APPENDING TABLE INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["Table"].append(mccr1.find("table").text)

						except:
							mccr_dc["Table"].append("NaN")

						# APPENDING GUESTS INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["Guests"].append(mccr1.find("guests").text)

						except:
							mccr_dc["Guests"].append("NaN")

						# APPENDING ORDER TYPE ID INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["OrderTypeID"].append(mccr1.find("ordertypeid").text)

						except:
							mccr_dc["OrderTypeID"].append("NaN")

						# APPENDING REVENUE CENTER ID INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["RevenueCenterID"].append(mccr1.find("revenuecenterid").text)

						except:
							mccr_dc["RevenueCenterID"].append("NaN")

						# APPENDING STATION OPENED ID INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["StationOpenedID"].append(mccr1.find("stationopenedid").text)

						except:
							mccr_dc["StationOpenedID"].append("NaN")

						# APPENDING TRANSFERER ID INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["TransfererID"].append(mccr1.find("transfererid").text)

						except:
							mccr_dc["TransfererID"].append("NaN")

						# APPENDING TRANSFERER NAME INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["TransfererName"].append(mccr1.find("transferername").text)

						except:
							mccr_dc["TransfererName"].append("NaN")

						# APPENDING TRANSFER TIME INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["TransferTime"].append(mccr1.find("transfertime").text)

						except:
							mccr_dc["TransferTime"].append("NaN")

						# APPENDING TOTAL INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["Total"].append(mccr1.find("total").text)

						except:
							mccr_dc["Total"].append("NaN")

						# APPENDING TAXABLE SALES 1 INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["TaxableSales1"].append(mccr1.find("taxablesales1").text)

						except:
							mccr_dc["TaxableSales1"].append("NaN")

						# APPENDING FLAGS TAB NAME ENTERED INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["FlagsTabNameEntered"].append(mccr1.find("flagstabnameentered").text)

						except:
							mccr_dc["FlagsTabNameEntered"].append("NaN")

						# APPENDING FLAGS BEVERAGES ORDERED INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["FlagsBeveragesOrdered"].append(mccr1.find("flagsbeveragesordered").text)

						except:
							mccr_dc["FlagsBeveragesOrdered"].append("NaN")

						# APPENDING DISCOUNT TOTAL AMOUNT INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["DiscountTotalAmount"].append(mccr1.find("discounttotalamount").text)

						except:
							mccr_dc["DiscountTotalAmount"].append("NaN")

						# APPENDING FLAGS REOPENED INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["FlagsReopened"].append(mccr1.find("flagsreopened").text)

						except:
							mccr_dc["FlagsReopened"].append("NaN")

						# APPENDING TIME REOPENED INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["TimeReopened"].append(mccr1.find("timereopened").text)

						except:
							mccr_dc["TimeReopened"].append("NaN")

						# APPENDING FLAGS USED INTO CHECK RECORD DATABASE ---

						try:
							mccr_dc["FlagsUsed"].append(mccr1.find("flagsused").text)

						except:
							mccr_dc["FlagsUsed"].append("NaN")

					# INPUT CHECK RECORD TABLE INTO DATABASE --- 

					mccr_pd = pd.DataFrame(mccr_dc)
					print(mccr_pd)

					for mccr2 in range(len(mccr_pd)):
						mccr3 = mccr_pd.iloc[mccr2]
						sqlx.execute("INSERT INTO CHECK_RECORD VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", mccr3)

					sql.commit()
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
					print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
					time.sleep(3)


				CR()

				# SEAT RECORD --- 

				def SR():
					# SEAT RECORD DICTIONARY --- 

					mcsr_dc = {

					"CheckInternal": [],
					"SeatNumber": [],
					"Key": [],
					"FlagsUsed": [],
					"Subtotal": [],
					"Total": [],
					"TaxTotal1": [],
					"CreditCardSurcharge": [],
					"ItemDiscountTotal": []

					}

					print(" -------------------------")
					print(" |   SEAT RECORD TABLE   |")
					print(" -------------------------\n")
					time.sleep(3)

					mcsr = mcsp.find_all("seatrecord")
					for mcsr1 in mcsr:
						# APPENDING CHECK INTERNAL INTO SEAT RECORD DATABASE --- 

						try:
							mcsr_dc["CheckInternal"].append(mcsr1.find("checkinternal").text)

						except:
							mcsr_dc["CheckInternal"].append("NaN")

						# APPENDING SEAT NUMBER INTO SEAT RECORD DATABASE --- 

						try:
							mcsr_dc["SeatNumber"].append(mcsr1.find("seatnumber").text)

						except:
							mcsr_dc["SeatNumber"].append("NaN")

						# APPENDING KEY INTO SEAT RECORD DATABASE ---

						try:
							mcsr_dc["Key"].append(mcsr1.find("key").text)

						except:
							mcsr_dc["Key"].append("NaN")

						# APPENDING FLAGS USED INTO SEAT RECORD DATABASE ---

						try:
							mcsr_dc["FlagsUsed"].append(mcsr1.find("flagsused").text)

						except:
							mcsr_dc["FlagsUsed"].append("NaN")

						# APPENDING SUBTOTAL INTO SEAT RECORD DATABASE ---

						try:
							mcsr_dc["Subtotal"].append(mcsr1.find("subtotal").text)

						except:
							mcsr_dc["Subtotal"].append("NaN")

						# APPENDING TOTAL INTO SEAT RECORD DATABASE ---

						try:
							mcsr_dc["Total"].append(mcsr1.find("total").text)

						except:
							mcsr_dc["Total"].append("NaN")

						# APPENDING TAX TOTAL 1 INTO SEAT RECORD DATABASE ---

						try:
							mcsr_dc["TaxTotal1"].append(mcsr1.find("taxtotal1").text)

						except:
							mcsr_dc["TaxTotal1"].append("NaN")

						# APPENDING CREDIT CARD SURCHARGE INTO SEAT RECORD DATABASE ---

						try:
							mcsr_dc["CreditCardSurcharge"].append(mcsr1.find("creditcardsurcharge").text)

						except:
							mcsr_dc["CreditCardSurcharge"].append("NaN")

						# APPENDING ITEM DISCOUNT TOTAL INTO SEAT RECORD DATABASE ---

						try:
							mcsr_dc["ItemDiscountTotal"].append(mcsr1.find("itemdiscounttotal").text)

						except:
							mcsr_dc["ItemDiscountTotal"].append("NaN")

					# INPUT SEAT RECORD TABLE INTO DATABASE --- 

					mcsr_pd = pd.DataFrame(mcsr_dc)
					print(mcsr_pd)

					for mcsr2 in range(len(mcsr_pd)):
						mcsr3 = mcsr_pd.iloc[mcsr2]
						sqlx.execute("INSERT INTO SEAT_RECORD VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", mcsr3)

					sql.commit()
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
					print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
					time.sleep(3)


				SR()

				# CHECK ITEM RECORD --- 

				def CIR():
					# CHECK ITEM RECORD DICTIONARY --- 

					mccir_dc = {

					"SeatKey": [],
					"Key": [],
					"Position": [],
					"RecordNumber": [],
					"ID": [],
					"GuestCheckName": [],
					"ReportGroupID": [],
					"SortKey": [],
					"StationID": [],
					"OwnerTimeCardID": [],
					"OwnerID": [],
					"OwnerName": [],
					"TimeStamp": [],
					"Price": [],
					"FlagsPrintModifier": [],
					"ApprovedBy": [],
					"TaxApplied1": [],
					"ItemKey": [],
					"PriceNumber": [],
					"Level": [],
					"FlagsKitchenComment": [],
					"FlagsIncludeInPrice": [],
					"FlagsDiscounted": [],
					"DiscountAmount": [],
					"DiscountInternalID":[],
					"Qty": [],
					"Extension": []

					}

					print(" -------------------------------")
					print(" |   CHECK ITEM RECORD TABLE   |")
					print(" -------------------------------\n")
					time.sleep(3)

					mccir = mcsp.find_all("checkitemrecord")
					for mccir1 in mccir:
						# APPENDING SEAT KEY INTO CHECK ITEM RECORD DATABASE --- 

						try:
							mccir_dc["SeatKey"].append(mccir1.find("seatkey").text)

						except:
							mccir_dc["SeatKey"].append("NaN")

						# APPENDING KEY INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["Key"].append(mccir1.find("key").text)

						except:
							mccir_dc["Key"].append("NaN")

						# APPENDING POSITION INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["Position"].append(mccir1.find("position").text)

						except:
							mccir_dc["Position"].append("NaN")

						# APPENDING RECORD NUMBER INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["RecordNumber"].append(mccir1.find("recordnumber").text)

						except:
							mccir_dc["RecordNumber"].append("NaN")

						# APPENDING ID INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["ID"].append(mccir1.find("id").text)

						except:
							mccir_dc["ID"].append("NaN")

						# APPENDING GUEST CHECK NAME INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["GuestCheckName"].append(mccir1.find("guestcheckname").text)

						except:
							mccir_dc["GuestCheckName"].append("NaN")

						# APPENDING REPORT GROUP ID INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["ReportGroupID"].append(mccir1.find("reportgroupid").text)

						except:
							mccir_dc["ReportGroupID"].append("NaN")

						# APPENDING SORT KEY INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["SortKey"].append(mccir1.find("sortkey").text)

						except:
							mccir_dc["SortKey"].append("NaN")

						# APPENDING STATION ID INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["StationID"].append(mccir1.find("stationid").text)

						except:
							mccir_dc["StationID"].append("NaN")

						# APPENDING OWNER TIME CARD ID INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["OwnerTimeCardID"].append(mccir1.find("ownertimecardid").text)

						except:
							mccir_dc["OwnerTimeCardID"].append("NaN")

						# APPENDING OWNER ID INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["OwnerID"].append(mccir1.find("ownerid").text)

						except:
							mccir_dc["OwnerID"].append("NaN")

						# APPENDING OWNER NAME INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["OwnerName"].append(mccir1.find("ownername").text)

						except:
							mccir_dc["OwnerName"].append("NaN")

						# APPENDING TIME STAMP INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["TimeStamp"].append(mccir1.find("timestamp").text)

						except:
							mccir_dc["TimeStamp"].append("NaN")

						# APPENDING PRICE INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["Price"].append(mccir1.find("price").text)

						except:
							mccir_dc["Price"].append("NaN")

						# APPENDING FLAGS PRINT MODIFIER INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["FlagsPrintModifier"].append(mccir1.find("flagsprintmodifier").text)

						except:
							mccir_dc["FlagsPrintModifier"].append("NaN")

						# APPENDING APPROVED BY INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["ApprovedBy"].append(mccir1.find("approvedby").text)

						except:
							mccir_dc["ApprovedBy"].append("NaN")

						# APPENDING TAX APPLIED 1 INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["TaxApplied1"].append(mccir1.find("taxapplied1").text)

						except:
							mccir_dc["TaxApplied1"].append("NaN")

						# APPENDING ITEM KEY INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["ItemKey"].append(mccir1.find("itemkey").text)

						except:
							mccir_dc["ItemKey"].append("NaN")

						# APPENDING PRICE NUMBER INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["PriceNumber"].append(mccir1.find("pricenumber").text)

						except:
							mccir_dc["PriceNumber"].append("NaN")

						# APPENDING LEVEL INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["Level"].append(mccir1.find("level").text)

						except:
							mccir_dc["Level"].append("NaN")

						# APPENDING FLAGS KITCHEN COMMENT INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["FlagsKitchenComment"].append(mccir1.find("flagskitchencomment").text)

						except:
							mccir_dc["FlagsKitchenComment"].append("NaN")

						# APPENDING FLAGS INCLUDE IN PRICE INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["FlagsIncludeInPrice"].append(mccir1.find("flagsincludeinprice").text)

						except:
							mccir_dc["FlagsIncludeInPrice"].append("NaN")

						# APPENDING FLAGS DISCOUNTED IN PRICE INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["FlagsDiscounted"].append(mccir1.find("flagsdiscounted").text)

						except:
							mccir_dc["FlagsDiscounted"].append("NaN")

						# APPENDING DISCOUNT AMOUNT IN PRICE INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["DiscountAmount"].append(mccir1.find("discountamount").text)

						except:
							mccir_dc["DiscountAmount"].append("NaN")

						# APPENDING DISCOUNT INTERNAL ID IN PRICE INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["DiscountInternalID"].append(mccir1.find("discountinternalid").text)

						except:
							mccir_dc["DiscountInternalID"].append("NaN")

						# APPENDING QTY IN PRICE INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["Qty"].append(mccir1.find("qty").text)

						except:
							mccir_dc["Qty"].append("NaN")

						# APPENDING EXTENSION IN PRICE INTO CHECK ITEM RECORD DATABASE ---

						try:
							mccir_dc["Extension"].append(mccir1.find("extension").text)

						except:
							mccir_dc["Extension"].append("NaN")

					# INPUT CHECK ITEM RECORD TABLE INTO DATABASE --- 

					mccir_pd = pd.DataFrame(mccir_dc)
					print(mccir_pd)

					for mccir2 in range(len(mccir_pd)):
						mccir3 = mccir_pd.iloc[mccir2]
						sqlx.execute("INSERT INTO CHECK_ITEM_RECORD VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", mccir3)

					sql.commit()
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
					print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
					time.sleep(3)


				CIR()

				# PAYMENT RECORD --- 

				def PR():
					# PAYMENT RECORD DICTIONARY --- 

					mcpr_dc = {

					"SeatKey": [],
					"Key": [],
					"Position": [],
					"ID": [],
					"RevenueCenterID": [],
					"Name": [],
					"Amount": [],
					"Tip": [],
					"OwnerID": [],
					"OwnerName": [],
					"OwnerTimeCardID": [],
					"StationID": [],
					"TimeStamp": [],
					"FlagsVerified": [],
					"FlagsApproved": [],
					"FlagsTrack2Recorded": [],
					"Approval": [],
					"Account": [],
					"CustomerName": [],
					"VoidID": [],
					"VoidEmployeeName": [],
					"TimeVoided": [],
					"VoidEmployeeID": []

					}

					print(" ----------------------------")
					print(" |   PAYMENT RECORD TABLE   |")
					print(" ----------------------------\n")
					time.sleep(3)

					mcpr = mcsp.find_all("paymentrecord")
					for mcpr1 in mcpr:
						# APPENDING SEAT KEY INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["SeatKey"].append(mcpr1.find("seatkey").text)

						except:
							mcpr_dc["SeatKey"].append("NaN")

						# APPENDING KEY INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["Key"].append(mcpr1.find("key").text)

						except:
							mcpr_dc["Key"].append("NaN")

						# APPENDING POSITION INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["Position"].append(mcpr1.find("position").text)

						except:
							mcpr_dc["Position"].append("NaN")

						# APPENDING ID INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["ID"].append(mcpr1.find("id").text)

						except:
							mcpr_dc["ID"].append("NaN")

						# APPENDING REVENUE CENTER ID INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["RevenueCenterID"].append(mcpr1.find("revenuecenterid").text)

						except:
							mcpr_dc["RevenueCenterID"].append("NaN")

						# APPENDING NAME INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["Name"].append(mcpr1.find("name").text)

						except:
							mcpr_dc["Name"].append("NaN")

						# APPENDING AMOUNT INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["Amount"].append(mcpr1.find("amount").text)

						except:
							mcpr_dc["Amount"].append("NaN")

						# APPENDING TIP INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["Tip"].append(mcpr1.find("tip").text)

						except:
							mcpr_dc["Tip"].append("NaN")

						# APPENDING OWNER ID INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["OwnerID"].append(mcpr1.find("ownerid").text)

						except:
							mcpr_dc["OwnerID"].append("NaN")

						# APPENDING OWNER NAME INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["OwnerName"].append(mcpr1.find("ownername").text)

						except:
							mcpr_dc["OwnerName"].append("NaN")

						# APPENDING OWNER TIME CARD ID INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["OwnerTimeCardID"].append(mcpr1.find("ownertimecardid").text)

						except:
							mcpr_dc["OwnerTimeCardID"].append("NaN")

						# APPENDING STATION ID INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["StationID"].append(mcpr1.find("stationid").text)

						except:
							mcpr_dc["StationID"].append("NaN")

						# APPENDING TIME STAMP INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["TimeStamp"].append(mcpr1.find("timestamp").text)

						except:
							mcpr_dc["TimeStamp"].append("NaN")

						# APPENDING FLAGS VERIFIED INTO PAYMENT RECORD DATABASE --- 

						try:
							mcpr_dc["FlagsVerified"].append(mcpr1.find("flagsverified").text)

						except:
							mcpr_dc["FlagsVerified"].append("NaN")

						# APPENDING FLAGS APPROVED INTO PAYMENT RECORD DATABASE ---

						try:
							mcpr_dc["FlagsApproved"].append(mcpr1.find("flagsapproved").text)

						except:
							mcpr_dc["FlagsApproved"].append("NaN")

						# APPENDING FLAGS TRACK 2 RECORDED INTO PAYMENT RECORD DATABASE ---

						try:
							mcpr_dc["FlagsTrack2Recorded"].append(mcpr1.find("flagstrack2recorded").text)

						except:
							mcpr_dc["FlagsTrack2Recorded"].append("NaN")

						# APPENDING APPROVAL INTO PAYMENT RECORD DATABASE ---

						try:
							mcpr_dc["Approval"].append(mcpr1.find("approval").text)

						except:
							mcpr_dc["Approval"].append("NaN")

						# APPENDING ACCOUNT INTO PAYMENT RECORD DATABASE ---

						try:
							mcpr_dc["Account"].append(mcpr1.find("account").text)

						except:
							mcpr_dc["Account"].append("NaN")

						# APPENDING CUSTOMER NAME INTO PAYMENT RECORD DATABASE ---

						try:
							mcpr_dc["CustomerName"].append(mcpr1.find("customername").text)

						except:
							mcpr_dc["CustomerName"].append("NaN")

						# APPENDING VOID ID INTO PAYMENT RECORD DATABASE ---

						try:
							mcpr_dc["VoidID"].append(mcpr1.find("voidid").text)

						except:
							mcpr_dc["VoidID"].append("NaN")

						# APPENDING VOID EMPLOYEE NAME INTO PAYMENT RECORD DATABASE ---

						try:
							mcpr_dc["VoidEmployeeName"].append(mcpr1.find("voidemployeename").text)

						except:
							mcpr_dc["VoidEmployeeName"].append("NaN")

						# APPENDING TIME VOIDED INTO PAYMENT RECORD DATABASE ---

						try:
							mcpr_dc["TimeVoided"].append(mcpr1.find("timevoided").text)

						except:
							mcpr_dc["TimeVoided"].append("NaN")

						# APPENDING VOID EMPLOYEE ID INTO PAYMENT RECORD DATABASE ---

						try:
							mcpr_dc["VoidEmployeeID"].append(mcpr1.find("voidemployeeid").text)

						except:
							mcpr_dc["VoidEmployeeID"].append("NaN")

					# INPUT PAYMENT RECORD TABLE INTO DATABASE --- 

					mcpr_pd = pd.DataFrame(mcpr_dc)
					print(mcpr_pd)

					for mcpr2 in range(len(mcpr_pd)):
						mcpr3 = mcpr_pd.iloc[mcpr2]
						sqlx.execute("INSERT INTO PAYMENT_RECORD VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", mcpr3)

					sql.commit()
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
					print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
					time.sleep(3)


				PR()

				# DISCOUNT RECORD --- 

				def DR():
					# DISCOUNT RECORD DICTIONARY --- 

					mcdr_dc = {

					"SeatKey": [],
					"Key": [],
					"Position": [],
					"ID": [],
					"IDExplicit": [],
					"DiscountInternalID": [],
					"Amount": [],
					"TimeStamp": [],
					"ApprovedByID": [],
					"ApprovedByName": [],
					"Source": []

					}

					print(" -----------------------------")
					print(" |   DISCOUNT RECORD TABLE   |")
					print(" -----------------------------\n")
					time.sleep(3)

					mcdr = mcsp.find_all("discountrecord")
					for mcdr1 in mcdr:
						# APPENDING SEAT KEY INTO DISCOUNT RECORD --- 

						try:
							mcdr_dc["SeatKey"].append(mcdr1.find("seatkey").text)

						except:
							mcdr_dc["SeatKey"].append("NaN")

						# APPENDING KEY INTO DISCOUNT RECORD --- 

						try:
							mcdr_dc["Key"].append(mcdr1.find("key").text)

						except:
							mcdr_dc["Key"].append("NaN")

						# APPENDING POSITION INTO DISCOUNT RECORD --- 

						try:
							mcdr_dc["Position"].append(mcdr1.find("position").text)

						except:
							mcdr_dc["Position"].append("NaN")

						# APPENDING ID INTO DISCOUNT RECORD --- 

						try:
							mcdr_dc["ID"].append(mcdr1.find("id").text)

						except:
							mcdr_dc["ID"].append("NaN")

						# APPENDING ID EXPLICIT INTO DISCOUNT RECORD --- 

						try:
							mcdr_dc["IDExplicit"].append(mcdr1.find("idexplicit").text)

						except:
							mcdr_dc["IDExplicit"].append("NaN")

						# APPENDING DISCOUNT INTERNAL ID INTO DISCOUNT RECORD --- 

						try:
							mcdr_dc["DiscountInternalID"].append(mcdr1.find("discountinternalid").text)

						except:
							mcdr_dc["DiscountInternalID"].append("NaN")

						# APPENDING AMOUNT INTO DISCOUNT RECORD --- 

						try:
							mcdr_dc["Amount"].append(mcdr1.find("amount").text)

						except:
							mcdr_dc["Amount"].append("NaN")

						# APPENDING TIME STAMP INTO DISCOUNT RECORD --- 

						try:
							mcdr_dc["TimeStamp"].append(mcdr1.find("timestamp").text)

						except:
							mcdr_dc["TimeStamp"].append("NaN")

						# APPENDING APPROVED BY ID INTO DISCOUNT RECORD --- 

						try:
							mcdr_dc["ApprovedByID"].append(mcdr1.find("approvedbyid").text)

						except:
							mcdr_dc["ApprovedByID"].append("NaN")

						# APPENDING APPROVED BY NAME INTO DISCOUNT RECORD --- 

						try:
							mcdr_dc["ApprovedByName"].append(mcdr1.find("approvedbyname").text)

						except:
							mcdr_dc["ApprovedByName"].append("NaN")

						# APPENDING SOURCE INTO DISCOUNT RECORD --- 

						try:
							mcdr_dc["Source"].append(mcdr1.find("source").text)

						except:
							mcdr_dc["Source"].append("NaN")

					# INPUT DISCOUNT RECORD TABLE INTO DATABASE --- 

					mcdr_pd = pd.DataFrame(mcdr_dc)
					print(mcdr_pd)

					for mcdr2 in range(len(mcdr_pd)):
						mcdr3 = mcdr_pd.iloc[mcdr2]
						sqlx.execute("INSERT INTO DISCOUNT_RECORD VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", mcdr3)

					sql.commit()
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
					print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
					time.sleep(3)


				DR()

				# DELETE RECORD --- 

				def DLTR():
					# DELETE RECORD DICTIONARY --- 

					mcdlt_dc = {

					"Key": [],
					"TimeStamp": [],
					"OwnerID": [],
					"OwnerName": [],
					"CheckID": [],
					"Amount": [],
					"ItemName": [],
					"ApprovedByEmployeeID": [],
					"ApprovedByName": [],
					"ApprovedByTimeCardID": []

					}

					print(" --------------------------")
					print(" |   DELETE RECORD TABLE   |")
					print(" --------------------------\n")
					time.sleep(3)

					mcdlt = mcsp.find_all("deleterecord")
					for mcdlt1 in mcdlt:
						# APPENDING KEY INTO DELETE RECORD --- 

						try:
							mcdlt_dc["Key"].append(mcdlt1.find("key").text)

						except:
							mcdlt_dc["Key"].append("NaN")

						# APPENDING TIME STAMP INTO DELETE RECORD --- 

						try:
							mcdlt_dc["TimeStamp"].append(mcdlt1.find("timestamp").text)

						except:
							mcdlt_dc["TimeStamp"].append("NaN")

						# APPENDING OWNER ID INTO DELETE RECORD --- 

						try:
							mcdlt_dc["OwnerID"].append(mcdlt1.find("ownerid").text)

						except:
							mcdlt_dc["OwnerID"].append("NaN")

						# APPENDING OWNER NAME INTO DELETE RECORD --- 

						try:
							mcdlt_dc["OwnerName"].append(mcdlt1.find("ownername").text)

						except:
							mcdlt_dc["OwnerName"].append("NaN")

						# APPENDING CHECK ID INTO DELETE RECORD --- 

						try:
							mcdlt_dc["CheckID"].append(mcdlt1.find("checkid").text)

						except:
							mcdlt_dc["CheckID"].append("NaN")

						# APPENDING AMOUNT INTO DELETE RECORD --- 

						try:
							mcdlt_dc["Amount"].append(mcdlt1.find("amount").text)

						except:
							mcdlt_dc["Amount"].append("NaN")

						# APPENDING ITEM NAME INTO DELETE RECORD --- 

						try:
							mcdlt_dc["ItemName"].append(mcdlt1.find("itemname").text)

						except:
							mcdlt_dc["ItemName"].append("NaN")

						# APPENDING APPROVED BY EMPLOYEE ID INTO DELETE RECORD --- 

						try:
							mcdlt_dc["ApprovedByEmployeeID"].append(mcdlt1.find("approvedbyemployeeid").text)

						except:
							mcdlt_dc["ApprovedByEmployeeID"].append("NaN")

						# APPENDING APPROVED BY NAME INTO DELETE RECORD --- 

						try:
							mcdlt_dc["ApprovedByName"].append(mcdlt1.find("approvedbyname").text)

						except:
							mcdlt_dc["ApprovedByName"].append("NaN")

						# APPENDING APPROVED BY TIME CARD ID INTO DELETE RECORD ---

						try:
							mcdlt_dc["ApprovedByTimeCardID"].append(mcdlt1.find("approvedbytimecardid").text)

						except:
							mcdlt_dc["ApprovedByTimeCardID"].append("NaN")

					# INPUT DELETE RECORD TABLE INTO DATABASE --- 

					mcdlt_pd = pd.DataFrame(mcdlt_dc)
					print(mcdlt_pd)

					for mcdlt2 in range(len(mcdlt_pd)):
						mcdlt3 = mcdlt_pd.iloc[mcdlt2]
						sqlx.execute("INSERT INTO DELETE_RECORD VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", mcdlt3)

					sql.commit()
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
					print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
					time.sleep(3)


				DLTR()

				# TIME CARD RECORD --- 

				def TCR():
					# TIME CARD RECORD DICTIONARY --- 

					mctc_dc = {

					"ID": [],
					"OwnerID": [],
					"JobID": [],
					"PayRate": [],
					"RevenueCenterID": [],
					"DeleteCount": [],
					"TimeIn": [],
					"TimeOut": [],
					"Edited": [],
					"RegularTime": [],
					"TotalTime": [],
					"AutomaticClockOut": [],
					"DailyOvertime": [],
					"DailyOTRate": [],
					"WeeklyOTRate": [],
					"DoubleOTRate": [],
					"Day6OTRate": [],
					"Day7OTRate": [],
					"Cost": [],
					"TotalCost": [],
					"RegularPay": [],
					"NoSales": [],
					"DoubleOvertime": [],
					"WeeklyOvertime": [],
					"Day7Overtime": [],
					"DeclaredTips": [],
					"Break1TimeIn": [],
					"Break1TimeOut": [],
					"Break1NewTimeIn": [],
					"Break1NewTimeOut": [],
					"BreakTime": [],
					"Deleted": []

					}

					print(" ------------------------------")
					print(" |   TIME CARD RECORD TABLE   |")
					print(" ------------------------------\n")
					time.sleep(3)

					mctc = mcsp.find_all("timecardrecord")
					for mctc1 in mctc:
						# APPENDING ID INTO TIME CARD RECORD DATABASE --- 

						try:
							mctc_dc["ID"].append(mctc1.find("id").text)

						except:
							mctc_dc["ID"].append("NaN")

						# APPENDING OWNER ID INTO TIME CARD RECORD DATABASE --- 

						try:
							mctc_dc["OwnerID"].append(mctc1.find("ownerid").text)

						except:
							mctc_dc["OwnerID"].append("NaN")

						# APPENDING JOB ID INTO TIME CARD RECORD DATABASE --- 

						try:
							mctc_dc["JobID"].append(mctc1.find("jobid").text)

						except:
							mctc_dc["JobID"].append("NaN")

						# APPENDING PAY RATE INTO TIME CARD RECORD DATABASE --- 

						try:
							mctc_dc["PayRate"].append(mctc1.find("payrate").text)

						except:
							mctc_dc["PayRate"].append("NaN")

						# APPENDING REVENUE CENTER ID INTO TIME CARD RECORD DATABASE --- 

						try:
							mctc_dc["RevenueCenterID"].append(mctc1.find("revenuecenterid").text)

						except:
							mctc_dc["RevenueCenterID"].append("NaN")

						# APPENDING DELETE COUNT INTO TIME CARD RECORD DATABASE --- 

						try:
							mctc_dc["DeleteCount"].append(mctc1.find("deletecount").text)

						except:
							mctc_dc["DeleteCount"].append("NaN")

						# APPENDING TIME IN INTO TIME CARD RECORD DATABASE --- 

						try:
							mctc_dc["TimeIn"].append(mctc1.find("timein").text)

						except:
							mctc_dc["TimeIn"].append("NaN")

						# APPENDING TIME OUT INTO TIME CARD RECORD DATABASE --- 

						try:
							mctc_dc["TimeOut"].append(mctc1.find("timeout").text)

						except:
							mctc_dc["TimeOut"].append("NaN")

						# APPENDING EDITED INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["Edited"].append(mctc1.find("edited").text)

						except:
							mctc_dc["Edited"].append("NaN")

						# APPENDING REGULAR TIME INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["RegularTime"].append(mctc1.find("regulartime").text)

						except:
							mctc_dc["RegularTime"].append("NaN")

						# APPENDING TOTAL TIME INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["TotalTime"].append(mctc1.find("totaltime").text)

						except:
							mctc_dc["TotalTime"].append("NaN")

						# APPENDING AUTOMATIC CLOCK OUT INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["AutomaticClockOut"].append(mctc1.find("automaticclockout").text)

						except:
							mctc_dc["AutomaticClockOut"].append("NaN")

						# APPENDING DAILY OVERTIME INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["DailyOvertime"].append(mctc1.find("dailyovertime").text)

						except:
							mctc_dc["DailyOvertime"].append("NaN")

						# APPENDING DAILY OT RATE INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["DailyOTRate"].append(mctc1.find("dailyotrate").text)

						except:
							mctc_dc["DailyOTRate"].append("NaN")

						# APPENDING WEEKLY OT RATE INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["WeeklyOTRate"].append(mctc1.find("weeklyotrate").text)

						except:
							mctc_dc["WeeklyOTRate"].append("NaN")

						# APPENDING DOUBLE OT RATE INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["DoubleOTRate"].append(mctc1.find("doubleotrate").text)

						except:
							mctc_dc["DoubleOTRate"].append("NaN")

						# APPENDING DAY 6 OT RATE INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["Day6OTRate"].append(mctc1.find("day6otrate").text)

						except:
							mctc_dc["Day6OTRate"].append("NaN")

						# APPENDING DAY 7 OT RATE INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["Day7OTRate"].append(mctc1.find("day7otrate").text)

						except:
							mctc_dc["Day7OTRate"].append("NaN")

						# APPENDING COST INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["Cost"].append(mctc1.find("cost").text)

						except:
							mctc_dc["Cost"].append("NaN")

						# APPENDING TOTAL COST INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["TotalCost"].append(mctc1.find("totalcost").text)

						except:
							mctc_dc["TotalCost"].append("NaN")

						# APPENDING REGUlAR PAY INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["RegularPay"].append(mctc1.find("regularpay").text)

						except:
							mctc_dc["RegularPay"].append("NaN")

						# APPENDING NO SALES INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["NoSales"].append(mctc1.find("nosales").text)

						except:
							mctc_dc["NoSales"].append("NaN")

						# APPENDING DOUBLE OVERTIME INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["DoubleOvertime"].append(mctc1.find("doubleovertime").text)

						except:
							mctc_dc["DoubleOvertime"].append("NaN")

						# APPENDING WEEKLY OVERTIME INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["WeeklyOvertime"].append(mctc1.find("weeklyovertime").text)

						except:
							mctc_dc["WeeklyOvertime"].append("NaN")

						# APPENDING DAY 7 OVERTIME INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["Day7Overtime"].append(mctc1.find("day7overtime").text)

						except:
							mctc_dc["Day7Overtime"].append("NaN")

						# APPENDING DECLARED TIPS INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["DeclaredTips"].append(mctc1.find("declaredtips").text)

						except:
							mctc_dc["DeclaredTips"].append("NaN")

						# APPENDING BREAK 1 TIME IN INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["Break1TimeIn"].append(mctc1.find("break1timein").text)

						except:
							mctc_dc["Break1TimeIn"].append("NaN")

						# APPENDING BREAK 1 TIME OUT INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["Break1TimeOut"].append(mctc1.find("break1timeout").text)

						except:
							mctc_dc["Break1TimeOut"].append("NaN")

						# APPENDING BREAK 1 NEW TIME IN INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["Break1NewTimeIn"].append(mctc1.find("break1newtimein").text)

						except:
							mctc_dc["Break1NewTimeIn"].append("NaN")

						# APPENDING BREAK 1 NEW TIME OUT INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["Break1NewTimeOut"].append(mctc1.find("break1newtimeout").text)

						except:
							mctc_dc["Break1NewTimeOut"].append("NaN")

						# APPENDING BREAK TIME INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["BreakTime"].append(mctc1.find("breaktime").text)

						except:
							mctc_dc["BreakTime"].append("NaN")

						# APPENDING DELETED INTO TIME CARD RECORD DATABASE ---

						try:
							mctc_dc["Deleted"].append(mctc1.find("deleted").text)

						except:
							mctc_dc["Deleted"].append("NaN")

					# INPUT TIME CARD RECORD TABLE INTO DATABASE --- 

					mctc_pd = pd.DataFrame(mctc_dc)
					print(mctc_pd)

					for mctc2 in range(len(mctc_pd)):
						mctc3 = mctc_pd.iloc[mctc2]
						sqlx.execute("INSERT INTO TIME_CARD_RECORD VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", mctc3)

					sql.commit()
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
					print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
					time.sleep(3)


				TCR()

				# EMPLOYEE SALES TOTALS --- 

				def EST():
					# EMPLOYEE SALES TOTALS RECORD DICTIONARY --- 

					mcestr_dc = {

					"OwnerID": [],
					"TimeCardID": [],
					"TippedSales": [],
					"OwnerNetChargeTips": [],
					"NetSales": [],
					"TotalSales":[],
					"TotalAccountable": [],
					"GrossCash": [],
					"TipsPaidOut": [],
					"CashAndChecks": [],
					"CreditCardTotal": [],
					"NetCash": [],
					"TotalPayments": [],
					"GuestCount": [],
					"CheckCount": [],
					"DiscountTotalCount": [],
					"DiscountTotal": [],
					"AverageCheckOpenTime": [],
					"TipPool1": [],
					"TipPool2": [],
					"ChargeSales": []

					}

					print(" ------------------------------------------")
					print(" |   EMPLOYEE SALES TOTALS RECORD TABLE   |")
					print(" ------------------------------------------\n")
					time.sleep(3)

					mcestr = mcsp.find_all("employeesalestotals")
					for mcestr1 in mcestr:
						# APPENDING OWNER ID INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["OwnerID"].append(mcestr1.find("ownerid").text)

						except:
							mcestr_dc["OwnerID"].append("NaN")

						# APPENDING TIME CARD ID INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["TimeCardID"].append(mcestr1.find("timecardid").text)

						except:
							mcestr_dc["TimeCardID"].append("NaN")

						# APPENDING TIPPED SALES INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["TippedSales"].append(mcestr1.find("tippedsales").text)

						except:
							mcestr_dc["TippedSales"].append("NaN")

						# APPENDING OWNER NET CHARGE TIPS INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["OwnerNetChargeTips"].append(mcestr1.find("ownernetchargetips").text)

						except:
							mcestr_dc["OwnerNetChargeTips"].append("NaN")

						# APPENDING NET SALES INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["NetSales"].append(mcestr1.find("netsales").text)

						except:
							mcestr_dc["NetSales"].append("NaN")

						# APPENDING TOTAL SALES INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["TotalSales"].append(mcestr1.find("totalsales").text)

						except:
							mcestr_dc["TotalSales"].append("NaN")

						# APPENDING TOTAL ACCOUNTABLE INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["TotalAccountable"].append(mcestr1.find("totalaccountable").text)

						except:
							mcestr_dc["TotalAccountable"].append("NaN")

						# APPENDING GROSS CASH INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["GrossCash"].append(mcestr1.find("grosscash").text)

						except:
							mcestr_dc["GrossCash"].append("NaN")

						# APPENDING TIPS PAID OUT INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["TipsPaidOut"].append(mcestr1.find("tipspaidout").text)

						except:
							mcestr_dc["TipsPaidOut"].append("NaN")

						# APPENDING CASH AND CHECKS INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["CashAndChecks"].append(mcestr1.find("cashandchecks").text)

						except:
							mcestr_dc["CashAndChecks"].append("NaN")

						# APPENDING CREDIT CARD TOTAL INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["CreditCardTotal"].append(mcestr1.find("creditcardtotal").text)

						except:
							mcestr_dc["CreditCardTotal"].append("NaN")

						# APPENDING NET CASH INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["NetCash"].append(mcestr1.find("netcash").text)

						except:
							mcestr_dc["NetCash"].append("NaN")

						# APPENDING TOTAL PAYMENTS INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["TotalPayments"].append(mcestr1.find("totalpayments").text)

						except:
							mcestr_dc["TotalPayments"].append("NaN")

						# APPENDING GUEST COUNT INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["GuestCount"].append(mcestr1.find("guestcount").text)

						except:
							mcestr_dc["GuestCount"].append("NaN")

						# APPENDING CHECK COUNT INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["CheckCount"].append(mcestr1.find("checkcount").text)

						except:
							mcestr_dc["CheckCount"].append("NaN")

						# APPENDING DISCOUNT TOTAL COUNT INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["DiscountTotalCount"].append(mcestr1.find("discounttotalcount").text)

						except:
							mcestr_dc["DiscountTotalCount"].append("NaN")

						# APPENDING DISCOUNT TOTAL INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["DiscountTotal"].append(mcestr1.find("discounttotal").text)

						except:
							mcestr_dc["DiscountTotal"].append("NaN")

						# APPENDING AVERAGE CHECK OPEN TIME INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["AverageCheckOpenTime"].append(mcestr1.find("averagecheckopentime").text)

						except:
							mcestr_dc["AverageCheckOpenTime"].append("NaN")

						# APPENDING TIP POOL 1 INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["TipPool1"].append(mcestr1.find("tippool1").text)

						except:
							mcestr_dc["TipPool1"].append("NaN")

						# APPENDING TIP POOL 2 INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["TipPool2"].append(mcestr1.find("tippool2").text)

						except:
							mcestr_dc["TipPool2"].append("NaN")

						# APPENDING CHARGE SALES INTO EMPLOYEE SALES TOTALS RECORD DATABASE ---

						try:
							mcestr_dc["ChargeSales"].append(mcestr1.find("chargesales").text)

						except:
							mcestr_dc["ChargeSales"].append("NaN")

					# INPUT EMPLOYEE SALES TOTALS RECORD TABLE INTO DATABASE --- 

					mcestr_pd = pd.DataFrame(mcestr_dc)
					print(mcestr_pd)

					for mcestr2 in range(len(mcestr_pd)):
						mcestr3 = mcestr_pd.iloc[mcestr2]
						sqlx.execute("INSERT INTO EMPLOYEE_SALES_TOTALS_RECORD VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", mcestr3)

					sql.commit()
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
					print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
					print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
					time.sleep(3)


				EST()

			shutil.rmtree("mc_ftpq", ignore_errors = True)

			print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
			print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
			print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
			time.sleep(3)

		elif bl == False:
			print(" [[ Copy Status: Failed ]]\n")
			print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
			print("|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
			print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
			shutil.rmtree("mc_ftpq", ignore_errors = True)
			time.sleep(3)

else:
	print("                                               Logging Out")