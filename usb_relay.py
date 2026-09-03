# serial monitor
import serial
import serial.tools.list_ports
import time


class USB_RELAY:
    def __init__(self, hw_id="0483:5740"):
        ports = list(serial.tools.list_ports.comports())
        port = None
        for p in ports:
            print(p, p.hwid)    
            if hw_id in p.hwid:
                port = p.device
        self.ser = serial.Serial(port=port, baudrate=9600, timeout=1)
        # close circuit A0 01 01 A2
        # Open circuit A0 01 00 A1

        self.off_command = b'\xA0\x01\x00\xA1'
        self.on_command = b'\xA0\x01\x01\xA2'
        self.state = {"CH1": False} # there are on and off states, but relay got normal open and normal close, so we can use this to track the state

    def get_response(self) -> bytes:
        # read response
        response = self.ser.readline()
        response = response.decode('utf-8').strip()
        # response is like CH1:ON or CH1:OFF, we can use this to update the state
        if response.startswith("CH1:"):
            if response.endswith("ON"):
                self.state["CH1"] = True
            elif response.endswith("OFF"):
                self.state["CH1"] = False

        return response

    def relay_off(self):
        self.ser.write(self.off_command)
        return self.get_response()

    def relay_on(self):
        self.ser.write(self.on_command)
        return self.get_response()

    def get_state(self):
        self.ser.write(self.get_state_command)
        return self.get_response()

    def toggle(self, hz: float):
        if hz <= 0:
            raise ValueError("Frequency must be positive")
        half_period = 1.0 / (2 * hz)
        while True:
            self.relay_on()
            print("Relay state:", self.state)
            time.sleep(half_period)
            self.relay_off()
            print("Relay state:", self.state)
            time.sleep(half_period)


def main():
    usb_relay = USB_RELAY()
    usb_relay.toggle(100)


if __name__ == '__main__':
    main()