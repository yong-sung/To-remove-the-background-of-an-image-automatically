import tkinter
import tkinter.font
from tkinter import *
from tkinter import filedialog
import os
import threading
from rembg import remove

# 변환 할 사진선택
def select_file_click(): # 파일 선택 버튼을 누르면 호출되는 함수
    dir_path = filedialog.askopenfilename(parent=window,initialdir="//",title='파일을 선택하세요')
    print(dir_path)
    start_path.config(text=dir_path)
    
# 시작버튼이 클릭되면 이미지 배경제거 쓰레드 실행
def btn_go_click(): # 실행 버튼을 누르면 호출되는 함수
    threading.Thread(target=img_proc_thread).start() # 이미지 배경 제거 작업을 수행하는 'img_proc_thread' 함수를 쓰레드로 실행
    
# 이미지 배경제거 쓰레드
def img_proc_thread(): # 선택한 이미지 파일을 읽어와 배경을 제거한 후 변환된 이미지를 저장
    file_path = start_path.cget("text") # 파일의 경로 표시
    lb_state.config(text="변환중 입니다...")
    
    # 선택한 이미지 파일의 경로에서 디렉토리 부분, 파일 이름 부분을 추출
    output_path = os.path.dirname(file_path) + "\\변환완료_" + os.path.basename(file_path)
    
    with open(file_path, 'rb') as i: # 선택한 이미지 파일을 바이너리 모드로 읽기 위해 염
        with open(output_path, 'wb') as o: # 변환된 이미지 파일을 바이너리 모드로 쓰기 위해 염
            input = i.read()
            output = remove(input) # 이미지 배경 제거
            o.write(output)
    lb_state.config(text="변환 완료!!!")
    
# tkinter 윈도우설정
window=tkinter.Tk()
window.title("이미지배경제거")
window.geometry("380x80+800+300")
window.resizable(False, False)

# 파일선택 버튼
start_path = Label(window,width=40,anchor="se") # 라벨 내용이 오른쪽 아래에 정렬
start_path.grid(row=0, column=0)
btn_start = tkinter.Button(window, overrelief="solid",text="파일선택", width=10, command=select_file_click, repeatdelay=1000, repeatinterval=100)
btn_start.grid(row=0, column=1)

# 실행버튼 생성
btn_go = tkinter.Button(window, overrelief="solid",text="실행", width=10, command=btn_go_click, repeatdelay=1000, repeatinterval=100)
btn_go.grid(row=3, column=0)

# 마지막줄에 상태를 표시하는 라벨 생성
lb_state = Label(window,width=40, text="파일을 선택 후 실행버튼을 눌러 실행하세요")
lb_state.grid(row=4, column=0)

window.mainloop()