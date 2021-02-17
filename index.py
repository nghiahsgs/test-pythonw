import io
import time

def write_file_line(file_name,ndung_line):
    f = io.open(file_name, 'a', encoding='utf-8')
    f.write('%s\n'%ndung_line)
    f.close()

file_name = 'log.txt'
for i in range(1000000):
    write_file_line(file_name,i)
    time.sleep(1)


