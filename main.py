import pandas as pd

list =[]
data = pd.read_excel('lab_pi_101.xlsx')
count = data.shape[0]
count1 =  data['Группа'].str.contains('ПИ101').sum()
pi101 = data[data['Группа'] == "ПИ101"]
stud_pi = len(pi101['Личный номер студента'].unique())
zachetki_pi = data.loc[data['Группа'] == 'ПИ101', 'Личный номер студента'].unique()
zachetki_pi1 = ', '.join(map(str, zachetki_pi))
control = data['Уровень контроля'].unique()
control1 = ', '.join(map(str, control))
goda = data['Год'].unique()
goda_sorted = sorted(goda)
goda1 = ', '.join(map(str, goda_sorted))
print('В исходном датасете содержалось', count, 'оценок, из них', count1, 'оценок относятся к группе ПИ101\n','В датасете находятся оценки', stud_pi, 
      'студентов ПИ101 со следующими личными номерами:', zachetki_pi1,'\n Используемые формы контроля:', control1,'\n Данные представлены по следующим учебным годам:', goda1)