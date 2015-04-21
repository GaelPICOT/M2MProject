#include "mbed.h"
#include "DHT/DHT.h"

//------------------------------------
// Hyperterminal configuration
// 9600 bauds, 8-bit data, no parity
//------------------------------------

Serial pc(SERIAL_TX, SERIAL_RX);
DHT dht(D2, 11);

DigitalIn presence(D7);
 
int main() {
  int i = 0;
  int move = 0, old_move = 0;
  int timer = 0;
  float old_temp=0, old_hum=0, temp=0, hum=0, err=0;
  while(1) {
      i++;
      wait(.2);
      if(i%10 == 0) {
        err = dht.readData();
        temp = dht.ReadTemperature(CELCIUS);
        hum = dht.ReadHumidity();
        if ((old_temp!=temp) || (old_hum!=hum) || (i%500==0)) {
            old_hum = hum;
            old_temp = temp;
            pc.printf("dht %i %.2f %.2f\n", err, hum, temp);
        }
      }
      if (timer == 0) {
           move = presence.read();
           if (move != old_move) {
              printf("p %d\n", move);
              old_move = move;
            }
           if (move == 1) {
               timer = 10;
            }
      } else {
          timer--;
      }
          
    
  }
}
 