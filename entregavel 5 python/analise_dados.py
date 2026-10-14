import re

# 1. EXCEÇÃO PERSONALIZADA
class FormatoInvalidoError(Exception):
    """Exceção acionada quando um dado não atende ao padrão exigido."""
    def __init__(self, mensagem="O formato do dado informado é inválido."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)


# 2. FUNÇÕES DE VALIDAÇÃO COM REGEX (Raw Strings)
def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))

def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao, cpf))

def validar_telefone(telefone):
    padrao = r"^\(\d{2}\)\d{5}-\d{4}$"
    return bool(re.match(padrao, telefone))

def validar_data(data):
    padrao = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(padrao, data))


# 3. LEITURA SEGURA E TRATAMENTO DE EXCEÇÕES (try/except/else/finally)
nome_arquivo = "dados.csv"
registros_validos = 0
registros_invalidos = 0
dados_processados = []

print("=== INICIANDO PROCESSAMENTO DE DADOS ===")

try:
    # Tentativa de abrir o arquivo com encoding utf-8
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        
        if len(linhas) <= 1:
            raise ValueError("O arquivo está vazio ou contém apenas o cabeçalho.")
            
        cabecalho = linhas[0].strip().split(",")
        colunas_esperadas = ["email", "cpf", "telefone", "data"]
        
        # Validação de colunas (KeyError / ValueError simulado)
        for col in colunas_esperadas:
            if col not in cabecalho:
                raise KeyError(f"A coluna obrigatória '{col}' não foi encontrada no arquivo CSV.")

        # Processamento das linhas de dados
        for num_linha, linha in enumerate(linhas[1:], start=2):
            partes = linha.strip().split(",")
            if len(partes) != 4:
                registros_invalidos += 1
                continue
                
            email, cpf, telefone, data = partes
            
            # Verificando com as regex
            if validar_email(email) and validar_cpf(cpf) and validar_telefone(telefone) and validar_data(data):
                registros_validos += 1
                dados_processados.append({"email": email, "cpf": cpf, "telefone": telefone, "data": data})
            else:
                registros_invalidos += 1
                # Testando a exceção personalizada por regra de negócio
                try:
                    if not validar_email(email):
                        raise FormatoInvalidoError(f"Linha {num_linha}: E-mail inválido ({email})")
                except FormatoInvalidoError as fe:
                    # Log interno da exceção personalizada
                    pass

except FileNotFoundError:
    print(f"[ERRO CRÍTICO] O arquivo '{nome_arquivo}' não foi encontrado.")
except KeyError as ke:
    print(f"[ERRO DE ESTRUTURA] {ke}")
except ValueError as ve:
    print(f"[ERRO DE VALOR] {ve}")
except Exception as e:
    print(f"[ERRO INESPERADO] Ocorreu uma falha: {e}")
else:
    print("[SUCESSO] Arquivo lido e validado estruturalmente sem erros de sistema.")
finally:
    print("[STATUS] Bloco FINALLY executado: Limpeza de recursos e encerramento do ciclo.\n")


# 4. RELATÓRIO FINAL FORMATADO (Utilizando f-strings)
total_registros = registros_validos + registros_invalidos

print("=" * 60)
print(f"{'RELATÓRIO FINAL DE ANÁLISE DE DADOS':^60}")
print("=" * 60)
print(f" Total de registros lidos      : {total_registros}")
print(f" Registros válidos (aprovados) : {registros_validos}")
print(f" Registros inválidos (rejeitados): {registros_invalidos}")
if total_registros > 0:
    taxa_sucesso = (registros_validos / total_registros) * 100
    print(f" Taxa de sucesso da análise    : {taxa_sucesso:.2f}%")
print("=" * 60)