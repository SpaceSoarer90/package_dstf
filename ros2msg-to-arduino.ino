void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    String msg_lx = Serial.readStringUntil('|');
    String msg_rz = Serial.readStringUntil('\n');

    uint32_t l_x = 0;
    uint32_t r_z = 0;

    Serial.println(msg_lx);

    for (int i = 0; i < 31; i++) {
      if (msg_lx[i] == '0') {
        l_x = l_x | 0;
      } else if (msg_lx[i] == '1') {
        l_x = l_x | 1;
      }
      l_x = l_x << 1;
    }

    Serial.print("l_x: ");
    Serial.println((float)l_x);



    Serial.println(msg_rz);

    for (int i = 0; i < 31; i++) {
      if (msg_rz[i] == '0') {
        r_z = r_z | 0;
      } else if (msg_rz[i] == '1') {
        r_z = r_z | 1;
      }
      r_z = r_z << 1;
    }

    Serial.print("r_z: ");
    Serial.println((float)r_z);
  }
}
