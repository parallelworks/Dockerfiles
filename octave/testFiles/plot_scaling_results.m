data = load('runTimes_t2_p05_49Incs.txt')
figure(1)

plot(data(:,1), 1./data(:,2),'bx-')
hold on
xlabel ('Number of processors')
idealTime = data(1,2)./data(:,1)
plot(data(:,1),1./idealTime ,'g--')
legend('Actual', 'Ideal')
print -deps strong-scaling-vgroove.eps
print -deps strong-scaling-vgroove.png

figure(2)
plot(data(:,1),data(:,2),'k-x')
hold on
plot(data(:,1),idealTime ,'g--')
xlabel ('Number of processors')
ylabel('Simulation Time - V-Groove (s)')
legend('Actual', 'Ideal')
print -deps Scaling-simTime-VGroove.eps
print -deps Scaling-simTime-VGroove.png
