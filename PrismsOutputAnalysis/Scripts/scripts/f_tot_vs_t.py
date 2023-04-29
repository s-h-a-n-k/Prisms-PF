import matplotlib.pyplot as plt
import sys



path=sys.argv[1]+"integratedFields.txt"
sloc=sys.argv[2]+"f_tot_vs_t.png"

with open(path,'r') as file:
	t=[];f_tot=[];
	for i in file:i_n=i.split();t.append(float(i_n[0]));f_tot.append(float(i_n[2]));

fig=plt.figure();timer=fig.canvas.new_timer(5000);timer.add_callback(plt.close);plt.plot(t,f_tot);plt.title("Global Free Energy Vs Time");plt.xlabel("t");plt.ylabel("f_tot");plt.savefig(sloc);timer.start();plt.show();
