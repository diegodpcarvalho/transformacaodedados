import pandas as pd
import zipfile
import os


def process_excel_to_zip(excel_path, output_zip, sheet_name=None):
    # 1. Ler o arquivo Excel sem índice extra
    xls = pd.ExcelFile(excel_path)
    sheet_name = sheet_name or xls.sheet_names[-1]  # Pegamos a última aba como padrão
    df = pd.read_excel(xls, sheet_name=sheet_name, index_col=None)  # Certificar que não lê índice

    # 2. Substituir abreviações
    df.replace({"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}, inplace=True)

    # 3. Salvar como CSV sem colunas "Unnamed"
    csv_filename = "dados_procedimentos.csv"
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')  # Certificar que não salva índice

    # 4. Compactar o arquivo CSV
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename)

    # 5. Remover o CSV temporário
    os.remove(csv_filename)
    print(f"Arquivo {output_zip} criado com sucesso!")


# Caminho do arquivo de entrada e saída
excel_path = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.xlsx"
output_zip = "Teste_Diego.zip"

# Executar
process_excel_to_zip(excel_path, output_zip)
