clear clc
Fs=1000;N=5000;
TIME=1:5000;
load('ECG.mat');
x=1:1:512;
M=a_2n2(55001:60000);
Fs=1000; %采样频率
fp=20;fs=100; %通带截止频率，阻带截止频率
rp=1.4;rs=1.6; %通带、阻带衰减
wp=2*pi*fp;ws=2*pi*fs;
[n,wn]=buttord(wp,ws,rp,rs,'s'); %'s'是确定巴特沃斯模拟滤波器阶次和 3dB 截止模拟频率
[z,P,k]=buttap(n); %设计归一化巴特沃斯模拟低通滤波器，z 为极点，p 为零点和 k 为增益
[bp,ap]=zp2tf(z,P,k) %转换为 Ha(p),bp 为分子系数，ap 为分母系数
[bs,as]=lp2lp(bp,ap,wp) %Ha(p)转换为低通 Ha(s)并去归一化，bs 为分子系数，as 为分母系数
[hs,ws]=freqs(bs,as); %模拟滤波器的幅频响应
[bz,az]=bilinear(bs,as,Fs); %对模拟滤波器双线性变换
[h1,w1]=freqz(bz,az); %数字滤波器的幅频响应
m=filter(bz,az,M(:,1));

% %-----------------带陷滤波器抑制工频干扰-------------------
% %50Hz 陷波器：由一个低通滤波器加上一个高通滤波器组成
% %而高通滤波器由一个全通滤波器减去一个低通滤波器构成
% Me=100; %滤波器阶数
% L=100; %窗口长度
% beta=100; %衰减系数
% Fs=1000;
% wc1=49/Fs*pi; %wc1 为高通滤波器截止频率，对应 51Hz
% wc2=51/Fs*pi ;%wc2 为低通滤波器截止频率，对应 49Hz
% h=ideal_lp(0.132*pi,Me)-ideal_lp(wc1,Me)+ideal_lp(wc2,Me); %h 为陷波器冲击响应
% w=kaiser(L,beta);
% y=h.*rot90(w); %y 为 50Hz 陷波器冲击响应序列
% m2=filter(y,1,m);
% 
% %------------------IIR 零相移数字滤波器纠正基线漂移-------------------
% Wp=1.4*2/Fs; %通带截止频率
% Ws=0.6*2/Fs; %阻带截止频率
% devel=0.005; %通带纹波
% Rp=20*log10((1+devel)/(1-devel)); %通带纹波系数
% Rs=60; %阻带衰减
% [N Wn]=ellipord(Wp,Ws,Rp,Rs,'s'); %求椭圆滤波器的阶次
% [b a]=ellip(N,Rp,Rs,Wn,'high'); %求椭圆滤波器的系数
% [hw,w]=freqz(b,a,5000);
% result =filter(b,a,m2);
% 
% figure
% freqz(bz,az);title('巴特沃斯低通滤波器幅频曲线');

figure
subplot(2,1,1);
plot(TIME,M(:,1));
xlabel('t(s)');ylabel('mv');title('原始心电信号波形');grid;

plot(TIME,m);
xlabel('t(s)');ylabel('mv');title('低通滤波后的时域图形');grid;

N=5000
n=0:N-1;
mf=fft(M(:,1),N); %进行频谱变换（傅里叶变换）
mag=abs(mf);
f=(0:length(mf)-1)*Fs/length(mf); %进行频率变换

figure
subplot(2,1,1)
plot(f,mag);axis([0,1000,1,50]);grid; %画出频谱图
xlabel('频率(HZ)');ylabel('幅值');title('心电信号频谱图');

mfa=fft(m,N); %进行频谱变换（傅里叶变换）
maga=abs(mfa);
fa=(0:length(mfa)-1)*Fs/length(mfa); %进行频率变换
subplot(2,1,2)
plot(fa,maga);axis([0,1000,1,50]);grid; %画出频谱图
xlabel('频率(HZ)');ylabel('幅值');title('低通滤波后心电信号频谱图');

wn=M(:,1);
P=10*log10(abs(fft(wn).^2)/N);
f=(0:length(P)-1)/length(P);
figure
plot(f,P);grid
xlabel('归一化频率');ylabel('功率(dB)');title('心电信号的功率谱');

RSF=a_2n2;
Threshold = (max(RSF) - min(RSF))*0.7 + min(RSF);
[R_pks,R_locs]=findpeaks(RSF,500,'MinPeakDistance', 0.5,'MinPeakHeight',Threshold);
plot(RSF);
hold on
plot(R_locs*500,R_pks,'x')
xinlv=(R_locs(11:361)-R_locs(1:351))*500/10;
xinlv=60*1000./xinlv;
x=R_locs(6:356)/2;
plot(x,xinlv)
title('心率(次/分钟)')
xlabel('t/s')
 
 