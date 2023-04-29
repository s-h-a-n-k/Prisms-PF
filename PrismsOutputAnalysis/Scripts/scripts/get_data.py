import vtk,numpy,os,sys,matplotlib.pyplot as plt;from vtk.util import numpy_support;


s=sys.argv[1]
b=sys.argv[2]
var=sys.argv[3]
sloc=sys.argv[4]

# print(comm, vars)

reader = vtk.vtkXMLUnstructuredGridReader()
def open_file(s:str):
    global reader
    reader.SetFileName(s)
    reader.Update()
    return reader.GetOutput()

def data_list(l)->list:
    return numpy_support.vtk_to_numpy(l).tolist()


class Data:
    def __init__(self,s:str)->None:
        self.content=open_file(s) 
    
    def vars_point(self,i=None)->dict|list:
        d=self.content.GetPointData()
        if i is not None:return data_list(d.GetArray(i));
        dic=dict()
        for i in range(d.GetNumberOfArrays()):dic[d.GetArrayName(i)]=data_list(d.GetArray(i));
        return dic

    def vars_field(self,i=None)->dict|list:
        d=self.content.GetFieldData()
        if i is not None:return data_list(d.GetArray(i));
        dic=dict()
        n=d.GetNumberOfArrays()
        for i in range(n):dic[d.GetArrayName(i)]=data_list(d.GetArray(i));
        return dic

    def vars_cell(self)->dict|list:
        d=self.content.GetFieldData()
        if i is not None:return data_list(d.GetArray(i));
        dic=dict()
        for i in range(d.GetNumberOfArrays()):dic[d.GetArrayName(i)]=data_list(d.GetArray(i));
        return dic

def phase_fraction(s:str,b=0.5,var='n',sloc=None,s1=None)->None:
    st=[];t=[];c1l=[];c2l=[];
    fl=os.listdir(s);fl.sort();
    for i in fl:
        if i.startswith("solution-") is True:
            d=Data(s+i);t.append(d.vars_field("TIME")[0]);
            try:st.append(d.vars_field("CYCLE")[0]);
            except:st.append(0.0)
            c=0
            for i in (v:=d.vars_point(var)):
                if i>b:c+=1;
            c1l.append(f:=c/len(v));c2l.append(1-f);
    if s1 is None:s1="Phase_Fraction_"+str(b)
    fig=plt.figure();timer=fig.canvas.new_timer(5000);timer.add_callback(plt.close);plt.plot(t,c1l,label="Phase 1");plt.plot(t,c2l,label="Phase 2");plt.ylim(0.0,1.0);plt.title("Phase Fraction Vs Time");plt.legend();plt.savefig(sloc+s1+".png");timer.start();plt.show();plt.close();
    with open(sloc+s1+".txt",'w') as f:
        f.write("Step\tTime\tPhase_Fraction_1\tPhase_Fraction_2\n")
        print("Step\tTime\tPhase_Fraction_1\tPhase_Fraction_2\n")
        for i in range(len(t)):
            f.write(str(st[i])+"\t"+str(t[i])+"\t"+str(c1l[i])+"\t"+str(c2l[i])+"\n")
            print(str(st[i])+"\t"+str(t[i])+"\t"+str(c1l[i])+"\t"+str(c2l[i]))
phase_fraction(s,float(b),var,sloc)

# if comm=="phase_fraction":
#     phase_fraction(*vars)
