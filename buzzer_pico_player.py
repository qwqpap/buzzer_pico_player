class Play_music:
    '''
使用蜂鸣器来在pico上面播放最多八个声道的音乐
using buzzer to play music on raspberry pico
channel_1~8的gpio引脚将设置为0，2，4，6，8，10，12，14
the channel_1~8 is for gpio 0，2，4，6，8，10，12，14
请确保列表长度相同（我懒了）
please make sure that the len of list is same
    '''
    def __init__(self, play_speed=120, channel_1=0, channel_2=0, channel_3=0, channel_4=0, channel_5=0, channel_6=0, channel_7=0, channel_8=0):
        from time import sleep
        from machine import Pin, PWM
        self.one_time = 60/play_speed
        self.c1 =channel_1
        self.c2 =channel_2
        self.c3 =channel_3
        self.c4 =channel_4
        self.c5 =channel_5
        self.c6 =channel_6
        self.c7 =channel_7
        self.c8 =channel_8
        
        #l means low,h means high ,s means #
        
        self.ldo  = 262
        self.ldos = 277
        self.lre  = 294
        self.lres = 311
        self.lmi  = 330
        self.lmis = 340
        self.lfa  = 349
        self.lfas = 370
        self.lso  = 392
        self.lsos = 415
        self.lla  = 440
        self.llas = 466
        self.lsi  = 494
        self.lsis = 524
        self.do  = 523
        self.dos = 554 
        self.re  = 578
        self.res = 622
        self.mi  = 659
        self.mis = 682
        self.fa  = 698
        self.fas = 740
        self.so  = 784
        self.sos = 831
        self.la  = 880
        self.las = 932
        self.si  = 988
        self.sis = 1046
        self.hdo  = 1046
        self.hdos = 1109
        self.hre  = 1175
        self.hres = 1245
        self.hmi  = 1318
        self.hmis = 1356
        self.hfa  = 1397
        self.hfas = 1480
        self.hso  = 1568
        self.hsos = 1661
        self.hla  = 1760
        self.hlas = 1865
        self.hsi  = 1976
        self.hsis = 2093
        self.stop = 200000
        self.f_liist = [51,55,58,61,65,69,73,77,82,87,92,97,103,110,116,123,130,138,146,155,164,174,186,195,207,220,233,246,self.ldo,self.ldos,self.lre,self.lres,self.lmi,self.lmis,self.lfa,self.lfas,self.lso,self.lsos,self.lla,self.llas,self.lsi,self.lsis,
                       self.do,self.dos,self.re,self.res,self.mi,self.mis,self.fa,self.fas,self.so,self.sos,self.la,self.las,self.si,self.sis,
                       self.hdo,self.hdos,self.hre,self.hres,self.hmi,self.hmis,self.hfa,self.hfas,self.hso,self.hsos,self.hla,self.hlas,self.hsi,self.hsis,2217,2349,2489,2637,2793,2959,3135,3322,3520,3729,3951,4186,4434,4698,4978,5274,5587,5919,6281,6644,7040,7458,7902
                        ,8372,8869,9397,9956,10548,self.stop]
        self.test_sb = -1
        self.length = 0
        if type(self.c1).__name__=='list':
            self.pwm1 = PWM(Pin(0))
            self.pwm1.duty_u16(32768)
            self.length = len(self.c1)
            self.test_sb = 1
        else:
            pass
        if type(self.c2).__name__=='list':
            self.pwm2 = PWM(Pin(2))
            self.pwm2.duty_u16(32768)
            self.length = len(self.c2)
            self.test_sb = 2
        else:
            pass   
        if type(self.c3).__name__=='list':
            self.pwm3 = PWM(Pin(4))
            self.pwm3.duty_u16(32768)
            self.length = len(self.c3)
            self.test_sb = 3
        else:
            pass
        if type(self.c4).__name__=='list':
            self.pwm4 = PWM(Pin(6))
            self.pwm4.duty_u16(32768)
            self.length = len(self.c4)
            self.test_sb = 4
        else:
            pass
        if type(self.c5).__name__=='list':
            self.pwm5 = PWM(Pin(8))
            self.pwm5.duty_u16(32768)
            self.length = len(self.c5)
            self.test_sb = 5
        else:
            pass
        if type(self.c6).__name__=='list':
            self.pwm6 = PWM(Pin(10))
            self.pwm6.duty_u16(32768)
            self.length = len(self.c6)
            self.test_sb = 6
        else:
            pass
        if type(self.c7).__name__=='list':
            self.pwm7 = PWM(Pin(12))
            self.pwm7.duty_u16(32768)
            self.length = len(self.c7)
            self.test_sb = 7
        else:
            pass
        if type(self.c8).__name__=='list':
            self.pwm8 = PWM(Pin(14))
            self.pwm8.duty_u16(32768)
            self.length = len(self.c8)
            self.test_sb = 8
        else:
            pass
        if self.test_sb == -1:
            raise Exception('please make sure there has least one list has been there')
    def play_music(self):
        import time
        i = 1
        while i <= self.length:
            j = i - 1 
            if type(self.c1).__name__=='list':
                self.pwm1.freq(self.f_liist[int(40 + self.c1[j] * 2)])
            if type(self.c2).__name__=='list':
                self.pwm2.freq(self.f_liist[int(40 + self.c2[j] * 2)])
            if type(self.c3).__name__=='list':
                self.pwm3.freq(self.f_liist[int(40 + self.c3[j] * 2)])
            if type(self.c4).__name__=='list':
                self.pwm4.freq(self.f_liist[int(40 + self.c4[j] * 2)])
            if type(self.c5).__name__=='list':
                self.pwm5.freq(self.f_liist[int(40 + self.c5[j] * 2)])
            if type(self.c6).__name__=='list':
                self.pwm6.freq(self.f_liist[int(40 + self.c6[j] * 2)])
            if type(self.c7).__name__=='list':
                self.pwm7.freq(self.f_liist[int(40 + self.c7[j] * 2)])
            if type(self.c8).__name__=='list':
                self.pwm8.freq(self.f_liist[int(40 + self.c8[j] * 2)])
           
            i = i+1
            time.sleep(self.one_time)
        if type(self.c1).__name__=='list':
            self.pwm1.duty_u16(0)
        if type(self.c2).__name__=='list':
            self.pwm2.duty_u16(0)
        if type(self.c3).__name__=='list':
            self.pwm3.duty_u16(0)
        if type(self.c4).__name__=='list':
            self.pwm4.duty_u16(0)
        if type(self.c5).__name__=='list':
            self.pwm5.duty_u16(0)
        if type(self.c6).__name__=='list':
            self.pwm6.duty_u16(0)
        if type(self.c7).__name__=='list':
            self.pwm7.duty_u16(0)
        if type(self.c8).__name__=='list':
            self.pwm8.duty_u16(0)
        def play_always(self):
            while True:
                self.play_music()
if __name__ == '__main__':

    channel_1 = [-2.0,1.0,3.0,-2.0,1.0,3.0,-2.0,1.0,3.0,-2.0,1.0,3.0,-2.0,1.0,3.0,-2.0,1.0,3.0,-2.0,-2.0,1.0,1.0,1.0,1.0,2.0,2.0,3.0,1.0,5.0,5.0,5.0,3.0,2.0,2.0,5.0,5.0,2.0,2.0,1.0,-1.0,3.0,3.0,3.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,-1.0,-1.0,0.0,0.0,1.0,2.0,-2.0,-2.0,1.0,1.0,2.0,3.0,4.0,4.0,4.0,3.0,2.0,1.0,2.0,2.0,2.0,2.0,1.0,2.0,3.0,1.0,5.0,5.0,5.0,3.0,2.0,2.0,5.0,5.0,2.0,2.0,1.0,-1.0,-1.0,-1.0,0.0,1.0,-2.0,-2.0,-2.0,-2.0,15.0,-2.0,-1.0,-1.0,0.0,0.0,1.0,2.0,-2.0,-2.0,1.0,1.0,2.0,3.0,4.0,4.0,4.0,3.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,15.0,15.0,15.0,15.0,3.0,4.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,6.0,5.0,4.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0,4.0,3.0,2.0,1.0,0.0,-1.0,-1.0,0.0,1.0,2.0,3.0,1.0,5.0,5.0,5.0,3.0,2.0,2.0,5.0,5.0,2.0,2.0,1.0,-1.0,3.0,3.0,3.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,-1.0,-1.0,0.0,0.0,1.0,2.0,-2.0,-2.0,1.0,1.0,2.0,3.0,4.0,4.0,4.0,3.0,2.0,1.0,2.0,2.0,2.0,2.0,1.0,2.0,3.0,1.0,5.0,5.0,5.0,3.0,2.0,2.0,5.0,5.0,2.0,2.0,1.0,-1.0,-1.0,-1.0,0.0,1.0,-2.0,-2.0,-2.0,-2.0,15.0,-2.0,-1.0,-1.0,0.0,0.0,1.0,2.0,-2.0,-2.0,1.0,1.0,2.0,3.0,4.0,4.0,4.0,3.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,15.0,15.0,15.0,15.0,3.0,4.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,6.0,5.0,4.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0,4.0,3.0,2.0,1.0,0.0,-1.0,-1.0,0.0,1.0,2.0,-2.0,-2.0,1.0,1.0,2.0,3.0,2.0,2.0,2.0,2.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,-2.0,-2.0,1.0,1.0,15.0,15.0,-2.0,-2.0,1.0,1.0,3.0,3.0,-2.0,-2.0,1.0,1.0,1.0,2.0,3.0,1.0,5.0,5.0,5.0,3.0,2.0,2.0,5.0,5.0,2.0,2.0,1.0,-1.0,3.0,3.0,3.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,-1.0,-1.0,0.0,0.0,1.0,2.0,-2.0,-2.0,1.0,1.0,2.0,3.0,4.0,4.0,4.0,3.0,2.0,1.0,2.0,2.0,2.0,2.0,1.0,2.0,3.0,1.0,5.0,5.0,5.0,3.0,2.0,2.0,5.0,5.0,2.0,2.0,1.0,-1.0,-1.0,-1.0,0.0,1.0,-2.0,-2.0,-2.0,-2.0,15.0,-2.0,-1.0,-1.0,0.0,0.0,1.0,2.0,-2.0,-2.0,1.0,1.0,2.0,3.0,4.0,4.0,4.0,3.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,15.0,15.0,15.0,15.0,3.0,4.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,6.0,5.0,4.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0,4.0,3.0,2.0,1.0,0.0,-1.0,-1.0,0.0,1.0,2.0,3.0,1.0,5.0,5.0,5.0,3.0,2.0,2.0,5.0,5.0,2.0,2.0,1.0,-1.0,3.0,3.0,3.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,-1.0,-1.0,0.0,0.0,1.0,2.0,-2.0,-2.0,1.0,1.0,2.0,3.0,4.0,4.0,4.0,3.0,2.0,1.0,2.0,2.0,2.0,2.0,1.0,2.0,3.0,1.0,5.0,5.0,5.0,3.0,2.0,2.0,5.0,5.0,2.0,2.0,1.0,-1.0,-1.0,-1.0,0.0,1.0,-2.0,-2.0,-2.0,-2.0,15.0,-2.0,-1.0,-1.0,0.0,0.0,1.0,2.0,-2.0,-2.0,1.0,1.0,2.0,3.0,4.0,4.0,4.0,3.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,15.0,15.0,15.0,15.0,3.0,4.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,6.0,5.0,4.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0,4.0,3.0,2.0,1.0,0.0,-1.0,-1.0,0.0,1.0,2.0,-2.0,-2.0,1.0,1.0,1.0,0.0,-1.0,-1.0,0.0,0.0,1.0,2.0,-2.0,-2.0,-2.0,-2.0,1.0,0.0,-1.0,-1.0,0.0,0.0,1.0,2.0,-2.0,-2.0,1.0,1.0,2.0,3.0,4.0,4.0,4.0,3.0,2.0,1.0,]

    channel_2 = [15,15,15,15,15,15,15,15,-1,1,3,3,3,3,3,3,-4,-2,0,0,0,0,0,0,-3,-1,1,1,1,1,1,1
                 -7,-4,-2,-2,-2,-2,-2,-2,-5,-3,-1,-1,-1,-1,-1,-1,-6,-4,-2,-2,-2,-2,-2,-2,-6,-2.5,0,0,0,0,0,0
                 -6,-6,-3.5,-2,0,0,3,3,-1,1,3,3,3,3,3,3,-4,-2,0,0,0,0,0,0,-3,-1,1,1,1,1,1,1,
                 0,-4,-2,-2,-2,-2,-2,-5,-5,-3,-1,-1,-1,-1,-1,-1,-6,-6,-4,-4,-4,-4,-4,-4,-5,-1,2,2,-4,-4,-4,-4,
                 -1,-1,-1,-1,-1,-1,15,15,-6,-4,-2,-2,-2,-2,1,1,-6,-6,-5,-5,-5,-5,15,15,-6,-4,-1,-1,-1,-1,1,1,
                 -6,-6,-4,-4,-2,-2,-2,-2,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    channel_3 = [15,15,15,15,15,15,6,7,8,8,8,7,8,8,10,10,7,7,7,7,7,7,3,3,6,6,6,5,6,6,8,8,
                 5,5,5,5,5,5,3,3,4,4,4,3,4,8,8,8,3,3,3,3,15,8,8,8,7,7,7,4.5,4,4,7,7,
                 7,7,7,7,7,7,6,7,8,8,8,7,8,8,10,10,7,7,7,7,7,7,3,3,6,6,6,5,6,6,8,8
                 ,5,5,5,5,5,5,3,3,4,4,8,7,7,7,8,8,9,9,10,8,8,8,8,8,8,8,7,6,6,7,7,5.5,5.5
                 ,6,6,6,6,6,6,8,9,10,10,10,9,10,10,12,12,9,9,9,9,9,9,5,5,8,8,8,7,8,8,10,10,
                 10,10,10,10,10,10,5,5,6,7,8,8,7,8,9,9,8,8,8,5,5,5,5,5,9,9,8,8,7,7,6,6]
    channel_4 = [15,15,15,15,15,15,15,15,-1,1,3,3,3,3,3,3,-4,-2,0,0,0,0,0,0,-3,-1,1,1,1,1,1,1,
                 -7,-4,-2,-2,-2,-2,-2,-2,-5,-3,-1,-1,-1,-1,-1,-1,-6,-4,-2,-2,-2,-2,-2,-2,-6,-2.5,0,0,0,0,0,0,
                 -6,-6,-3.5,-2,0,0,3,3,-1,1,3,3,3,3,3,3,-4,-2,0,0,0,0,0,0,-3,-1,1,1,1,1,1,1,
                 0,-4,-2,-2,-2,-2,-2,-5,-5,-3,-1,-1,-1,-1,-1,-1,-6,-6,-4,-4,-4,-4,-4,-4,-5,-1,2,2,-1.5,-1.5,-1.5,-1.5,
                 1,1,1,1,1,1,15,15,-6,-4,-2,-2,-2,-2,1,1,-6,-6,-5,-5,-5,-5,15,15,-6,-4,-1,-1,-1,-1,1,1,
                 -6,-6,-4,-4,-2,-2,-2,-2,-1,-1,-1,-1,0,0,0,0,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1]
    channel_5 = [15,15,15,15,15,15,15,15,-1,1,3,3,3,3,3,3,-4,-2,0,0,0,0,0,0,-3,-1,1,1,1,1,1,1,
                 -7,-4,-2,-2,-2,-2,-2,-2,-5,-3,-1,-1,-1,-1,-1,-1,-6,-4,-2,-2,-2,-2,-2,-2,-6,-2.5,0,0,0,0,0,0,
                 -6,-6,-3.5,-2,0,0,3,3,-1,1,3,3,3,3,3,3,-4,-2,0,0,0,0,0,0,-3,-1,1,1,1,1,1,1,
                 0,-4,-2,-2,-2,-2,-2,-5,-5,-3,-1,-1,-1,-1,-1,-1,-6,-6,-4,-4,-4,-4,-4,-4,-5,-1,2,2,0,0,0,0,
                 3,3,3,3,3,3,15,15,-6,-4,-2,-2,-2,-2,1,1,-6,-6,-5,-5,-5,-5,15,15,-6,-4,-1,-1,-1,-1,1,1,
                 -6,-6,-4,-4,-2,-2,-2,-2,-1,-1,-1,-1,0,0,0,0,-2,-2,-2,-2,-2,-2,-2,-2,-5,-5,-5,-5,-5,-5,-5,-5]

    a = Play_music(240,channel_1,channel_1,channel_1,channel_1,channel_1,channel_1,channel_1,channel_1)
    a.play_music()
else:
    pass
