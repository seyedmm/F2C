from tkinter import *
import webbrowser

root = Tk()
root.geometry('400x350')
root.resizable(width=False, height=False)
root.title("Farenhait to Celcios converter")



def convert():
    deg=celc.get()
    try:
        deg = int(deg)

        far=((deg - 32)*5)/9
        far = round(far,2)
        final=Tk()
        final.geometry('300x280')
        final.resizable(height=False,width=False)
        final.title('نتیجه نهایی')


        finaltitr= Label(final, text = "تبدیل موفق", font=('Sahel Black', 35), fg='#62bb47')
        finaltext1= Label(final, text = ":فارنهایت", font=('Shabnam Bold', 20))
        finaltext2= Label(final, text = deg, font=('Shabnam Bold', 20))
        finaltext3= Label(final, text = ":سلسیوس(سانتیگراد)", font=('Shabnam Bold', 20))
        finaltext4= Label(final, text = far, font=('Shabnam Bold', 20))


        finaltitr.pack()
        finaltext1.pack()
        finaltext2.pack()
        finaltext3.pack()
        finaltext4.pack()
    except ValueError:
        if str(deg) == '':
            errmsg = 'کادر درجه نباید\nخالی باشد'
        else:
            errmsg= 'لطفا یک عدد در\nکادر وارد کنید'
        error = Tk()
        error.title('خطا')
        error.geometry('400x300')
        error.resizable(height=False,width=False)

        finaltitr= Label(error, text = "تبدیل ناموفق", font=('Sahel Black', 35), fg='#f37e0b')
        errortext=Label(error,text=errmsg, font=('Sahel Black', 45), fg='red')

        finaltitr.pack()
        errortext.pack()
    except:

        error = Tk()
        error.title('خطا')
        error.geometry('400x200')
        error.resizable(height=False,width=False)
        finaltitr= Label(error, text = "تبدیل ناموفق", font=('Sahel Black', 35), fg='#f37e0b')
        errortext=Label(error,text='خطای نامشخص', font=('Sahel Black', 45), fg='red')
        finaltitr.pack()
        errortext.pack()

def omigo():
    webbrowser.open('https://omigo.ir/r/3t4j')




titr=Label(root,text="تبدیل کننده فارنهایت\nبه سلسیوس(سانتیگراد)",font=('Sahel Black',30))
titr.pack()
celc = Entry(root, font=("Vazir",16))
celc.pack()
button= Button(root,text="به سلسیوس تبدیلش کن",command=convert,font=('Lalezar',17), fg='#2b97f3', activeforeground='#1575c6')
button.pack()
contact= Button(root,text="نظرات، پیشنهادات و\nانتقادات، ارتباط با سازنده",command=omigo, font=('Lalezar',13), fg='#62bb47', activeforeground='#2b97f3')
contact.pack()


root.mainloop()
