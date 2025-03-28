# 🏥 Extração de Dados do Anexo I - Rol de Procedimentos  

## 📌 Descrição do Projeto  
Este projeto tem como objetivo **extrair, estruturar e processar** os dados da tabela **"Rol de Procedimentos e Eventos em Saúde"**, presente no **Anexo I** de um documento PDF/XLSX.  
O resultado é salvo em um **arquivo CSV estruturado** e compactado em um **arquivo ZIP**.  

---

## 🚀 Funcionalidades Implementadas  

### 🔍 1. Leitura e Processamento do Arquivo  
✅ Identifica e carrega a aba correta do Anexo I.  
✅ Ignora páginas de capa e sumário, focando apenas na **tabela de dados**.  

### 🛠️ 2. Limpeza e Estruturação  
✅ Detecta automaticamente a linha onde começam os **cabeçalhos reais**.  
✅ Remove **linhas desnecessárias** e corrige **dados inconsistentes**.  
✅ Padroniza os nomes das colunas para um formato mais legível.  

### 🔄 3. Substituição de Abreviações  
✅ **OD** → "Seg. Odontológica"  
✅ **AMB** → "Seg. Ambulatorial"  

### 📄 4. Geração do Arquivo CSV  
✅ Exporta os dados processados para um **arquivo CSV com codificação UTF-8**.  

### 📦 5. Compactação do Arquivo  
✅ O CSV é compactado em um **arquivo ZIP** nomeado como `Teste_{seu_nome}.zip`.  

---

## 🎯 Diferenciais e Melhorias  
- **📌 Automatização Completa**: Da leitura até a geração do arquivo ZIP, sem intervenção manual.  
- **🔄 Flexibilidade**: Adaptável para outros formatos e novas versões do Anexo I.  
- **🛠️ Boas Práticas**:  
  - Uso da biblioteca **Pandas** para processamento eficiente.  
  - Identificação **dinâmica** do cabeçalho para evitar ajustes manuais.  
  - **Tratamento de erros** para garantir robustez no processamento.  

---

## ⚙️ Pré-requisitos  
Certifique-se de ter **Python 3.8+** instalado.  

Instale as bibliotecas necessárias executando:  
```bash
pip install pandas openpyxl



