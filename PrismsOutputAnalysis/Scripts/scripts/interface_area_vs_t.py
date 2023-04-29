import matplotlib.pyplot as plt
import sys


sloc=sys.argv[1]

# loc=input("Enter location of vtu files\n")
with open(sloc+"iarea_vs_t.txt",'r') as file:
        t=[];a=[];
        for i in file.readlines()[1:]:ni=i.split();t.append(float(ni[1]));a.append(float(ni[2]));
        fig=plt.figure();timer=fig.canvas.new_timer(5000);timer.add_callback(plt.close);plt.plot(t,a);plt.title("Interface Area Vs Time");plt.xlabel("t");plt.ylabel("Total length of interface");plt.savefig(sloc+"iarea_vs_t.png");timer.start();plt.show();
