from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('control_server', port=502)
client.connect()

client.write_register(1, 123, unit=1)
response = client.read_holding_registers(1, 1, unit=1)
print(f"Register 1 value: {response.registers[0]}")

client.close()