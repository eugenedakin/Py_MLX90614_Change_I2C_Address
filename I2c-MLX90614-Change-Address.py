import time
from smbus2 import SMBus

# Define addresses and register
OLD_ADDRESS = 0x5A   # Factory default
NEW_ADDRESS = 0x5C   # Your target address
EEPROM_REG = 0x2E    # The SMBus register for the I2C slave address

# Initialize the I2C bus (normally bus 1 on Raspberry Pi)
bus = SMBus(1)

# Enable Packet Error Checking (PEC) required by the MLX90614
bus.enable_pec()

try:
    print(f"Reading current register value at address {hex(OLD_ADDRESS)}...")
    current_val = bus.read_word_data(OLD_ADDRESS, EEPROM_REG)
    print(f"Current raw data in register: {hex(current_val)}")
    
    # Step 1: Erase the register. The MLX90614 requires writing 0x0000 first.
    print("Erasing old address register...")
    bus.write_word_data(OLD_ADDRESS, EEPROM_REG, 0x0000)
    time.sleep(0.05) # Give the EEPROM time to write
    
    # Step 2: Write the new address. 
    # The high byte usually defaults to 0xBE (or 0x00 depends on the batch). 
    # We will preserve the high byte from the original read and drop in 0x5B.
    high_byte = current_val & 0xFF00
    new_register_value = high_byte | NEW_ADDRESS
    
    print(f"Writing new address value {hex(new_register_value)}...")
    bus.write_word_data(OLD_ADDRESS, EEPROM_REG, new_register_value)
    time.sleep(0.05)
    
    # Step 3: Verify the write
    print("Verifying registry contents...")
    check_val = bus.read_word_data(OLD_ADDRESS, EEPROM_REG)
    print(f"Read back register value: {hex(check_val)}")
    
    if (check_val & 0x00FF) == NEW_ADDRESS:
        print("\n🎉 SUCCESS! Please completely POWER CYCLE the MLX90614 sensor now.")
        print("Once turned back on, it will respond to address 0x5C.")
    else:
        print("\n❌ Error: The value did not save correctly.")

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("Ensure your sensor is wired correctly and I2C is enabled.")
finally:
    bus.close()
