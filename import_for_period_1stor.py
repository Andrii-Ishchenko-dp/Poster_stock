import requests
import xlwt


token = '578064:4602865fe26394f496eb17b40a03f60b'

storage=[] # склады в заведении, id, название
count_stor=0

url_stor = 'https://joinposter.com/api/storage.getStorages?token={}'
res_stor = requests.get(url_stor.format(token)).json()
for l in res_stor['response']:
      countofstor ={
            'id':res_stor['response'][count_stor]['storage_id'],
            'name': res_stor['response'][count_stor]['storage_name']
      }
      count_stor+=1
      storage.append(countofstor)

print(storage)

data_start = input('Введите дату начала в формате ГГГГММДД: ')
data_konec_vsei_vigruzki = input('Введите дату конца в формате ГГГГММДД: ')
data_end = data_start
days = (int(data_konec_vsei_vigruzki) - int(data_start))+1
itog=[]
listofname=[] #Список названий ингредиентов и товаров
wb = xlwt.Workbook()

for o in range(len(storage)):

      while int(data_konec_vsei_vigruzki)+1>int(data_end):

            url = 'https://joinposter.com/api/storage.getReportMovement?token={}' \
                  '&dateFrom={}' \
                  '&dateTo={}' \
                  '&storage_id={}' \
                  '&type=0'
            # значение 0 позволяет выбрать все типы сущностей на складе, а также, все склады

            res = requests.get(url.format(token,data_start,data_end,storage[o]['id'])).json()
            count_ing = 0
            itog.append(data_end)
            for i in res['response']:

                  ingred = {
                        'name':res['response'][count_ing]['ingredient_name'],
                        'end':res['response'][count_ing]['end'],
                        'cost_end': res['response'][count_ing]['cost_end']
                  }
                  itog.append(ingred)
                  if res['response'][count_ing]['ingredient_name'] not in listofname: #создал список уникальных названий ингредиентов
                        listofname.append(res['response'][count_ing]['ingredient_name'])
                  count_ing += 1
            data_end = str(int(data_end)+1)



      ws = wb.add_sheet(storage[o]['name'])
      ws.write(0, 0, 'Название:')
      for i in range(len(listofname)): #выгрузил название в список
            ws.write(i+1,0,listofname[i])

      kolichestvo_stolpcov = 1

      for i in itog:
            if type(i) is str:
                  ws.write(0, kolichestvo_stolpcov, i)
                  kolichestvo_stolpcov+=1

      itog.pop(0)
      x=1
      y=1
      for i in range(len(listofname)):
            for t in range(len(itog)):
                  if type(itog[t]) is str:
                        x+=1
                        continue
                  if listofname[i] == itog[t]['name']:
                        ws.write(y,x,itog[t]['end'])
            y+=1
            x=1

wb.save('{}-{}.xls'.format(data_start, data_konec_vsei_vigruzki))








