Whid=[0.4,0.5;0.3,0.2]
Wout=[0.8;0.7] 
input=[0.7,0.3]

SUMhid=input*Whid
Ahid=sigmoid(SUMhid)
SUMout=Ahid*Wout
Aout=purelin(SUMout)
DELTAout=(T-Aout)*dpurelin(Aout)
DELTAhid=DELTAout*Wout*[dsigmoid(SUMhid(1)), dsigmoid(SUMhid(2))]
Wout=Wout*DELTAout*Ahid
Whid(:,1)=Whid(:,1)+DELTAhid(1)*input'
Whid(:,2)=Whid(:,2)+DELTAhid(2)*input'
purelin(sigmoid(input*Whid)*Wout)