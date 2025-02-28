from django.shortcuts import render
from .models import WeatherData  
import serial
import time

arduino_port = '/dev/ttyUSB0'  # Altere para a porta correta do seu Arduino
baud_rate = 9600


def get_data_from_arduino():
    try:
        ser = serial.Serial(arduino_port, baud_rate, timeout=1)
        # Aguarda para que a comunicação seja estabelecida
        time.sleep(5)

        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            if "Temperatura" in line:
                temperatura = float(line.split(
                    ":")[1].strip().replace("°C", "").strip())
                chuva_status = ser.readline().decode('utf-8').rstrip()

                # Salvar os dados no banco de dados
                WeatherData.objects.create(
                    temperature=temperatura, rain_status=chuva_status)

                return temperatura, chuva_status
        return "Nenhum dado recebido", "Status desconhecido"
    except serial.SerialException:
        return "Erro ao conectar com o Arduino", "Status desconhecido"

# View que renderiza a página HTML com a temperatura e o status de chuva


def index(request):
    # Obtém temperatura e status da chuva
    temperatura, chuva_status = get_data_from_arduino()
    context = {
        'temperatura': temperatura,  # Passa a temperatura para o template
        'chuva_status': chuva_status  # Passa o status de chuva para o template
    }
    return render(request, 'index.html', context)


def data_list(request):
    weather_data = WeatherData.objects.all().order_by('-timestamp')  # Pega todos os dados, ordenados por timestamp
    return render(request, 'data_list.html', {'weather_data': weather_data})
