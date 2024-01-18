clear clc
Fs=1000;N=5000;
TIME=1:5000;
load('ECG.mat');
x=1:1:512;
M=a_2n2(55001:60000);
Fs=1000; %����Ƶ��
fp=20;fs=100; %ͨ����ֹƵ�ʣ������ֹƵ��
rp=1.4;rs=1.6; %ͨ�������˥��
wp=2*pi*fp;ws=2*pi*fs;
[n,wn]=buttord(wp,ws,rp,rs,'s'); %'s'��ȷ��������˹ģ���˲����״κ� 3dB ��ֹģ��Ƶ��
[z,P,k]=buttap(n); %��ƹ�һ��������˹ģ���ͨ�˲�����z Ϊ���㣬p Ϊ���� k Ϊ����
[bp,ap]=zp2tf(z,P,k) %ת��Ϊ Ha(p),bp Ϊ����ϵ����ap Ϊ��ĸϵ��
[bs,as]=lp2lp(bp,ap,wp) %Ha(p)ת��Ϊ��ͨ Ha(s)��ȥ��һ����bs Ϊ����ϵ����as Ϊ��ĸϵ��
[hs,ws]=freqs(bs,as); %ģ���˲����ķ�Ƶ��Ӧ
[bz,az]=bilinear(bs,as,Fs); %��ģ���˲���˫���Ա任
[h1,w1]=freqz(bz,az); %�����˲����ķ�Ƶ��Ӧ
m=filter(bz,az,M(:,1));

% %-----------------�����˲������ƹ�Ƶ����-------------------
% %50Hz �ݲ�������һ����ͨ�˲�������һ����ͨ�˲������
% %����ͨ�˲�����һ��ȫͨ�˲�����ȥһ����ͨ�˲�������
% Me=100; %�˲�������
% L=100; %���ڳ���
% beta=100; %˥��ϵ��
% Fs=1000;
% wc1=49/Fs*pi; %wc1 Ϊ��ͨ�˲�����ֹƵ�ʣ���Ӧ 51Hz
% wc2=51/Fs*pi ;%wc2 Ϊ��ͨ�˲�����ֹƵ�ʣ���Ӧ 49Hz
% h=ideal_lp(0.132*pi,Me)-ideal_lp(wc1,Me)+ideal_lp(wc2,Me); %h Ϊ�ݲ��������Ӧ
% w=kaiser(L,beta);
% y=h.*rot90(w); %y Ϊ 50Hz �ݲ��������Ӧ����
% m2=filter(y,1,m);
% 
% %------------------IIR �����������˲�����������Ư��-------------------
% Wp=1.4*2/Fs; %ͨ����ֹƵ��
% Ws=0.6*2/Fs; %�����ֹƵ��
% devel=0.005; %ͨ���Ʋ�
% Rp=20*log10((1+devel)/(1-devel)); %ͨ���Ʋ�ϵ��
% Rs=60; %���˥��
% [N Wn]=ellipord(Wp,Ws,Rp,Rs,'s'); %����Բ�˲����Ľ״�
% [b a]=ellip(N,Rp,Rs,Wn,'high'); %����Բ�˲�����ϵ��
% [hw,w]=freqz(b,a,5000);
% result =filter(b,a,m2);
% 
% figure
% freqz(bz,az);title('������˹��ͨ�˲�����Ƶ����');

figure
subplot(2,1,1);
plot(TIME,M(:,1));
xlabel('t(s)');ylabel('mv');title('ԭʼ�ĵ��źŲ���');grid;

plot(TIME,m);
xlabel('t(s)');ylabel('mv');title('��ͨ�˲����ʱ��ͼ��');grid;

N=5000
n=0:N-1;
mf=fft(M(:,1),N); %����Ƶ�ױ任������Ҷ�任��
mag=abs(mf);
f=(0:length(mf)-1)*Fs/length(mf); %����Ƶ�ʱ任

figure
subplot(2,1,1)
plot(f,mag);axis([0,1000,1,50]);grid; %����Ƶ��ͼ
xlabel('Ƶ��(HZ)');ylabel('��ֵ');title('�ĵ��ź�Ƶ��ͼ');

mfa=fft(m,N); %����Ƶ�ױ任������Ҷ�任��
maga=abs(mfa);
fa=(0:length(mfa)-1)*Fs/length(mfa); %����Ƶ�ʱ任
subplot(2,1,2)
plot(fa,maga);axis([0,1000,1,50]);grid; %����Ƶ��ͼ
xlabel('Ƶ��(HZ)');ylabel('��ֵ');title('��ͨ�˲����ĵ��ź�Ƶ��ͼ');

wn=M(:,1);
P=10*log10(abs(fft(wn).^2)/N);
f=(0:length(P)-1)/length(P);
figure
plot(f,P);grid
xlabel('��һ��Ƶ��');ylabel('����(dB)');title('�ĵ��źŵĹ�����');

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
title('����(��/����)')
xlabel('t/s')
 
 