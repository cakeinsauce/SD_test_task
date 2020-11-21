# SD test task
## Установка  

Для установки зависимостей используйте
```pip install -r requirements.txt```  
Для запуска сервиса используйте ```python source.py```  
Сущности хранятся в коллекции ```e_store```   
 
## Добавление товара  

Для добавления товара используйте:  
1) ```curl -X POST http://127.0.0.1:5000/ -H "content-type: application/json" -d "{"name" : "Xiaomi MI A1", "description" : "Smartphone", "specification" : {"display" : "IPS", "CPU" : "Cortex-A53", "Camera": "12MP dual back, 5 MP front", "WIFI": "802.11 a/b/g/n/ac"}}"```
  
2) ```curl -X POST  http://127.0.0.1:5000/ -H "content-type: application/json" -d "{"name" : "IPhone SE", "description" : "Smartphone", "specification" : {"display" : "IPS", "CPU" : "A13 Bionic", "Camera": "12MP back, 7 MP front"}}"```  

## Поиск товара по имени и/или параметру  

Для поиска товара используйте:  
Для поиска по имени используется параметр ```name```, для поиска по параметру используется параметр ```spec```. 
Для разделения, в значении параметра между ключом:значением используется нижнее подчёркивание.  
```curl -X GET "http://127.0.0.1:5000/find?name=<value>&spec=<spec"s key>_<spec"s value>" -H "content-type: application/json"```  
Запросы ниже: 
1) Поиск по имени и параметру: ```curl -X GET "http://127.0.0.1:5000/find?name=IPhone%20SE&spec=CPU_A13Bionic" -H "content-type: application/json"```
2) Поиск по имени: ```curl -X GET "http://127.0.0.1:5000/find?name=Xiaomi%20MI%20A1" -H "content-type: application/json"```
3) Поиск по параметру: ```curl -X GET "http://127.0.0.1:5000/find?spec=CPU_A13Bionic" -H "content-type: application/json"```  
  
## Поиск товара по ID  

Для получения деталей товара по ID используйте:  
```curl -X GET http://127.0.0.1:5000/<merch_id> -H "content-type: application/json"```  
Например:  
```curl -X GET http://127.0.0.1:5000/5fb92c9e31ea0e94794b6c5f -H "content-type: application/json"```
