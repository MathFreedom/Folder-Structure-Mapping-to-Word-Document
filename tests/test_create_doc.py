import os
import sys

# Ensure the project root is on the import path so the module can be imported
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from folder_structure_to_word import collect_folder_structure, create_doc


def test_create_doc_creates_output_dir(tmp_path):
    # Set up a sample directory with a file
    sample_dir = tmp_path / "sample"
    sub_dir = sample_dir / "sub"
    sub_dir.mkdir(parents=True)
    (sub_dir / "file.txt").write_text("data")

    # Collect structure and attempt to save document in non-existent directory
    folder_structure = collect_folder_structure(str(sample_dir))
    output_path = tmp_path / "nonexistent" / "output.docx"
    create_doc(folder_structure, str(output_path))

    assert output_path.exists()
