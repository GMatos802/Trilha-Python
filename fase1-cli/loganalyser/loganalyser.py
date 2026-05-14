import re 
import argparse 
from collections import Counter
from pathlib import Path 

def lerArquivo(caminho):
    try:
        with open(caminho, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return 
    
def criarRelatorio(linhas):
    regex_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    regex_erro = r'ERROR: (.+)'
    regex_info = r'INFO: (.+)'

    ips = []
    erros = []
    infos = []

    for linha in linhas:
        match_ip = re.search(regex_ip, linha)
        match_erro = re.search(regex_erro, linha)
        match_info = re.search(regex_info, linha)
        if match_ip:
            ips.append(match_ip.group())
        if match_erro:
            erros.append(match_erro.group(1))     
        if match_info:
            infos.append(match_info.group(1))  

    return ips, erros, infos

def main():

    parser = argparse.ArgumentParser(description= " Lẽ arquivos de log e retorna análise de erros, ips e infos")
    parser.add_argument("pasta", help="Pasta em que os logs serão analisados", nargs="?")
    parser.add_argument("--error", "-e", help="Resume apenas a análise dos erros", action="store_true")
    parser.add_argument("--info", "-i", help="Resume apenas as infos", action="store_true")
    parser.add_argument("--output", "-o", help="Salva logs em arquivo TXT")
    args = parser.parse_args()

    if args.pasta:    
        pasta_log = Path(args.pasta)
    else:
        print("--- LOG ANALYSER ---")
        print(f"A pasta atual é: {Path.cwd()} ")
        entrada = input("Digite o caminho da pasta com os arquivos de log a serem analisados: ")
        pasta_log = Path(entrada) 
        
    if not pasta_log.exists() or not pasta_log.is_dir():
        print("Caminho inválido!")
        return 
    
    contador_arquivos = 0
    conteudo_relatorio = []
    mostrar_tudo = not args.error and not args.info

    for arquivo in Path(pasta_log).iterdir(): 
        if arquivo.is_file() and arquivo.suffix == '.log':
            contador_arquivos += 1 
            linhas = lerArquivo(arquivo)
            if not linhas:
                continue
            
            ips, erros, infos = criarRelatorio(linhas)

            counter_erros = Counter(erros)
            counter_infos = Counter(infos)
            
            relatorio_atual =[]
            relatorio_atual.append("-------------------")
            relatorio_atual.append(f"...ARQUIVO {contador_arquivos}: {arquivo}")
            relatorio_atual.append(f"- Quantidade de IPs únicos encontrados: {len(set(ips))}")

            if mostrar_tudo or args.error:
                relatorio_atual.append(f"- Erros mais comuns encontrados: {counter_erros.most_common(3)}")
            if mostrar_tudo or args.info:
                relatorio_atual.append(f"- Confirmação de informações: {counter_infos.most_common(3)}")

            relatorio_atual.append("-------------------")

            texto_final = "\n".join(relatorio_atual)

            print(texto_final)

            if args.output:
                conteudo_relatorio.append(texto_final)

    if args.output and contador_arquivos > 0:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write("\n\n".join(conteudo_relatorio))
        print(f"\n[!] Relatório salvo com sucesso em {args.output}")

if __name__ == '__main__':
    main() 
