import os
from pathlib import Path
from docling.document_converter import DocumentConverter


def convert_folder_to_markdown(input_folder, output_folder):
    input_path = Path(input_folder)
    output_path = Path(output_folder)

    if not input_path.exists():
        print("❌ Input folder does not exist.")
        return

    output_path.mkdir(parents=True, exist_ok=True)

    converter = DocumentConverter()
    supported_extensions = [".pdf", ".docx"]

    for file_path in input_path.iterdir():
        if file_path.suffix.lower() in supported_extensions:
            try:
                print(f"Processing: {file_path.name}")

                doc = converter.convert(str(file_path)).document
                markdown_content = doc.export_to_markdown()

                output_file = output_path / (file_path.stem + ".md")

                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(markdown_content)

                print(f"✅ Saved: {output_file.name}")

            except Exception as e:
                print(f"❌ Error processing {file_path.name}: {e}")
        else:
            print(f"Skipping unsupported file: {file_path.name}")

    print("\n🎉 Conversion complete.")


if __name__ == "__main__":
    input_folder = input("Enter input folder path: ").strip()
    output_folder = input("Enter output folder path: ").strip()

    convert_folder_to_markdown(input_folder, output_folder)