import requests
import xlwt


token = '578064:4602865fe26394f496eb17b40a03f60b'
data_start = input('Введите дату начала в формате ГГГГММДД: ')
data_konec_vsei_vigruzki = input('Введите дату конца в формате ГГГГММДД: ')
data_end = data_start
days = (int(data_konec_vsei_vigruzki) - int(data_start))+1
itog=[]
print(days)

while int(data_konec_vsei_vigruzki)+1>int(data_end):

      url = 'https://joinposter.com/api/storage.getReportMovement?token={}' \
            '&dateFrom={}' \
            '&dateTo={}' \
            '&storage_id=5' \
            '&type=0'
      # значение 0 позволяет выбрать все типы сущностей на складе, а также, все склады

      res = requests.get(url.format(token,data_start,data_end)).json()
      count_ing = 0
      itog.append(data_end)
      for i in res['response']:

            ingred = {
                  'name':res['response'][count_ing]['ingredient_name'],
                  'end':res['response'][count_ing]['end'],
                  'cost_end': res['response'][count_ing]['cost_end']
            }
            itog.append(ingred)
            count_ing += 1
      data_end = str(int(data_end)+1)

print(itog)

dict_bez_0_ostatkov=[]
kolichestvo_stolpcov = 1
wb = xlwt.Workbook()
ws = wb.add_sheet('Все склады')
ws.write(0, 0, 'Название:')
ws.write(0, 1, data_start)


#Какие проблемы?
# 1. избавиться от нулевых остатков
# 2. Решить вопрос, если ингредиент заканчивается в выбранный период времени, чтобы не сыпалась выгрузка, так как съедут значения
# 3. Подумать над выгрузкой не по столпцам, а по строкам.



# def importexel(*kwargs):
#
#       wb = xlwt.Workbook()
#       ws = wb.add_sheet('Все склады')
#       ws.write(0, 0, 'Название:')
#       ws.write(0, 1, data_end)
#       ws.write(0, 2, 'Себестоимость:')
#       ws.write(0, 3, 'Остаток в деньгах:')
#       dict_bez_0_ostatkov = []
#       for i in range(len(itog)):
#             if itog[i]['end'] == 0:
#                   continue
#             dict_bez_0_ostatkov.append(itog[i])
#
#       for i in range(len(dict_bez_0_ostatkov)):
#
#             ws.write(1 + i, 0, dict_bez_0_ostatkov[i]['name'])
#             ws.write(1 + i, 1, dict_bez_0_ostatkov[i]['end'])
#             ws.write(1 + i, 2, dict_bez_0_ostatkov[i]['cost_end'])
#             ws.write(1 + i, 3, xlwt.Formula("B{}*C{}".format(i+2,i+2)))
#       ws.write(len(dict_bez_0_ostatkov)+1, 3, xlwt.Formula("SUM(D2:D{})".format(len(dict_bez_0_ostatkov)+1)))
#       wb.save('{}-{}.xls'.format(data_start, data_end))
#
#
# importexel(itog)

# print(res)


#Сделать выгрузку остатков по дням в эксель. Каждая вкладка будет отвечать за отдельный склад и одна вкладка с общей инфой




