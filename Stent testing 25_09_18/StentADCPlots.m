clc
clear all
close all
%% ADC characteristics
MaxADCVoltage=5;
ADCRes=8
ADCStep=5/2^(8);

ADCData= struct()
files = dir('*/*.csv')
for ii=1:numel(files)
    temp=csvread(strcat(files(ii).folder,'/',files(ii).name));
    ADCData(ii).name=files(ii).name;
    ADCData(ii).data=temp(2:end,2:end)*ADCStep*100;
end
%% 20mm/s
figure1=figure
nc1=[0 1 2 3 4 6 7];
Dis40mm=[0 6 6 6 3.5 1 0];
nc2=[0 1 2 4 6 7];
Dis50mm=[0.5 5.5 6 5 3 0];
nc3=[0 1 3 5 6 7];
Dis60mm=[0 5 5.5 3.5 1 0];

kkk=1.5;
subplot(3,1,1),
    plot(nc1,Dis40mm,'-*',nc2,Dis50mm,'-o',...
        nc3,Dis60mm,'-^','LineWidth',kkk)
    xlabel('number of cycles (n_c)','FontSize', 12)
    ylabel('Displacement (mm)','FontSize', 12)
    legend('40 mm at 20 mm/s','50 mm at 20 mm/s', '60 mm at 20 mm/s',...
        'Location','South')
    set(gca,'linewidth',1.5,...
     'xcolor',[0,0,0]);
    setFigProp2([14.4 14],12);
% 30 mm/s
nc1=[0 1 2 4 6];
Dis40mm=[1 6.2 8.0 8.2 8.5];
nc2=[0 1 2 6];
Dis50mm=[1 6.6 8 8.3];
nc3=[0 2 4];
Dis60mm=[1.1 8.2 8.5];
subplot(3,1,2),
    plot(nc1,Dis40mm,'-*',nc2,Dis50mm,'-o',...
        nc3,Dis60mm,'-^','LineWidth',kkk);
    xlabel('number of cycles (n_c)','FontSize', 12)
    ylabel('Displacement (mm)','FontSize', 12)
    legend('40 mm at 30 mm/s','50 mm at 30 mm/s', '60 mm at 30 mm/s','Location','SouthEast')
    set(gca,'linewidth',1.5,...
     'xcolor',[0,0,0]);
    setFigProp2([14.4 14],12);
% 40 mm/s
nc1=[0 1 2 5 8];
Dis40mm=[1.1 5.4 6 6.5 7];
nc2=[0 1 2 4 7];
Dis50mm=[1.1 3.3 5 5.5 6.5];
nc3=[0 1 2 4 8];
Dis60mm=[1 5 6 6.5 7];
subplot(3,1,3),
    plot(nc1,Dis40mm,'-*',nc2,Dis50mm,'-o',...
        nc3,Dis60mm,'-^','LineWidth',kkk)
    xlabel('number of cycles (n_c)','FontSize', 12)
    ylabel('Displacement (mm)','FontSize', 12)
    legend('40 mm at 40 mm/s','50 mm at 40 mm/s', '60 mm at 40 mm/s','Location','SouthEast')
    set(gca,'linewidth',1.5,...
     'xcolor',[0,0,0]);
    setFigProp2([16.4 14],12);

% Create textbox
annotation(figure1,'textbox',...
    [0.0169252468265162 0.791164658634534 0.0148095909732017 0.04518473895582],...
    'String',{'(a)'},...
    'FontSize',12,...
    'FitBoxToText','off',...
    'EdgeColor','none');

% Create textbox
annotation(figure1,'textbox',...
    [0.0218617771509168 0.504016064257027 0.0148095909732017 0.04518473895582],...
    'String','(b)',...
    'FontSize',12,...
    'FitBoxToText','off',...
    'EdgeColor','none');

% Create textbox
annotation(figure1,'textbox',...
    [0.0211565585331453 0.230923694779114 0.0148095909732017 0.0451847389558206],...
    'String','(c)',...
    'FontSize',12,...
    'FitBoxToText','off',...
    'EdgeColor','none');

%   matlabToLatexEps('disptraj',300);
%% Plot for different speed
kkk=1.5;
t=[0:0.1:30-0.1];
plot(t,ADCData(6).data(1:300,9),'LineWidth',kkk)
hold on
plot(t,ADCData(7).data(1:300,9),'LineWidth',kkk)
plot(t,ADCData(8).data(1:300,9),'LineWidth',kkk)
hold off
I=legend({'60 mm at 20mm/s','60 mm at 30mm/s','60 mm at 40mm/s'},'location','southeast')
ylabel('Pressure (kPa)')
xlabel('time (s)')
set(gca,'linewidth',1.5,...
     'xcolor',[0,0,0]);
setFigProp2([14.4,8],12);
% matlabToLatexEps('pressuretraj',300);