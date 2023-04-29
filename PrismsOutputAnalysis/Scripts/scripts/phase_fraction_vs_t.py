import matplotlib.pyplot as plt
import sys


sloc=sys.argv[1]

# loc=input("Enter location of vtu files\n")
with open(sloc+"phi_vs_t.txt",'r') as file:
        t=[];c1=[];c2=[];
        for i in file.readlines()[1:]:ni=i.split();t.append(float(ni[1]));c1.append(float(ni[2]));c2.append(float(ni[3]));
        fig=plt.figure();timer=fig.canvas.new_timer(5000);timer.add_callback(plt.close);plt.plot(t,c1,label="c=1");plt.plot(t,c2,label="c=0");plt.ylim(0.0,1.0);plt.xlabel("t");plt.title("Phase Fraction Vs Time");plt.ylabel("fraction");plt.legend();plt.savefig(sloc+"phi_vs_t.png");timer.start();plt.show();
