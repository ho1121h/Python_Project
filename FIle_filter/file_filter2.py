import os
import shutil
import tkinter as tk
from tkinter import filedialog

def classify_files(source_folder, dest_folder, ignored_extensions=[]):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1]
            
            if file_extension.lower() in ignored_extensions:
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

def start_classification():
    source_folder = source_entry.get()
    dest_folder = dest_entry.get()

    # 무시할 확장자를 여기에 추가 (소문자로)
    ignored_extensions = ['exe', 'zip', 'rar','png','jpg',
                          'jpeg','7z','sh','geojson','gif']

    classify_files(source_folder, dest_folder, ignored_extensions)
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

# 시작 버튼
start_button = tk.Button(app, text="분류 시작", command=start_classification)
start_button.grid(row=2, column=0, columnspan=3, pady=10)

# 결과 텍스트
result_label = tk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# GUI 실행
app.mainloop()
