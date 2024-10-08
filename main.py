from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class mainWidget(BoxLayout):
    label_text = NumericProperty(0)
    firstButton = ObjectProperty(None)

    calcul_list = []
    second_calc_list = []

    operateur = False
    multiplication = False
    somme = False
    division = False
    moins = False
    sign_operateur = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def button1Clicked(self, button1):
        if self.operateur == False:
            self.calcul_list.append(button1.text)
            self.ids.calcLabel.text = "".join(self.calcul_list)
            print(str("".join(self.calcul_list)))
        else:
            self.second_calc_list.append(button1.text)
            self.ids.calcLabel.text = "".join(self.second_calc_list)
            print(str("".join(self.second_calc_list)))


    def button2Clicked(self, button2):

        if self.operateur == False:
            self.calcul_list.append(button2.text)
            self.ids.calcLabel.text = "".join(self.calcul_list)
            # self.ids.calcLabel.text = button2.text
            print(str("".join(self.calcul_list)))
        else:
            self.second_calc_list.append(button2.text)
            self.ids.calcLabel.text = "".join(self.second_calc_list)
            # self.ids.calcLabel.text = button2.text
            print(str("".join(self.second_calc_list)))


    def button3Clicked(self, button3):
        if self.operateur == False:
            self.calcul_list.append(button3.text)
            self.ids.calcLabel.text = "".join(self.calcul_list)
        else:
            self.second_calc_list.append(button3.text)
            self.ids.calcLabel.text = "".join(self.second_calc_list)

    def button4Clicked(self, button4):
        if self.operateur == False:
            self.calcul_list.append(button4.text)
            self.ids.calcLabel.text = "".join(self.calcul_list)
        else:
            self.second_calc_list.append(button4.text)
            self.ids.calcLabel.text = "".join(self.second_calc_list)

    def button5Clicked(self, button5):
        if self.operateur == False:
            self.calcul_list.append(button5.text)
            self.ids.calcLabel.text = "".join(self.calcul_list)
        else:
            self.second_calc_list.append(button5.text)
            self.ids.calcLabel.text = "".join(self.second_calc_list)

    def button6Clicked(self, button6):

        if self.operateur == False:

            self.calcul_list.append(button6.text)
            self.ids.calcLabel.text = "".join(self.calcul_list)

        else:

            self.second_calc_list.append(button6.text)
            self.ids.calcLabel.text = "".join(self.second_calc_list)


    def button7Clicked(self, button7):
        if self.operateur == False:
            self.calcul_list.append(button7.text)
            self.ids.calcLabel.text = "".join(self.calcul_list)

        else:
            self.second_calc_list.append(button7.text)
            self.ids.calcLabel.text = "".join(self.second_calc_list)

    def button8Clicked(self, button8):

        if self.operateur == False:
            self.calcul_list.append(button8.text)
            self.ids.calcLabel.text = "".join(self.calcul_list)
        else:
            self.second_calc_list.append(button8.text)
            self.ids.calcLabel.text = "".join(self.second_calc_list)

    def button9Clicked(self, button9):
        if self.operateur == False:
            self.calcul_list.append(button9.text)
            self.ids.calcLabel.text = "".join(self.calcul_list)
        else:
            self.second_calc_list.append(button9.text)
            self.ids.calcLabel.text = "".join(self.second_calc_list)

    def button0Clicked(self, button0):
        if self.operateur == False:
            self.calcul_list.append(button0.text)
            self.ids.calcLabel.text = "".join(self.calcul_list)
        else:
            self.second_calc_list.append(button0.text)
            self.ids.calcLabel.text = "".join(self.second_calc_list)

    def buttonPlusClicked(self, buttonPluss):
        self.somme = True
        self.division = False
        self.moins = False
        self.multiplication = False
        self.operateur = True
        self.sign_operateur = "+"
        if self.operateur:
            # self.calcul_list.append(buttonPlus.text)
            self.ids.calcLabel.text = self.sign_operateur
        # self.operateur = False

    def buttonMinusClicked(self, buttonMinus):
        self.moins = True
        self.somme = False
        self.division = False
        self.multiplication = False
        self.operateur = True
        self.sign_operateur = "-"
        if self.operateur:
            # self.calcul_list.append(buttonMinus.text)
            self.ids.calcLabel.text = self.sign_operateur
        # self.operateur = False

    def buttonDivisionClicked(self, buttonDivision):
        self.division = True
        self.somme = False
        self.moins = False
        self.multiplication = False
        self.operateur = True
        self.sign_operateur = "÷"
        if self.operateur:
            # self.calcul_list.append(buttonDivision.text)
            self.ids.calcLabel.text = self.sign_operateur


    '''def buttonDivisionClicked(self, buttonPlus):
        self.operateur = True
        calc = int(self.calcul_list)
        self.ids.calcLabel.text = str(calc)'''

    def buttonMultiplicationClicked(self, buttonFois):
        self.multiplication = True
        self.moins = False
        self.somme = False
        self.division = False
        self.operateur = True
        self.sign_operateur = "*"
        if self.operateur:
            # self.calcul_list.append(buttonFois.text)
            self.ids.calcLabel.text = self.sign_operateur
        # self.operateur = False

    def my_sum(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b

    def my_div(self, a, b):
        return a / b



    def buttonEqualClicked(self, buttonEqual):


        # total_calc_list = int("".join(self.calcul_list)) + int(self.sign_operateur) + int("".join(self.second_calc_list))

        # self.calcul_list = "".join(self.calcul_list)
        # total_calc = self.calcul_list
        # self.calcul_list.append(buttonEqual.text)
        # self.ids.calcLabel.text = str(total_calc)
        # self.ids.calcLabel.text = str(total_calc_list)
        # int(''.join(map(str, liste)))
        if self.somme:
            print(self.calcul_list)
            a = int(''.join(map(str, self.calcul_list)))
            print(int(''.join(map(str, self.calcul_list))))
            b = int(''.join(map(str, self.second_calc_list)))
            resultat = self.my_sum(a, b)
            self.ids.calcLabel.text = str(resultat)

        if self.multiplication:
            a = float(''.join(map(str, self.calcul_list)))
            b = float(''.join(map(str, self.second_calc_list)))
            resultat = self.multi(a, b)
            self.ids.calcLabel.text = str(resultat)


        if self.moins:
            a = int(''.join(map(str, self.calcul_list)))
            b = int(''.join(map(str, self.second_calc_list)))
            resultat = self.minus(a, b)
            self.ids.calcLabel.text = str(resultat)

        if self.division:
            print(self.calcul_list)
            print(self.second_calc_list)
            a = float(''.join(map(str, self.calcul_list)))
            b = float(''.join(map(str, self.second_calc_list)))
            resultat = self.my_div(a, b)
            self.ids.calcLabel.text = str(resultat)


        self.multiplication = False
        self.moins = False
        self.somme = False
        self.division = False


    def clear_button_clicked(self, ClearButton):
        self.calcul_list.clear()
        self.second_calc_list.clear()
        self.operateur = False
        self.multiplication = False
        self.somme = False
        self.division = False
        self.moins = False
        self.sign_operateur = ""
        self.ids.calcLabel.text = "0"


class calcButtons(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class myCalcApp(App):
    pass


myCalcApp().run()