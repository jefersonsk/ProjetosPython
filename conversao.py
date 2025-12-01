valor = float(input('Digite valor b: '))

kb = valor / 10 ** 3
mb = kb / 10 ** 3
gb = mb / 10 ** 3
tb = gb / 10 ** 3
byte = valor / 8
kbyte = byte / 1000
mbyte = kbyte / 1000
gbyte = mbyte / 1000
tbyte = gbyte / 1000
kilobyte = byte / 1024
megabyte = kilobyte / 1024
gigabyte = megabyte / 1024
terabyte = gigabyte / 1024

print(f'kb: {kb:.6f}')
print(f'mb: {mb:.6f}')
print(f'gb: {gb:.6f}')
print(f'tb: {tb:.6f}')
print(f'B: {byte:6f}')
print(f'kB: {kbyte:.6f}')
print(f'MB: {mbyte:.6F}')
print(f'GB: {gbyte:.6f}')
print(f'TB: {tbyte:.6f}')
print(f'KiB: {kilobyte:.6f}')
print(f'MiB: {megabyte:.6f}')
print(f'GiB: {gigabyte:.6f}')
print(f'TiB: {terabyte:.6f}')