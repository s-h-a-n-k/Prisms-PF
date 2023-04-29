import matplotlib.pyplot as plt
import sys


b=sys.argv[1]
sloc=sys.argv[2]

# loc=input("Enter location of vtu files\n")
with open(sloc+"domain_stats_vs_t_"+str(b)+".txt",'r') as file:
        t1=[];t2=[];nd1=[];nd2=[];c=0;
        for i in file:
                if c==0:
                    if i.startswith("Less than ") is True:c=1;continue;
                if c==1:
                        if i.startswith("More than ") is True:c=2;continue;
                if c==1:
                        i_n=i.split();t1.append(float(i_n[1]));nd1.append(float(i_n[2]));
                if c==2:
                        i_n=i.split();t2.append(float(i_n[1]));nd2.append(float(i_n[2]));

fig=plt.figure();timer=fig.canvas.new_timer(5000);timer.add_callback(plt.close);plt.plot(t1,nd1,'b',label="Less than "+b);plt.plot(t2,nd2,'r',label="More than "+b);plt.title("Number of domains Vs Time");plt.xlabel("t");plt.ylabel("no. domains");plt.legend();plt.savefig(sloc+"domain_count_vs_t_"+b+".png");timer.start();plt.show();

