from PyPDF2 import PdfWriter, PdfReader

def split_pdf(input_path, output_path):
    input_pdf = PdfReader(open(input_path, "rb"))

    for i in range(len(input_pdf.pages)):
        output = PdfWriter()
        output.add_page(input_pdf.pages[i])
        output_file_path = "{}/document-page{}.pdf".format(output_path, i)
        with open(output_file_path, "wb") as output_stream:
            output.write(output_stream)

# Example usage:
input_file_path = "/source/path/document.pdf"
output_directory = "/path/to/output/directory"
split_pdf(input_file_path, output_directory)
