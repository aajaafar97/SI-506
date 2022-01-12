# SI 506 Problem Set 03

# PART 1
print('\nPART 1')

day_1 = [
    'Kennedy & Company Education Strategies, LLC',
    'Congressional Research Service',
    'M&T Bank',
    'MassMutual Michigan Metro',
    'Alliance for Catholic Eduation (ACE Teaching Fellows)',
    'enFocus',
    'Buckle',
    'Defense Finance and Accounting Services (DFAS)',
    'AllianceBernstein',
    "Domino's",
    'Epic',
    'Fisher Investments',
    'goPuff dba GoBrands Inc.',
    'Govern For America',
    'Guidehouse',
    'Maxim Integrated Now Part of Analog Devices',
    'Equitable Advisors',
    'Exelon Corporation'
    ]


# PROBLEM 1
print('\nPROBLEM 1')
day_1.sort()
# 1.1

print(f'\nSorted Day 1 List: {day_1}.')

# 1.2
a_companies = day_1[0:2]




print(f"\nThe companies that start with 'A' are {a_companies}.")

# 1.3
num_a_companies = len(a_companies)

print(f"\nThere are {num_a_companies} companies that start with the letter 'A'.")


# PROBLEM 2
print('\nPROBLEM 2')

# 2.1
e_companies = []

for company in day_1:
    if company.lower().startswith('e'):
        e_companies.append(company)

print(e_companies)
# 2.2
num_e_lower = 0

for company in e_companies:
    if company.startswith('e'):
        num_e_lower = num_e_lower+1

print(num_e_lower)


# PART 2

salaries = """Domino's|Graphic Designer|39000
Fisher Investments|Analyst|95916
Department of Health & Human Services|Technical Writing Specialist|76703
Splunk|Front-End Engineer|139554
Domino's|Senior Technical Writer|98000
Department of Health & Human Services|Analyst|71754
Domino's|Digital Specialist|93000
Splunk|Product Manager|134633
Dimensional Insight|Consultant|69359
Splunk|Customer Success Manager|125720
Edgeworth Economics|Consultant|80190
Edgeworth Economics|Economic Consultant|80645
Edgeworth Economics|Computer Systems Engineer|98495
Domino's|Analyst|77937
Fisher Investments|Research Associate|79141
Splunk|Data Analyst|117652
"""


# PROBLEM 3
print('\nPROBLEM 3')
sal_strings = salaries.splitlines()

print(sal_strings)

sal_lists = [] 

for sal in sal_strings:
    sal_list = sal.split('|')
    sal_lists.append(sal_list)

print(sal_lists)

# PROBLEM 4
print('\nPROBLEM 4')
dom_sals = []

i=0
while i <  len(sal_lists):
    name = sal_lists[i][0]
    if "Domino's" in name:
        dom_sals.append(sal_lists[i])
    i +=1

print(dom_sals)

dom_idx = []

i=0
while i <  len(sal_lists):
    name = sal_lists[i][0]
    if "Domino's" in name:
        dom_idx.append(i)
    i +=1

print(dom_idx)



# PROBLEM 5
print('\nPROBLEM 5')
consultant_sals = []


analyst_sals = []
for company in sal_lists:
    if 'Consultant' in company[1]:
        consultant_sals.append(company)
    elif 'Analyst' in company:
        analyst_sals.append(company)

print(analyst_sals)

# PROBLEM 6
print('\nPROBLEM 6')

max_analyst_sal = 0
max_analyst_company = ""

for company in analyst_sals:
    if int(company[2]) > max_analyst_sal:
        max_analyst_sal = int(company[2])
        max_analyst_company = company[0]
 
print(max_analyst_company)

print(max_analyst_sal)
# PROBLEM 7
print('\nPROBLEM 7')
sal_great = []
sal_too_low = []
for i in range(10):
    print(sal_lists[i])
    

for company in sal_lists[:10]:
    if int(company[2]) > 50000:
        sal_great.append(company)
    else:
        sal_too_low.append(company)


print(sal_great)
print(sal_too_low)





