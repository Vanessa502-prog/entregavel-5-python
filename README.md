# Sistema de Análise de Dados com Python

Repositório desenvolvido para o entregável da Semana 05 (Desafio Sprint 5), com foco em manipulação segura de arquivos, expressões regulares (regex), tratamento robusto de exceções e geração de relatórios automatizados.

# 🚀 Funcionalidades do Projeto
1. **Leitura Segura de Arquivos (`with open`)**: Garante a abertura e o fechamento correto de arquivos CSV utilizando codificação UTF-8.
2. **Validação com Expressões Regulares (`re`)**:
   - **E-mail**: Validação de estrutura padrão de domínios e caracteres (`r"^[\w\.-]+@[\w\.-]+\.\w+$"`).
   - **CPF**: Validação do formato com pontos e traços (`r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"`).
   - **Telefone**: Validação de formato com DDD entre parênteses (`r"^\(\d{2}\)\d{5}-\d{4}$"`).
   - **Data**: Validação do formato ISO `AAAA-MM-DD` (`r"^\d{4}-\d{2}-\d{2}$"`).
3. **Tratamento de Exceções**: Uso estruturado de `try/except/else/finally` para capturar exceções comuns como `FileNotFoundError`, `KeyError` e `ValueError`.
4. **Exceção Personalizada (`FormatoInvalidoError`)**: Classe criada herdando de `Exception` para tratar violações específicas das regras de validação de dados.
5. **Relatório Formatado**: Geração de métricas estatísticas detalhadas utilizando **f-strings**.

# 📂 Exemplo de Entrada (`dados.csv`)
```csv
email,cpf,telefone,data
vanessa.lima@email.com,123.456.789-01,(98)99999-9999,2026-10-13
email_errado.com,12345678901,9899999999,13-10-2026
