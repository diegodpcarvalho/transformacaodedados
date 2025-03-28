# Extração de Dados do Anexo I - Rol de Procedimentos

## 📌 Descrição do Projeto
Este projeto tem como objetivo extrair, estruturar e processar os dados contidos na tabela **"Rol de Procedimentos e Eventos em Saúde"** presente no Anexo I de um documento PDF/XLSX. O resultado é salvo em um arquivo CSV estruturado e compactado em um arquivo ZIP.

## 🚀 Funcionalidades Implementadas
### 🔍 1. Leitura e Processamento do Arquivo Original
- Identifica e carrega corretamente a aba correspondente ao Anexo I.
- Ignora as seções de capa e sumário, focando apenas na tabela de dados.

### 🛠️ 2. Limpeza e Estruturação dos Dados
- Identifica automaticamente a linha onde os cabeçalhos reais começam.
- Remove linhas desnecessárias e dados inconsistentes.
- Padroniza os nomes das colunas para um formato mais legível e coerente.

### 🔄 3. Substituição de Abreviações
- **OD** (Odontológico) foi substituído por **Seg. Odontológica**.
- **AMB** (Ambulatorial) foi substituído por **Seg. Ambulatorial**.

### 📄 4. Geração do Arquivo CSV
- Exporta os dados processados para um arquivo CSV com codificação UTF-8.

### 📦 5. Compactação do Arquivo
- O arquivo CSV é compactado em um arquivo **ZIP** nomeado no formato `Teste_{seu_nome}.zip`.

## 🎯 Melhorias e Diferenciais
✅ **Automatização Completa**: O processo foi projetado para funcionar automaticamente, desde a leitura até a geração do arquivo ZIP.
✅ **Flexibilidade**: Pode ser facilmente adaptado para outros formatos de dados ou novas versões do Anexo I.
✅ **Uso de Boas Práticas**:
- Pandas para manipulação de dados de forma eficiente.
- Identificação dinâmica da linha de cabeçalho para evitar ajustes manuais.
- Tratamento de erros para garantir a robustez do processamento.

## ⚡ Como Executar
1. Certifique-se de ter **Python 3.8+** instalado.
2. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas openpyxl
   ```
3. Execute o script Python fornecido.
4. O arquivo ZIP será gerado automaticamente na pasta de destino.

## 📩 Contato
Caso tenha dúvidas ou precise de melhorias, estou à disposição para refinamentos e otimizações. 

🔹 Obrigado pela oportunidade! 🔹



