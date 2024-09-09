# Table name:     google_salaries
# Empid	first_name	last_name	department	education	salary
# 376	Gary	Stokes	Accounting	Master	56760
# 377	Lorenzo	Cortez	Accounting	Doctorate	74127
# 378	Roberta	Mcgee	Administration	Primary	23987
# 379	Myrtle	Munoz	Administration	Primary	31079
# 380	Molly	Walker	Administration	Primary	20725
# 381	Maria	Simmons	Administration	Secondary	39723
# 382	Muriel	Hernandez	Administration	Bachelor	58555
# 383	Andres	Watson	BI	Bachelor	56834
# 384	Wayne	Leonard	BI	Master	65180
# 385	Julius	Poole	BI	Master	55842


# Table name:     google_laptop
# LaptopId	Empid	Brand	Price
# 100	376	Bran1	567600
# 101	377	Bran3	741270
# 102	378	Bran4	239870
# 103	379	Bran10	310790
# 104	380	Bran2	207250
# 105	381	Bran5	397230
# 106	382	Bran8	585550
# 107	383	Bran9	568340
# 108	384	Bran7	651800
# 109	385	Bran6	558420


# Write the join query for which employee is assigned for which laptop 
# Output sample
# LaptopId	Empid	Brand	Price	first_name	last_name
# 100	376	Bran1	567600	Gary	Stokes
# 101	377	Bran3	741270	Lorenzo	Cortez
# 102	378	Bran4	239870	Roberta	Mcgee
# 103	379	Bran10	310790	Myrtle	Munoz
# 104	380	Bran2	207250	Molly	Walker
# 105	381	Bran5	397230	Maria	Simmons
# 106	382	Bran8	585550	Muriel	Hernandez
# 107	383	Bran9	568340	Andres	Watson
# 108	384	Bran7	651800	Wayne	Leonard
# 109	385	Bran6	558420	Julius	Poole


# Answer:
# SELECT 
#     google_laptop.LaptopId, 
#     google_laptop.Empid, 
#     google_laptop.Brand, 
#     google_laptop.Price, 
#     google_salaries.first_name, 
#     google_salaries.last_name
# FROM 
#     google_laptop
# JOIN 
#     google_salaries 
# ON 
#     google_laptop.Empid = google_salaries.Empid;
