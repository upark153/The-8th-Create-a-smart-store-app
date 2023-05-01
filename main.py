import pymysql
import time
import random
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import MySQLdb
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

plt.rc('font', family = 'Malgun Gothic')
form_class = uic.loadUiType('main.ui')[0]

class Thread(QThread):
    old = pyqtSignal(int)
    # 초기화 메서드
    def __init__(self, parent): # parent는 Main에서 전달하는 self이다.(Main의 인스턴스)
        super().__init__(parent)
        self.parent = parent # self.parent를 사용하여 Main 위젯을 제어할 수 있다.
        self.running = True
        self.num = 0
        self.timer = QTimer(self) # 윈도우가 생성될 때 QTimer 객체 생성해야함
        self.timer.start(1000) # 생성한 객체에 interval(1초) 추가 설정
        self.timer.timeout.connect(self.timeout)
        self.mydb = MySQLdb.connect(host='localhost', port=3306, user='root', password='1073',
                                  db='mealkit', charset='utf8', autocommit=True)
        self.curs = self.mydb.cursor()
        self.curs.execute("SELECT DISTINCT MEALKIT_NAME from mealkit.recipe")
        result = self.curs.fetchall()
        self.list = []
        if result:
            for i in result:
                self.list.append(i[0])
        self.cur_date = QDate.currentDate()
        self.date = self.cur_date.toString(Qt.ISODate)
        self.cur_time = QTime.currentTime()
        self.time = self.cur_time.toString("hh:mm:ss")

        #상품별 판매 금액을 넣어둘 변수
        self.tteokbokki = 0
        self.rozetteokbokki = 0
        self.kimchi = 0
        self.soba = 0
        self.pasta = 0
        self.sondobu = 0
        self.total = 0
        #상품별 판매 개수를 넣어둘 변수
        self.tteokbokki_n = 0
        self.rozetteokbokki_n = 0
        self.kimchi_n = 0
        self.soba_n = 0
        self.pasta_n = 0
        self.sondobu_n = 0
        self.total_n = 0
        self.parent.order_comboBox.currentTextChanged.connect(self.go)
        # self.parent.order_comboBox.currentTextChanged.connect(self.go)


    def run(self):
        # 쓰레드로 동작시킬 함수 내용 구현
        while self.running:
            self.b = random.choice(self.list)
            self.parent.order_comboBox.addItem(self.b)
            self.curs.execute("SELECT DISTINCT SALES from mealkit.recipe where MEALKIT_NAME = '"+self.parent.order_comboBox.currentText()+"'")
            result = self.curs.fetchall()
            if result:
                for i in result:
                    if self.parent.order_comboBox.currentText() == self.parent.food1.text():
                        self.tteokbokki += int(i[0])
                        self.tteokbokki_n += 1
                        self.parent.price_lineEdit1.setText(str(self.tteokbokki))
                        self.parent.number_lineEdit1.setText(str(self.tteokbokki_n))
                        self.curs.execute(
                            "INSERT INTO mealkit.customer_order(date,time,food,count,price,order_result) VALUES ('" + self.date + "', '" + self.time + "', '" + self.parent.food1.text() + "', 1, 4000, 'N') ")
                        self.mydb.commit()
                    elif self.parent.order_comboBox.currentText() == self.parent.food2.text():
                        self.rozetteokbokki += int(i[0])
                        self.rozetteokbokki_n += 1
                        self.parent.price_lineEdit2.setText(str(self.rozetteokbokki))
                        self.parent.number_lineEdit2.setText(str(self.rozetteokbokki_n))
                        self.curs.execute(
                            "INSERT INTO mealkit.customer_order(date,time,food,count,price,order_result) VALUES ('" + self.date + "', '" + self.time + "', '" + self.parent.food2.text() + "', 1, 8000, 'N') ")
                        self.mydb.commit()

                    elif self.parent.order_comboBox.currentText() == self.parent.food3.text():
                        self.kimchi += int(i[0])
                        self.kimchi_n += 1
                        self.parent.price_lineEdit3.setText(str(self.kimchi))
                        self.parent.number_lineEdit3.setText(str(self.kimchi_n))
                        self.curs.execute(
                            "INSERT INTO mealkit.customer_order(date,time,food,count,price,order_result) VALUES ('" + self.date + "', '" + self.time + "', '" + self.parent.food3.text() + "', 1, 10000, 'N') ")
                        self.mydb.commit()

                    elif self.parent.order_comboBox.currentText() == self.parent.food4.text():
                        self.soba += int(i[0])
                        self.soba_n += 1
                        self.parent.price_lineEdit4.setText(str(self.soba))
                        self.parent.number_lineEdit4.setText(str(self.soba_n))
                        self.curs.execute(
                            "INSERT INTO mealkit.customer_order(date,time,food,count,price,order_result) VALUES ('" + self.date + "', '" + self.time + "', '" + self.parent.food4.text() + "', 1, 13000, 'N') ")
                        self.mydb.commit()

                    elif self.parent.order_comboBox.currentText() == self.parent.food5.text():
                        self.pasta += int(i[0])
                        self.pasta_n += 1
                        self.parent.price_lineEdit5.setText(str(self.pasta))
                        self.parent.number_lineEdit5.setText(str(self.pasta_n))
                        self.curs.execute(
                            "INSERT INTO mealkit.customer_order(date,time,food,count,price,order_result) VALUES ('" + self.date + "', '" + self.time + "', '" + self.parent.food5.text() + "', 1, 30000, 'N') ")
                        self.mydb.commit()

                    elif self.parent.order_comboBox.currentText() == self.parent.food6.text():
                        self.sondobu += int(i[0])
                        self.sondobu_n +=1
                        self.parent.price_lineEdit6.setText(str(self.sondobu))
                        self.parent.number_lineEdit6.setText(str(self.sondobu_n))
                        self.curs.execute(
                            "INSERT INTO mealkit.customer_order(date,time,food,count,price,order_result) VALUES ('" + self.date + "', '" + self.time + "', '" + self.parent.food6.text() + "', 1, 10000, 'N') ")
                        self.mydb.commit()

                    self.old.emit(self.num)
                    self.num += 1
                    self.sleep(1)

                    self.total = self.tteokbokki + self.rozetteokbokki + self.kimchi + self.soba +self.pasta + self.sondobu
                    self.total_n = self.tteokbokki_n + self.rozetteokbokki_n + self.kimchi_n + self.soba_n + self.pasta_n + self.sondobu_n
                    self.parent.price_lineEdit7.setText(str(self.total))
                    self.parent.total_number_lineEdit.setText(str(self.total_n))
                    self.parent.order_comboBox.clear()

            time.sleep(30)

    def resume(self):
        self.running = True

    def pause(self):
        self.running = False

    def go(self):
        QMessageBox.about(self.parent,'주문알림',f'{self.parent.order_comboBox.currentText()}를 주문했습니다.')
        time.sleep(1)


    def timeout(self):
        self.cur_date = QDate.currentDate()
        self.str_date = self.cur_date.toString(Qt.ISODate)
        self.cur_time = QTime.currentTime()
        self.str_time = self.cur_time.toString("hh:mm:ss")
        self.parent.statusBar().showMessage(f'현재 날짜:{self.str_date}, 현재 시간: {self.str_time}')

# 스레드 클래스
class Inventoryzero(QThread):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.power=True

    # 스레드 할 때 돌아가야하는 조건문
    def run(self):
        while self.power:
            # 밀키트, 재료 DB 가져오기
            conn=pymysql.connect(host='localhost', port=3306, user='root', password='1073',
                                  db='mealkit', charset='utf8', autocommit=True)
            c=conn.cursor()
            c.execute(f'select * from (select MEALKIT_NAME,convert(min(b.INVENTORY/a.RECIPE_GRAM), signed integer) as 최대개수 \
            from mealkit.recipe as a inner join `mealkit`.`jaelyo` as b on a.RECIPE_CODE = b.RECIPE_CODE \
            group by MEALKIT_NAME)t where 최대개수<2')
            alarm_db=c.fetchall()
            conn.commit()
            conn.close()
            if bool(alarm_db) == True:
                for i in range(len(alarm_db)):
                    self.parent.lack_of_material_label_2.setText(f'{alarm_db[i][0]}\n재고부족')
                    time.sleep(2)
            else:
                self.parent.lack_of_material_label_2.setText(f'재고부족알림창')

class question_thread(QThread):
    def __init__(self, question):
        super().__init__(question)
        self.question = question
        self.db = pymysql.connect(host='localhost', port=3306, user='root', password='1073',
                                  db='mealkit', charset='utf8', autocommit=True)
        self.cursor = self.db.cursor()
        self.question.question_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def run(self):
        while True:
            print("!")
            self.cursor.execute(f"select idcustomer_order from mealkit.complain")
            a = self.cursor.fetchall()

            self.order_id_list = []
            for i in a:
                self.order_id_list.append(i)
            print(self.order_id_list)
            self.order_id_list2 = []
            for j in range(len(self.order_id_list)):
                self.order_id_list2.append(self.order_id_list[j][0])
            print(self.order_id_list2)
            self.num1 = random.sample(self.order_id_list2, 1)
            print(self.num1)
            self.cursor.execute(f"select * from mealkit.complain")
            b = self.cursor.fetchall()
            if b:
                self.complain_list = []
                for i in b:
                    self.complain_list.append(i)
                print(self.complain_list)
                self.question.question_signal = False

                for i in range(len(self.complain_list)):
                        self.question.question_tableWidget.insertRow(i)
                        self.question.question_tableWidget.setColumnCount(4)
                        self.question.question_tableWidget.setItem(i, 0, QTableWidgetItem(str(self.complain_list[i][1])))
                        self.question.question_tableWidget.setItem(i, 1, QTableWidgetItem(str(self.complain_list[i][2])))
                        self.question.question_tableWidget.setItem(i, 2, QTableWidgetItem(str(self.complain_list[i][4])))
                        self.question.question_tableWidget.setItem(i, 3, QTableWidgetItem(str(self.complain_list[i][5])))
                        time.sleep(1)
                        self.question.question_signal = True

                if self.question.question_signal == True:
                    self.question.label_32.setText("질문게시판에 글이 올라왔습니다.")


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.manager_signup_complete_btn.clicked.connect(self.signup_manager)
        self.manager_signup_btn.clicked.connect(self.signup)
        self.manager_login_btn.clicked.connect(self.login_manager)
        self.manager_login_signup_btn.clicked.connect(self.login)
        self.recipe_management_btn.clicked.connect(self.recipe_manage)
        self.recipe_lookup_btn.clicked.connect(self.recipe_index)
        self.recipe_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mealkit_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.recipe_tableWidget.cellClicked.connect(self.click_mealkit)
        self.recipe_index_btn.clicked.connect(self.show_jo)
        self.pushButton.clicked.connect(self.add_recipe)
        self.inventory_management_btn.clicked.connect(self.inventory_management)
        self.item_enrollment_btn_2.clicked.connect(self.add_mealkit)
        self.product_registration_btn.clicked.connect(self.add_product)
        self.recipe_management_btn.clicked.connect(self.recipe_manage)
        self.question_manage_btn_2.clicked.connect(self.question_issue)
        self.jumun_btn_2.clicked.connect(self.mainpage)
        self.question_main_btn.clicked.connect(self.mainpage)
        self.recipe_main_btn_2.clicked.connect(self.mainpage)
        self.recipe_management_go_btn_2.clicked.connect(self.recipe_manage)
        self.inventoryzero = Inventoryzero(self)
        self.inventoryzero.start()
        self.logout_btn.clicked.connect(self.logout)
        # 주문내역제조 버튼 눌렀을 떄
        self.jumun_btn.clicked.connect(self.order_discount_go)
        # 재고조회버튼 눌렀을 때
        self.material_check_btn_2.clicked.connect(self.inventory_search)
        # 재고일괄발주 눌렀을 때
        self.material_check_btn_3.clicked.connect(self.balju)
        # 밀키트 재고량 보이기
        self.make_mealkit()
        self.w = pg.PlotWidget(title="Basic Plot")
        self.mydb = MySQLdb.connect(host='localhost', port=3306, user='root', password='1073',
                                  db='mealkit', charset='utf8', autocommit=True)
        self.curs = self.mydb.cursor()
        self.stackedWidget.setCurrentIndex(0)
        self.menubar.setVisible(True)
        self.timer = QTimer(self)  # 윈도우가 생성될 때 QTimer 객체 생성해야함
        self.timer.start(1000)  # 생성한 객체에 interval(1초) 추가 설정
        self.timer.timeout.connect(self.timeout)
        self.manager_login_btn.clicked.connect(self.threadAction)
        self.actionmainpage.triggered.connect(self.mainpage)
        self.manager_signup_btn.clicked.connect(self.signup)
        self.manager_login_signup_btn.clicked.connect(self.login)
        self.actionlogout.triggered.connect(self.pause)
        self.product_registration_btn.clicked.connect(self.add_product)
        self.actionproduct.triggered.connect(self.add_product)
        self.recipe_management_btn.clicked.connect(self.recipe_manage)
        self.actionreceipe.triggered.connect(self.recipe_manage)
        self.order_management_btn.clicked.connect(self.order)
        self.actionorder.triggered.connect(self.order)
        self.inventory_management_btn.clicked.connect(self.inventory)
        self.actioninventory.triggered.connect(self.inventory)
        self.sales_graph_btn.clicked.connect(self.draw_sales)
        self.inventory_lookup_btn.clicked.connect(self.inventory)


        self.item_choice_combobox.addItems(['-', '떡볶이', '로제떡볶이', '아끼소바', '봉골레파스타','김치찌개', '순두부찌개'])
        self.db = pymysql.connect(host='localhost', port=3306, user='root', password='1073',
                                  db='mealkit', charset='utf8', autocommit=True)
        self.cursor = self.db.cursor()

    def login(self):
        self.stackedWidget.setCurrentIndex(0)

    def signup(self):
        self.stackedWidget.setCurrentIndex(1)

    def mainpage(self):
        self.stackedWidget.setCurrentIndex(2)
        self.menubar.setVisible(True)

    def add_product(self):
        self.stackedWidget.setCurrentIndex(3)

    def order(self):
        self.stackedWidget.setCurrentIndex(4)

    def inventory_management(self):
        self.stackedWidget.setCurrentIndex(5)

    def recipe_manage(self):
        self.stackedWidget.setCurrentIndex(6)

    def question_issue(self):
        self.stackedWidget.setCurrentIndex(7)

    def signup_manager(self):
        self.a = self.manager_id_signup.text()
        self.b = self.manager_password_signup.text()
        self.c = self.manager_birth_signup.text()
        self.d = self.manager_phone_signup.text()
        self.e = self.manager_email_signup.text()
        self.f = self.manager_address_signup.text()

        if self.a =='' or self.b == '' or self.c == '' or self.d =='' or self.e =='' or self.f =='':
            QMessageBox.warning(self, '.', '필수 기재사항을 다 입력해주세요')
            self.stackedWidget.setCurrentIndex(1)

        else:
            self.cursor.execute(f"insert into mealkit.manager_join(MANAGER_ID, MANAGER_PW, MANAGER_BIRTH, MANAGER_PHONE, MANAGER_EMAIL, MANAGER_ADDRESS) "
                            f"values ('{self.a}','{self.b}','{self.c}', '{self.d}','{self.e}','{self.f}')")
            self.cursor.fetchall()
            QMessageBox.information(self, '.', '회원가입에 성공하셨습니다.')
            self.stackedWidget.setCurrentIndex(0)


    def login_manager(self):
        self.cursor.execute("select * from mealkit.manager_join")
        self.login_manager_list = []
        a = self.cursor.fetchall()
        for i in a:
            self.login_manager_list.append(i)
        print(self.login_manager_list)

        for j in range(len(self.login_manager_list)):
            if self.login_manager_list[j][0] == self.manager_id_lineEdit.text() and self.login_manager_list[j][1] == self.manager_password_lineEdit.text():
                QMessageBox.information(self, '.', f'{self.login_manager_list[j][0]}님 반갑습니다.')
                self.stackedWidget.setCurrentIndex(2)
                self.run_question()
                break


        if self.login_manager_list[j][0] != self.manager_id_lineEdit.text() or self.login_manager_list[j][1] != self.manager_password_lineEdit.text():
            QMessageBox.warning(self, '.', '아이디나 비밀번호가 맞지 않습니다.')
            self.manager_id_lineEdit.clear()
            self.manager_password_lineEdit.clear()
            self.stackedWidget.setCurrentIndex(0)

    def recipe_index(self):
        if self.item_choice_combobox.currentText() == '떡볶이':
            self.cursor.execute("select * from mealkit.recipe where MEALKIT_NAME = '떡볶이'")
            self.dduk_basic_list = []
            a = self.cursor.fetchall()
            for i in a:
                self.dduk_basic_list.append(i)
            print(self.dduk_basic_list)
            self.recipe_tableWidget.setRowCount(len(self.dduk_basic_list))
            self.recipe_tableWidget.setColumnCount(len(self.dduk_basic_list[0]))
            for j in range(len(self.dduk_basic_list)):
                for k in range(len(self.dduk_basic_list[j])):
                    self.recipe_tableWidget.setItem(j, k, QTableWidgetItem(str(self.dduk_basic_list[j][k])))

            self.item_price_subcategory.setText(self.dduk_basic_list[0][3])


        if self.item_choice_combobox.currentText() == '로제떡볶이':
            self.cursor.execute("select * from mealkit.recipe where MEALKIT_NAME = '로제떡볶이'")
            self.dduk_basic_list2 = []
            a = self.cursor.fetchall()
            for i in a:
                self.dduk_basic_list2.append(i)
            print(self.dduk_basic_list2)
            self.recipe_tableWidget.setRowCount(len(self.dduk_basic_list2))
            self.recipe_tableWidget.setColumnCount(len(self.dduk_basic_list2[0]))
            for j in range(len(self.dduk_basic_list2)):
                for k in range(len(self.dduk_basic_list2[j])):
                    self.recipe_tableWidget.setItem(j, k, QTableWidgetItem(str(self.dduk_basic_list2[j][k])))

            self.item_price_subcategory.setText(self.dduk_basic_list2[0][3])


        if self.item_choice_combobox.currentText() == '아끼소바':
            self.cursor.execute("select * from mealkit.recipe where MEALKIT_NAME = '아끼소바'")
            self.dduk_basic_list3 = []
            a = self.cursor.fetchall()
            for i in a:
                self.dduk_basic_list3.append(i)
            print(self.dduk_basic_list3)
            self.recipe_tableWidget.setRowCount(len(self.dduk_basic_list3))
            self.recipe_tableWidget.setColumnCount(len(self.dduk_basic_list3[0]))
            for j in range(len(self.dduk_basic_list3)):
                for k in range(len(self.dduk_basic_list3[j])):
                    self.recipe_tableWidget.setItem(j, k, QTableWidgetItem(str(self.dduk_basic_list3[j][k])))

            self.item_price_subcategory.setText(self.dduk_basic_list3[0][3])

        if self.item_choice_combobox.currentText() == '봉골레파스타':
            self.cursor.execute("select * from mealkit.recipe where MEALKIT_NAME = '봉골레파스타'")
            self.dduk_basic_list4 = []
            a = self.cursor.fetchall()
            for i in a:
                self.dduk_basic_list4.append(i)
            print(self.dduk_basic_list4)
            self.recipe_tableWidget.setRowCount(len(self.dduk_basic_list4))
            self.recipe_tableWidget.setColumnCount(len(self.dduk_basic_list4[0]))
            for j in range(len(self.dduk_basic_list4)):
                for k in range(len(self.dduk_basic_list4[j])):
                    self.recipe_tableWidget.setItem(j, k, QTableWidgetItem(str(self.dduk_basic_list4[j][k])))

            self.item_price_subcategory.setText(self.dduk_basic_list4[0][3])

        if self.item_choice_combobox.currentText() == '김치찌개':
            self.cursor.execute("select * from mealkit.recipe where MEALKIT_NAME = '김치찌개'")
            self.dduk_basic_list5 = []
            a = self.cursor.fetchall()
            for i in a:
                self.dduk_basic_list5.append(i)
            print(self.dduk_basic_list5)
            self.recipe_tableWidget.setRowCount(len(self.dduk_basic_list5))
            self.recipe_tableWidget.setColumnCount(len(self.dduk_basic_list5[0]))
            for j in range(len(self.dduk_basic_list5)):
                for k in range(len(self.dduk_basic_list5[j])):
                    self.recipe_tableWidget.setItem(j, k, QTableWidgetItem(str(self.dduk_basic_list5[j][k])))

            self.item_price_subcategory.setText(self.dduk_basic_list5[0][3])

        if self.item_choice_combobox.currentText() == '순두부찌개':
            self.cursor.execute("select * from mealkit.recipe where MEALKIT_NAME = '순두부찌개'")
            self.dduk_basic_list6 = []
            a = self.cursor.fetchall()
            for i in a:
                self.dduk_basic_list6.append(i)
            print(self.dduk_basic_list6)
            self.recipe_tableWidget.setRowCount(len(self.dduk_basic_list6))
            self.recipe_tableWidget.setColumnCount(len(self.dduk_basic_list6[0]))
            for j in range(len(self.dduk_basic_list6)):
                for k in range(len(self.dduk_basic_list6[j])):
                    self.recipe_tableWidget.setItem(j, k, QTableWidgetItem(str(self.dduk_basic_list6[j][k])))

            self.item_price_subcategory.setText(self.dduk_basic_list6[0][3])


    def click_mealkit(self):
        self.m_list = []
        for i in range(self.recipe_tableWidget.columnCount()):
            self.m_list.append(self.recipe_tableWidget.item(self.recipe_tableWidget.currentRow(), i).text())
        print(self.m_list)
        QMessageBox.information(self, '.', f'{self.m_list[4]}(이)가 들어가는 밀키트를 찾았습니다')
        self.cursor.execute(f"select * from mealkit.recipe where RECIPE_CODE = '{self.m_list[5]}'")
        a = self.cursor.fetchall()
        self.recipe_code_list = []
        for i in a:
            self.recipe_code_list.append(i)
        print(self.recipe_code_list)
        self.mealkit_tableWidget.setRowCount(len(self.recipe_code_list))
        self.mealkit_tableWidget.setColumnCount(len(self.recipe_code_list[0]))
        for j in range(len(self.recipe_code_list)):
            for k in range(len(self.recipe_code_list[j])):
                self.mealkit_tableWidget.setItem(j, k, QTableWidgetItem(str(self.recipe_code_list[j][k])))

    def add_recipe(self):

        if self.lineEdit.text() != '' and self.lineEdit_5.text() != '' and self.lineEdit_7.text() != '' and self.lineEdit_8.text() != '' and self.lineEdit_9.text() != '':
                self.cursor.execute(f"insert into mealkit.jaelyo (RECIPE_CODE, RECIPE_NAME, BASE_GRAM, GRAM_PRICE, INVENTORY) values('{self.lineEdit.text()}', '{self.lineEdit_5.text()}', '{self.lineEdit_7.text()}','{self.lineEdit_8.text()}','{self.lineEdit_9.text()}')")
                self.cursor.fetchall()
                QMessageBox.information(self, '.', '레시피 추가 완료.')

        else:
            QMessageBox.warning(self, '.', '기재사항을 다 입력하십시오')
            self.stackedWidget.setCurrentIndex(6)

    def show_jo(self):
        self.cursor.execute("select * from mealkit.jaelyo")
        a = self.cursor.fetchall()
        self.jo_list = []
        for i in a:
            self.jo_list.append(i)
        print(self.jo_list)

        self.jo_tableWidget.setRowCount(len(self.jo_list))
        self.jo_tableWidget.setColumnCount(len(self.jo_list[0]))
        for j in range(len(self.jo_list)):
            for k in range(len(self.jo_list[j])):
                self.jo_tableWidget.setItem(j, k, QTableWidgetItem(str(self.jo_list[j][k])))

    def add_mealkit(self):
        self.cursor.execute(f"insert into mealkit.recipe (MEALKIT_NAME, MEALKIT_CODE, COST_PRICE, SALES, RECIPE_NAME, RECIPE_CODE, RECIPE_GRAM, RECIPE_COST) values('{self.item_name_lineEdit.text()}', '{self.item_mealcode_lineEdit.text()}', {self.item_cp_lineEdit.text()}, '{self.item_price_lineEdit.text()}', '{self.item_recipe_name_lineEdit.text()}', '{self.item_recipe_code_lineEdit.text()}', '{self.item_gram_lineEdit.text()}', '{self.item_recipe_price_lineEdit.text()}')")
        self.cursor.fetchall()
        QMessageBox.information(self, '.', '상품 등록 완료.')

    def run_question(self):
        z = question_thread(self)
        z.start()

    def logout(self):
        self.manager_id_lineEdit.clear()
        self.manager_password_lineEdit.clear()
        self.item_name_lineEdit.clear()
        self.item_mealcode_lineEdit.clear()
        self.item_cp_lineEdit.clear()
        self.item_price_lineEdit.clear()
        self.item_recipe_name_lineEdit.clear()
        self.item_recipe_code_lineEdit.clear()
        self.item_gram_lineEdit.clear()
        self.item_recipe_price_lineEdit.clear()
        self.item_price_subcategory.clear()
        self.lineEdit.clear()
        self.lineEdit_5.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.price_lineEdit7.clear()
        self.total_number_lineEdit.clear()
        self.price_lineEdit1.clear()
        self.number_lineEdit1.clear()
        self.price_lineEdit2.clear()
        self.number_lineEdit2.clear()
        self.price_lineEdit3.clear()
        self.number_lineEdit3.clear()
        self.price_lineEdit4.clear()
        self.number_lineEdit4.clear()
        self.price_lineEdit5.clear()
        self.number_lineEdit5.clear()
        self.price_lineEdit6.clear()
        self.number_lineEdit6.clear()

        self.question_tableWidget.clear()
        self.stackedWidget.setCurrentIndex(0)
        QMessageBox.information(self, '.', '로그아웃')

    #--------------------------------------------고연재---------------------------------------------------------------

    # 재고일괄발주 눌렀을 때
    def balju(self):
        # 재고량 DB 재고량 10000으로 일괄적용
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='1073',
                                  db='mealkit', charset='utf8', autocommit=True)
        a = conn.cursor()
        a.execute(f'update `mealkit`.`jaelyo` set inventory=10000')
        conn.commit()
        conn.close()
        # 변화된 재고량으로 보여주기
        self.inventory_show()
        self.make_mealkit()

    # 재고조회버튼 눌렀을 때
    def inventory_search(self):
        self.inventory_show()  # 재고량 보여주기
        self.make_mealkit()  # 밀키트 수량 보여주기

    # 밀키트별 제조가능 갯수 구하기
    def make_mealkit(self):
        # 밀키트, 재료 DB로 밀키트별 제조가능갯수 가져오기
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='1073',
                                  db='mealkit', charset='utf8', autocommit=True)
        c = conn.cursor()
        c.execute(f'select a.MEALKIT_NAME,convert(min(b.INVENTORY/a.RECIPE_GRAM), signed integer) as 최소갯수 from recipe as a inner join jaelyo as b \
        on a.RECIPE_code=b.RECIPE_CODE group by mealkit_name order by a.mealkit_name')
        make_list = c.fetchall()
        conn.commit()
        conn.close()
        # 라벨에 셋팅
        self.current_amount_label_kimchi.setText(f'{make_list[0][1]}개')
        self.current_amount_label_tteokbokki1.setText(f'{make_list[1][1]}개')
        self.current_amount_label_tteokbokki2.setText(f'{make_list[2][1]}개')
        self.current_amount_label_pasta.setText(f'{make_list[3][1]}개')
        self.current_amount_label_softtofu.setText(f'{make_list[4][1]}개')
        self.current_amount_label_soba.setText(f'{make_list[5][1]}개')

    # 재료:재고량 보여주기
    def inventory_show(self):
        # DB 가져오기
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='1073',
                                  db='mealkit', charset='utf8', autocommit=True)
        c = conn.cursor()
        c.execute(f'SELECT * FROM `mealkit`.`jaelyo` order by inventory')
        self.jaelyo_db = c.fetchall()
        conn.commit()
        conn.close()

        # table 위젯 열, 행 셋팅
        header_list = ['재료명', '재고량(g)']
        self.current_matarial_tableWidget.setColumnCount(len(header_list))
        self.current_matarial_tableWidget.setRowCount(len(self.jaelyo_db))
        self.current_matarial_tableWidget.setHorizontalHeaderLabels(header_list)

        # 테이블 위젯의 헤더정렬
        self.current_matarial_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 각 셀에 값 넣기
        for i in range(len(self.jaelyo_db)):
            self.current_matarial_tableWidget.setItem(i, 0, QTableWidgetItem(str(self.jaelyo_db[i][1])))  # 재료명
        for i in range(len(self.jaelyo_db)):
            self.current_matarial_tableWidget.setItem(i, 1, QTableWidgetItem(str(self.jaelyo_db[i][4])))  # 재고량(g)

    # 제조 안한 주문을 전체 가져와서 order_discount 매서드를 활용해서 전체 바꿔주기
    def order_discount_go(self):
        # order_result='N'인 항목 전체 가져오기
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='1073',
                                  db='mealkit', charset='utf8', autocommit=True)
        c = conn.cursor()
        c.execute(f'SELECT * FROM mealkit.customer_order where order_result="N"')
        standard_db = c.fetchall()
        conn.commit()
        conn.close()
        # 제조할 주문이 없을 경우
        if bool(standard_db) == False:
            QMessageBox.information(self, '알림', '주문이 없습니다')
        # 제조할 주문이 있는 경우
        else:
            # 반복문과 매서드를 활용하여 아직 제조 안한 주문을 하나씩 처리함.
            for i in range(len(standard_db)):
                self.order_discount()  # order_result='N'인 한 개의 주문을 가져와서 재고량 감소시키는 메서드
        self.make_mealkit()  # 밀키트 재고량 보여주는 매서드

    # order_result='N'인 한 개의 주문을 가져와서 재고량 감소시키는 메서드
    def order_discount(self):
        # order_result='N'인 한개의 주문 가져옴
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='1073',
                                  db='mealkit', charset='utf8', autocommit=True)
        c = conn.cursor()
        c.execute(f'SELECT * FROM mealkit.customer_order where order_result="N" limit 1')
        self.count_db = c.fetchall()

        # 주문한 만큼의 재고가 충분히 있는지 확인을 위한 쿼리문
        c.execute(f'select * from (select MEALKIT_NAME,convert(min(b.INVENTORY/a.RECIPE_GRAM), signed integer) as 최대개수 \
        from mealkit.recipe as a inner join `mealkit`.`jaelyo` as b on a.RECIPE_CODE = b.RECIPE_CODE \
        group by MEALKIT_NAME)t where MEALKIT_NAME="{self.count_db[0][3]}" and 최대개수<{self.count_db[0][4]}')
        alarm_db = c.fetchall()
        conn.commit()
        conn.close()

        # 최대개수가 주문량보다 부족한 제품이 있을 때
        if bool(alarm_db) == True:
            if bool(alarm_db) == True and self.count_db[0][3] == alarm_db[0][0]:
                QMessageBox.information(self, '알림', f'{self.count_db[0][3]}재고 부족, 재료 일괄 발주')
                self.balju()
                QMessageBox.information(self, '알림', f'발주완료, 밀키트 제조')
            else:
                self.order_repeat()
        else:
            self.order_repeat()

    # 주문시 반복해서 쓰이는 메서드
    def order_repeat(self):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='1073',
                                  db='mealkit', charset='utf8', autocommit=True)
        c = conn.cursor()

        # 가져온 주문의 재고량과 1번 제조시 들어가는 재료량 가져오기
        c.execute(f'SELECT a.MEALKIT_NAME,b.RECIPE_NAME,a.recipe_gram,b.inventory FROM recipe as a \
                                    inner join mealkit.jaelyo as b on a.RECIPE_CODE=b.RECIPE_CODE where a.mealkit_name="{self.count_db[0][3]}"')
        inventory_db = c.fetchall()

        # 주문 음식의 재고량 변화, order_result="Y"로 변경
        for i in range(len(inventory_db)):
            c.execute(f'update mealkit.jaelyo set inventory={inventory_db[i][3] - int(inventory_db[i][2]) * int(self.count_db[0][4])} where recipe_name="{inventory_db[i][1]}"')
        c.execute(f'update customer_order set order_result="Y" where idcustomer_order="{self.count_db[0][0]}"')
        QMessageBox.information(self, '알림', f'{self.count_db[0][0]}번, {self.count_db[0][3]}주문이 정상적으로 처리되었습니다')
        conn.commit()
        conn.close()
        self.make_mealkit()
        self.inventory_show()

    # --------------------------------------------임성경---------------------------------------------------------------

    def old(self, num):
        print(num)
        # QMessageBox.about(self, '주문알림', f'{num}번 {self.order_comboBox.currentText()}를 주문했습니다.')

    def inventory(self):
        self.curs.execute("SELECT * from mealkit.customer_order")
        result = self.curs.fetchall()
        Row = 0
        self.order_tableWidget.setRowCount(len(result))
        if result:
            for i in result:
                self.order_tableWidget.setItem(Row, 0, QTableWidgetItem(str(i[0])))
                self.order_tableWidget.setItem(Row, 1, QTableWidgetItem(str(i[1])))
                self.order_tableWidget.setItem(Row, 2, QTableWidgetItem(str(i[2])))
                self.order_tableWidget.setItem(Row, 3, QTableWidgetItem(str(i[3])))
                self.order_tableWidget.setItem(Row, 4, QTableWidgetItem(str(int(i[4]))))
                self.order_tableWidget.setItem(Row, 5, QTableWidgetItem(str(int(i[5]))))
                Row += 1
        else:
            pass

    def draw_sales(self):
        self.curs.execute("SELECT food, count(*) from customer_order group by food")
        result = self.curs.fetchall()
        print(result)
        self.curs.execute("SELECT DISTINCT MEALKIT_NAME, COST_PRICE from recipe")
        result1 = self.curs.fetchall()
        print(result1)
        # 그래프 x축 설정

        sales_x = ["떡볶이", "로제떡볶이", "김치찌개", "아끼소바", "파스타", "순두부찌개"]

        x_dict = dict(enumerate(sales_x))
        ticks = [list(zip(x_dict.keys(), x_dict.values()))]

        # 그래프 y값 설정
        self.curs.execute('SELECT food, SUM(price) from customer_order GROUP BY food')
        result = self.curs.fetchall()
        print(result)
        print(result[0][0])
        print(result[0][1])
        if result:
            for i in range(len(sales_x)):
                if i == 0:
                    tteokbokki = result[i][1]
                elif i == 1:
                    rozetteokbokki = result[i][1]
                elif i == 2:
                    kimchi = result[i][1]
                elif i == 3:
                    soba = result[i][1]
                elif i == 4:
                    pasta = result[i][1]
                elif i == 5:
                    sondobu = result[i][1]
        print(tteokbokki, rozetteokbokki, pasta, soba, kimchi, sondobu)

        sales_y = [tteokbokki, rozetteokbokki, kimchi, soba, pasta, sondobu]

        # 그래프 x축 설정
        self.sales_graph.setLabel ('bottom', '[판매상품 별 매출]')
        sales_bottom = self.sales_graph.getAxis('bottom')
        sales_bottom.setTicks(ticks)

        # 그래프 y축 설정
        s_yticks = [[(0, '0원'), (100000, '10만원'), (500000, '50만원'), (1000000, '100만원'), (2000000, '200만원')]]
        sales_left = self.sales_graph.getAxis('left')
        sales_left.setTicks(s_yticks)

        # 매출 그래프 그리기

        x = np.arange(6)
        bar = pg.BarGraphItem(x=x, height=sales_y, width=0.2, pen=None, brush='g', name='판매상품별 매출')
        self.sales_graph.addLegend(offset=(0, 1))
        self.sales_graph.addItem(bar)

    def timeout(self):
        self.cur_date = QDate.currentDate()
        self.str_date = self.cur_date.toString(Qt.ISODate)
        self.cur_time = QTime.currentTime()
        self.str_time = self.cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(f'현재 날짜:{self.str_date}, 현재 시간: {self.str_time}')

    # 주문 버튼을 눌렀을 때 실행 될 메서드
    def threadAction(self):
        self.stackedWidget.setCurrentIndex(2)
        self.a = Thread(self)  # self 는 Main의 인스턴스, Thread 클래스에서 parent로 전달
        self.a.resume()
        self.a.start()
        self.a.old.connect(self.old)

    def pause(self):
        self.a.pause()
        self.stackedWidget.setCurrentIndex(0)

# --------------------------------------------박의용---------------------------------------------------------------

if __name__ =="__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()