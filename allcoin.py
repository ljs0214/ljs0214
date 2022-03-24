import pyupbit
import time
import datetime
import math
import requests
import traceback

class autoTrade1 :
    def __init__(self, start_cash, ticker1, ticker2, ticker3, ticker4, ticker5, ticker6, ticker7, ticker8, ticker9, ticker10) :
        self.fee = 0.05 # 수수료
        self.target_price1 = 0 # 목표 매수가
        self.target_price2 = 0 # 목표 매수가
        self.target_price3 = 0 # 목표 매수가
        self.target_price4 = 0 # 목표 매수가
        self.target_price5 = 0 # 목표 매수가
        self.target_price6 = 0 # 목표 매수가
        self.target_price7 = 0 # 목표 매수가
        self.target_price8 = 0 # 목표 매수가
        self.target_price9 = 0 # 목표 매수가
        self.target_price10 = 0 # 목표 매수가
        self.bull1 = False # 상승장 여부
        self.bull2 = False # 상승장 여부
        self.bull3 = False # 상승장 여부
        self.bull4 = False # 상승장 여부
        self.bull5 = False # 상승장 여부
        self.bull6 = False # 상승장 여부
        self.bull7 = False # 상승장 여부
        self.bull8 = False # 상승장 여부
        self.bull9 = False # 상승장 여부
        self.bull10 = False # 상승장 여부
        self.ticker1 = ticker1 # 티커
        self.ticker2 = ticker2 # 티커
        self.ticker3 = ticker3 # 티커
        self.ticker4 = ticker4 # 티커
        self.ticker5 = ticker5 # 티커
        self.ticker6 = ticker6 # 티커
        self.ticker7 = ticker7 # 티커
        self.ticker8 = ticker8 # 티커
        self.ticker9 = ticker9 # 티커
        self.ticker10 = ticker10 # 티커
        self.buy_yn1 = True # 매수 여부
        self.buy_yn2 = False
        self.buy_yn3 = True
        self.buy_yn4 = True
        self.buy_yn5 = True
        self.buy_yn6 = True
        self.buy_yn7 = True
        self.buy_yn8 = False
        self.buy_yn9 = True
        self.buy_yn10 = False
        self.start_cash = start_cash # 시작 자산

        # self.timer = 0
        self.get_today_data1()
        self.get_today_data2()
        self.get_today_data3()
        self.get_today_data4()
        self.get_today_data5()
        self.get_today_data6()
        self.get_today_data7()
        self.get_today_data8()
        self.get_today_data9()
        self.get_today_data10()

    def start(self) :
        now = datetime.datetime.now() # 현재 시간
        slackBot.message("자동 매매 프로그램이 시작되었습니다\n시작 시간 : " + str(now) + "\n매매 대상 : " + self.ticker1 + "\n시작 자산 : " + str(self.start_cash))
        slackBot.message("자동 매매 프로그램이 시작되었습니다\n시작 시간 : " + str(now) + "\n매매 대상 : " + self.ticker2 + "\n시작 자산 : " + str(self.start_cash))
        slackBot.message("자동 매매 프로그램이 시작되었습니다\n시작 시간 : " + str(now) + "\n매매 대상 : " + self.ticker3 + "\n시작 자산 : " + str(self.start_cash))
        slackBot.message("자동 매매 프로그램이 시작되었습니다\n시작 시간 : " + str(now) + "\n매매 대상 : " + self.ticker4 + "\n시작 자산 : " + str(self.start_cash))
        slackBot.message("자동 매매 프로그램이 시작되었습니다\n시작 시간 : " + str(now) + "\n매매 대상 : " + self.ticker5 + "\n시작 자산 : " + str(self.start_cash))
        slackBot.message("자동 매매 프로그램이 시작되었습니다\n시작 시간 : " + str(now) + "\n매매 대상 : " + self.ticker6 + "\n시작 자산 : " + str(self.start_cash))
        slackBot.message("자동 매매 프로그램이 시작되었습니다\n시작 시간 : " + str(now) + "\n매매 대상 : " + self.ticker7 + "\n시작 자산 : " + str(self.start_cash))
        slackBot.message("자동 매매 프로그램이 시작되었습니다\n시작 시간 : " + str(now) + "\n매매 대상 : " + self.ticker8 + "\n시작 자산 : " + str(self.start_cash))
        slackBot.message("자동 매매 프로그램이 시작되었습니다\n시작 시간 : " + str(now) + "\n매매 대상 : " + self.ticker9 + "\n시작 자산 : " + str(self.start_cash))
        slackBot.message("자동 매매 프로그램이 시작되었습니다\n시작 시간 : " + str(now) + "\n매매 대상 : " + self.ticker10 + "\n시작 자산 : " + str(self.start_cash))
        openTime = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=9, seconds=10) # 09:00:10

        while True :
            try :
                now = datetime.datetime.now()
                current_price1 = pyupbit.get_current_price(self.ticker1)
                current_price2 = pyupbit.get_current_price(self.ticker2)
                current_price3 = pyupbit.get_current_price(self.ticker3)
                current_price4 = pyupbit.get_current_price(self.ticker4)
                current_price5 = pyupbit.get_current_price(self.ticker5)
                current_price6 = pyupbit.get_current_price(self.ticker6)
                current_price7 = pyupbit.get_current_price(self.ticker7)
                current_price8 = pyupbit.get_current_price(self.ticker8)
                current_price9 = pyupbit.get_current_price(self.ticker9)
                current_price10 = pyupbit.get_current_price(self.ticker10)
               
                # if(self.timer % 60 == 0) :
                #     print(now, "\topenTime :", openTime, "\tTarget :", self.target_price1, "\tCurrent :", current_price1, "\tBull :", self.bull, "\tBuy_yn :", self.buy_yn1)

                if openTime < now < openTime + datetime.timedelta(seconds=5) :
                    openTime = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=20, seconds=10)
                    if(self.buy_yn1) :
                        print("==================== [ 매도 시도 ] ====================")
                        slackBot.message("매도 시도"+ str(self.ticker1))
                        self.sell_coin1()
                    self.get_today_data1() # 데이터 갱신
                    if(self.buy_yn2) :
                        print("==================== [ 매도 시도 ] ====================")
                        slackBot.message("매도 시도"+ str(self.ticker2))
                        self.sell_coin2()
                    self.get_today_data2() # 데이터 갱신
                    if(self.buy_yn3) :
                        print("==================== [ 매도 시도 ] ====================")
                        slackBot.message("매도 시도"+ str(self.ticker3))
                        self.sell_coin3()
                    self.get_today_data3() # 데이터 갱신
                    if(self.buy_yn4) :
                        print("==================== [ 매도 시도 ] ====================")
                        slackBot.message("매도 시도"+ str(self.ticker4))
                        self.sell_coin4()
                    self.get_today_data4() # 데이터 갱신
                    if(self.buy_yn5) :
                        print("==================== [ 매도 시도 ] ====================")
                        slackBot.message("매도 시도"+ str(self.ticker5))
                        self.sell_coin5()
                    self.get_today_data5() # 데이터 갱신
                    if(self.buy_yn6) :
                        print("==================== [ 매도 시도 ] ====================")
                        slackBot.message("매도 시도"+ str(self.ticker6))
                        self.sell_coin6()
                    self.get_today_data6() # 데이터 갱신
                    if(self.buy_yn7) :
                        print("==================== [ 매도 시도 ] ====================")
                        slackBot.message("매도 시도"+ str(self.ticker7))
                        self.sell_coin7()
                    self.get_today_data7() # 데이터 갱신
                    if(self.buy_yn8) :
                        print("==================== [ 매도 시도 ] ====================")
                        slackBot.message("매도 시도"+ str(self.ticker8))
                        self.sell_coin8()
                    self.get_today_data8() # 데이터 갱신
                    if(self.buy_yn9) :
                        print("==================== [ 매도 시도 ] ====================")
                        slackBot.message("매도 시도"+ str(self.ticker9))
                        self.sell_coin9()
                    self.get_today_data9() # 데이터 갱신
                    if(self.buy_yn10) :
                        print("==================== [ 매도 시도 ] ====================")
                        slackBot.message("매도 시도"+ str(self.ticker10))
                        self.sell_coin10()
                    self.get_today_data10() # 데이터 갱신

                if((current_price1 >= self.target_price1) and self.bull1 and not self.buy_yn1) : # 매수 시도
                    print("==================== [ 매수 시도 ] ====================")
                    slackBot.message("매수 시도"+ str(self.ticker1))
                    self.buy_coin1()
                if((current_price2 >= self.target_price2) and self.bull2 and not self.buy_yn2) : # 매수 시도
                    print("==================== [ 매수 시도 ] ====================")
                    slackBot.message("매수 시도"+ str(self.ticker2))
                    self.buy_coin2()
                if((current_price3 >= self.target_price3) and self.bull3 and not self.buy_yn3) : # 매수 시도
                    print("==================== [ 매수 시도 ] ====================")
                    slackBot.message("매수 시도"+ str(self.ticker3))
                    self.buy_coin3()
                if((current_price4 >= self.target_price4) and self.bull4 and not self.buy_yn4) : # 매수 시도
                    print("==================== [ 매수 시도 ] ====================")
                    slackBot.message("매수 시도"+ str(self.ticker4))
                    self.buy_coin4()
                if((current_price5 >= self.target_price5) and self.bull5 and not self.buy_yn5) : # 매수 시도
                    print("==================== [ 매수 시도 ] ====================")
                    slackBot.message("매수 시도"+ str(self.ticker5))
                    self.buy_coin5()
                if((current_price6 >= self.target_price6) and self.bull6 and not self.buy_yn6) : # 매수 시도
                    print("==================== [ 매수 시도 ] ====================")
                    slackBot.message("매수 시도"+ str(self.ticker6))
                    self.buy_coin6()
                if((current_price7 >= self.target_price7) and self.bull7 and not self.buy_yn7) : # 매수 시도
                    print("==================== [ 매수 시도 ] ====================")
                    slackBot.message("매수 시도"+ str(self.ticker7))
                    self.buy_coin7()
                if((current_price8 >= self.target_price8) and self.bull8 and not self.buy_yn8) : # 매수 시도
                    print("==================== [ 매수 시도 ] ====================")
                    slackBot.message("매수 시도"+ str(self.ticker8))
                    self.buy_coin8()
                if((current_price9 >= self.target_price9) and self.bull9 and not self.buy_yn9) : # 매수 시도
                    print("==================== [ 매수 시도 ] ====================")
                    slackBot.message("매수 시도"+ str(self.ticker9))
                    self.buy_coin9()
                if((current_price10 >= self.target_price10) and self.bull10 and not self.buy_yn10) : # 매수 시도
                    print("==================== [ 매수 시도 ] ====================")
                    slackBot.message("매수 시도"+ str(self.ticker10))
                    self.buy_coin10()                          
            except Exception as err:
                slackBot.message("!!! 프로그램 오류 발생 !!!")
                slackBot.message(err)
                traceback.print_exc()
         
            # self.timer += 1
            time.sleep(1)

    def get_today_data1(self) :
        print("\n==================== [ 데이터 갱신 시도 ] ====================")
        daily_data1 = pyupbit.get_ohlcv(self.ticker1, count=41)
        # 노이즈 계산 ( 1- 절대값(시가 - 종가) / (고가 - 저가) )
        daily_data1['noise'] = 1 - abs(daily_data1['open'] - daily_data1['close']) / (daily_data1['high'] - daily_data1['low'])
        # 노이즈 1일 평균
        daily_data1['noise_ma20'] = daily_data1['noise'].rolling(window=1).mean().shift(1)
        # 변동폭 ( 고가 - 저가 )
        daily_data1['range'] = daily_data1['high'] - daily_data1['low']
        # 목표매수가 ( 시가 + 변동폭 * K )
        daily_data1['targetPrice'] = daily_data1['open'] + daily_data1['range'].shift(1) * daily_data1['noise_ma20']
        # 5일 이동평균선
        daily_data1['ma5'] = daily_data1['close'].rolling(window=15, min_periods=1).mean().shift(1)
        # 상승장 여부
        daily_data1['bull'] = daily_data1['open'] > daily_data1['ma5']

        today1 = daily_data1.iloc[-1]

        self.target_price1 = today1.targetPrice

        self.bull1 = today1.bull
        print(daily_data1.tail())
        print("Target Price :", self.target_price1, "\tBull :", self.bull1)
        print("==================== [ 데이터 갱신 완료 ] ====================\n")
    
    def get_today_data2(self) :
        print("\n==================== [ 데이터 갱신 시도 ] ====================")
        daily_data2 = pyupbit.get_ohlcv(self.ticker2, count=41)
        # 노이즈 계산 ( 1- 절대값(시가 - 종가) / (고가 - 저가) )
        daily_data2['noise'] = 1 - abs(daily_data2['open'] - daily_data2['close']) / (daily_data2['high'] - daily_data2['low'])
        # 노이즈 1일 평균
        daily_data2['noise_ma20'] = daily_data2['noise'].rolling(window=1).mean().shift(1)
        # 변동폭 ( 고가 - 저가 )
        daily_data2['range'] = daily_data2['high'] - daily_data2['low']
        # 목표매수가 ( 시가 + 변동폭 * K )
        daily_data2['targetPrice'] = daily_data2['open'] + daily_data2['range'].shift(1) * daily_data2['noise_ma20']
        # 5일 이동평균선
        daily_data2['ma5'] = daily_data2['close'].rolling(window=10, min_periods=1).mean().shift(1)
        # 상승장 여부
        daily_data2['bull'] = daily_data2['open'] > daily_data2['ma5']

        today2 = daily_data2.iloc[-1]

        self.target_price2 = today2.targetPrice

        self.bull2 = today2.bull
        print(daily_data2.tail())
        print("Target Price :", self.target_price2, "\tBull :", self.bull2)
        print("==================== [ 데이터 갱신 완료 ] ====================\n")

    def get_today_data3(self) :
        print("\n==================== [ 데이터 갱신 시도 ] ====================")
        daily_data3 = pyupbit.get_ohlcv(self.ticker3, count=41)
        # 노이즈 계산 ( 1- 절대값(시가 - 종가) / (고가 - 저가) )
        daily_data3['noise'] = 1 - abs(daily_data3['open'] - daily_data3['close']) / (daily_data3['high'] - daily_data3['low'])
        # 노이즈 1일 평균
        daily_data3['noise_ma20'] = daily_data3['noise'].rolling(window=1).mean().shift(1)
        # 변동폭 ( 고가 - 저가 )
        daily_data3['range'] = daily_data3['high'] - daily_data3['low']
        # 목표매수가 ( 시가 + 변동폭 * K )
        daily_data3['targetPrice'] = daily_data3['open'] + daily_data3['range'].shift(1) * daily_data3['noise_ma20']
        # 5일 이동평균선
        daily_data3['ma5'] = daily_data3['close'].rolling(window=10, min_periods=1).mean().shift(1)
        # 상승장 여부
        daily_data3['bull'] = daily_data3['open'] > daily_data3['ma5']

        today3 = daily_data3.iloc[-1]

        self.target_price3 = today3.targetPrice

        self.bull3 = today3.bull
        print(daily_data3.tail())
        print("Target Price :", self.target_price3, "\tBull :", self.bull3)
        print("==================== [ 데이터 갱신 완료 ] ====================\n")    

    def get_today_data4(self) :
        print("\n==================== [ 데이터 갱신 시도 ] ====================")
        daily_data4 = pyupbit.get_ohlcv(self.ticker4, count=41)
        # 노이즈 계산 ( 1- 절대값(시가 - 종가) / (고가 - 저가) )
        daily_data4['noise'] = 1 - abs(daily_data4['open'] - daily_data4['close']) / (daily_data4['high'] - daily_data4['low'])
        # 노이즈 1일 평균
        daily_data4['noise_ma20'] = daily_data4['noise'].rolling(window=1).mean().shift(1)
        # 변동폭 ( 고가 - 저가 )
        daily_data4['range'] = daily_data4['high'] - daily_data4['low']
        # 목표매수가 ( 시가 + 변동폭 * K )
        daily_data4['targetPrice'] = daily_data4['open'] + daily_data4['range'].shift(1) * daily_data4['noise_ma20']
        # 5일 이동평균선
        daily_data4['ma5'] = daily_data4['close'].rolling(window=10, min_periods=1).mean().shift(1)
        # 상승장 여부
        daily_data4['bull'] = daily_data4['open'] > daily_data4['ma5']

        today4 = daily_data4.iloc[-1]

        self.target_price4 = today4.targetPrice

        self.bull4 = today4.bull
        print(daily_data4.tail())
        print("Target Price :", self.target_price4, "\tBull :", self.bull4)
        print("==================== [ 데이터 갱신 완료 ] ====================\n")

    def get_today_data5(self) :
        print("\n==================== [ 데이터 갱신 시도 ] ====================")
        daily_data5 = pyupbit.get_ohlcv(self.ticker5, count=41)
        # 노이즈 계산 ( 1- 절대값(시가 - 종가) / (고가 - 저가) )
        daily_data5['noise'] = 1 - abs(daily_data5['open'] - daily_data5['close']) / (daily_data5['high'] - daily_data5['low'])
        # 노이즈 1일 평균
        daily_data5['noise_ma50'] = daily_data5['noise'].rolling(window=1).mean().shift(1)
        # 변동폭 ( 고가 - 저가 )
        daily_data5['range'] = daily_data5['high'] - daily_data5['low']
        # 목표매수가 ( 시가 + 변동폭 * K )
        daily_data5['targetPrice'] = daily_data5['open'] + daily_data5['range'].shift(1) * daily_data5['noise_ma50']
        # 5일 이동평균선
        daily_data5['ma5'] = daily_data5['close'].rolling(window=5, min_periods=1).mean().shift(1)
        # 상승장 여부
        daily_data5['bull'] = daily_data5['open'] > daily_data5['ma5']

        today5 = daily_data5.iloc[-1]

        self.target_price5 = today5.targetPrice

        self.bull5 = today5.bull
        print(daily_data5.tail())
        print("Target Price :", self.target_price5, "\tBull :", self.bull5)
        print("==================== [ 데이터 갱신 완료 ] ====================\n")    
    
    def get_today_data6(self) :
        print("\n==================== [ 데이터 갱신 시도 ] ====================")
        daily_data6 = pyupbit.get_ohlcv(self.ticker6, count=41)
        # 노이즈 계산 ( 1- 절대값(시가 - 종가) / (고가 - 저가) )
        daily_data6['noise'] = 1 - abs(daily_data6['open'] - daily_data6['close']) / (daily_data6['high'] - daily_data6['low'])
        # 노이즈 1일 평균
        daily_data6['noise_ma60'] = daily_data6['noise'].rolling(window=1).mean().shift(1)
        # 변동폭 ( 고가 - 저가 )
        daily_data6['range'] = daily_data6['high'] - daily_data6['low']
        # 목표매수가 ( 시가 + 변동폭 * K )
        daily_data6['targetPrice'] = daily_data6['open'] + daily_data6['range'].shift(1) * daily_data6['noise_ma60']
        # 5일 이동평균선
        daily_data6['ma5'] = daily_data6['close'].rolling(window=2, min_periods=1).mean().shift(1)
        # 상승장 여부
        daily_data6['bull'] = daily_data6['open'] > daily_data6['ma5']

        today6 = daily_data6.iloc[-1]

        self.target_price6 = today6.targetPrice

        self.bull6 = today6.bull
        print(daily_data6.tail())
        print("Target Price :", self.target_price6, "\tBull :", self.bull6)
        print("==================== [ 데이터 갱신 완료 ] ====================\n")

    def get_today_data7(self) :
        print("\n==================== [ 데이터 갱신 시도 ] ====================")
        daily_data7 = pyupbit.get_ohlcv(self.ticker7, count=41)
        # 노이즈 계산 ( 1- 절대값(시가 - 종가) / (고가 - 저가) )
        daily_data7['noise'] = 1 - abs(daily_data7['open'] - daily_data7['close']) / (daily_data7['high'] - daily_data7['low'])
        # 노이즈 1일 평균
        daily_data7['noise_ma70'] = daily_data7['noise'].rolling(window=1).mean().shift(1)
        # 변동폭 ( 고가 - 저가 )
        daily_data7['range'] = daily_data7['high'] - daily_data7['low']
        # 목표매수가 ( 시가 + 변동폭 * K )
        daily_data7['targetPrice'] = daily_data7['open'] + daily_data7['range'].shift(1) * daily_data7['noise_ma70']
        # 5일 이동평균선
        daily_data7['ma5'] = daily_data7['close'].rolling(window=10, min_periods=1).mean().shift(1)
        # 상승장 여부
        daily_data7['bull'] = daily_data7['open'] > daily_data7['ma5']

        today7 = daily_data7.iloc[-1]

        self.target_price7 = today7.targetPrice

        self.bull7 = today7.bull
        print(daily_data7.tail())
        print("Target Price :", self.target_price7, "\tBull :", self.bull7)
        print("==================== [ 데이터 갱신 완료 ] ====================\n")     

    def get_today_data8(self) :
        print("\n==================== [ 데이터 갱신 시도 ] ====================")
        daily_data8 = pyupbit.get_ohlcv(self.ticker8, count=41)
        # 노이즈 계산 ( 1- 절대값(시가 - 종가) / (고가 - 저가) )
        daily_data8['noise'] = 1 - abs(daily_data8['open'] - daily_data8['close']) / (daily_data8['high'] - daily_data8['low'])
        # 노이즈 1일 평균
        daily_data8['noise_ma80'] = daily_data8['noise'].rolling(window=1).mean().shift(1)
        # 변동폭 ( 고가 - 저가 )
        daily_data8['range'] = daily_data8['high'] - daily_data8['low']
        # 목표매수가 ( 시가 + 변동폭 * K )
        daily_data8['targetPrice'] = daily_data8['open'] + daily_data8['range'].shift(1) * daily_data8['noise_ma80']
        # 5일 이동평균선
        daily_data8['ma5'] = daily_data8['close'].rolling(window=2, min_periods=1).mean().shift(1)
        # 상승장 여부
        daily_data8['bull'] = daily_data8['open'] > daily_data8['ma5']

        today8 = daily_data8.iloc[-1]

        self.target_price8 = today8.targetPrice

        self.bull8 = today8.bull
        print(daily_data8.tail())
        print("Target Price :", self.target_price8, "\tBull :", self.bull8)
        print("==================== [ 데이터 갱신 완료 ] ====================\n")

    def get_today_data9(self) :
        print("\n==================== [ 데이터 갱신 시도 ] ====================")
        daily_data9 = pyupbit.get_ohlcv(self.ticker9, count=41)
        # 노이즈 계산 ( 1- 절대값(시가 - 종가) / (고가 - 저가) )
        daily_data9['noise'] = 1 - abs(daily_data9['open'] - daily_data9['close']) / (daily_data9['high'] - daily_data9['low'])
        # 노이즈 1일 평균
        daily_data9['noise_ma90'] = daily_data9['noise'].rolling(window=1).mean().shift(1)
        # 변동폭 ( 고가 - 저가 )
        daily_data9['range'] = daily_data9['high'] - daily_data9['low']
        # 목표매수가 ( 시가 + 변동폭 * K )
        daily_data9['targetPrice'] = daily_data9['open'] + daily_data9['range'].shift(1) * daily_data9['noise_ma90']
        # 5일 이동평균선
        daily_data9['ma5'] = daily_data9['close'].rolling(window=5, min_periods=1).mean().shift(1)
        # 상승장 여부
        daily_data9['bull'] = daily_data9['open'] > daily_data9['ma5']

        today9 = daily_data9.iloc[-1]

        self.target_price9 = today9.targetPrice

        self.bull9 = today9.bull
        print(daily_data9.tail())
        print("Target Price :", self.target_price9, "\tBull :", self.bull9)
        print("==================== [ 데이터 갱신 완료 ] ====================\n")

    def get_today_data10(self) :
        print("\n==================== [ 데이터 갱신 시도 ] ====================")
        daily_data10 = pyupbit.get_ohlcv(self.ticker10, count=41)
        # 노이즈 계산 ( 1- 절대값(시가 - 종가) / (고가 - 저가) )
        daily_data10['noise'] = 1 - abs(daily_data10['open'] - daily_data10['close']) / (daily_data10['high'] - daily_data10['low'])
        # 노이즈 1일 평균
        daily_data10['noise_ma100'] = daily_data10['noise'].rolling(window=1).mean().shift(1)
        # 변동폭 ( 고가 - 저가 )
        daily_data10['range'] = daily_data10['high'] - daily_data10['low']
        # 목표매수가 ( 시가 + 변동폭 * K )
        daily_data10['targetPrice'] = daily_data10['open'] + daily_data10['range'].shift(1) * daily_data10['noise_ma100']
        # 5일 이동평균선
        daily_data10['ma5'] = daily_data10['close'].rolling(window=10, min_periods=1).mean().shift(1)
        # 상승장 여부
        daily_data10['bull'] = daily_data10['open'] > daily_data10['ma5']

        today10 = daily_data10.iloc[-1]

        self.target_price10 = today10.targetPrice

        self.bull10 = today10.bull
        print(daily_data10.tail())
        print("Target Price :", self.target_price10, "\tBull :", self.bull10)
        print("==================== [ 데이터 갱신 완료 ] ====================\n")
         

    def buy_coin1(self) :
        self.buy_yn1 = True
        balance = upbit.get_balance() # 잔고 조회
        
        if balance > 5000 : # 잔고 5000원 이상일 때
            upbit.buy_market_order(self.ticker1, 50000)

            buy_price1 = pyupbit.get_orderbook(self.ticker1)['orderbook_units'][0]['ask_price'] # 최우선 매도 호가
            print('====================매수 시도====================')
            slackBot.message("#매수 주문 : " + str(self.ticker1))
            slackBot.message("#매수 주문 가격 : " + str(buy_price1) + "원")

    def buy_coin2(self) :
        self.buy_yn2 = True
        balance = upbit.get_balance() # 잔고 조회
        
        if balance > 5000 : # 잔고 5000원 이상일 때
            upbit.buy_market_order(self.ticker2, 50000)

            buy_price2 = pyupbit.get_orderbook(self.ticker2)['orderbook_units'][0]['ask_price'] # 최우선 매도 호가
            print('====================매수 시도====================')
            slackBot.message("#매수 주문 : " + str(self.ticker2))
            slackBot.message("#매수 주문 가격 : " + str(buy_price2) + "원")

    def buy_coin3(self) :
        self.buy_yn3 = True
        balance = upbit.get_balance() # 잔고 조회
        
        if balance > 5000 : # 잔고 5000원 이상일 때
            upbit.buy_market_order(self.ticker3, 50000)

            buy_price3 = pyupbit.get_orderbook(self.ticker3)['orderbook_units'][0]['ask_price'] # 최우선 매도 호가
            print('====================매수 시도====================')
            slackBot.message("#매수 주문 : " + str(self.ticker3))
            slackBot.message("#매수 주문 가격 : " + str(buy_price3) + "원")

    def buy_coin4(self) :
        self.buy_yn4 = True
        balance = upbit.get_balance() # 잔고 조회
        
        if balance > 5000 : # 잔고 5000원 이상일 때
            upbit.buy_market_order(self.ticker4, 50000)

            buy_price4 = pyupbit.get_orderbook(self.ticker4)['orderbook_units'][0]['ask_price'] # 최우선 매도 호가
            print('====================매수 시도====================')
            slackBot.message("#매수 주문 : " + str(self.ticker4))
            slackBot.message("#매수 주문 가격 : " + str(buy_price4) + "원")                
    
    def buy_coin5(self) :
        self.buy_yn5 = True
        balance = upbit.get_balance() # 잔고 조회
        
        if balance > 5000 : # 잔고 5000원 이상일 때
            upbit.buy_market_order(self.ticker5, 50000)

            buy_price5 = pyupbit.get_orderbook(self.ticker5)['orderbook_units'][0]['ask_price'] # 최우선 매도 호가
            print('====================매수 시도====================')
            slackBot.message("#매수 주문 : " + str(self.ticker5))
            slackBot.message("#매수 주문 가격 : " + str(buy_price5) + "원")

    def buy_coin6(self) :
        self.buy_yn6 = True
        balance = upbit.get_balance() # 잔고 조회
        
        if balance > 5000 : # 잔고 5000원 이상일 때
            upbit.buy_market_order(self.ticker6, 50000)

            buy_price6 = pyupbit.get_orderbook(self.ticker6)['orderbook_units'][0]['ask_price'] # 최우선 매도 호가
            print('====================매수 시도====================')
            slackBot.message("#매수 주문 : " + str(self.ticker6))
            slackBot.message("#매수 주문 가격 : " + str(buy_price6) + "원")

    def buy_coin7(self) :
        self.buy_yn7 = True
        balance = upbit.get_balance() # 잔고 조회
        
        if balance > 5000 : # 잔고 5000원 이상일 때
            upbit.buy_market_order(self.ticker7, 50000)

            buy_price7 = pyupbit.get_orderbook(self.ticker7)['orderbook_units'][0]['ask_price'] # 최우선 매도 호가
            print('====================매수 시도====================')
            slackBot.message("#매수 주문 : " + str(self.ticker7))
            slackBot.message("#매수 주문 가격 : " + str(buy_price7) + "원")

    def buy_coin8(self) :
        self.buy_yn8 = True
        balance = upbit.get_balance() # 잔고 조회
        
        if balance > 5000 : # 잔고 5000원 이상일 때
            upbit.buy_market_order(self.ticker8, 50000)

            buy_price8 = pyupbit.get_orderbook(self.ticker8)['orderbook_units'][0]['ask_price'] # 최우선 매도 호가
            print('====================매수 시도====================')
            slackBot.message("#매수 주문 : " + str(self.ticker8))
            slackBot.message("#매수 주문 가격 : " + str(buy_price8) + "원")

    def buy_coin9(self) :
        self.buy_yn9 = True
        balance = upbit.get_balance() # 잔고 조회
        
        if balance > 5000 : # 잔고 5000원 이상일 때
            upbit.buy_market_order(self.ticker9, 50000)

            buy_price9 = pyupbit.get_orderbook(self.ticker9)['orderbook_units'][0]['ask_price'] # 최우선 매도 호가
            print('====================매수 시도====================')
            slackBot.message("#매수 주문 : " + str(self.ticker9))
            slackBot.message("#매수 주문 가격 : " + str(buy_price9) + "원")

    def buy_coin10(self) :
        self.buy_yn10 = True
        balance = upbit.get_balance() # 잔고 조회
        
        if balance > 5000 : # 잔고 5000원 이상일 때
            upbit.buy_market_order(self.ticker10, 50000)

            buy_price10 = pyupbit.get_orderbook(self.ticker10)['orderbook_units'][0]['ask_price'] # 최우선 매도 호가
            print('====================매수 시도====================')
            slackBot.message("#매수 주문 : " + str(self.ticker10))
            slackBot.message("#매수 주문 가격 : " + str(buy_price10) + "원")


    def sell_coin1(self) :
        self.buy_yn1 = False
        balance = upbit.get_balance(self.ticker1) # 잔고 조회

        upbit.sell_market_order(ticker1, balance)

        sell_price1 = pyupbit.get_orderbook(self.ticker1)['orderbook_units'][0]['bid_price'] # 최우선 매수 호가
        print('====================매도 시도====================')
        slackBot.message("#매도 주문 : " + str(self.ticker1))
        slackBot.message("#매도 주문 가격 : " + str(sell_price1) + "원")
    

    def sell_coin2(self) :
        self.buy_yn2 = False
        balance = upbit.get_balance(self.ticker2) # 잔고 조회

        upbit.sell_market_order(ticker2, balance)

        sell_price2 = pyupbit.get_orderbook(self.ticker2)['orderbook_units'][0]['bid_price'] # 최우선 매수 호가
        print('====================매도 시도====================')
        slackBot.message("#매도 주문 : " + str(self.ticker2))
        slackBot.message("#매도 주문 가격 : " + str(sell_price2) + "원")

    def sell_coin3(self) :
        self.buy_yn3 = False
        balance = upbit.get_balance(self.ticker3) # 잔고 조회

        upbit.sell_market_order(ticker3, balance)

        sell_price3 = pyupbit.get_orderbook(self.ticker3)['orderbook_units'][0]['bid_price'] # 최우선 매수 호가
        print('====================매도 시도====================')
        slackBot.message("#매도 주문 : " + str(self.ticker3))
        slackBot.message("#매도 주문 가격 : " + str(sell_price3) + "원")

    def sell_coin4(self) :
        self.buy_yn4 = False
        balance = upbit.get_balance(self.ticker4) # 잔고 조회

        upbit.sell_market_order(ticker4, balance)

        sell_price4 = pyupbit.get_orderbook(self.ticker4)['orderbook_units'][0]['bid_price'] # 최우선 매수 호가
        print('====================매도 시도====================')
        slackBot.message("#매도 주문 : " + str(self.ticker4))
        slackBot.message("#매도 주문 가격 : " + str(sell_price4) + "원")

    def sell_coin5(self) :
        self.buy_yn5 = False
        balance = upbit.get_balance(self.ticker5) # 잔고 조회

        upbit.sell_market_order(ticker5, balance)

        sell_price5 = pyupbit.get_orderbook(self.ticker5)['orderbook_units'][0]['bid_price'] # 최우선 매수 호가
        print('====================매도 시도====================')
        slackBot.message("#매도 주문 : " + str(self.ticker5))
        slackBot.message("#매도 주문 가격 : " + str(sell_price5) + "원")

    def sell_coin6(self) :
        self.buy_yn6 = False
        balance = upbit.get_balance(self.ticker6) # 잔고 조회

        upbit.sell_market_order(ticker6, balance)

        sell_price6 = pyupbit.get_orderbook(self.ticker6)['orderbook_units'][0]['bid_price'] # 최우선 매수 호가
        print('====================매도 시도====================')
        slackBot.message("#매도 주문 : " + str(self.ticker6))
        slackBot.message("#매도 주문 가격 : " + str(sell_price6) + "원")

    def sell_coin7(self) :
        self.buy_yn7 = False
        balance = upbit.get_balance(self.ticker7) # 잔고 조회

        upbit.sell_market_order(ticker7, balance)

        sell_price7 = pyupbit.get_orderbook(self.ticker7)['orderbook_units'][0]['bid_price'] # 최우선 매수 호가
        print('====================매도 시도====================')
        slackBot.message("#매도 주문 : " + str(self.ticker7))
        slackBot.message("#매도 주문 가격 : " + str(sell_price7) + "원")

    def sell_coin8(self) :
        self.buy_yn8 = False
        balance = upbit.get_balance(self.ticker8) # 잔고 조회

        upbit.sell_market_order(ticker8, balance)

        sell_price8 = pyupbit.get_orderbook(self.ticker8)['orderbook_units'][0]['bid_price'] # 최우선 매수 호가
        print('====================매도 시도====================')
        slackBot.message("#매도 주문 : " + str(self.ticker8))
        slackBot.message("#매도 주문 가격 : " + str(sell_price8) + "원")

    def sell_coin9(self) :
        self.buy_yn9 = False
        balance = upbit.get_balance(self.ticker9) # 잔고 조회

        upbit.sell_market_order(ticker9, balance)

        sell_price9 = pyupbit.get_orderbook(self.ticker9)['orderbook_units'][0]['bid_price'] # 최우선 매수 호가
        print('====================매도 시도====================')
        slackBot.message("#매도 주문 : " + str(self.ticker9))
        slackBot.message("#매도 주문 가격 : " + str(sell_price9) + "원")

    def sell_coin10(self) :
        self.buy_yn10 = False
        balance = upbit.get_balance(self.ticker10) # 잔고 조회

        upbit.sell_market_order(ticker10, balance)

        sell_price10 = pyupbit.get_orderbook(self.ticker10)['orderbook_units'][0]['bid_price'] # 최우선 매수 호가
        print('====================매도 시도====================')
        slackBot.message("#매도 주문 : " + str(self.ticker10))
        slackBot.message("#매도 주문 가격 : " + str(sell_price10) + "원")


class slack :
    def __init__(self, token, channel) :
        self.token = token
        self.channel = channel

    def message(self, message):
        response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + self.token},
        data={"channel": self.channel,"text": message}
    )


acc_key = ""    # Access Key
sec_key = ""    # Secret Key
app_token = ""  # App Token
channel = "#autotrading"    # Slack Channel Name

upbit = pyupbit.Upbit(acc_key, sec_key)
slackBot = slack(app_token, channel)

start_cash = upbit.get_balance()
ticker1 = "KRW-ATOM"
ticker2 = "KRW-BTC"
ticker3 = "KRW-ETH"
ticker4 = "KRW-XRP"
ticker5 = "KRW-DOT"
ticker6 = "KRW-SOL"
ticker7 = "KRW-SAND"
ticker8 = "KRW-AVAX"
ticker9 = "KRW-OMG"
ticker10 = "KRW-ETC"
tradingBot1 = autoTrade1(start_cash, ticker1, ticker2, ticker3, ticker4, ticker5, ticker6, ticker7, ticker8, ticker9, ticker10 )
tradingBot1.start()

