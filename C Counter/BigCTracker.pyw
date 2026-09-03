from pathlib import Path
import inspect
import datetime
import tkinter as tk
import Foods

today = datetime.date.today()

base_dir = Path(__file__).resolve().parent
logs_dir = base_dir / "logs"
logs_dir.mkdir(exist_ok=True)

FilePath = logs_dir / f"{today}.txt"

window = tk.Tk()
window.geometry("850x450")
window.title("Big C")

window.iconbitmap(base_dir / "C.ico")

def RefreshDailyCalorieCount(CalorieAmountToAdd):
    PreviousCalories = GetStoredCals()
    NewAmount = CalorieAmountToAdd + PreviousCalories
    TotalDailyCalorie.set(NewAmount)
    WriteCals(NewAmount)

def WriteCals(Cals):
    with open(FilePath,"w") as f:
        f.write(str(Cals))

def GetStoredCals() -> int:

    if Path(FilePath).exists():
        with open(FilePath, "r") as f:
            content = f.read().strip()
            return int(content) if content else 0
    else:
        with open(FilePath,"w") as f:
            f.write("")
            return 0
        


def Getinput():
    temp = CalorieInputBox.get()
    CalorieAmount = int(temp)
    print(CalorieAmount)
    CalorieInputBox.delete(0,len(temp))
    RefreshDailyCalorieCount(CalorieAmount)

TotalDailyCalorie = tk.StringVar()
TotalDailyCalorie.set("")
RefreshDailyCalorieCount(0)

CalorieInputBox = tk.Entry(window)
CalorieInputBox.pack(pady=20,padx=10)

for name, obj in inspect.getmembers(Foods,inspect.isclass):
    if obj.__module__ == Foods.__name__:
        instance = obj()
        insName = getattr(instance,"Name", None)
        insCals = getattr(instance,"Calories",None)
        print(insCals)

        instanceButton = tk.Button(window,
                                   text=f"{insName}: {insCals} Calories",
                                   command= lambda cals = insCals: RefreshDailyCalorieCount(cals))
        instanceButton.pack(anchor= "ne", side="top",pady=5,padx=10)




SubmitButton = tk.Button(window,text='Submit',command=Getinput)
SubmitButton.pack()


TotalDailyCalorieText = tk.Label(master=window,textvariable=TotalDailyCalorie,font=("Times New Roman", 52))
TotalDailyCalorieText.pack(pady= 45)





window.mainloop()


