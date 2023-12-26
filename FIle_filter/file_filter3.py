import os
import shutil
import tkinter as tk
from tkinter import filedialog, simpledialog

def classify_files(source_folder, dest_folder, selected_extensions=[]):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1]
            
            if file_extension.lower() not in selected_extensions:
                print(f"Ignoring file with extension {file_extension}: {filename}")
                continue
            
            dest_folder_path = os.path.join(dest_folder, file_extension)

            if not os.path.exists(dest_folder_path):
                os.makedirs(dest_folder_path)

            shutil.move(file_path, os.path.join(dest_folder_path, filename))

def browse_source_folder():
    folder_selected = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, folder_selected)

def browse_dest_folder():
    folder_selected = filedialog.askdirectory()
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, folder_selected)

def browse_extensions():
    extensions_selected = simpledialog.askstring("선택한 확장자", "쉼표로 구분하여 확장자를 입력하세요 (예: pdf, docx, xls):")
    if extensions_selected is not None:
        selected_extensions = [ext.strip() for ext in extensions_selected.split(',')]
        extensions_label.config(text=f"선택한 확장자: {', '.join(selected_extensions)}")

def start_classification():
    source_folder = source_entry.get()
    dest_folder = dest_entry.get()

    if not source_folder or not dest_folder:
        result_label.config(text="폴더를 선택하세요.")
        return

    selected_extensions = [ext.strip() for ext in extensions_label.cget("text").split(': ')[1].split(', ')]

    if not selected_extensions:
        result_label.config(text="적어도 하나 이상의 확장자를 선택하세요.")
        return

    classify_files(source_folder, dest_folder, selected_extensions)
    result_label.config(text="파일이 성공적으로 분류되었습니다.")

# GUI 생성
app = tk.Tk()
app.title("File Classifier")

# Source 폴더 라벨 및 엔트리 위젯
source_label = tk.Label(app, text="다운로드 받은 파일이 있는 폴더:")
source_label.grid(row=0, column=0, padx=10, pady=10)

source_entry = tk.Entry(app, width=50)
source_entry.grid(row=0, column=1, padx=10, pady=10)

source_button = tk.Button(app, text="폴더 선택", command=browse_source_folder)
source_button.grid(row=0, column=2, padx=10, pady=10)

# Destination 폴더 라벨 및 엔트리 위젯
dest_label = tk.Label(app, text="분류된 파일을 저장할 폴더:")
dest_label.grid(row=1, column=0, padx=10, pady=10)

dest_entry = tk.Entry(app, width=50)
dest_entry.grid(row=1, column=1, padx=10, pady=10)

dest_button = tk.Button(app, text="폴더 선택", command=browse_dest_folder)
dest_button.grid(row=1, column=2, padx=10, pady=10)

# 선택한 확장자 라벨 및 버튼
extensions_label = tk.Label(app, text="선택한 확장자:")
extensions_label.grid(row=2, column=0, padx=10, pady=10)

extensions_button = tk.Button(app, text="확장자 선택", command=browse_extensions)
extensions_button.grid(row=2, column=1, padx=10, pady=10)

# 시작 버튼
start_button = tk.Button(app, text="분류 시작", command=start_classification)
start_button.grid(row=3, column=0, columnspan=3, pady=10)

# 결과 텍스트
result_label = tk.Label(app, text="")
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# GUI 실행
app.mainloop()
