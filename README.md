# Explicação Técnica do Projeto de Monitoramento Ambiental

## 1. Coleta de Dados com o Arduino

### Sensores Utilizados:

- **DHT11**: Sensor responsável por medir a temperatura do ambiente. Ele é conectado a um dos pinos digitais do Arduino.
- **Sensor de Chuva** (simulado): Um sensor digital é utilizado para detectar a presença de chuva. Ele retorna um valor lógico (alto ou baixo) dependendo da presença ou ausência de água.

### Código Arduino:

O Arduino lê periodicamente os dados dos sensores e envia essas informações via comunicação serial para o computador, onde o Django as processa.

No código do Arduino:
- A temperatura é lida através do sensor DHT11 e enviada pela porta serial.
- O status da chuva é detectado por meio de um pino digital e, em seguida, enviado pelo mesmo canal de comunicação.

### Exemplo de Saída Serial:
```
Temperatura: 25.00 °C
SEM CHUVA
```

## 2. Comunicação Serial com o Python

### pySerial:

O **pySerial** é uma biblioteca Python usada para estabelecer comunicação entre o Arduino e o computador. A aplicação Python, que roda juntamente com o Django, lê as informações vindas da porta serial e processa os dados.

### Função `get_data_from_arduino`:

Esta função lê os dados vindos da porta serial e os decodifica. Ela separa a temperatura e o status da chuva e os salva no banco de dados. Caso não haja dados disponíveis ou ocorra algum erro, ele retorna uma mensagem adequada.

```python
def get_data_from_arduino():
    # Código responsável por conectar ao Arduino, ler os dados e salvar no banco
```

## 3. Armazenamento dos Dados

### Banco de Dados SQLite:

O projeto utiliza o **SQLite**, um banco de dados leve e integrado, gerenciado pelo Django. Os dados coletados são salvos em uma tabela chamada `WeatherData`, que contém as seguintes colunas:
- **Temperatura** (float)
- **Status da Chuva** (string)
- **Timestamp** (data e hora)

O Django ORM (Object Relational Mapping) é usado para manipular os dados de forma simples e eficiente, permitindo consultas, inserções e outras operações no banco de dados.

#### Modelo `WeatherData`:

```python
class WeatherData(models.Model):
    temperature = models.FloatField()
    rain_status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
```

## 4. Interface Web com Django

### Exibição em Tempo Real:

Para que as informações de temperatura e status da chuva sejam exibidas em tempo real, a aplicação Django apresenta uma página web onde os usuários podem acompanhar a leitura dos módulos do arduíno a cada 10 segundos, para isso, podemos utilizar JavaScript para fazer atualizações periódicas da página.

### View `index`:

```python
def index(request):a
temperatura, chuva_status = get_data_from_arduino()
context = {
    'temperatura': temperatura,  
    'chuva_status': chuva_status 
}
return render(request, 'index.html', context)
```

#### Template HTML:

```html
    <div>
        <p>A temperatura capturada pelo sensor é: <strong>{{ temperatura }} °C</strong></p>
        <p>Status da chuva: <strong>{{ chuva_status }}</strong></p>
    </div>
```

### Exibição dos Dados:

A aplicação Django apresenta uma página web onde os usuários podem visualizar as leituras de temperatura e status da chuva. Os dados são carregados diretamente do banco de dados e exibidos em uma tabela, organizados pela data e hora da leitura.

#### View `data_list`:

Esta view recupera todos os dados do banco de dados e os envia para um template HTML que renderiza uma tabela com os valores.

```python
def data_list(request):
    weather_data = WeatherData.objects.all().order_by('-timestamp')
    return render(request, 'data_list.html', {'weather_data': weather_data})
```

#### Template HTML:

```html
<table>
    <thead>
        <tr>
            <th>Data e Hora</th>
            <th>Temperatura (°C)</th>
            <th>Status da Chuva</th>
        </tr>
    </thead>
    <tbody>
        {% for data in weather_data %}
        <tr>
            <td>{{ data.timestamp }}</td>
            <td>{{ data.temperature }}</td>
            <td>{{ data.rain_status }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

## 5. Fluxo de Funcionamento

1. **Leitura dos Sensores**: O Arduino lê a temperatura e o status da chuva a cada dois segundos.
2. **Envio via Serial**: Os dados são enviados ao computador por meio da porta serial.
3. **Processamento com Django**: O Python recebe os dados, processa-os e os armazena no banco de dados SQLite.
4. **Exibição em Tempo Real**: O JavaScript atualiza os valores de temperatura e status de chuva a cada 10 segundos na página web.
5. **Exibição Web**: Uma interface web em Django exibe as informações armazenadas de forma organizada e fácil de entender.

## Conclusão

Este projeto integra hardware e software de forma eficiente, permitindo o monitoramento de temperatura e chuva em tempo real. A simplicidade do Arduino e do sensor DHT11, combinada com a robustez do Django e do banco de dados SQLite, oferece uma solução prática para monitoramento ambiental em diversos cenários.
