import PyPDF2
import os
import re

class Merger:
    def __init__(self, root):
        # self.merger = PyPDF2.PdfFileMerger()
        self.root = root

    def merge_files(self, paths, progress_bar, show_progress_bar):
        self.merger = PyPDF2.PdfFileMerger()  

        for value, pdf in enumerate(paths):
            print(value)
            
            self.merger.append(pdf)
            self.move_bar(progress_bar, paths, value, show_progress_bar)
            
        self.save_file()
        self.merger.close()
        print("zrobione")
        
    

    def move_bar(self, progress_bar, pdf_amount, value, show_progress_bar):

        show_progress_bar()
        value += 1
        progress_bar['value'] = value/len(pdf_amount) * 100
        self.root.update()
        print(value/len(pdf_amount) * 100)
        self.check_if_bar_full(value, pdf_amount, progress_bar)

    
    def check_if_bar_full(self, value, pdf_amount, progress_bar):
        if value/len(pdf_amount) * 100 == 100:
            progress_bar.pack_forget()        


    #(result)[0-9]+.pdf
    def merge_all_files(self, progress_bar, show_progress_bar):
        self.merger = PyPDF2.PdfFileMerger()
        pdfs = self.get_pdf_files()
        progress_bar['value'] = 0

        for value, pdf in enumerate(pdfs):
            self.merger.append(pdf)
            self.move_bar(progress_bar, pdfs, value, show_progress_bar)
            
        self.save_file()
        self.merger.close()
        print("zrobione")

    def save_file(self):
        saved_amount = self.number_of_existing_merged_pdfs()
        self.merger.write(f"result{saved_amount+1}.pdf")
        # self.merger.close()
        self.root.update()

    def get_pdf_files(self):
        #^(?!result).*.pdf
        #^(?!result).*.pdf\b
        files = self.list_files()

        print(files)
        pdfs = []

        for file_name in files:
            if re.search(r"^(?!result).*.pdf\b", file_name) != None:
            # if file_name.endswith(".pdf"):
                pdfs.append(file_name)
        print(pdfs)
        return pdfs
    
    def list_files(self):
        files = os.listdir()
        return files

    def number_of_existing_merged_pdfs(self):
        print("MERGE FUNCTION")
        files = self.list_files()
        # print(files)
        pdfs = []
        pdf_number = []
        for file_name in files:
            # print(file_name)

            if re.search("lt[0-9]+.pdf", file_name) != None:
                pdfs.append(file_name)
                if re.search("[0-9]", file_name) != None:
                    pdf_number.append(re.search("[0-9]", file_name))
                

                # print("FOUND ONE!")
        # print(pdfs)
        print(pdf_number)

        return len(pdf_number)





    



