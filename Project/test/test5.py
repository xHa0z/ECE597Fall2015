import opc
pattern = [ 0, 0, 255 ] * 8 * 8
client = opc.Client('192.168.7.2:7890')
client.put_pixels(pattern)
