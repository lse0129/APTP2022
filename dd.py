import sympy
from tkinter import *
from sympy.plotting import plot

#gui 창 생성
root=Tk()
root.title("접선의 방정식")
root.geometry("640x400+100+100")
root.resizable(width=FALSE, height=FALSE)

#문자열을 입력 받기 위한 공간
funtion=StringVar()
var1=StringVar()
domains=StringVar()
domaine=StringVar()

#x를 심볼로 선언
x = sympy.symbols("x")

#함수, 접점, x의 범위를 입력 받음
def input():
    f = funtion.get()

    x1 = var1.get()
    x1 = float(x1)

    start = domains.get()
    start = float(start)

    end = domaine.get()
    end = float(end)

    sik(f, x1, start, end)

#문자열을 식으로 전환, 자동 미분, 접선의 방정식 생성
def sik(f, x1, start, end):
    f = sympy.sympify(f)

    f_diff = sympy.diff(f, x)

    y1 = float(f.subs(x, x1))
    g = (f_diff.subs(x, x1)) * (x - x1) + y1

    draw(f, g, f_diff, x1, y1, start, end)

#그래프와 관련된 정보를 gui창에 출력, 그래프 그리기
def draw(f, g, f_diff, x1, y1, start, end):
    Message(root, text="함수:").grid(row=5, column=0)
    Message(root, text=f).grid(row=5, column=1)

    Message(root, text="도함수:").grid(row=6, column=0)
    Message(root, text=f_diff).grid(row=6, column=1)

    Message(root, text="접점:").grid(row=7, column=0)
    Message(root, text="({0}, {1})".format(x1, y1)).grid(row=7, column=1)

    Message(root, text="접선의 방정식:").grid(row=8, column=0)
    Message(root, text=g).grid(row=8, column=1)

    p1 = plot(f, (x, start, end), show=False, legend=True)
    p2 = plot(g, (x, start, end), show=False, legend=True)

    p2[0].line_color='r'
    p1.append(p2[0])
    p1.show()


Label(root, text="함수").grid(row=1, column=0)
Label(root, text="접점").grid(row=2, column=0)
Label(root, text="x축 범위").grid(row=3, column=0)

#함수, 접점, 범위 입력 받는 빈칸
Entry(root, textvariable=funtion).grid(row=1, column=1)
Entry(root, textvariable=var1).grid(row=2, column=1)
Entry(root, textvariable=domains, width=10).grid(row=3, column=1)
Entry(root, textvariable=domaine, width=10).grid(row=3, column=2)

#함수를 실행시키는 버튼
Button(root, text="DRaW iT", command=input).grid(row=1, column=3)

root.mainloop()