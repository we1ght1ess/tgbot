import pandas as pd

data = pd.read_excel('lab_pi_101.xlsx')
count = data.shape[0]
count1 =  data['Группа'].str.contains('ПИ101').sum()
zpi = data[data['Группа'] == "ПИ101"]
z = len(zpi['Личный номер студента'].unique())
upi = data.loc[data['Группа'] == 'ПИ101', 'Личный номер студента'].unique()
control = data['Уровень контроля'].unique()
goda = data['Год'].unique()
print('В исходном датасете содержалось', count, 'оценок, из них', count1, 'оценок относятся к группе ПИ101')
print('В датасете находятся оценки', z, 'студентов ПИ101 со следующими личными номерами:', upi)
print('Используемые формы контроля:', control)
print('Данные представлены по следующим учебным годам:', goda)