#include <DHT.h>

// Definindo o pino de dados do DHT11 e o tipo de sensor
#define DHTPIN 2     // Pino onde o DHT11 está conectado
#define DHTTYPE DHT11 // Tipo do sensor (DHT11)
#define pinSensorD 3

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Inicializa a comunicação serial
  pinMode(pinSensorD, INPUT);
  Serial.begin(9600);
  
  // Inicializa o sensor DHT
  dht.begin();
}

void loop() {
  // Aguarda 2 segundos entre as leituras
  delay(2000);

  // Leitura da temperatura em Celsius
  float temperature = dht.readTemperature();

  // Verifica se houve erro na leitura do sensor
  if (isnan(temperature)) {
    Serial.println("Erro ao ler do sensor DHT!");
  } else {
    // Envia a temperatura pela comunicação serial
    Serial.print("Temperatura: ");
    Serial.print(temperature);
    Serial.println(" °C");
  }
  if (digitalRead(pinSensorD)) {
     Serial.println("SEM CHUVA ");
  } 
  else {
     Serial.println("ESTA CHUVENDO ");
  }
}
