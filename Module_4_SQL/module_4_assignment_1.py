# Table name:     google_salaries
# id	first_name	last_name	department	education	salary
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
# 386	Louis	Baker	Facilities	Primary	31158
# 387	Sandra	Wright	HR	Primary	24082
# 388	Jenny	Peterson	HR	Secondary	31098
# 389	Ellis	Hodges	HR	Secondary	38128
# 390	Larry	Jacobs	IT	Secondary	33544
# 391	Milton	Pratt	IT	Secondary	35476
# 392	Marvin	Gilbert	IT	Bachelor	41147
# 393	Geoffrey	Montgomery	IT	Bachelor	47757
# 394	Anne	Mann	IT	Master	54863
# 395	Marjorie	Malone	Legal	Bachelor	45149
# 396	Erika	Fuller	Legal	Master	53391
# 397	Guadalupe	Shaw	Legal	Doctorate	62994
# 398	Benny	Scott	Legal	Doctorate	77474
# 399	Geraldine	Stewart	Management	Doctorate	79689
# 400	Sylvia	Ingram	Management	Doctorate	75944


# Select all the columns where employees are getting salary more than 50000
# Ans: 
# SELECT * FROM google_salaries WHERE salary > 50000

# Select first name, department and education where employees first name are started with ‘Ma’
# Ans:
# SELECT first_name, department, education FROM google_salaries WHERE first_name LIKE 'Ma%'

# Select unique department.
# Ans:
# SELECT DISTINCT department FROM google_salaries

# Make a group by education and present the total salary for every group 
# Ans:    
# SELECT education, SUM(salary) AS total_salary FROM google_salaries GROUP BY education