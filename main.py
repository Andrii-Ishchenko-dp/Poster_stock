import requests
import xlwt


token = '578064:4602865fe26394f496eb17b40a03f60b'
data_start = '20100101'
data_end = input('Введите дату в формате ГГГГММДД: ')

url = 'https://joinposter.com/api/storage.getReportMovement?token={}' \
      '&dateFrom={}' \
      '&dateTo={}' \
      '&storage_id=5' \
      '&type=0'
# значение 0 позволяет выбрать все типы сущностей на складе, а также, все склады

style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

itog=[]

res = requests.get(url.format(token,data_start,data_end)).json()
count_ing = 0
count_name = 0

for i in res['response']:

      ingred = {
            'name':res['response'][count_ing]['ingredient_name'],
            'end':res['response'][count_ing]['end']
      }
      itog.append(ingred)
      count_ing += 1


def importexel(*kwargs):

      wb = xlwt.Workbook()
      ws = wb.add_sheet('Все склады')
      ws.write(0, 0, 'Название:')
      ws.write(0, 1, data_end)
      dict_bez_0_ostatkov = []
      for i in range(len(itog)):
            if itog[i]['end'] == 0:
                  continue
            dict_bez_0_ostatkov.append(itog[i])

      for i in range(len(dict_bez_0_ostatkov)):

            ws.write(1 + i, 0, dict_bez_0_ostatkov[i]['name'])
            ws.write(1 + i, 1, dict_bez_0_ostatkov[i]['end'])


      wb.save('example1.xls')


importexel(itog)

print(res)
print(itog)
print(count_ing)

#Сделать выгрузку остатков по дням в эксель. Каждая вкладка будет отвечать за отдельный склад и одна вкладка с общей инфой




