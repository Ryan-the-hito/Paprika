class MyWidget(QWidget):  # 主窗口
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.center()
        self.setWindowTitle('App timer')
        self.setFixedSize(500, 320)

        self.widget1 = QComboBox(self)
        self.widget1.setFixedWidth(110)
        defalist2 = ['Quit', 'Force Quit', 'Stop Playing']
        self.widget1.addItems(defalist2)
        self.widget1.setCurrentIndex(1)

        self.widget0 = QComboBox(self)
        self.widget0.setFixedWidth(110)
        self.defalist = ['Which app']
        resp = applescript.tell.app("System Events", '''
        tell application "System Events"
            set listOfProcesses to every process
            set allProcess to {}

            repeat with processItem in listOfProcesses
                set procname to name of processItem as string
                set processDic to {procname}
                copy processDic to end of allProcess
            end repeat

            return allProcess
        end tell''')
        assert resp.code == 0, resp.err
        runlist = resp.out.split(', ')
        runlist.sort()
        self.defalist = self.defalist + runlist
        self.widget0.addItems(self.defalist)
        self.widget0.setCurrentIndex(0)

        self.widget8 = QComboBox(self)
        self.widget8.setFixedWidth(110)
        self.defalistonfo = ['On', 'After']
        self.widget8.addItems(self.defalistonfo)
        self.widget8.setCurrentIndex(0)

        self.widget7 = QComboBox(self)
        self.widget7.setFixedWidth(70)
        self.widget7.setEditable(True)
        ISOYEAR = '%Y'
        theYear = datetime.datetime.now().strftime(ISOYEAR)
        self.widget7.setCurrentText(str(theYear))
        self.widget7.setValidator(QIntValidator(1, 2999))

        lbl1 = QLabel('-', self)

        self.widget2 = QComboBox(self)
        self.widget2.setFixedWidth(70)
        self.widget2.setEditable(True)
        defalist3 = ['01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12']
        self.widget2.addItems(defalist3)
        ISOMONTH = '%m'
        theMonth = datetime.datetime.now().strftime(ISOMONTH)
        if str(theMonth) in defalist3:
            num = defalist3.index(str(theMonth))
            self.widget2.setCurrentIndex(num)
        myregexp = QRegularExpression('(?:1[0-2]|[1-9])')
        myvalidator = QRegularExpressionValidator(myregexp, self.widget2)
        self.widget2.setValidator(myvalidator)

        lbl2 = QLabel('-', self)

        self.widget3 = QComboBox(self)
        self.widget3.setFixedWidth(70)
        self.widget3.setEditable(True)
        self.defalist4 = ['01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12', '13', '14',
                     '15', '16', '17', '18', '19', '20', '21',
                     '22', '23', '24', '25', '26', '27', '28',
                     '29', '30', '31']
        self.widget3.addItems(self.defalist4)
        ISODAY = '%d'
        theDay = datetime.datetime.now().strftime(ISODAY)
        if str(theDay) in self.defalist4:
            num = self.defalist4.index(str(theDay))
            self.widget3.setCurrentIndex(num)
        myregexp2 = QRegularExpression('([1-9]|[1-2]\d|3[0-1])')
        myvalidator2 = QRegularExpressionValidator(myregexp2, self.widget3)
        self.widget3.setValidator(myvalidator2)

        self.widget4 = QComboBox(self)
        self.widget4.setFixedWidth(70)
        self.widget4.setEditable(True)
        defalist5 = ['00', '01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12', '13', '14',
                     '15', '16', '17', '18', '19', '20', '21',
                     '22', '23']
        self.widget4.addItems(defalist5)
        ISOHOUR = '%H'
        theHour = datetime.datetime.now().strftime(ISOHOUR)
        if str(theHour) in defalist5:
            num = defalist5.index(str(theHour))
            self.widget4.setCurrentIndex(num)
        myregexp3 = QRegularExpression('\d|1\d|2[0-3]|0')
        myvalidator3 = QRegularExpressionValidator(myregexp3, self.widget4)
        self.widget4.setValidator(myvalidator3)

        lbl4 = QLabel(':', self)

        self.widget5 = QComboBox(self)
        self.widget5.setFixedWidth(70)
        self.widget5.setEditable(True)
        defalist6 = ['00', '01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12', '13', '14',
                     '15', '16', '17', '18', '19', '20', '21',
                     '22', '23', '24', '25', '26', '27', '28',
                     '29', '30', '31', '32', '33', '34', '35',
                     '36', '37', '38', '39', '40', '41', '42',
                     '43', '44', '45', '46', '47', '48', '49',
                     '50', '51', '52', '53', '54', '55', '56',
                     '57', '58', '59']
        self.widget5.addItems(defalist6)
        ISOMINUTE = '%M'
        theMinute = datetime.datetime.now().strftime(ISOMINUTE)
        if str(theMinute) in defalist6:
            num = defalist6.index(str(theMinute))
            self.widget5.setCurrentIndex(num)
        myregexp4 = QRegularExpression('\d|[1-5]\d|0')
        myvalidator4 = QRegularExpressionValidator(myregexp4, self.widget5)
        self.widget5.setValidator(myvalidator4)

        lbl5 = QLabel(':', self)

        self.widget6 = QComboBox(self)
        self.widget6.setFixedWidth(70)
        self.widget6.setEditable(True)
        defalist7 = ['00', '01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12', '13', '14',
                     '15', '16', '17', '18', '19', '20', '21',
                     '22', '23', '24', '25', '26', '27', '28',
                     '29', '30', '31', '32', '33', '34', '35',
                     '36', '37', '38', '39', '40', '41', '42',
                     '43', '44', '45', '46', '47', '48', '49',
                     '50', '51', '52', '53', '54', '55', '56',
                     '57', '58', '59']
        self.widget6.addItems(defalist7)
        ISOSECOND = '%S'
        theSecond = datetime.datetime.now().strftime(ISOSECOND)
        if str(theSecond) in defalist7:
            num = defalist7.index(str(theSecond))
            self.widget6.setCurrentIndex(num)
        myregexp5 = QRegularExpression('\d|[1-5]\d|0')
        myvalidator5 = QRegularExpressionValidator(myregexp5, self.widget6)
        self.widget6.setValidator(myvalidator5)

        lbl10 = QLabel('   Hour(s)   ', self)
        lbl11 = QLabel(':', self)
        lbl12 = QLabel('  Minute(s) ', self)
        lbl13 = QLabel(':', self)
        lbl14 = QLabel(' Second(s)', self)

        self.le1 = QLineEdit(self)
        self.le1.setFixedWidth(60)
        self.le1.setText('0')
        self.le1.setValidator(QIntValidator())
        lbl15 = QLabel(' : ', self)
        self.le2 = QLineEdit(self)
        self.le2.setFixedWidth(60)
        self.le2.setText('0')
        self.le2.setValidator(QIntValidator())
        lbl16 = QLabel(' : ', self)
        self.le3 = QLineEdit(self)
        self.le3.setFixedWidth(60)
        self.le3.setText('0')
        self.le3.setValidator(QIntValidator())

        lbl7 = QLabel('The app will ', self)

        self.lbl8 = QLabel(' ', self)
        self.lbl8.setText(self.widget1.currentText())

        lbl9 = QLabel(' after', self)

        self.lcd = QLCDNumber(self)
        self.lcd.setFixedHeight(80)
        self.lcd.setFixedWidth(300)
        self.lcd.setDigitCount(8)
        lctext = '00:00:00'
        self.lcd.display(lctext)

        self.mybutton1 = QPushButton('Start', self)
        self.mybutton1.setFixedWidth(150)
        self.mybutton1.clicked.connect(self.switchontimer)

        self.mybutton2 = QPushButton('Stop/Refresh', self)
        self.mybutton2.setFixedWidth(150)
        self.mybutton2.clicked.connect(self.switchoffTimer)

        qw2 = QWidget()
        vbox2 = QHBoxLayout()
        vbox2.setContentsMargins(0, 0, 0, 0)
        vbox2.addStretch()
        vbox2.addWidget(self.widget1)
        vbox2.addWidget(self.widget0)
        vbox2.addWidget(self.widget8)
        vbox2.addStretch()
        qw2.setLayout(vbox2)

        self.qw21 = QWidget()
        vbox21 = QHBoxLayout()
        vbox21.setContentsMargins(0, 0, 0, 0)
        vbox21.addStretch()
        vbox21.addWidget(self.widget7)
        vbox21.addWidget(lbl1)
        vbox21.addWidget(self.widget2)
        vbox21.addWidget(lbl2)
        vbox21.addWidget(self.widget3)
        vbox21.addStretch()
        self.qw21.setLayout(vbox21)

        self.qw22 = QWidget()
        vbox22 = QHBoxLayout()
        vbox22.setContentsMargins(0, 0, 0, 0)
        vbox22.addStretch()
        vbox22.addWidget(self.widget4)
        vbox22.addWidget(lbl4)
        vbox22.addWidget(self.widget5)
        vbox22.addWidget(lbl5)
        vbox22.addWidget(self.widget6)
        vbox22.addStretch()
        self.qw22.setLayout(vbox22)

        self.qw23 = QWidget()
        vbox23 = QHBoxLayout()
        vbox23.setContentsMargins(0, 0, 0, 0)
        vbox23.addStretch()
        vbox23.addWidget(lbl10)
        vbox23.addWidget(lbl11)
        vbox23.addWidget(lbl12)
        vbox23.addWidget(lbl13)
        vbox23.addWidget(lbl14)
        vbox23.addStretch()
        self.qw23.setLayout(vbox23)
        self.qw23.setVisible(False)

        self.qw24 = QWidget()
        vbox24 = QHBoxLayout()
        vbox24.setContentsMargins(0, 0, 0, 0)
        vbox24.addStretch()
        vbox24.addWidget(self.le1)
        vbox24.addWidget(lbl15)
        vbox24.addWidget(self.le2)
        vbox24.addWidget(lbl16)
        vbox24.addWidget(self.le3)
        vbox24.addStretch()
        self.qw24.setLayout(vbox24)
        self.qw24.setVisible(False)

        qw3 = QWidget()
        vbox3 = QHBoxLayout()
        vbox3.setContentsMargins(0, 0, 0, 0)
        vbox3.addStretch()
        vbox3.addWidget(lbl7)
        vbox3.addWidget(self.lbl8)
        vbox3.addWidget(lbl9)
        vbox3.addStretch()
        qw3.setLayout(vbox3)

        qw4 = QWidget()
        vbox4 = QHBoxLayout()
        vbox4.setContentsMargins(0, 0, 0, 0)
        vbox4.addStretch()
        vbox4.addWidget(self.lcd)
        vbox4.addStretch()
        qw4.setLayout(vbox4)

        qw5 = QWidget()
        vbox5 = QHBoxLayout()
        vbox5.setContentsMargins(0, 0, 0, 0)
        vbox5.addStretch()
        vbox5.addWidget(self.mybutton1)
        vbox5.addWidget(self.mybutton2)
        vbox5.addStretch()
        qw5.setLayout(vbox5)

        vbox6 = QVBoxLayout()
        vbox6.setContentsMargins(0, 0, 0, 0)
        vbox6.addStretch()
        vbox6.addWidget(qw2)
        vbox6.addWidget(self.qw21)
        vbox6.addWidget(self.qw22)
        vbox6.addWidget(self.qw23)
        vbox6.addWidget(self.qw24)
        vbox6.addWidget(qw3)
        vbox6.addWidget(qw4)
        vbox6.addWidget(qw5)
        vbox6.addStretch()
        self.setLayout(vbox6)

        self.mytimer = QTimer(self)
        self.mytimer.timeout.connect(self.onTimer)
        self.widget1.currentIndexChanged.connect(self.quitChange)
        self.widget2.currentIndexChanged.connect(self.monthChange)
        self.widget8.currentIndexChanged.connect(self.onforChange)

    def switchontimer(self):
        if self.widget8.currentIndex() == 0 and self.widget0.currentIndex() != 0:
            ISOYEAR = '%Y'
            theYear = datetime.datetime.now().strftime(ISOYEAR)
            ISOMONTH = '%m'
            theMonth = datetime.datetime.now().strftime(ISOMONTH)
            ISODAY = '%d'
            theDay = datetime.datetime.now().strftime(ISODAY)
            ISOHOUR = '%H'
            theHour = datetime.datetime.now().strftime(ISOHOUR)
            ISOMINUTE = '%M'
            theMinute = datetime.datetime.now().strftime(ISOMINUTE)
            ISOSECOND = '%S'
            theSecond = datetime.datetime.now().strftime(ISOSECOND)
            if theYear == self.widget7.currentText() and theMonth == self.widget2.currentText() and theDay == self.widget3.currentText():
                nowTime = int(theHour)*3600 + int(theMinute)*60 + int(theSecond)
                willTime = int(self.widget4.currentText())*3600 + int(self.widget5.currentText())*60 + int(self.widget6.currentText())
                if willTime > nowTime:
                    self.counter = willTime - nowTime
                    HourLeft = int(self.counter / 3600)
                    MinuteLeft = int(int(self.counter - HourLeft * 3600) / 60)
                    SecondLeft = int(self.counter - HourLeft * 3600 - MinuteLeft * 60)
                    disHour = str(HourLeft)
                    disMinute = str(MinuteLeft)
                    disSecond = str(SecondLeft)
                    if HourLeft < 10:
                        disHour = '0' + str(HourLeft)
                    if MinuteLeft < 10:
                        disMinute = '0' + str(MinuteLeft)
                    if SecondLeft < 10:
                        disSecond = '0' + str(SecondLeft)
                    legacy = str(disHour) + ':' + str(disMinute) + ':' + str(disSecond)
                    self.lcd.display(legacy)
                    self.mybutton1.setStyleSheet('''
                    border: 1px outset grey;
                    background-color: #0085FF;
                    border-radius: 4px;
                    padding: 1px;
                    color: #FFFFFF''')
                    self.mybutton1.setText('Started')
                    self.mybutton1.setDisabled(True)
                    self.mybutton2.setDisabled(False)
                    self.mytimer.start(1000)
            if theYear != self.widget7.currentText() or theMonth != self.widget2.currentText() or theDay != self.widget3.currentText():
                daysgap = self.days_diff(date(int(theYear), int(theMonth), int(theDay)),
                                         date(int(self.widget7.currentText()), int(self.widget2.currentText()), int(self.widget3.currentText())))
                if daysgap == 1:
                    part1 = 86400 - (int(theHour)*3600 + int(theMinute)*60 + int(theSecond))
                    part2 = 0
                    part3 = int(self.widget4.currentText())*3600 + int(self.widget5.currentText())*60 + int(self.widget6.currentText())
                    self.counter = part1 + part2 + part3
                    HourLeft = int(self.counter / 3600)
                    MinuteLeft = int(int(self.counter - HourLeft * 3600) / 60)
                    SecondLeft = int(self.counter - HourLeft * 3600 - MinuteLeft * 60)
                    disHour = str(HourLeft)
                    disMinute = str(MinuteLeft)
                    disSecond = str(SecondLeft)
                    if HourLeft < 10:
                        disHour = '0' + str(HourLeft)
                    if MinuteLeft < 10:
                        disMinute = '0' + str(MinuteLeft)
                    if SecondLeft < 10:
                        disSecond = '0' + str(SecondLeft)
                    legacy = str(disHour) + ':' + str(disMinute) + ':' + str(disSecond)
                    self.lcd.display(legacy)
                    self.mybutton1.setStyleSheet('''
                    border: 1px outset grey;
                    background-color: #0085FF;
                    border-radius: 4px;
                    padding: 1px;
                    color: #FFFFFF''')
                    self.mybutton1.setText('Started')
                    self.mybutton1.setDisabled(True)
                    self.mybutton2.setDisabled(False)
                    self.mytimer.start(1000)
                if daysgap > 1:
                    part1 = 86400 - (int(theHour) * 3600 + int(theMinute) * 60 + int(theSecond))
                    part2 = (daysgap - 1) * 86400
                    part3 = int(self.widget4.currentText()) * 3600 + int(self.widget5.currentText()) * 60 + int(
                        self.widget6.currentText())
                    self.counter = part1 + part2 + part3
                    HourLeft = int(self.counter / 3600)
                    MinuteLeft = int(int(self.counter - HourLeft * 3600) / 60)
                    SecondLeft = int(self.counter - HourLeft * 3600 - MinuteLeft * 60)
                    disHour = str(HourLeft)
                    disMinute = str(MinuteLeft)
                    disSecond = str(SecondLeft)
                    if HourLeft < 10:
                        disHour = '0' + str(HourLeft)
                    if MinuteLeft < 10:
                        disMinute = '0' + str(MinuteLeft)
                    if SecondLeft < 10:
                        disSecond = '0' + str(SecondLeft)
                    legacy = str(disHour) + ':' + str(disMinute) + ':' + str(disSecond)
                    self.lcd.display(legacy)
                    self.mybutton1.setStyleSheet('''
                    border: 1px outset grey;
                    background-color: #0085FF;
                    border-radius: 4px;
                    padding: 1px;
                    color: #FFFFFF''')
                    self.mybutton1.setText('Started')
                    self.mybutton1.setDisabled(True)
                    self.mybutton2.setDisabled(False)
                    self.mytimer.start(1000)
        if self.widget8.currentIndex() == 1 and self.widget0.currentIndex() != 0:
            if self.le1.text() != '' and self.le2.text() != '' and self.le3.text() != '':
                sec1 = int(self.le1.text()) * 3600
                sec2 = int(self.le2.text()) * 60
                sec3 = int(self.le3.text())
                self.counter = sec1 + sec2 + sec3
                HourLeft = int(self.counter / 3600)
                MinuteLeft = int(int(self.counter - HourLeft * 3600) / 60)
                SecondLeft = int(self.counter - HourLeft * 3600 - MinuteLeft * 60)
                disHour = str(HourLeft)
                disMinute = str(MinuteLeft)
                disSecond = str(SecondLeft)
                if HourLeft < 10:
                    disHour = '0' + str(HourLeft)
                if MinuteLeft < 10:
                    disMinute = '0' + str(MinuteLeft)
                if SecondLeft < 10:
                    disSecond = '0' + str(SecondLeft)
                legacy = str(disHour) + ':' + str(disMinute) + ':' + str(disSecond)
                self.lcd.display(legacy)
                self.mybutton1.setStyleSheet('''
                border: 1px outset grey;
                background-color: #0085FF;
                border-radius: 4px;
                padding: 1px;
                color: #FFFFFF''')
                self.mybutton1.setText('Started')
                self.mybutton1.setDisabled(True)
                self.mybutton2.setDisabled(False)
                self.mytimer.start(1000)

    def days_diff(self, start, end):
        return (end - start).days

    def switchoffTimer(self):
        defalist3 = ['01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12']
        defalist4 = ['01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12', '13', '14',
                     '15', '16', '17', '18', '19', '20', '21',
                     '22', '23', '24', '25', '26', '27', '28',
                     '29', '30', '31']
        defalist5 = ['00', '01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12', '13', '14',
                     '15', '16', '17', '18', '19', '20', '21',
                     '22', '23']
        defalist6 = ['00', '01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12', '13', '14',
                     '15', '16', '17', '18', '19', '20', '21',
                     '22', '23', '24', '25', '26', '27', '28',
                     '29', '30', '31', '32', '33', '34', '35',
                     '36', '37', '38', '39', '40', '41', '42',
                     '43', '44', '45', '46', '47', '48', '49',
                     '50', '51', '52', '53', '54', '55', '56',
                     '57', '58', '59']
        defalist7 = ['00', '01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12', '13', '14',
                     '15', '16', '17', '18', '19', '20', '21',
                     '22', '23', '24', '25', '26', '27', '28',
                     '29', '30', '31', '32', '33', '34', '35',
                     '36', '37', '38', '39', '40', '41', '42',
                     '43', '44', '45', '46', '47', '48', '49',
                     '50', '51', '52', '53', '54', '55', '56',
                     '57', '58', '59']
        self.mytimer.stop()
        ISOYEAR = '%Y'
        theYear = datetime.datetime.now().strftime(ISOYEAR)
        self.widget7.setCurrentText(str(theYear))
        ISOMONTH = '%m'
        theMonth = datetime.datetime.now().strftime(ISOMONTH)
        if str(theMonth) in defalist3:
            num = defalist3.index(str(theMonth))
            self.widget2.setCurrentIndex(num)
        ISODAY = '%d'
        theDay = datetime.datetime.now().strftime(ISODAY)
        if str(theDay) in defalist4:
            num = defalist4.index(str(theDay))
            self.widget3.setCurrentIndex(num)
        ISOHOUR = '%H'
        theHour = datetime.datetime.now().strftime(ISOHOUR)
        if str(theHour) in defalist5:
            num = defalist5.index(str(theHour))
            self.widget4.setCurrentIndex(num)
        ISOMINUTE = '%M'
        theMinute = datetime.datetime.now().strftime(ISOMINUTE)
        if str(theMinute) in defalist6:
            num = defalist6.index(str(theMinute))
            self.widget5.setCurrentIndex(num)
        ISOSECOND = '%S'
        theSecond = datetime.datetime.now().strftime(ISOSECOND)
        if str(theSecond) in defalist7:
            num = defalist7.index(str(theSecond))
            self.widget6.setCurrentIndex(num)
        self.lcd.display('00:00:00')
        self.mybutton1.setDisabled(False)
        self.mybutton1.setStyleSheet('''
        border: 1px outset grey;
        background-color: #FFFFFF;
        border-radius: 4px;
        padding: 1px;
        color: #000000''')
        self.mybutton1.setText('Start')
        self.defalist = ['Which app']
        resp = applescript.tell.app("System Events", '''
        tell application "System Events"
            set listOfProcesses to every process
            set allProcess to {}

            repeat with processItem in listOfProcesses
                set procname to name of processItem as string
                set processDic to {procname}
                copy processDic to end of allProcess
            end repeat

            return allProcess
        end tell''')
        try:
            assert resp.code == 0, resp.err
            runlist = resp.out.split(', ')
            runlist.sort()
            self.defalist = self.defalist + runlist
        except Exception as e:
            pass
        self.widget0.clear()
        self.widget0.addItems(self.defalist)
        self.widget0.setCurrentIndex(0)
        self.widget1.setCurrentIndex(1)
        self.le1.setText('0')
        self.le2.setText('0')
        self.le3.setText('0')

    def onTimer(self):
        self.counter -= 1
        HourLeft = int(self.counter / 3600)
        MinuteLeft = int(int(self.counter - HourLeft*3600) / 60)
        SecondLeft = int(self.counter - HourLeft*3600 - MinuteLeft*60)
        disHour = str(HourLeft)
        disMinute = str(MinuteLeft)
        disSecond = str(SecondLeft)
        if HourLeft < 10:
            disHour = '0' + str(HourLeft)
        if MinuteLeft < 10:
            disMinute = '0' + str(MinuteLeft)
        if SecondLeft < 10:
            disSecond = '0' + str(SecondLeft)
        legacy = str(disHour) + ':' + str(disMinute) + ':' + str(disSecond)
        self.lcd.display(legacy)

        if self.counter == 0:
            self.mytimer.stop()
            if self.widget1.currentIndex() == 0:
                cmd = f"""osascript -e '''tell application "System Events" to tell process "{self.widget0.currentText()}"
                click menu item "Quit {self.widget0.currentText()}" of menu "{self.widget0.currentText()}" of menu bar item "{self.widget0.currentText()}" of menu bar 1 of application process "{self.widget0.currentText()}" of application "System Events"
                end tell'''"""
                os.system(cmd)
                CMD = '''
                on run argv
                  display notification (item 2 of argv) with title (item 1 of argv)
                end run
                '''
                self.notify(CMD, "App Timer", f"{self.widget0.currentText()} has been quitted!")
            if self.widget1.currentIndex() == 1:
                cmd = f"""osascript -e '''tell application "System Events" to tell process "{self.widget0.currentText()}"
                click menu item "Force Quit {self.widget0.currentText()}" of menu "Apple" of menu bar item "Apple" of menu bar 1 of application process "{self.widget0.currentText()}" of application "System Events"
                end tell'''"""
                os.system(cmd)
                CMD = '''
                on run argv
                  display notification (item 2 of argv) with title (item 1 of argv)
                end run
                '''
                self.notify(CMD, "App Timer", f"{self.widget0.currentText()} has been force quitted!")
            if self.widget1.currentIndex() == 2 and self.widget0.currentText() == 'Music':
                cmd = f"""osascript -e '''tell application "System Events" to tell process "Music"
                click menu item "Stop" of menu "Controls" of menu bar item "Controls" of menu bar 1 of application process "Music" of application "System Events"
                end tell'''"""
                os.system(cmd)
                CMD = '''
                on run argv
                  display notification (item 2 of argv) with title (item 1 of argv)
                end run
                '''
                self.notify(CMD, "App Timer", f"Music is stopped!")
            if self.widget1.currentIndex() == 2 and self.widget0.currentText() == 'Cog':
                cmd = f"""osascript -e '''tell application "System Events" to tell process "Cog"
                click menu item "Stop" of menu "Control" of menu bar item "Control" of menu bar 1 of application process "Cog" of application "System Events"
                end tell'''"""
                os.system(cmd)
                CMD = '''
                on run argv
                  display notification (item 2 of argv) with title (item 1 of argv)
                end run
                '''
                self.notify(CMD, "App Timer", f"Cog is stopped!")
            self.switchoffTimer()

    def quitChange(self, i):
        if i == 0:
            self.lbl8.setText(self.widget1.currentText())
            newlist = self.defalist
            self.widget0.clear()
            self.widget0.addItems(newlist)
            self.widget0.setCurrentIndex(0)
        if i == 1:
            self.lbl8.setText(self.widget1.currentText())
            newlist = self.defalist
            self.widget0.clear()
            self.widget0.addItems(newlist)
            self.widget0.setCurrentIndex(0)
        if i == 2:
            self.lbl8.setText(self.widget1.currentText())
            newlist = ['Which app']
            if 'Music' in self.defalist:
                newlist.append('Music')
            if 'Cog' in self.defalist:
                newlist.append('Cog')
            self.widget0.clear()
            self.widget0.addItems(newlist)
            self.widget0.setCurrentIndex(0)

    def monthChange(self):
        if self.widget2.currentText() == '02':
            if int(self.widget7.currentText()) / 4 == 0:
                self.defalist4 = ['01', '02', '03', '04', '05', '06', '07',
                                  '08', '09', '10', '11', '12', '13', '14',
                                  '15', '16', '17', '18', '19', '20', '21',
                                  '22', '23', '24', '25', '26', '27', '28',
                                  '29']
            if int(self.widget7.currentText()) / 4 != 0:
                self.defalist4 = ['01', '02', '03', '04', '05', '06', '07',
                                  '08', '09', '10', '11', '12', '13', '14',
                                  '15', '16', '17', '18', '19', '20', '21',
                                  '22', '23', '24', '25', '26', '27', '28']
        if self.widget2.currentText() == '01' or \
                self.widget2.currentText() == '03' or \
                self.widget2.currentText() == '05' or \
                self.widget2.currentText() == '07' or \
                self.widget2.currentText() == '08' or \
                self.widget2.currentText() == '10' or \
                self.widget2.currentText() == '12':
            self.defalist4 = ['01', '02', '03', '04', '05', '06', '07',
                              '08', '09', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21',
                              '22', '23', '24', '25', '26', '27', '28',
                              '29', '30', '31']
        if self.widget2.currentText() == '04' or \
                self.widget2.currentText() == '06' or \
                self.widget2.currentText() == '09' or \
                self.widget2.currentText() == '11':
            self.defalist4 = ['01', '02', '03', '04', '05', '06', '07',
                              '08', '09', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21',
                              '22', '23', '24', '25', '26', '27', '28',
                              '29', '30']
        self.widget3.clear()
        self.widget3.addItems(self.defalist4)
        ISOMONTH = '%m'
        theMonth = datetime.datetime.now().strftime(ISOMONTH)
        if self.widget2.currentText() != theMonth:
            self.widget3.setCurrentIndex(0)
        if self.widget2.currentText() == theMonth:
            ISODAY = '%d'
            theDay = datetime.datetime.now().strftime(ISODAY)
            if str(theDay) in self.defalist4:
                num = self.defalist4.index(str(theDay))
                self.widget3.setCurrentIndex(num)

    def onforChange(self):
        if self.widget8.currentIndex() == 0:
            self.qw21.setVisible(True)
            self.qw22.setVisible(True)
            self.qw23.setVisible(False)
            self.qw24.setVisible(False)
        if self.widget8.currentIndex() == 1:
            self.qw21.setVisible(False)
            self.qw22.setVisible(False)
            self.qw23.setVisible(True)
            self.qw24.setVisible(True)

    def notify(self, CMD, title, text):
        subprocess.call(['osascript', '-e', CMD, title, text])

    def activate(self):  # 设置窗口显示
        self.switchoffTimer()
        self.show()
        self.setFocus()

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

style_sheet_ori = '''
    QTabWidget::pane {
        border: 1px solid #ECECEC;
        background: #ECECEC;
        border-radius: 9px;
}
    QPushButton{
        border: 1px outset grey;
        background-color: #FFFFFF;
        border-radius: 4px;
        padding: 1px;
        color: #000000
}
    QPushButton:pressed{
        border: 1px outset grey;
        background-color: #0085FF;
        border-radius: 4px;
        padding: 1px;
        color: #FFFFFF
}
    QPlainTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
    QPlainTextEdit#edit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #FFFFFF;
        color: rgb(113, 113, 113);
        font: 14pt Helvetica;
}
    QLineEdit{
        border-radius:4px;
        border: 1px outset lightgray;
        background-color: #FFFFFF;
}
    QTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
    QLCDNumber{
        border: 1px transparent;  
        border-radius:4px;
        padding: 1px 5px 1px 3px;
}
'''