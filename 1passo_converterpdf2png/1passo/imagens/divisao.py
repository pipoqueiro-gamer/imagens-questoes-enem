import os
import fitz  # PyMuPDF

pdf_path = "enem2024.pdf"
output_folder = "imagens"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Em 300 DPI, precisamos aplicar uma matriz de zoom (300 / 72 = 4.166)
zoom = 300 / 72
matriz = fitz.Matrix(zoom, zoom)

print(f"Convertendo '{pdf_path}' para imagens com 300 DPI...")

try:
    # Abre o documento PDF
    doc = fitz.open(pdf_path)

    for i, pagina in enumerate(doc):
        # Renderiza a página como uma imagem (pixmap) com alta resolução
        pix = pagina.get_pixmap(matrix=matriz)

        image_filename = os.path.join(output_folder, f"pagina_enem_{i+1}.png")
        # Salva o arquivo final
        pix.save(image_filename)
        print(f"Página {i+1} salva como '{image_filename}'")

    print(
        f"\nConversão concluída! As imagens foram salvas na pasta '{output_folder}'."
    )

except Exception as e:
    print(f"Ocorreu um erro durante a conversão: {e}")
