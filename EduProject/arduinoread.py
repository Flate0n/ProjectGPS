import serial
# Открываем последовательный порт
ser = serial.Serial('COM3', 9600)
date=[];
# Открываем файл для записи данных
def send(text):
    pass
    #data.append

with open('data.csv', 'w') as f:
    # Бесконечный цикл для чтения данных
    while True:
        # Читаем строку из последовательного порта
        line = ser.readline().decode().strip()
        # Записываем строку в файл
        f.write(line + '\n')
        # Сбрасываем буфер записи файла
        f.flush()