# buzzer_pico_player
using buzzer to play music on raspberry pico
## 简体中文说明
你需要给库初始化的时候传递乐谱的速度（节拍/分钟），以及可选的八个声道，分别控制GPIO0,2,4,6,8,10,12,14,需要以列表的形式传递
列表的内容包括从-6到15的数字1，2，3，4，5（do,ri,mi,fa,so)，1.5即为#do,休止符代表是15，往下也是如此
请务必确保多通道列表长度相同，不然可能会不工作sorry
