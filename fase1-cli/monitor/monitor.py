import psutil
import time 
import os 

def formatar_barra(porcentagem, tamanho=20):
    preenchido = int(porcentagem/(100/tamanho))
    barra = "█" * preenchido + "-" * (tamanho - preenchido)
    return f"[{barra}] {porcentagem}%"

def info_cpu():
    uso = psutil.cpu_percent()
    print(f"CPU:        {formatar_barra(uso)}")

def info_memory():
    mem = psutil.virtual_memory()
    total_gb = mem.total / (1024 ** 3)
    total_used = mem.used / (1024 ** 3)

    print(f"Memória:    {formatar_barra(mem.percent)}")
    print(f"       {total_used:.2f}GB / {total_gb:.2f}GB")

def info_disk():
    disk = psutil.disk_usage('/')

    total_gb = disk.total / (1024 ** 3 )
    total_used = disk.used / (1024 ** 3 )

    print(f"Disco:      {formatar_barra(disk.percent)}")
    print(f"       {total_used:.2f}GB / {total_gb:.2f}GB")

def main():

    while True:
        os.system('clear')
        print("= = = MONITOR DE SISTEMA = = =")
        print("-" * 50)
        info_cpu()
        print()
        info_memory()
        print()
        info_disk()
        print("-" * 50)

        time.sleep(2)

if __name__ == "__main__":
    main()
