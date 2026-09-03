# usb-relay-diustou

USB relay control library for Diustou USB relay devices.

## Installation

```bash
pip install usb-relay-diustou
# or uv 
uv add usb-relay-diustou
```

## Usage

```python
from usb_relay_diustou import USB_RELAY

# Initialize (auto-detects device by default)
relay = USB_RELAY()

# Control channels
relay.relay_on()   # Turn on
relay.relay_off()  # Turn off
relay.get_state()  # Get current state

# Toggle at frequency (runs until interrupted)
relay.toggle(100)  # 100 Hz toggle
```

## Custom device

```python
relay = USB_RELAY(hw_id="0483:5740")
```

## CLI

```bash
usb-relay-diustou
```
