import sympy
from tkinter import *
from sympy.plotting import plot
import pygame

pygame.init()
pygame.display.set_caption("SSE | Alpha")
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)

startpage = pygame.image.load("startpage.jpg")

size = (532,464)
screen = pygame.display.set_mode(size)

done = True

def runProgram():
    global done
    while done:
        screen.blit(startpage, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    column_index = event.pos[0] // 60
                    row_index = event.pos[1] // 60
                    if 1 <= column_index <= 6 and 1 <= row_index <= 2 :
                        # gui 창 생성
                        root = Tk()
                        root.title("Draw Graph")
                        root.geometry("532x464+685+278")
                        root.resizable(width=FALSE, height=FALSE)
                        root.option_add("*Font", "맑은고딕 10")

                        # 문자열을 입력 받기 위한 공간
                        funtion = StringVar()
                        domains = StringVar()
                        domaine = StringVar()

                        # x를 심볼로 선언
                        x = sympy.symbols("x")

                        # 함수, 접점, x의 범위를 입력 받음
                        def input():
                            f = funtion.get()

                            start = domains.get()
                            start = float(start)

                            end = domaine.get()
                            end = float(end)

                            sik(f, start, end)

                        # 문자열을 식으로 전환, 자동 미분, 접선의 방정식 생성
                        def sik(f, start, end):
                            f = sympy.sympify(f)
                            draw(f, start, end)

                        # 그래프와 관련된 정보를 gui창에 출력, 그래프 그리기
                        def draw(f, start, end):
                            Label(root, text="함수 :").grid(row=4, column=0)
                            Label(root, text=f).grid(row=4, column=1)

                            p1 = plot(f, (x, start, end), show=False, legend=True)

                            p1.show()

                        Label(root, text="Draw Graph").grid(row=1, column=1)
                        Label(root, text="함수").grid(row=2, column=0)
                        Label(root, text="x축 범위").grid(row=3, column=0)

                        # 함수, 접점, 범위 입력 받는 빈칸
                        Entry(root, textvariable=funtion).grid(row=2, column=1)
                        Entry(root, textvariable=domains, width=10).grid(row=3, column=1)
                        Entry(root, textvariable=domaine, width=10).grid(row=3, column=2)

                        # 함수를 실행시키는 버튼
                        Button(root, text="Draw It", command=input).grid(row=1, column=4)
                        Button(root, text="Quit", command=root.destroy).grid(row=1, column=5)

                        root.mainloop()
                    elif 1 <= column_index <= 6 and 3 <= row_index <= 4 :
                        # gui 창 생성
                        root = Tk()
                        root.title("Draw Tangent Line")
                        root.geometry("532x464+685+278")
                        root.resizable(width=FALSE, height=FALSE)
                        root.option_add("*Font", "맑은고딕 10")

                        # 문자열을 입력 받기 위한 공간
                        funtion = StringVar()
                        var1 = StringVar()
                        domains = StringVar()
                        domaine = StringVar()

                        # x를 심볼로 선언
                        x = sympy.symbols("x")

                        # 함수, 접점, x의 범위를 입력 받음
                        def input():
                            f = funtion.get()

                            x1 = var1.get()
                            x1 = float(x1)

                            start = domains.get()
                            start = float(start)

                            end = domaine.get()
                            end = float(end)

                            sik(f, x1, start, end)

                        # 문자열을 식으로 전환, 자동 미분, 접선의 방정식 생성
                        def sik(f, x1, start, end):
                            f = sympy.sympify(f)

                            f_diff = sympy.diff(f, x)

                            y1 = float(f.subs(x, x1))
                            g = (f_diff.subs(x, x1)) * (x - x1) + y1

                            draw(f, g, f_diff, x1, y1, start, end)

                        # 그래프와 관련된 정보를 gui창에 출력, 그래프 그리기
                        def draw(f, g, f_diff, x1, y1, start, end):
                            Label(root, text="함수 :").grid(row=5, column=0)
                            Label(root, text=f).grid(row=5, column=1)

                            Label(root, text="도함수 :").grid(row=6, column=0)
                            Label(root, text=f_diff).grid(row=6, column=1)

                            Label(root, text="접점 :").grid(row=7, column=0)
                            Label(root, text="({0}, {1})".format(x1, y1)).grid(row=7, column=1)

                            Label(root, text="접선의 방정식 :").grid(row=8, column=0)
                            Label(root, text=g).grid(row=8, column=1)

                            p1 = plot(f, (x, start, end), show=False, legend=True)
                            p2 = plot(g, (x, start, end), show=False, legend=True)

                            p2[0].line_color = 'r'
                            p1.append(p2[0])
                            p1.show()

                        Label(root, text="Draw Tangent Line").grid(row=1, column=1)
                        Label(root, text="함수").grid(row=2, column=0)
                        Label(root, text="접점").grid(row=3, column=0)
                        Label(root, text="x축 범위").grid(row=4, column=0)

                        # 함수, 접점, 범위 입력 받는 빈칸
                        Entry(root, textvariable=funtion).grid(row=2, column=1)
                        Entry(root, textvariable=var1).grid(row=3, column=1)
                        Entry(root, textvariable=domains, width=10).grid(row=4, column=1)
                        Entry(root, textvariable=domaine, width=10).grid(row=4, column=2)

                        # 함수를 실행시키는 버튼
                        Button(root, text="Draw It", command=input).grid(row=1, column=4)
                        Button(root, text="Quit", command=root.destroy).grid(row=1, column=5)

                        root.mainloop()

                    elif 1 <= column_index <= 6 and 5 <= row_index <= 6 :
                        # gui 창 생성
                        root = Tk()
                        root.title("Calculate Integral")
                        root.geometry("532x464+685+278")
                        root.resizable(width=FALSE, height=FALSE)
                        root.option_add("*Font", "맑은고딕 10")

                        # 문자열을 입력 받기 위한 공간
                        funtion = StringVar()
                        var1 = StringVar()
                        var2 = StringVar()
                        domains = StringVar()
                        domaine = StringVar()

                        # x를 심볼로 선언
                        x = sympy.symbols("x")
                        y = sympy.symbols("y")

                        # 함수, 접점, x의 범위를 입력 받음
                        def input():
                            f = funtion.get()

                            x1 = var1.get()
                            x1 = float(x1)

                            x2 = var2.get()
                            x2 = float(x2)

                            start = domains.get()
                            start = float(start)

                            end = domaine.get()
                            end = float(end)

                            sik(f, x1, x2, start, end)

                        # 문자열을 식으로 전환, 자동 미분, 접선의 방정식 생성
                        def sik(f, x1, x2, start, end):
                            f = sympy.sympify(f)

                            f_integrate = sympy.integrate(f, x)
                            result = sympy.integrate(f, (x, x1, x2))

                            draw(f, f_integrate, x1, x2, start, end, result)

                        # 그래프와 관련된 정보를 gui창에 출력, 그래프 그리기
                        def draw(f, f_integrate, x1, x2, start, end, result):
                            Label(root, text="함수 :").grid(row=5, column=0)
                            Label(root, text=f).grid(row=5, column=1)

                            Label(root, text="부정적분 :").grid(row=6, column=0)
                            Label(root, text=f_integrate).grid(row=6, column=1)

                            Label(root, text="적분 범위 :").grid(row=7, column=0)
                            Label(root, text="({0}, {1})".format(x1, x2)).grid(row=7, column=1)

                            Label(root, text="적분 결과 :").grid(row=8, column=0)
                            Label(root, text=result).grid(row=8, column=1)

                            line1= x1
                            line1 =sympy.sympify(line1)
                            p1 = plot(f, (x, start, end), show=False, legend=True)

                            p1.show()

                        Label(root, text="Calculate Integral").grid(row=1, column=1)
                        Label(root, text="함수").grid(row=2, column=0)
                        Label(root, text="적분 범위").grid(row=3, column=0)
                        Label(root, text="x축 범위").grid(row=4, column=0)

                        # 함수, 접점, 범위 입력 받는 빈칸
                        Entry(root, textvariable=funtion).grid(row=2, column=1)
                        Entry(root, textvariable=var1, width=10).grid(row=3, column=1)
                        Entry(root, textvariable=var2, width=10).grid(row=3, column=2)
                        Entry(root, textvariable=domains, width=10).grid(row=4, column=1)
                        Entry(root, textvariable=domaine, width=10).grid(row=4, column=2)

                        # 함수를 실행시키는 버튼
                        Button(root, text="Draw It", command=input).grid(row=1, column=4)
                        Button(root, text="Quit", command=root.destroy).grid(row=1, column=5)

                        root.mainloop()

        pygame.display.update()

runProgram()
pygame.quit()