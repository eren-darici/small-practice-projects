import pandas as pd

df = pd.read_excel('applicants.xlsx')


mailsX = []

mailsY = []

mailsZ = []

mailsF = []

applicantsX = df[df['X']==1]
applicantsY = df[df['Y']==1]
applicantsTugce = df[df['Z']==1]
applicantsBatu = df[df['F']==1]

outputX = applicantsX.to_excel('applicantsX.xlsx', engine='xlsxwriter')
outputY = applicantsY.to_excel('applicantsY.xlsx', engine='xlsxwriter')
outputZ = applicantsZ.to_excel('applicantsZ.xlsx', engine='xlsxwriter')
outputF = applicantsF.to_excel('applicantsF.xlsx', engine='xlsxwriter')
